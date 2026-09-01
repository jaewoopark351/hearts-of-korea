from __future__ import annotations

import csv
import hashlib
import json
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.evidence_manifest import write_manifest


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
TOOL = REPOSITORY_ROOT / "tools" / "map_fresh_scan.py"


def write_text(root: Path, relative: str, text: str) -> None:
    path = root / Path(relative)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def write_bmp(root: Path, relative: str, rows: list[list[tuple[int, int, int]]]) -> None:
    height = len(rows)
    width = len(rows[0])
    stride = ((width * 3 + 3) // 4) * 4
    pixel_data = bytearray()
    for row in reversed(rows):
        encoded = bytearray()
        for red, green, blue in row:
            encoded.extend((blue, green, red))
        encoded.extend(b"\x00" * (stride - len(encoded)))
        pixel_data.extend(encoded)
    offset = 54
    size = offset + len(pixel_data)
    header = bytearray(b"BM")
    header.extend(struct.pack("<IHHI", size, 0, 0, offset))
    header.extend(struct.pack("<IiiHHIIiiII", 40, width, height, 1, 24, 0, len(pixel_data), 0, 0, 0, 0))
    path = root / Path(relative)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(header + pixel_data)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


class MapFreshScanTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.base = Path(self.temporary.name)
        self.vanilla = self.base / "vanilla"
        self.mod = self.base / "mod"
        self.dependency = self.base / "dependency"
        self.old = self.base / "old"
        for root in (self.vanilla, self.mod, self.dependency, self.old):
            root.mkdir()
        self._write_valid_fixture()
        self.original = self.base / "original"
        shutil.copytree(self.mod, self.original)
        self.old_manifest = self.base / "old-manifest.tsv"
        write_manifest(self.old, self.old_manifest)
        self.old_manifest_sha256 = hashlib.sha256(
            self.old_manifest.read_bytes()
        ).hexdigest()
        self.original_manifest = self.base / "original-manifest.tsv"
        write_manifest(self.original, self.original_manifest)
        self.original_manifest_sha256 = hashlib.sha256(
            self.original_manifest.read_bytes()
        ).hexdigest()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _write_valid_fixture(self) -> None:
        vanilla_definition = (
            "0;0;0;0;land;false;unknown;0\n"
            "1;255;0;0;land;false;plains;1\n"
            "2;0;0;255;sea;false;ocean;0\n"
        )
        mod_definition = vanilla_definition + "3;0;255;0;land;false;forest;1\n"
        for root in (self.vanilla, self.old):
            write_text(root, "map/definition.csv", vanilla_definition)
            write_bmp(root, "map/provinces.bmp", [[(255, 0, 0), (0, 0, 255)]])
            write_text(root, "history/states/1-base.txt", "state = { id = 1 provinces = { 1 } }\n")
            write_text(
                root,
                "map/strategicregions/100-base.txt",
                "strategic_region = { id = 100 provinces = { 1 2 } }\n",
            )
        write_text(self.mod, "map/definition.csv", mod_definition)
        write_bmp(
            self.mod,
            "map/provinces.bmp",
            [[(255, 0, 0), (0, 0, 255), (0, 255, 0)]],
        )
        write_text(
            self.mod,
            "history/states/2-custom.txt",
            "state = {\n    id = 2\n    provinces = { 3 }\n}\n",
        )
        write_text(
            self.mod,
            "map/strategicregions/101-custom.txt",
            "strategic_region = { id = 101 provinces = { 3 } }\n",
        )
        write_text(
            self.mod,
            "events/candidate_refs.txt",
            "country_event = { trigger = { controls_state = 2 controls_province = 3 } }\n",
        )
        write_text(
            self.mod,
            "events/reference_2.txt",
            "country_event = { }\n",
        )
        for excluded in (
            ".git",
            ".local-artifacts",
            "docs",
            "Docs",
            "tools",
            "tests",
        ):
            write_text(
                self.mod,
                f"{excluded}/must-not-be-scanned.txt",
                "state = 2 province = 3\n",
            )
        write_text(self.vanilla, "map/railways.txt", "1 2 1 3\n")
        write_text(self.vanilla, "map/supply_nodes.txt", "1 1\n")
        write_text(
            self.vanilla,
            "map/adjacencies.csv",
            "From;To;Type;Through;start_x;start_y;stop_x;stop_y;Rule;Comment\n"
            "1;3;sea;-1;-1;-1;-1;-1;;test\n"
            "-1;-1;;-1;-1;-1;-1;-1;-1\n",
        )
        write_text(
            self.vanilla,
            "map/buildings.txt",
            (
                "1;arms_factory;0;0;0;0;0\n"
                "1;air_base;0;0;0;0;0\n"
                "1;rocket_site_spawn;0;0;0;0;0\n"
                "2;air_base;0;0;0;0;0\n"
                "2;rocket_site_spawn;0;0;0;0;0"
            ),
        )
        write_text(
            self.vanilla,
            "map/unitstacks.txt",
            "1;0;0;0;0;0;0\n2;0;0;0;0;0;0\n3;0;0;0;0;0;0\n",
        )
        write_text(
            self.dependency,
            "localisation/test_l_english.yml",
            (
                "l_english:\n"
                " STATE_2_suffix:0 \"2\"\n"
                " STATE_3:0 \"Wrong entity type\"\n"
                " VICTORY_POINTS_3_suffix:0 \"Custom province\"\n"
                " VICTORY_POINTS_2:0 \"Wrong entity type\"\n"
                " # STATE_2:0 \"Comment only\"\n"
            ),
        )

    def run_tool(self, output: Path, *, old: bool = True) -> subprocess.CompletedProcess[str]:
        command = [
            sys.executable,
            str(TOOL),
            "--vanilla-root",
            str(self.vanilla),
            "--mod-root",
            str(self.mod),
            "--dependency-root",
            str(self.dependency),
            "--output",
            str(output),
        ]
        if old:
            command.extend(
                (
                    "--old-vanilla-root",
                    str(self.old),
                    "--old-vanilla-manifest",
                    str(self.old_manifest),
                    "--old-vanilla-manifest-sha256",
                    self.old_manifest_sha256,
                    "--old-vanilla-label",
                    "synthetic-old",
                    "--original-root",
                    str(self.original),
                    "--original-manifest",
                    str(self.original_manifest),
                    "--original-manifest-sha256",
                    self.original_manifest_sha256,
                    "--original-label",
                    "synthetic-original",
                )
            )
        return subprocess.run(command, text=True, capture_output=True, check=False)

    def test_valid_synthetic_overlay_outputs_deterministic_inventory(self) -> None:
        first = self.base / "result-one"
        second = self.base / "result-two"
        completed = self.run_tool(first)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        completed = self.run_tool(second)
        self.assertEqual(completed.returncode, 0, completed.stderr)

        expected_files = {
            "findings.tsv",
            "inputs.tsv",
            "references.tsv",
            "summary.json",
            "three_way_files.tsv",
        }
        self.assertEqual({path.name for path in first.iterdir()}, expected_files)
        for name in expected_files:
            self.assertEqual((first / name).read_bytes(), (second / name).read_bytes())

        summary = json.loads((first / "summary.json").read_text(encoding="utf-8"))
        self.assertEqual(summary["runtime_compatibility"], "UNPROVEN")
        self.assertEqual(summary["static_result"], "PASS_WITH_LIMITATIONS")
        self.assertEqual(summary["three_way_status"], "INVENTORY_ONLY")
        self.assertEqual(
            summary["old_vanilla_identity"]["content_verification"], "PASS"
        )
        self.assertEqual(
            summary["hok_original_identity"]["content_verification"], "PASS"
        )
        self.assertEqual(
            summary["vfs"]["precedence_low_to_high"],
            ["vanilla", "dependency", "mod"],
        )

        inputs = read_tsv(first / "inputs.tsv")
        definition_inputs = [row for row in inputs if row["relative_path"] == "map/definition.csv"]
        self.assertEqual(
            {row["layer"] for row in definition_inputs},
            {"vanilla", "mod", "old_vanilla", "hok_original"},
        )
        self.assertEqual(
            next(row for row in definition_inputs if row["layer"] == "mod")["effective"],
            "yes",
        )
        for row in inputs:
            self.assertEqual(len(row["sha256"]), 64)
            int(row["sha256"], 16)

        codes = {row["code"] for row in read_tsv(first / "findings.tsv")}
        self.assertIn("CUSTOM_PROVINCE_ID", codes)
        self.assertIn("CUSTOM_STATE_ID", codes)
        self.assertIn("RUNTIME_COMPATIBILITY_UNPROVEN", codes)
        references = read_tsv(first / "references.tsv")
        self.assertFalse(
            any("must-not-be-scanned.txt" in row["relative_path"] for row in references)
        )
        self.assertFalse(
            any("must-not-be-scanned.txt" in row["relative_path"] for row in inputs)
        )
        self.assertTrue(
            any(row["entity_type"] == "province" and row["entity_id"] == "3" for row in references)
        )
        self.assertTrue(
            any(row["entity_type"] == "state" and row["entity_id"] == "2" for row in references)
        )
        physical_keys = [
            (
                row["entity_type"],
                row["entity_id"],
                row["source_layer"],
                row["relative_path"],
                row["line"],
                row["column"],
            )
            for row in references
        ]
        self.assertEqual(len(physical_keys), len(set(physical_keys)))
        self.assertTrue(
            any(
                row["entity_type"] == "state"
                and row["entity_id"] == "2"
                and "state_localisation_token" in row["context"]
                and row["confidence"] == "HIGH"
                for row in references
            )
        )
        state_definition = next(
            row
            for row in references
            if row["entity_type"] == "state"
            and row["entity_id"] == "2"
            and row["source_layer"] == "mod"
            and row["relative_path"] == "history/states/2-custom.txt"
            and row["line"] == "2"
        )
        self.assertEqual(state_definition["column"], "10")
        self.assertIn("state_definition_id", state_definition["context"])
        self.assertIn("state_candidate_numeric", state_definition["context"])
        self.assertTrue(
            any(
                row["entity_type"] == "state"
                and row["entity_id"] == "2"
                and row["context"] == "comment_numeric_candidate"
                and row["confidence"] == "LOW"
                for row in references
            )
        )
        self.assertTrue(all(row["effective"] in {"yes", "no"} for row in references))
        self.assertTrue(
            any(
                row["entity_type"] == "state"
                and row["entity_id"] == "2"
                and row["relative_path"] == "events/reference_2.txt"
                and row["line"] == "0"
                and row["context"] == "relative_path_numeric_candidate"
                and row["confidence"] == "LOW"
                for row in references
            )
        )
        self.assertTrue(
            any(
                row["entity_type"] == "province"
                and row["entity_id"] == "3"
                and "victory_point_localisation_token" in row["context"]
                and row["confidence"] == "HIGH"
                for row in references
            )
        )
        self.assertFalse(
            any(
                row["entity_type"] == "province"
                and row["entity_id"] == "3"
                and "state_localisation_token" in row["context"]
                for row in references
            )
        )
        self.assertFalse(
            any(
                row["entity_type"] == "state"
                and row["entity_id"] == "2"
                and "victory_point_localisation_token" in row["context"]
                for row in references
            )
        )
        three_way = read_tsv(first / "three_way_files.tsv")
        definition_three_way = next(
            row
            for row in three_way
            if row["relative_path"] == "map/definition.csv"
        )
        self.assertEqual(definition_three_way["original_present"], "yes")
        self.assertEqual(definition_three_way["old_vs_original"], "different")

    def test_detects_cross_file_integrity_failures_and_legal_sentinel_boundary(self) -> None:
        write_text(
            self.mod,
            "history/states/2-duplicate.txt",
            "state = { id = 2 provinces = { 3 } }\n",
        )
        write_text(self.mod, "map/railways.txt", "1 2 1 99\n")
        write_text(self.mod, "map/supply_nodes.txt", "1 99\n")
        write_text(
            self.mod,
            "map/adjacencies.csv",
            "From;To;Type;Through\n-1;3;sea;-1\n-1;-1;;-1\n1;3;sea;-1\n",
        )
        write_text(self.mod, "map/buildings.txt", "999;arms_factory;0;0;0;0;0")
        write_text(self.mod, "map/unitstacks.txt", "99;0;0;0;0;0;0\n")
        output = self.base / "failures"
        completed = self.run_tool(output, old=False)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        findings = read_tsv(output / "findings.tsv")
        codes = {row["code"] for row in findings}
        self.assertTrue(
            {
                "DUPLICATE_STATE_ID",
                "LAND_PROVINCE_MULTIPLE_STATES",
                "RAILWAY_UNKNOWN_PROVINCE",
                "SUPPLY_NODE_UNKNOWN_PROVINCE",
                "ADJACENCY_PARTIAL_SENTINEL",
                "ADJACENCY_SENTINEL_NOT_LAST",
                "BUILDING_UNKNOWN_STATE",
                "UNITSTACK_UNKNOWN_PROVINCE",
            }.issubset(codes)
        )
        summary = json.loads((output / "summary.json").read_text(encoding="utf-8"))
        self.assertEqual(summary["static_result"], "FAIL")
        self.assertEqual(summary["three_way_status"], "BLOCKED")

    def test_detects_effective_state_id_gap(self) -> None:
        write_text(
            self.mod,
            "history/states/3-gap-boundary.txt",
            "state = { id = 3 provinces = { } }\n",
        )
        write_text(
            self.mod,
            "history/states/7-gap-boundary.txt",
            "state = { id = 7 provinces = { } }\n",
        )
        write_text(
            self.mod,
            "map/buildings.txt",
            (
                "1;air_base;0;0;0;0;0\n"
                "1;rocket_site_spawn;0;0;0;0;0\n"
                "2;air_base;0;0;0;0;0\n"
                "2;rocket_site_spawn;0;0;0;0;0\n"
                "3;air_base;0;0;0;0;0\n"
                "3;rocket_site_spawn;0;0;0;0;0\n"
                "7;air_base;0;0;0;0;0\n"
                "7;rocket_site_spawn;0;0;0;0;0"
            ),
        )

        output = self.base / "state-id-gap"
        completed = self.run_tool(output, old=False)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        findings = read_tsv(output / "findings.tsv")
        missing = [row for row in findings if row["code"] == "MISSING_STATE_ID"]
        self.assertEqual([row["entity_id"] for row in missing], ["4", "5", "6"])
        self.assertTrue(all(row["severity"] == "ERROR" for row in missing))
        self.assertTrue(all(row["entity_type"] == "state" for row in missing))
        self.assertTrue(
            all("continuous from 1 through 7" in row["detail"] for row in missing)
        )
        error_codes = {row["code"] for row in findings if row["severity"] == "ERROR"}
        self.assertEqual(error_codes, {"MISSING_STATE_ID"})
        summary = json.loads((output / "summary.json").read_text(encoding="utf-8"))
        self.assertEqual(summary["static_result"], "FAIL")

    def test_detects_buildings_trailing_newline(self) -> None:
        for label, line_ending in (("lf", "\n"), ("crlf", "\r\n")):
            with self.subTest(line_ending=label):
                write_text(
                    self.mod,
                    "map/buildings.txt",
                    "2;arms_factory;0;0;0;0;0" + line_ending,
                )
                output = self.base / f"buildings-trailing-{label}"
                completed = self.run_tool(output, old=False)
                self.assertEqual(completed.returncode, 0, completed.stderr)
                findings = read_tsv(output / "findings.tsv")
                trailing = next(
                    row
                    for row in findings
                    if row["code"] == "BUILDINGS_TRAILING_NEWLINE"
                )
                self.assertEqual(trailing["severity"], "ERROR")
                self.assertEqual(trailing["relative_path"], "map/buildings.txt")
                self.assertEqual(trailing["line"], "2")
                self.assertIn(label.upper(), trailing["detail"])
                self.assertIn("empty final row", trailing["detail"])
                summary = json.loads(
                    (output / "summary.json").read_text(encoding="utf-8")
                )
                self.assertEqual(summary["static_result"], "FAIL")

    def test_detects_effective_state_missing_air_base_site(self) -> None:
        write_text(
            self.mod,
            "map/buildings.txt",
            (
                "1;rocket_site_spawn;0;0;0;0;0\n"
                "2;air_base;0;0;0;0;0\n"
                "2;rocket_site_spawn;0;0;0;0;0"
            ),
        )
        output = self.base / "missing-air-base-site"
        completed = self.run_tool(output, old=False)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        findings = read_tsv(output / "findings.tsv")
        missing_air = [
            row
            for row in findings
            if row["code"] == "BUILDING_MISSING_AIR_BASE_SITE"
        ]
        self.assertEqual(len(missing_air), 1)
        self.assertEqual(missing_air[0]["severity"], "ERROR")
        self.assertEqual(missing_air[0]["entity_type"], "state")
        self.assertEqual(missing_air[0]["entity_id"], "1")
        self.assertEqual(missing_air[0]["source_layer"], "mod")
        self.assertEqual(missing_air[0]["relative_path"], "map/buildings.txt")
        self.assertFalse(
            any(
                row["code"] == "BUILDING_MISSING_ROCKET_SITE_SPAWN"
                for row in findings
            )
        )

    def test_detects_effective_state_missing_rocket_site_spawn(self) -> None:
        write_text(
            self.mod,
            "map/buildings.txt",
            (
                "1;air_base;0;0;0;0;0\n"
                "2;air_base;0;0;0;0;0\n"
                "2;rocket_site_spawn;0;0;0;0;0"
            ),
        )
        output = self.base / "missing-rocket-site-spawn"
        completed = self.run_tool(output, old=False)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        findings = read_tsv(output / "findings.tsv")
        missing_rocket = [
            row
            for row in findings
            if row["code"] == "BUILDING_MISSING_ROCKET_SITE_SPAWN"
        ]
        self.assertEqual(len(missing_rocket), 1)
        self.assertEqual(missing_rocket[0]["severity"], "ERROR")
        self.assertEqual(missing_rocket[0]["entity_type"], "state")
        self.assertEqual(missing_rocket[0]["entity_id"], "1")
        self.assertEqual(missing_rocket[0]["source_layer"], "mod")
        self.assertEqual(missing_rocket[0]["relative_path"], "map/buildings.txt")
        self.assertFalse(
            any(
                row["code"] == "BUILDING_MISSING_AIR_BASE_SITE"
                for row in findings
            )
        )

    def test_detects_unitstack_global_order_inversion(self) -> None:
        write_text(
            self.mod,
            "map/unitstacks.txt",
            "1;0;0;0;0;0;0\n3;0;0;0;0;0;0\n2;0;0;0;0;0;0\n",
        )
        output = self.base / "unitstack-order-inversion"
        completed = self.run_tool(output, old=False)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        findings = read_tsv(output / "findings.tsv")
        inversion = next(
            row for row in findings if row["code"] == "UNITSTACK_ORDER_INVERSION"
        )
        self.assertEqual(inversion["severity"], "ERROR")
        self.assertEqual(inversion["relative_path"], "map/unitstacks.txt")
        self.assertEqual(inversion["line"], "3")
        self.assertIn("previous line 2 key=(0, 3)", inversion["detail"])
        self.assertIn("current key=(0, 2)", inversion["detail"])
        summary = json.loads((output / "summary.json").read_text(encoding="utf-8"))
        self.assertEqual(summary["static_result"], "FAIL")

    def test_duplicate_membership_within_one_state_is_not_multiple_states(self) -> None:
        write_text(
            self.mod,
            "history/states/2-custom.txt",
            "state = { id = 2 provinces = { 3 3 } }\n",
        )
        output = self.base / "duplicate-membership"
        completed = self.run_tool(output, old=False)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        findings = read_tsv(output / "findings.tsv")
        province_three = [
            row
            for row in findings
            if row["entity_type"] == "province" and row["entity_id"] == "3"
        ]
        self.assertTrue(
            any(
                row["code"] == "STATE_DUPLICATE_PROVINCE_MEMBERSHIP"
                for row in province_three
            )
        )
        self.assertFalse(
            any(
                row["code"] == "LAND_PROVINCE_MULTIPLE_STATES"
                for row in province_three
            )
        )

    def test_auxiliary_inherited_assets_are_hashed_without_old_vanilla(self) -> None:
        bitmap_paths = (
            "map/heightmap.bmp",
            "map/terrain.bmp",
            "map/rivers.bmp",
            "map/trees.bmp",
            "map/cities.bmp",
            "map/world_normal.bmp",
        )
        for relative in bitmap_paths:
            write_bmp(self.vanilla, relative, [[(1, 2, 3)]])
        write_text(self.vanilla, "map/ambient_object.txt", "object = { }\n")

        output = self.base / "auxiliary-assets"
        completed = self.run_tool(output, old=False)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        inputs = read_tsv(output / "inputs.tsv")
        by_path = {row["relative_path"]: row for row in inputs}
        for relative in (*bitmap_paths, "map/ambient_object.txt"):
            self.assertIn(relative, by_path)
            self.assertEqual(by_path[relative]["layer"], "vanilla")
            self.assertEqual(by_path[relative]["effective"], "yes")
            self.assertIn("auxiliary_map_inventory", by_path[relative]["roles"])
        expected_hash = hashlib.sha256(
            (self.vanilla / "map/ambient_object.txt").read_bytes()
        ).hexdigest()
        self.assertEqual(by_path["map/ambient_object.txt"]["sha256"], expected_hash)
        findings = read_tsv(output / "findings.tsv")
        generic_headers = [
            row for row in findings if row["code"] == "BMP_GENERIC_HEADER_INVENTORY"
        ]
        self.assertEqual({row["relative_path"] for row in generic_headers}, set(bitmap_paths))
        self.assertTrue(all("semantics=UNPROVEN" in row["detail"] for row in generic_headers))
        summary = json.loads((output / "summary.json").read_text(encoding="utf-8"))
        self.assertEqual(summary["three_way_status"], "BLOCKED")

    def test_existing_output_is_rejected_without_overwrite(self) -> None:
        output = self.base / "already-exists"
        output.mkdir()
        marker = output / "marker.txt"
        marker.write_text("preserve", encoding="utf-8")
        completed = self.run_tool(output)
        self.assertEqual(completed.returncode, 2)
        self.assertEqual(marker.read_text(encoding="utf-8"), "preserve")
        self.assertEqual({path.name for path in output.iterdir()}, {"marker.txt"})

    def test_output_location_cannot_contaminate_input_roots(self) -> None:
        unsafe_outputs = (
            self.vanilla / "audit-output",
            self.dependency / "audit-output",
            self.old / "audit-output",
            self.original / "audit-output",
            self.mod / "events" / "audit-output",
        )
        for output in unsafe_outputs:
            with self.subTest(output=output):
                completed = self.run_tool(output)
                self.assertEqual(completed.returncode, 2)
                self.assertFalse(output.exists())

        allowed = self.mod / ".local-artifacts" / "audit-output"
        completed = self.run_tool(allowed)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertTrue((allowed / "summary.json").is_file())

    def test_old_vanilla_requires_matching_manifest_identity(self) -> None:
        output = self.base / "missing-old-identity"
        command = [
            sys.executable,
            str(TOOL),
            "--vanilla-root",
            str(self.vanilla),
            "--mod-root",
            str(self.mod),
            "--old-vanilla-root",
            str(self.old),
            "--output",
            str(output),
        ]
        completed = subprocess.run(
            command, text=True, capture_output=True, check=False
        )
        self.assertEqual(completed.returncode, 2)
        self.assertFalse(output.exists())

        mismatched = self.base / "mismatched-old-identity"
        command.extend(
            (
                "--old-vanilla-manifest",
                str(self.old_manifest),
                "--old-vanilla-manifest-sha256",
                "0" * 64,
                "--old-vanilla-label",
                "synthetic-old",
                "--original-root",
                str(self.original),
                "--original-manifest",
                str(self.original_manifest),
                "--original-manifest-sha256",
                self.original_manifest_sha256,
                "--original-label",
                "synthetic-original",
            )
        )
        command[command.index(str(output))] = str(mismatched)
        completed = subprocess.run(
            command, text=True, capture_output=True, check=False
        )
        self.assertEqual(completed.returncode, 2)
        self.assertFalse(mismatched.exists())

    def test_hok_original_cannot_equal_or_overlap_mutable_mod_root(self) -> None:
        for label, unsafe_original in (
            ("same", self.mod),
            ("nested", self.mod / "immutable-looking-copy"),
        ):
            with self.subTest(label=label):
                if label == "nested":
                    unsafe_original.mkdir()
                output = self.base / f"unsafe-original-{label}"
                command = [
                    sys.executable,
                    str(TOOL),
                    "--vanilla-root",
                    str(self.vanilla),
                    "--mod-root",
                    str(self.mod),
                    "--old-vanilla-root",
                    str(self.old),
                    "--old-vanilla-manifest",
                    str(self.old_manifest),
                    "--old-vanilla-manifest-sha256",
                    self.old_manifest_sha256,
                    "--old-vanilla-label",
                    "synthetic-old",
                    "--original-root",
                    str(unsafe_original),
                    "--original-manifest",
                    str(self.original_manifest),
                    "--original-manifest-sha256",
                    self.original_manifest_sha256,
                    "--original-label",
                    "synthetic-original",
                    "--output",
                    str(output),
                ]
                completed = subprocess.run(
                    command, text=True, capture_output=True, check=False
                )
                self.assertEqual(completed.returncode, 2)
                self.assertIn(
                    "must be physically separate, non-overlapping roots",
                    completed.stderr,
                )
                self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
