#!/usr/bin/env python3
"""Deterministic, read-only static inventory for Hearts of Iron IV map data.

This tool deliberately does not propose ID migrations, merge map data, or claim
runtime compatibility.  It models only an exact-relative-path overlay in the
order vanilla -> dependency -> mod and records the limitations of that model in
``summary.json``.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import shutil
import struct
import sys
import tempfile
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Sequence

try:
    from tools.evidence_manifest import verify_manifest
except ModuleNotFoundError:  # Direct execution from the tools directory.
    from evidence_manifest import verify_manifest


TOOL_VERSION = "12"
TEXT_SUFFIXES = {
    ".asset",
    ".csv",
    ".gfx",
    ".gui",
    ".json",
    ".lua",
    ".mod",
    ".txt",
    ".yaml",
    ".yml",
}
ENTITY_ROOTS = {
    "state": ("history/states/", "state"),
    "strategic_region": ("map/strategicregions/", "strategic_region"),
}
FLAT_MAP_FILES = {
    "map/definition.csv",
    "map/provinces.bmp",
    "map/railways.txt",
    "map/supply_nodes.txt",
    "map/adjacencies.csv",
    "map/buildings.txt",
    "map/unitstacks.txt",
}
AUXILIARY_MAP_PATHS = (
    "map/heightmap.bmp",
    "map/terrain.bmp",
    "map/ambient_object.txt",
    "map/rivers.bmp",
    "map/trees.bmp",
    "map/cities.bmp",
    "map/world_normal.bmp",
)
DEVELOPMENT_TOP_LEVELS = frozenset(
    {
        ".agents",
        ".codex",
        ".git",
        ".github",
        ".local-artifacts",
        ".vscode",
        "docs",
        "tests",
        "tools",
    }
)


@dataclass(frozen=True)
class Layer:
    name: str
    root: Path
    files: dict[str, Path]


@dataclass
class InputRecord:
    layer: str
    relative_path: str
    source_path: str
    size: int
    sha256: str
    effective: str
    shadowed_by: str
    roles: set[str] = field(default_factory=set)


@dataclass(frozen=True)
class Finding:
    severity: str
    category: str
    code: str
    evidence_grade: str
    entity_type: str = ""
    entity_id: str = ""
    source_layer: str = ""
    relative_path: str = ""
    line: int | str = ""
    column: int | str = ""
    detail: str = ""


@dataclass(frozen=True)
class Occurrence:
    entity_type: str
    entity_id: int
    source_layer: str
    relative_path: str
    line: int
    column: int
    context: str
    confidence: str
    snippet: str


@dataclass(frozen=True)
class DefinitionRow:
    province_id: int
    rgb: tuple[int, int, int]
    province_type: str
    coastal: str
    terrain: str
    continent: str
    line: int

    def comparable(self) -> tuple[object, ...]:
        return (
            self.rgb,
            self.province_type,
            self.coastal,
            self.terrain,
            self.continent,
        )


@dataclass(frozen=True)
class Token:
    value: str
    line: int
    column: int


@dataclass(frozen=True)
class Member:
    entity_id: int
    line: int
    column: int


@dataclass(frozen=True)
class EntityRecord:
    kind: str
    internal_id: int | None
    id_line: int
    id_column: int
    members: tuple[Member, ...]
    source_layer: str
    relative_path: str


@dataclass(frozen=True)
class ParseIssue:
    severity: str
    code: str
    line: int
    column: int
    detail: str


@dataclass(frozen=True)
class EntityParse:
    records: tuple[EntityRecord, ...]
    issues: tuple[ParseIssue, ...]


class ScanError(Exception):
    """An expected command-line or input error."""


def _verify_layer_identity(
    layer: Layer,
    manifest_path: Path | None,
    expected_manifest_sha256: str | None,
    label: str | None,
    subject: str,
) -> dict[str, object]:
    if manifest_path is None or expected_manifest_sha256 is None or label is None:
        raise ScanError(
            f"{subject} requires manifest, expected manifest SHA-256, and label"
        )
    manifest = manifest_path.resolve()
    if not manifest.is_file():
        raise ScanError(f"{subject} manifest is not a file: {manifest}")
    expected = expected_manifest_sha256.casefold()
    if not re.fullmatch(r"[0-9a-f]{64}", expected):
        raise ScanError(
            f"{subject} manifest SHA-256 must be 64 hexadecimal characters"
        )
    actual = hashlib.sha256(manifest.read_bytes()).hexdigest()
    if actual != expected:
        raise ScanError(
            f"{subject} manifest identity mismatch: expected {expected}, found {actual}"
        )
    try:
        verification, verification_code = verify_manifest(layer.root, manifest)
    except (OSError, ValueError) as exc:
        raise ScanError(f"{subject} manifest verification failed: {exc}") from exc
    if verification_code != 0:
        raise ScanError(
            f"{subject} root does not match its manifest: "
            f"missing={len(verification['missing'])}, "
            f"extra={len(verification['extra'])}, "
            f"mismatches={len(verification['mismatches'])}"
        )
    return {
        "label": label,
        "label_evidence": "USER_SUPPLIED_UNPROVEN",
        "manifest": str(manifest),
        "manifest_sha256": actual,
        "files": verification["actual_files"],
        "bytes": verification["actual_bytes"],
        "content_verification": "PASS",
    }


class MapScanner:
    def __init__(
        self,
        vanilla_root: Path,
        mod_root: Path,
        dependency_root: Path | None,
        old_vanilla_root: Path | None,
        old_vanilla_manifest: Path | None = None,
        old_vanilla_manifest_sha256: str | None = None,
        old_vanilla_label: str | None = None,
        original_root: Path | None = None,
        original_manifest: Path | None = None,
        original_manifest_sha256: str | None = None,
        original_label: str | None = None,
    ) -> None:
        if original_root is not None:
            resolved_mod_root = mod_root.resolve()
            resolved_original_root = original_root.resolve()
            if (
                resolved_original_root == resolved_mod_root
                or resolved_original_root.is_relative_to(resolved_mod_root)
                or resolved_mod_root.is_relative_to(resolved_original_root)
            ):
                raise ScanError(
                    "HOK_ORIGINAL and the mutable mod working tree must be "
                    "physically separate, non-overlapping roots: "
                    f"original={resolved_original_root}; mod={resolved_mod_root}"
                )

        self.findings: list[Finding] = []
        self.occurrences: list[Occurrence] = []
        self.inputs: dict[tuple[str, str], InputRecord] = {}
        self.byte_cache: dict[tuple[str, str], bytes] = {}
        self.text_cache: dict[tuple[str, str], str] = {}
        self.entity_cache: dict[tuple[str, str, str], EntityParse] = {}

        roots: list[tuple[str, Path]] = [("vanilla", vanilla_root)]
        if dependency_root is not None:
            roots.append(("dependency", dependency_root))
        roots.append(("mod", mod_root))
        self.layers = tuple(self._make_layer(name, root) for name, root in roots)
        self.layer_by_name = {layer.name: layer for layer in self.layers}
        self.old_layer = (
            self._make_layer("old_vanilla", old_vanilla_root)
            if old_vanilla_root is not None
            else None
        )
        self.original_layer = (
            self._make_layer("hok_original", original_root)
            if original_root is not None
            else None
        )
        self.old_vanilla_identity: dict[str, object] | None = None
        self.hok_original_identity: dict[str, object] | None = None
        if self.old_layer is not None:
            if self.original_layer is None:
                raise ScanError(
                    "old vanilla three-way inventory also requires --original-root"
                )
            self.old_vanilla_identity = _verify_layer_identity(
                self.old_layer,
                old_vanilla_manifest,
                old_vanilla_manifest_sha256,
                old_vanilla_label,
                "old vanilla",
            )
            self.hok_original_identity = _verify_layer_identity(
                self.original_layer,
                original_manifest,
                original_manifest_sha256,
                original_label,
                "HOK_ORIGINAL",
            )
        elif any(
            value is not None
            for value in (
                old_vanilla_manifest,
                old_vanilla_manifest_sha256,
                old_vanilla_label,
                original_root,
                original_manifest,
                original_manifest_sha256,
                original_label,
            )
        ):
            raise ScanError(
                "old vanilla and HOK_ORIGINAL identity options require --old-vanilla-root"
            )

        effective: dict[str, tuple[Layer, Path]] = {}
        for layer in self.layers:
            for relative_path, source in layer.files.items():
                effective[relative_path] = (layer, source)
        self.effective = effective
        self._report_case_collisions()

        self.definition_rows_by_layer: dict[str, dict[int, list[DefinitionRow]]] = {}
        self.effective_definition_rows: dict[int, list[DefinitionRow]] = {}
        self.effective_state_records: list[EntityRecord] = []
        self.effective_region_records: list[EntityRecord] = []
        self.candidates: dict[str, dict[int, set[str]]] = {
            "province": defaultdict(set),
            "state": defaultdict(set),
        }
        self.candidate_sources: dict[str, dict[int, set[str]]] = {
            "province": defaultdict(set),
            "state": defaultdict(set),
        }
        self.three_way_rows: list[dict[str, str]] = []

    @staticmethod
    def _make_layer(name: str, root: Path | None) -> Layer:
        if root is None:
            raise ScanError(f"missing root for layer {name}")
        root = root.resolve()
        if not root.is_dir():
            raise ScanError(f"{name} root is not a directory: {root}")
        files: dict[str, Path] = {}
        try:
            paths = sorted(
                (path for path in root.rglob("*") if path.is_file()),
                key=lambda path: path.relative_to(root).as_posix(),
            )
        except OSError as exc:
            raise ScanError(f"cannot enumerate {name} root {root}: {exc}") from exc
        for path in paths:
            relative = path.relative_to(root).as_posix()
            if (
                name == "mod"
                and relative.split("/", 1)[0].casefold() in DEVELOPMENT_TOP_LEVELS
            ):
                continue
            files[relative] = path
        return Layer(name=name, root=root, files=files)

    def _report_case_collisions(self) -> None:
        spellings: dict[str, set[str]] = defaultdict(set)
        for layer in self.layers:
            for relative in layer.files:
                spellings[relative.casefold()].add(relative)
        for folded, variants in sorted(spellings.items()):
            if len(variants) > 1:
                self.add_finding(
                    "WARNING",
                    "vfs",
                    "VFS_CASE_VARIANTS",
                    detail=(
                        "Exact-relative-path overlay keeps these as distinct paths; "
                        f"platform loader behavior is not inferred: {', '.join(sorted(variants))}"
                    ),
                )

    def add_finding(
        self,
        severity: str,
        category: str,
        code: str,
        *,
        evidence_grade: str = "CONFIRMED",
        entity_type: str = "",
        entity_id: int | str = "",
        source_layer: str = "",
        relative_path: str = "",
        line: int | str = "",
        column: int | str = "",
        detail: str = "",
    ) -> None:
        self.findings.append(
            Finding(
                severity=severity,
                category=category,
                code=code,
                evidence_grade=evidence_grade,
                entity_type=entity_type,
                entity_id=str(entity_id),
                source_layer=source_layer,
                relative_path=relative_path,
                line=line,
                column=column,
                detail=detail,
            )
        )

    def _effective_status(self, layer: Layer, relative: str) -> tuple[str, str]:
        selected = self.effective.get(relative)
        if selected is None:
            return "no", ""
        if selected[0].name == layer.name:
            return "yes", ""
        return "no", selected[0].name

    def read_bytes(self, layer: Layer, relative: str, role: str) -> bytes:
        key = (layer.name, relative)
        source = layer.files.get(relative)
        if source is None:
            raise ScanError(f"missing file in {layer.name}: {relative}")
        if key not in self.byte_cache:
            try:
                data = source.read_bytes()
            except OSError as exc:
                raise ScanError(f"cannot read {source}: {exc}") from exc
            self.byte_cache[key] = data
            if layer.name in {"old_vanilla", "hok_original"}:
                effective, shadowed_by = "reference", ""
            else:
                effective, shadowed_by = self._effective_status(layer, relative)
            self.inputs[key] = InputRecord(
                layer=layer.name,
                relative_path=relative,
                source_path=str(source),
                size=len(data),
                sha256=hashlib.sha256(data).hexdigest(),
                effective=effective,
                shadowed_by=shadowed_by,
            )
        self.inputs[key].roles.add(role)
        return self.byte_cache[key]

    def read_text(self, layer: Layer, relative: str, role: str) -> str:
        key = (layer.name, relative)
        data = self.read_bytes(layer, relative, role)
        if key not in self.text_cache:
            try:
                text = data.decode("utf-8-sig")
            except UnicodeDecodeError:
                text = data.decode("cp1252", errors="replace")
                self.add_finding(
                    "WARNING",
                    "input",
                    "TEXT_DECODE_FALLBACK",
                    evidence_grade="UNPROVEN",
                    source_layer=layer.name,
                    relative_path=relative,
                    detail="Decoded as cp1252 for lexical inventory after UTF-8 failed.",
                )
            self.text_cache[key] = text
        return self.text_cache[key]

    def selected(self, relative: str) -> tuple[Layer, Path] | None:
        return self.effective.get(relative)

    def run(self) -> None:
        self._scan_definitions()
        self._scan_bmp()
        self._scan_auxiliary_map_assets()
        self._scan_entities()
        self._classify_candidates()
        self._scan_railways()
        self._scan_supply_nodes()
        self._scan_adjacencies()
        self._scan_buildings()
        self._scan_unitstacks()
        self._scan_candidate_occurrences()
        self._three_way_inventory()
        self._add_limitations()

    def _scan_definitions(self) -> None:
        relative = "map/definition.csv"
        for layer in self.layers:
            if relative in layer.files:
                report = self.selected(relative)[0].name == layer.name  # type: ignore[index]
                self.definition_rows_by_layer[layer.name] = self._parse_definition(
                    layer, relative, report=report
                )
        selected = self.selected(relative)
        if selected is None:
            self.add_finding(
                "ERROR", "definition", "DEFINITION_MISSING", relative_path=relative
            )
            self.effective_definition_rows = {}
            return
        self.effective_definition_rows = self.definition_rows_by_layer[selected[0].name]
        for province_id, rows in sorted(self.effective_definition_rows.items()):
            for row in rows:
                self.occurrences.append(
                    Occurrence(
                        "province",
                        province_id,
                        selected[0].name,
                        relative,
                        row.line,
                        1,
                        "definition_id",
                        "HIGH",
                        f"{province_id};{row.rgb[0]};{row.rgb[1]};{row.rgb[2]}",
                    )
                )

    def _parse_definition(
        self, layer: Layer, relative: str, *, report: bool
    ) -> dict[int, list[DefinitionRow]]:
        text = self.read_text(layer, relative, "definition")
        rows_by_id: dict[int, list[DefinitionRow]] = defaultdict(list)
        rows_by_rgb: dict[tuple[int, int, int], list[DefinitionRow]] = defaultdict(list)
        reader = csv.reader(io.StringIO(text), delimiter=";")
        for line_number, fields in enumerate(reader, start=1):
            if not fields or all(not field.strip() for field in fields):
                continue
            if fields[0].lstrip().startswith("#"):
                continue
            if len(fields) < 8:
                if report:
                    self.add_finding(
                        "ERROR",
                        "definition",
                        "DEFINITION_FIELD_COUNT",
                        source_layer=layer.name,
                        relative_path=relative,
                        line=line_number,
                        detail=f"Expected at least 8 semicolon fields, found {len(fields)}.",
                    )
                continue
            try:
                province_id = int(fields[0].strip())
                rgb = tuple(int(fields[index].strip()) for index in (1, 2, 3))
            except ValueError:
                if report:
                    self.add_finding(
                        "ERROR",
                        "definition",
                        "DEFINITION_NON_INTEGER_ID_OR_RGB",
                        source_layer=layer.name,
                        relative_path=relative,
                        line=line_number,
                        detail="Province ID and RGB fields must be decimal integers.",
                    )
                continue
            if province_id < 0 or any(value < 0 or value > 255 for value in rgb):
                if report:
                    self.add_finding(
                        "ERROR",
                        "definition",
                        "DEFINITION_ID_OR_RGB_RANGE",
                        entity_type="province",
                        entity_id=province_id,
                        source_layer=layer.name,
                        relative_path=relative,
                        line=line_number,
                        detail=f"ID must be non-negative and RGB channels 0..255; got {rgb}.",
                    )
                continue
            row = DefinitionRow(
                province_id=province_id,
                rgb=(rgb[0], rgb[1], rgb[2]),
                province_type=fields[4].strip(),
                coastal=fields[5].strip(),
                terrain=fields[6].strip(),
                continent=fields[7].strip(),
                line=line_number,
            )
            rows_by_id[province_id].append(row)
            rows_by_rgb[row.rgb].append(row)
            if report and row.province_type not in {"land", "sea", "lake"}:
                self.add_finding(
                    "WARNING",
                    "definition",
                    "DEFINITION_UNKNOWN_TYPE",
                    evidence_grade="UNPROVEN",
                    entity_type="province",
                    entity_id=province_id,
                    source_layer=layer.name,
                    relative_path=relative,
                    line=line_number,
                    detail=f"Unrecognized static scanner type: {row.province_type!r}.",
                )
        if report:
            for province_id, rows in sorted(rows_by_id.items()):
                if len(rows) > 1:
                    self.add_finding(
                        "ERROR",
                        "definition",
                        "DEFINITION_DUPLICATE_ID",
                        entity_type="province",
                        entity_id=province_id,
                        source_layer=layer.name,
                        relative_path=relative,
                        detail="Definition lines: " + ", ".join(str(row.line) for row in rows),
                    )
                    self.candidates["province"][province_id].add("duplicate_effective_id")
                    self.candidate_sources["province"][province_id].add(layer.name)
            for rgb, rows in sorted(rows_by_rgb.items()):
                ids = sorted({row.province_id for row in rows})
                if len(rows) > 1 and not (ids == [0] and rgb == (0, 0, 0)):
                    self.add_finding(
                        "ERROR",
                        "definition",
                        "DEFINITION_DUPLICATE_RGB",
                        entity_type="province",
                        entity_id=",".join(str(value) for value in ids),
                        source_layer=layer.name,
                        relative_path=relative,
                        detail=f"RGB {rgb} occurs on lines "
                        + ", ".join(str(row.line) for row in rows),
                    )
                    for province_id in ids:
                        self.candidates["province"][province_id].add("duplicate_effective_rgb")
                        self.candidate_sources["province"][province_id].add(layer.name)
        return dict(rows_by_id)

    def _scan_bmp(self) -> None:
        relative = "map/provinces.bmp"
        selected = self.selected(relative)
        if selected is None:
            self.add_finding("ERROR", "bmp", "PROVINCES_BMP_MISSING", relative_path=relative)
            return
        layer = selected[0]
        colors_by_layer: dict[str, Counter[tuple[int, int, int]]] = {}
        inventory_layers = list(self.layers)
        if self.old_layer is not None:
            inventory_layers.append(self.old_layer)
        if self.original_layer is not None:
            inventory_layers.append(self.original_layer)
        for inventory_layer in inventory_layers:
            if relative not in inventory_layer.files:
                continue
            role = (
                "provinces_bmp"
                if inventory_layer.name == layer.name
                else "provinces_bmp_layer_inventory"
            )
            data = self.read_bytes(inventory_layer, relative, role)
            parsed_colors = self._parse_24bit_bmp(
                data, inventory_layer.name, relative
            )
            if parsed_colors is not None:
                colors_by_layer[inventory_layer.name] = parsed_colors

        colors = colors_by_layer.get(layer.name)
        if colors is None:
            return
        rgb_to_rows: dict[tuple[int, int, int], list[DefinitionRow]] = defaultdict(list)
        for rows in self.effective_definition_rows.values():
            for row in rows:
                rgb_to_rows[row.rgb].append(row)
        for rgb, count in sorted(colors.items()):
            if rgb not in rgb_to_rows:
                self.add_finding(
                    "ERROR",
                    "bmp",
                    "BMP_RGB_WITHOUT_DEFINITION",
                    source_layer=layer.name,
                    relative_path=relative,
                    detail=f"RGB {rgb} appears in {count} pixel(s) but has no valid definition row.",
                )
        for rgb, rows in sorted(rgb_to_rows.items()):
            if rgb not in colors:
                for row in rows:
                    if row.province_id == 0 and rgb == (0, 0, 0):
                        continue
                    self.add_finding(
                        "ERROR",
                        "bmp",
                        "DEFINITION_RGB_NOT_IN_BMP",
                        entity_type="province",
                        entity_id=row.province_id,
                        source_layer=layer.name,
                        relative_path=relative,
                        detail=f"Definition RGB {rgb} does not occur in provinces.bmp.",
                    )

        vanilla_colors = colors_by_layer.get("vanilla")
        if vanilla_colors is not None and layer.name != "vanilla":
            target_only = set(vanilla_colors) - set(colors)
            overlay_only = set(colors) - set(vanilla_colors)
            self.add_finding(
                "INFO",
                "bmp",
                "BMP_LAYER_RGB_SET_COMPARISON",
                source_layer=layer.name,
                relative_path=relative,
                detail=(
                    f"target_distinct_rgb={len(vanilla_colors)}; "
                    f"effective_distinct_rgb={len(colors)}; "
                    f"target_only_rgb={len(target_only)}; "
                    f"effective_only_rgb={len(overlay_only)}; geometry_identity=UNPROVEN"
                ),
            )

    def _parse_24bit_bmp(
        self, data: bytes, layer_name: str, relative: str
    ) -> Counter[tuple[int, int, int]] | None:
        if len(data) < 54 or data[:2] != b"BM":
            self.add_finding(
                "ERROR",
                "bmp",
                "BMP_INVALID_HEADER",
                source_layer=layer_name,
                relative_path=relative,
                detail="Missing BMP signature or minimum header bytes.",
            )
            return None
        try:
            declared_size = struct.unpack_from("<I", data, 2)[0]
            pixel_offset = struct.unpack_from("<I", data, 10)[0]
            dib_size = struct.unpack_from("<I", data, 14)[0]
            width = struct.unpack_from("<i", data, 18)[0]
            height = struct.unpack_from("<i", data, 22)[0]
            planes = struct.unpack_from("<H", data, 26)[0]
            bit_count = struct.unpack_from("<H", data, 28)[0]
            compression = struct.unpack_from("<I", data, 30)[0]
        except struct.error:
            self.add_finding(
                "ERROR", "bmp", "BMP_TRUNCATED_HEADER", source_layer=layer_name,
                relative_path=relative
            )
            return None
        invalid = []
        if dib_size < 40:
            invalid.append(f"DIB size {dib_size} < 40")
        if width <= 0 or height == 0:
            invalid.append(f"invalid dimensions {width}x{height}")
        if planes != 1:
            invalid.append(f"planes={planes}")
        if bit_count != 24:
            invalid.append(f"bit_count={bit_count}, expected 24")
        if compression != 0:
            invalid.append(f"compression={compression}, expected BI_RGB (0)")
        if pixel_offset < 14 + dib_size:
            invalid.append(f"pixel offset {pixel_offset} overlaps headers")
        if invalid:
            self.add_finding(
                "ERROR",
                "bmp",
                "BMP_UNSUPPORTED_FORMAT",
                source_layer=layer_name,
                relative_path=relative,
                detail="; ".join(invalid),
            )
            return None
        row_stride = ((width * 3 + 3) // 4) * 4
        required = pixel_offset + row_stride * abs(height)
        if required > len(data):
            self.add_finding(
                "ERROR",
                "bmp",
                "BMP_TRUNCATED_PIXELS",
                source_layer=layer_name,
                relative_path=relative,
                detail=f"Need at least {required} bytes, found {len(data)}.",
            )
            return None
        if declared_size not in (0, len(data)):
            self.add_finding(
                "WARNING",
                "bmp",
                "BMP_DECLARED_SIZE_MISMATCH",
                source_layer=layer_name,
                relative_path=relative,
                detail=f"Header declares {declared_size} bytes; actual size is {len(data)}.",
            )
        colors: Counter[tuple[int, int, int]] = Counter()
        pixels = memoryview(data)
        for row_index in range(abs(height)):
            start = pixel_offset + row_index * row_stride
            row = pixels[start : start + width * 3]
            for column in range(width):
                offset = column * 3
                colors[(row[offset + 2], row[offset + 1], row[offset])] += 1
        self.add_finding(
            "INFO",
            "bmp",
            "BMP_HEADER_INVENTORY",
            source_layer=layer_name,
            relative_path=relative,
            detail=(
                f"width={width}; height={height}; bit_count={bit_count}; "
                f"compression={compression}; distinct_rgb={len(colors)}"
            ),
        )
        return colors

    def _scan_auxiliary_map_assets(self) -> None:
        """Hash selected inherited/overlaid assets and inventory BMP headers only."""
        for relative in AUXILIARY_MAP_PATHS:
            selected = self.selected(relative)
            if selected is None:
                continue
            layer = selected[0]
            data = self.read_bytes(layer, relative, "auxiliary_map_inventory")
            self.add_finding(
                "INFO",
                "map_asset",
                "AUXILIARY_MAP_INPUT_INVENTORY",
                source_layer=layer.name,
                relative_path=relative,
                detail=f"Effective exact-path input hashed; size={len(data)} bytes.",
            )
            if Path(relative).suffix.casefold() == ".bmp":
                self._inventory_generic_bmp_header(data, layer.name, relative)

    def _inventory_generic_bmp_header(
        self, data: bytes, layer_name: str, relative: str
    ) -> None:
        if len(data) < 34 or data[:2] != b"BM":
            self.add_finding(
                "WARNING",
                "map_asset",
                "BMP_GENERIC_HEADER_UNREADABLE",
                evidence_grade="UNPROVEN",
                source_layer=layer_name,
                relative_path=relative,
                detail="Minimum BMP header inventory could not be read.",
            )
            return
        try:
            dib_size = struct.unpack_from("<I", data, 14)[0]
            width = struct.unpack_from("<i", data, 18)[0]
            height = struct.unpack_from("<i", data, 22)[0]
            bit_count = struct.unpack_from("<H", data, 28)[0]
            compression = struct.unpack_from("<I", data, 30)[0]
        except struct.error:
            self.add_finding(
                "WARNING",
                "map_asset",
                "BMP_GENERIC_HEADER_UNREADABLE",
                evidence_grade="UNPROVEN",
                source_layer=layer_name,
                relative_path=relative,
                detail="BMP header ended before required inventory fields.",
            )
            return
        self.add_finding(
            "INFO",
            "map_asset",
            "BMP_GENERIC_HEADER_INVENTORY",
            source_layer=layer_name,
            relative_path=relative,
            detail=(
                f"width={width}; height={height}; bit_count={bit_count}; "
                f"compression={compression}; dib_size={dib_size}; semantics=UNPROVEN"
            ),
        )

    @staticmethod
    def _lex_paradox(text: str) -> tuple[list[Token], list[ParseIssue]]:
        tokens: list[Token] = []
        issues: list[ParseIssue] = []
        index = 0
        line = 1
        column = 1
        length = len(text)
        while index < length:
            char = text[index]
            if char in " \t\r":
                index += 1
                column += 1
                continue
            if char == "\n":
                index += 1
                line += 1
                column = 1
                continue
            if char == "#":
                while index < length and text[index] != "\n":
                    index += 1
                    column += 1
                continue
            if char in "{}=":
                tokens.append(Token(char, line, column))
                index += 1
                column += 1
                continue
            if char == '"':
                start_line, start_column = line, column
                index += 1
                column += 1
                value_chars: list[str] = []
                escaped = False
                while index < length:
                    current = text[index]
                    if current == "\n":
                        line += 1
                        column = 1
                        value_chars.append(current)
                        index += 1
                        escaped = False
                        continue
                    if current == '"' and not escaped:
                        index += 1
                        column += 1
                        break
                    value_chars.append(current)
                    escaped = current == "\\" and not escaped
                    if current != "\\":
                        escaped = False
                    index += 1
                    column += 1
                else:
                    issues.append(
                        ParseIssue(
                            "ERROR",
                            "PARADOX_UNTERMINATED_QUOTE",
                            start_line,
                            start_column,
                            "Quoted string reaches end of file.",
                        )
                    )
                tokens.append(Token("".join(value_chars), start_line, start_column))
                continue
            start = index
            start_column = column
            while index < length and text[index] not in " \t\r\n{}=#\"":
                index += 1
                column += 1
            if start == index:
                index += 1
                column += 1
            else:
                tokens.append(Token(text[start:index], line, start_column))
        return tokens, issues

    def _parse_entity(self, layer: Layer, relative: str, kind: str) -> EntityParse:
        key = (layer.name, relative, kind)
        cached = self.entity_cache.get(key)
        if cached is not None:
            return cached
        text = self.read_text(layer, relative, f"{kind}_definition")
        tokens, issues = self._lex_paradox(text)
        mutable_issues = list(issues)
        stack: list[int] = []
        matching: dict[int, int] = {}
        depth_before: list[int] = []
        depth = 0
        for index, token in enumerate(tokens):
            depth_before.append(depth)
            if token.value == "{":
                stack.append(index)
                depth += 1
            elif token.value == "}":
                if not stack:
                    mutable_issues.append(
                        ParseIssue("ERROR", "PARADOX_UNMATCHED_CLOSE_BRACE", token.line, token.column, "Unmatched }.")
                    )
                else:
                    opening = stack.pop()
                    matching[opening] = index
                    depth -= 1
        for opening in stack:
            token = tokens[opening]
            mutable_issues.append(
                ParseIssue("ERROR", "PARADOX_UNMATCHED_OPEN_BRACE", token.line, token.column, "Unmatched {.")
            )

        root_name = ENTITY_ROOTS[kind][1]
        records: list[EntityRecord] = []
        index = 0
        while index + 2 < len(tokens):
            if (
                depth_before[index] == 0
                and tokens[index].value == root_name
                and tokens[index + 1].value == "="
                and tokens[index + 2].value == "{"
            ):
                opening = index + 2
                closing = matching.get(opening)
                if closing is None:
                    index += 3
                    continue
                internal_values: list[Token] = []
                members: list[Member] = []
                cursor = opening + 1
                while cursor < closing:
                    if depth_before[cursor] != 1:
                        cursor += 1
                        continue
                    token = tokens[cursor]
                    if token.value == "id" and cursor + 2 < closing and tokens[cursor + 1].value == "=":
                        internal_values.append(tokens[cursor + 2])
                        cursor += 3
                        continue
                    if (
                        token.value == "provinces"
                        and cursor + 2 < closing
                        and tokens[cursor + 1].value == "="
                        and tokens[cursor + 2].value == "{"
                    ):
                        member_open = cursor + 2
                        member_close = matching.get(member_open)
                        if member_close is None or member_close > closing:
                            cursor += 3
                            continue
                        for member_token in tokens[member_open + 1 : member_close]:
                            if re.fullmatch(r"-?\d+", member_token.value):
                                members.append(Member(int(member_token.value), member_token.line, member_token.column))
                            elif member_token.value not in {"{", "}", "="}:
                                mutable_issues.append(
                                    ParseIssue(
                                        "ERROR",
                                        "ENTITY_NON_INTEGER_MEMBER",
                                        member_token.line,
                                        member_token.column,
                                        f"Non-integer token in provinces block: {member_token.value!r}.",
                                    )
                                )
                        cursor = member_close + 1
                        continue
                    cursor += 1
                internal_id: int | None = None
                id_line = tokens[index].line
                id_column = tokens[index].column
                if not internal_values:
                    mutable_issues.append(
                        ParseIssue("ERROR", "ENTITY_MISSING_ID", tokens[index].line, tokens[index].column, f"{root_name} block has no direct id assignment.")
                    )
                else:
                    if len(internal_values) > 1:
                        mutable_issues.append(
                            ParseIssue("ERROR", "ENTITY_MULTIPLE_IDS", internal_values[1].line, internal_values[1].column, f"{root_name} block has multiple direct id assignments.")
                        )
                    value = internal_values[0]
                    id_line, id_column = value.line, value.column
                    if re.fullmatch(r"\d+", value.value):
                        internal_id = int(value.value)
                    else:
                        mutable_issues.append(
                            ParseIssue("ERROR", "ENTITY_NON_INTEGER_ID", value.line, value.column, f"Entity id is not a non-negative integer: {value.value!r}.")
                        )
                if not members:
                    mutable_issues.append(
                        ParseIssue("WARNING", "ENTITY_EMPTY_PROVINCES", tokens[index].line, tokens[index].column, f"{root_name} block has no parsed province members.")
                    )
                records.append(
                    EntityRecord(
                        kind=kind,
                        internal_id=internal_id,
                        id_line=id_line,
                        id_column=id_column,
                        members=tuple(members),
                        source_layer=layer.name,
                        relative_path=relative,
                    )
                )
                index = closing + 1
                continue
            index += 1
        if not records:
            mutable_issues.append(
                ParseIssue("ERROR", "ENTITY_ROOT_BLOCK_NOT_FOUND", 1, 1, f"No top-level {root_name} = {{ ... }} block was parsed.")
            )
        result = EntityParse(tuple(records), tuple(mutable_issues))
        self.entity_cache[key] = result
        return result

    def _scan_entities(self) -> None:
        self.effective_state_records = self._effective_entity_records("state")
        self.effective_region_records = self._effective_entity_records("strategic_region")
        self._validate_entity_set("state", self.effective_state_records)
        self._validate_entity_set("strategic_region", self.effective_region_records)

    def _effective_entity_records(self, kind: str) -> list[EntityRecord]:
        prefix = ENTITY_ROOTS[kind][0]
        records: list[EntityRecord] = []
        for relative in sorted(self.effective):
            if not relative.startswith(prefix) or Path(relative).suffix.lower() != ".txt":
                continue
            layer = self.effective[relative][0]
            parsed = self._parse_entity(layer, relative, kind)
            records.extend(parsed.records)
            for issue in parsed.issues:
                self.add_finding(
                    issue.severity,
                    kind,
                    issue.code,
                    source_layer=layer.name,
                    relative_path=relative,
                    line=issue.line,
                    column=issue.column,
                    detail=issue.detail,
                )
        return records

    def _validate_entity_set(self, kind: str, records: Sequence[EntityRecord]) -> None:
        by_id: dict[int, list[EntityRecord]] = defaultdict(list)
        membership: dict[int, list[tuple[EntityRecord, Member]]] = defaultdict(list)
        entity_label = "state" if kind == "state" else "strategic_region"
        for record in records:
            if record.internal_id is not None:
                by_id[record.internal_id].append(record)
                self.occurrences.append(
                    Occurrence(
                        entity_label,
                        record.internal_id,
                        record.source_layer,
                        record.relative_path,
                        record.id_line,
                        record.id_column,
                        f"{entity_label}_definition_id",
                        "HIGH",
                        f"id={record.internal_id}",
                    )
                )
            for member in record.members:
                membership[member.entity_id].append((record, member))
                self.occurrences.append(
                    Occurrence(
                        "province",
                        member.entity_id,
                        record.source_layer,
                        record.relative_path,
                        member.line,
                        member.column,
                        f"{entity_label}_province_membership",
                        "HIGH",
                        str(member.entity_id),
                    )
                )
                if member.entity_id not in self.effective_definition_rows:
                    self.add_finding(
                        "ERROR",
                        kind,
                        f"{kind.upper()}_UNKNOWN_PROVINCE",
                        entity_type="province",
                        entity_id=member.entity_id,
                        source_layer=record.source_layer,
                        relative_path=record.relative_path,
                        line=member.line,
                        column=member.column,
                        detail=f"Province is referenced by {entity_label} but absent from effective definition.csv.",
                    )
        for internal_id, definitions in sorted(by_id.items()):
            if len(definitions) > 1:
                sources = ", ".join(
                    f"{record.source_layer}:{record.relative_path}" for record in definitions
                )
                self.add_finding(
                    "ERROR",
                    kind,
                    f"DUPLICATE_{kind.upper()}_ID",
                    entity_type=entity_label,
                    entity_id=internal_id,
                    detail=f"Effective definitions: {sources}",
                )
                if kind == "state":
                    self.candidates["state"][internal_id].add("duplicate_effective_id")
                    self.candidate_sources["state"][internal_id].update(
                        record.source_layer for record in definitions
                    )

        if kind == "state" and by_id:
            maximum_state_id = max(by_id)
            for missing_state_id in sorted(
                set(range(1, maximum_state_id + 1)).difference(by_id)
            ):
                self.add_finding(
                    "ERROR",
                    "state",
                    "MISSING_STATE_ID",
                    entity_type="state",
                    entity_id=missing_state_id,
                    detail=(
                        "No parsed effective state definition has this ID; "
                        "effective state IDs must be continuous from 1 through "
                        f"{maximum_state_id}."
                    ),
                )

        if kind == "state":
            required_ids = {
                province_id
                for province_id, rows in self.effective_definition_rows.items()
                if any(row.province_type == "land" for row in rows) and province_id != 0
            }
        else:
            required_ids = {
                province_id for province_id in self.effective_definition_rows if province_id != 0
            }
        for province_id in sorted(required_ids):
            owners = membership.get(province_id, [])
            if not owners:
                self.add_finding(
                    "ERROR",
                    kind,
                    "LAND_PROVINCE_MISSING_STATE" if kind == "state" else "PROVINCE_MISSING_STRATEGIC_REGION",
                    entity_type="province",
                    entity_id=province_id,
                    detail=f"No effective {entity_label} membership was parsed.",
                )
            else:
                by_owner: dict[
                    tuple[str, str, int | None, int],
                    list[tuple[EntityRecord, Member]],
                ] = defaultdict(list)
                for record, member in owners:
                    owner_key = (
                        record.source_layer,
                        record.relative_path,
                        record.internal_id,
                        record.id_line,
                    )
                    by_owner[owner_key].append((record, member))
                duplicate_code = (
                    "STATE_DUPLICATE_PROVINCE_MEMBERSHIP"
                    if kind == "state"
                    else "STRATEGIC_REGION_DUPLICATE_PROVINCE_MEMBERSHIP"
                )
                for duplicate_occurrences in by_owner.values():
                    if len(duplicate_occurrences) <= 1:
                        continue
                    record = duplicate_occurrences[0][0]
                    self.add_finding(
                        "ERROR",
                        kind,
                        duplicate_code,
                        entity_type="province",
                        entity_id=province_id,
                        source_layer=record.source_layer,
                        relative_path=record.relative_path,
                        line=duplicate_occurrences[0][1].line,
                        column=duplicate_occurrences[0][1].column,
                        detail=(
                            "The same provinces block repeats this province at "
                            + ", ".join(
                                f"{member.line}:{member.column}"
                                for _, member in duplicate_occurrences
                            )
                        ),
                    )
                if len(by_owner) <= 1:
                    continue
                detail = ", ".join(
                    f"{record.relative_path}:{member.line}"
                    for record, member in (
                        occurrences[0] for occurrences in by_owner.values()
                    )
                )
                self.add_finding(
                    "ERROR",
                    kind,
                    "LAND_PROVINCE_MULTIPLE_STATES" if kind == "state" else "PROVINCE_MULTIPLE_STRATEGIC_REGIONS",
                    entity_type="province",
                    entity_id=province_id,
                    detail=f"Membership occurrences: {detail}",
                )
        if kind == "state":
            land_ids = required_ids
            for province_id, owners in sorted(membership.items()):
                if province_id in self.effective_definition_rows and province_id not in land_ids:
                    for record, member in owners:
                        self.add_finding(
                            "ERROR",
                            "state",
                            "STATE_NONLAND_PROVINCE",
                            entity_type="province",
                            entity_id=province_id,
                            source_layer=record.source_layer,
                            relative_path=record.relative_path,
                            line=member.line,
                            column=member.column,
                            detail="State provinces block includes a definition not typed as land.",
                        )

    def _classify_candidates(self) -> None:
        vanilla_defs = self.definition_rows_by_layer.get("vanilla", {})
        vanilla_rgb: dict[tuple[int, int, int], set[int]] = defaultdict(set)
        for province_id, rows in vanilla_defs.items():
            for row in rows:
                vanilla_rgb[row.rgb].add(province_id)
        selected_definition = self.selected("map/definition.csv")
        definition_layers = (
            [selected_definition[0]]
            if selected_definition is not None
            and selected_definition[0].name != "vanilla"
            else []
        )
        for layer in definition_layers:
            for province_id, rows in sorted(self.definition_rows_by_layer.get(layer.name, {}).items()):
                for row in rows:
                    if province_id not in vanilla_defs:
                        classification = "custom"
                        self.add_finding(
                            "INFO",
                            "candidate",
                            "CUSTOM_PROVINCE_ID",
                            entity_type="province",
                            entity_id=province_id,
                            source_layer=layer.name,
                            relative_path="map/definition.csv",
                            line=row.line,
                            detail="ID is present in this overlay definition and absent from target vanilla definition.",
                        )
                    elif all(row.comparable() != base.comparable() for base in vanilla_defs[province_id]):
                        classification = "overlap_different_definition"
                        self.add_finding(
                            "WARNING",
                            "candidate",
                            "PROVINCE_ID_OVERLAP_DIFFERENT",
                            evidence_grade="STRONGLY_SUPPORTED",
                            entity_type="province",
                            entity_id=province_id,
                            source_layer=layer.name,
                            relative_path="map/definition.csv",
                            line=row.line,
                            detail="Same ID has different static definition fields in target vanilla and overlay; geographic identity is not inferred.",
                        )
                    else:
                        continue
                    self.candidates["province"][province_id].add(classification)
                    self.candidate_sources["province"][province_id].add(layer.name)
                    other_ids = vanilla_rgb.get(row.rgb, set()) - {province_id}
                    if other_ids:
                        self.candidates["province"][province_id].add("rgb_used_by_other_vanilla_id")
                        self.add_finding(
                            "WARNING",
                            "candidate",
                            "PROVINCE_RGB_OVERLAP_OTHER_ID",
                            evidence_grade="STRONGLY_SUPPORTED",
                            entity_type="province",
                            entity_id=province_id,
                            source_layer=layer.name,
                            relative_path="map/definition.csv",
                            line=row.line,
                            detail=f"RGB {row.rgb} belongs to target vanilla ID(s) {sorted(other_ids)}.",
                        )

        vanilla_states = self._layer_entity_ids(
            self.layer_by_name["vanilla"], "state", include_shadowed=True
        )
        effective_upper_states: dict[str, dict[int, list[EntityRecord]]] = defaultdict(
            lambda: defaultdict(list)
        )
        for record in self.effective_state_records:
            if record.source_layer == "vanilla" or record.internal_id is None:
                continue
            effective_upper_states[record.source_layer][record.internal_id].append(record)
        for layer in self.layers:
            if layer.name == "vanilla":
                continue
            upper_states = effective_upper_states.get(layer.name, {})
            for state_id, records in sorted(upper_states.items()):
                classification = "overlap" if state_id in vanilla_states else "custom"
                self.candidates["state"][state_id].add(classification)
                self.candidate_sources["state"][state_id].add(layer.name)
                code = "STATE_ID_OVERLAP" if classification == "overlap" else "CUSTOM_STATE_ID"
                severity = "WARNING" if classification == "overlap" else "INFO"
                grade = "UNPROVEN" if classification == "overlap" else "CONFIRMED"
                for record in records:
                    self.add_finding(
                        severity,
                        "candidate",
                        code,
                        evidence_grade=grade,
                        entity_type="state",
                        entity_id=state_id,
                        source_layer=layer.name,
                        relative_path=record.relative_path,
                        line=record.id_line,
                        detail=(
                            "ID also exists in target vanilla; semantic/geographic conflict is not inferred."
                            if classification == "overlap"
                            else "ID is absent from parsed target vanilla state definitions."
                        ),
                    )

    def _layer_entity_ids(
        self, layer: Layer, kind: str, *, include_shadowed: bool = False
    ) -> dict[int, list[EntityRecord]]:
        result: dict[int, list[EntityRecord]] = defaultdict(list)
        prefix = ENTITY_ROOTS[kind][0]
        for relative in sorted(layer.files):
            if relative.startswith(prefix) and Path(relative).suffix.lower() == ".txt":
                if not include_shadowed and self._effective_status(layer, relative)[0] != "yes":
                    continue
                parsed = self._parse_entity(layer, relative, kind)
                for record in parsed.records:
                    if record.internal_id is not None:
                        result[record.internal_id].append(record)
                        entity_type = "state" if kind == "state" else "strategic_region"
                        self.occurrences.append(
                            Occurrence(
                                entity_type,
                                record.internal_id,
                                layer.name,
                                relative,
                                record.id_line,
                                record.id_column,
                                f"source_{entity_type}_definition_id",
                                "HIGH",
                                f"id={record.internal_id}",
                            )
                        )
                    for member in record.members:
                        self.occurrences.append(
                            Occurrence(
                                "province",
                                member.entity_id,
                                layer.name,
                                relative,
                                member.line,
                                member.column,
                                f"source_{entity_type}_province_membership",
                                "HIGH",
                                str(member.entity_id),
                            )
                        )
        return result

    @staticmethod
    def _content_lines(text: str) -> Iterable[tuple[int, str]]:
        for line_number, raw in enumerate(text.splitlines(), start=1):
            content = raw.split("#", 1)[0].rstrip()
            if content.strip():
                yield line_number, content

    @staticmethod
    def _token_columns(line: str) -> list[tuple[str, int]]:
        return [(match.group(0), match.start() + 1) for match in re.finditer(r"\S+", line)]

    def _known_province(self, value: int) -> bool:
        return value in self.effective_definition_rows and value != 0

    def _land_province(self, value: int) -> bool:
        return self._known_province(value) and any(
            row.province_type == "land" for row in self.effective_definition_rows[value]
        )

    def _effective_state_ids(self) -> set[int]:
        return {
            record.internal_id
            for record in self.effective_state_records
            if record.internal_id is not None
        }

    def _scan_railways(self) -> None:
        relative = "map/railways.txt"
        selected = self.selected(relative)
        if selected is None:
            self.add_finding("ERROR", "railway", "RAILWAYS_MISSING", relative_path=relative)
            return
        layer = selected[0]
        text = self.read_text(layer, relative, "railways")
        for line_number, content in self._content_lines(text):
            matches = list(re.finditer(r"\S+", content))
            tokens = [match.group(0) for match in matches]
            try:
                numbers = [int(token) for token in tokens]
            except ValueError:
                self.add_finding(
                    "ERROR", "railway", "RAILWAY_NON_INTEGER", source_layer=layer.name,
                    relative_path=relative, line=line_number, detail=content
                )
                continue
            if len(numbers) < 3:
                self.add_finding(
                    "ERROR", "railway", "RAILWAY_FIELD_COUNT", source_layer=layer.name,
                    relative_path=relative, line=line_number,
                    detail="Expected level, declared path length, and at least one province."
                )
                continue
            level, declared, *provinces = numbers
            if level <= 0:
                self.add_finding(
                    "ERROR", "railway", "RAILWAY_INVALID_LEVEL", source_layer=layer.name,
                    relative_path=relative, line=line_number, detail=f"level={level}"
                )
            if declared != len(provinces):
                self.add_finding(
                    "ERROR", "railway", "RAILWAY_DECLARED_LENGTH_MISMATCH",
                    source_layer=layer.name, relative_path=relative, line=line_number,
                    detail=f"declared={declared}; parsed={len(provinces)}"
                )
            for offset, province_id in enumerate(provinces, start=2):
                column = matches[offset].start() + 1 if offset < len(matches) else 1
                self.occurrences.append(
                    Occurrence("province", province_id, layer.name, relative, line_number, column, "railway_path", "HIGH", content)
                )
                if not self._known_province(province_id):
                    self.add_finding(
                        "ERROR", "railway", "RAILWAY_UNKNOWN_PROVINCE", entity_type="province",
                        entity_id=province_id, source_layer=layer.name, relative_path=relative,
                        line=line_number, column=column, detail=content
                    )
                elif not self._land_province(province_id):
                    self.add_finding(
                        "ERROR", "railway", "RAILWAY_NONLAND_PROVINCE", entity_type="province",
                        entity_id=province_id, source_layer=layer.name, relative_path=relative,
                        line=line_number, column=column, detail=content
                    )

    def _scan_supply_nodes(self) -> None:
        relative = "map/supply_nodes.txt"
        selected = self.selected(relative)
        if selected is None:
            self.add_finding("ERROR", "supply", "SUPPLY_NODES_MISSING", relative_path=relative)
            return
        layer = selected[0]
        text = self.read_text(layer, relative, "supply_nodes")
        for line_number, content in self._content_lines(text):
            matches = list(re.finditer(r"\S+", content))
            tokens = [match.group(0) for match in matches]
            if len(tokens) != 2:
                self.add_finding(
                    "ERROR", "supply", "SUPPLY_NODE_FIELD_COUNT", source_layer=layer.name,
                    relative_path=relative, line=line_number,
                    detail=f"Expected exactly 2 integer fields; got {len(tokens)}."
                )
                continue
            try:
                level, province_id = (int(token) for token in tokens)
            except ValueError:
                self.add_finding(
                    "ERROR", "supply", "SUPPLY_NODE_NON_INTEGER", source_layer=layer.name,
                    relative_path=relative, line=line_number, detail=content
                )
                continue
            column = matches[1].start() + 1
            self.occurrences.append(
                Occurrence("province", province_id, layer.name, relative, line_number, column, "supply_node", "HIGH", content)
            )
            if level <= 0:
                self.add_finding(
                    "ERROR", "supply", "SUPPLY_NODE_INVALID_LEVEL", source_layer=layer.name,
                    relative_path=relative, line=line_number, detail=f"level={level}"
                )
            if not self._known_province(province_id):
                self.add_finding(
                    "ERROR", "supply", "SUPPLY_NODE_UNKNOWN_PROVINCE", entity_type="province",
                    entity_id=province_id, source_layer=layer.name, relative_path=relative,
                    line=line_number, column=column, detail=content
                )
            elif not self._land_province(province_id):
                self.add_finding(
                    "ERROR", "supply", "SUPPLY_NODE_NONLAND_PROVINCE", entity_type="province",
                    entity_id=province_id, source_layer=layer.name, relative_path=relative,
                    line=line_number, column=column, detail=content
                )

    def _scan_adjacencies(self) -> None:
        relative = "map/adjacencies.csv"
        selected = self.selected(relative)
        if selected is None:
            self.add_finding("ERROR", "adjacency", "ADJACENCIES_MISSING", relative_path=relative)
            return
        layer = selected[0]
        text = self.read_text(layer, relative, "adjacencies")
        parsed_rows: list[tuple[int, list[str], str]] = []
        for line_number, raw in enumerate(text.splitlines(), start=1):
            if not raw.strip() or raw.lstrip().startswith("#"):
                continue
            fields = next(csv.reader([raw], delimiter=";"))
            if fields and fields[0].strip().casefold() == "from":
                continue
            parsed_rows.append((line_number, fields, raw))
        terminators = 0
        for row_index, (line_number, fields, raw) in enumerate(parsed_rows):
            if len(fields) < 4:
                self.add_finding(
                    "ERROR", "adjacency", "ADJACENCY_FIELD_COUNT", source_layer=layer.name,
                    relative_path=relative, line=line_number,
                    detail=f"Expected at least 4 semicolon fields, found {len(fields)}."
                )
                continue
            try:
                from_id = int(fields[0].strip())
                to_id = int(fields[1].strip())
                through_id = int(fields[3].strip())
            except ValueError:
                self.add_finding(
                    "ERROR", "adjacency", "ADJACENCY_NON_INTEGER_ENDPOINT", source_layer=layer.name,
                    relative_path=relative, line=line_number, detail=raw
                )
                continue
            if from_id == -1 and to_id == -1:
                terminators += 1
                if row_index != len(parsed_rows) - 1:
                    self.add_finding(
                        "ERROR", "adjacency", "ADJACENCY_SENTINEL_NOT_LAST", source_layer=layer.name,
                        relative_path=relative, line=line_number,
                        detail="The -1/-1 terminator is followed by another data row."
                    )
                continue
            if (from_id == -1) != (to_id == -1):
                self.add_finding(
                    "ERROR", "adjacency", "ADJACENCY_PARTIAL_SENTINEL", source_layer=layer.name,
                    relative_path=relative, line=line_number, detail=raw
                )
            for field_index, (label, province_id) in enumerate(
                (("from", from_id), ("to", to_id), ("through", through_id))
            ):
                if label == "through" and province_id == -1:
                    continue
                column = 1 + sum(len(value) + 1 for value in fields[: (0, 1, 3)[field_index]])
                self.occurrences.append(
                    Occurrence("province", province_id, layer.name, relative, line_number, column, f"adjacency_{label}", "HIGH", raw)
                )
                if not self._known_province(province_id):
                    self.add_finding(
                        "ERROR", "adjacency", "ADJACENCY_UNKNOWN_PROVINCE", entity_type="province",
                        entity_id=province_id, source_layer=layer.name, relative_path=relative,
                        line=line_number, column=column, detail=f"field={label}; {raw}"
                    )
        if terminators == 0:
            self.add_finding(
                "WARNING", "adjacency", "ADJACENCY_TERMINATOR_NOT_FOUND",
                evidence_grade="UNPROVEN", source_layer=layer.name, relative_path=relative,
                detail="No final -1;-1 sentinel row was parsed; exact target-version requirement remains unproven."
            )

    def _scan_buildings(self) -> None:
        relative = "map/buildings.txt"
        selected = self.selected(relative)
        if selected is None:
            self.add_finding("ERROR", "buildings", "BUILDINGS_MISSING", relative_path=relative)
            return
        layer = selected[0]
        data = self.read_bytes(layer, relative, "buildings")
        if data.endswith(b"\n"):
            line_ending = "CRLF" if data.endswith(b"\r\n") else "LF"
            self.add_finding(
                "ERROR", "buildings", "BUILDINGS_TRAILING_NEWLINE",
                source_layer=layer.name, relative_path=relative,
                line=data.count(b"\n") + 1, column=1,
                detail=(
                    f"Effective buildings file ends with {line_ending}; HOI4 1.19.2 "
                    "-debug parses the resulting empty final row and reports an invalid "
                    "argument count. End the file at the final data byte."
                ),
            )
        text = self.read_text(layer, relative, "buildings")
        states = self._effective_state_ids()
        air_base_states: set[int] = set()
        rocket_site_states: set[int] = set()
        for line_number, content in self._content_lines(text):
            fields = content.split(";")
            column = len(content) - len(content.lstrip()) + 1
            try:
                state_id = int(fields[0].strip())
            except (ValueError, IndexError):
                self.add_finding(
                    "ERROR", "buildings", "BUILDING_INVALID_STATE_ID", source_layer=layer.name,
                    relative_path=relative, line=line_number, detail=content
                )
                continue
            self.occurrences.append(
                Occurrence("state", state_id, layer.name, relative, line_number, column, "building_top_level_state", "HIGH", content)
            )
            if state_id not in states:
                self.add_finding(
                    "ERROR", "buildings", "BUILDING_UNKNOWN_STATE", entity_type="state",
                    entity_id=state_id, source_layer=layer.name, relative_path=relative,
                    line=line_number, column=column, detail=content
                )
            building_type = fields[1].strip() if len(fields) > 1 else ""
            if building_type == "air_base":
                air_base_states.add(state_id)
            elif building_type == "rocket_site_spawn":
                rocket_site_states.add(state_id)
        for state_id in sorted(states - air_base_states):
            self.add_finding(
                "ERROR", "buildings", "BUILDING_MISSING_AIR_BASE_SITE",
                entity_type="state", entity_id=state_id, source_layer=layer.name,
                relative_path=relative,
                detail=(
                    "Effective state has no air_base row keyed by its state ID in "
                    "the effective map/buildings.txt."
                ),
            )
        for state_id in sorted(states - rocket_site_states):
            self.add_finding(
                "ERROR", "buildings", "BUILDING_MISSING_ROCKET_SITE_SPAWN",
                entity_type="state", entity_id=state_id, source_layer=layer.name,
                relative_path=relative,
                detail=(
                    "Effective state has no rocket_site_spawn row keyed by its state ID "
                    "in the effective map/buildings.txt; HOI4 uses this spawn point for "
                    "both rocket sites and mega gun emplacements."
                ),
            )

    def _scan_unitstacks(self) -> None:
        relative = "map/unitstacks.txt"
        selected = self.selected(relative)
        if selected is None:
            self.add_finding("ERROR", "unitstacks", "UNITSTACKS_MISSING", relative_path=relative)
            return
        layer = selected[0]
        text = self.read_text(layer, relative, "unitstacks")
        previous_key: tuple[int, int] | None = None
        previous_line = 0
        for line_number, content in self._content_lines(text):
            fields = content.split(";")
            column = len(content) - len(content.lstrip()) + 1
            try:
                province_id = int(fields[0].strip())
            except (ValueError, IndexError):
                self.add_finding(
                    "ERROR", "unitstacks", "UNITSTACK_INVALID_PROVINCE_ID",
                    source_layer=layer.name, relative_path=relative, line=line_number,
                    detail=content
                )
                continue
            self.occurrences.append(
                Occurrence("province", province_id, layer.name, relative, line_number, column, "unitstack_top_level_province", "HIGH", content)
            )
            if not self._known_province(province_id):
                self.add_finding(
                    "ERROR", "unitstacks", "UNITSTACK_UNKNOWN_PROVINCE", entity_type="province",
                    entity_id=province_id, source_layer=layer.name, relative_path=relative,
                    line=line_number, column=column, detail=content
                )
            try:
                slot = int(fields[1].strip())
            except (ValueError, IndexError):
                continue
            key = (slot, province_id)
            if previous_key is not None and key <= previous_key:
                self.add_finding(
                    "ERROR", "unitstacks", "UNITSTACK_ORDER_INVERSION",
                    source_layer=layer.name, relative_path=relative,
                    line=line_number, column=column,
                    detail=(
                        "Rows must be strictly increasing by (slot, province): "
                        f"previous line {previous_line} key={previous_key}; "
                        f"current key={key}."
                    ),
                )
            previous_key = key
            previous_line = line_number

    def _scan_candidate_occurrences(self) -> None:
        candidate_union = set(self.candidates["province"]) | set(self.candidates["state"])
        if not candidate_union:
            return
        number_pattern = re.compile(r"(?<!\d)(\d+)(?!\d)")
        for relative in sorted(self.effective):
            layer = self.effective[relative][0]
            for match in number_pattern.finditer(relative):
                value = int(match.group(1))
                if value not in candidate_union:
                    continue
                possible = {
                    entity_type
                    for entity_type in ("province", "state")
                    if value in self.candidates[entity_type]
                }
                for entity_type in possible:
                    self.occurrences.append(
                        Occurrence(
                            entity_type,
                            value,
                            layer.name,
                            relative,
                            0,
                            match.start() + 1,
                            "relative_path_numeric_candidate",
                            "LOW",
                            relative,
                        )
                    )
            if Path(relative).suffix.lower() not in TEXT_SUFFIXES:
                continue
            text = self.read_text(layer, relative, "candidate_reference_scan")
            for line_number, raw in enumerate(text.splitlines(), start=1):
                for match in number_pattern.finditer(raw):
                    value = int(match.group(1))
                    if value not in candidate_union:
                        continue
                    possible = {
                        entity_type
                        for entity_type in ("province", "state")
                        if value in self.candidates[entity_type]
                    }
                    selected_types, context, confidence = self._classify_lexical_context(
                        raw, match.start(), value, possible, relative
                    )
                    snippet = raw.strip()[:240]
                    for entity_type in selected_types:
                        self.occurrences.append(
                            Occurrence(
                                entity_type,
                                value,
                                layer.name,
                                relative,
                                line_number,
                                match.start() + 1,
                                context,
                                confidence,
                                snippet,
                            )
                        )

    @staticmethod
    def _classify_lexical_context(
        raw: str,
        start: int,
        value: int,
        possible: set[str],
        relative: str,
    ) -> tuple[set[str], str, str]:
        before_comment = raw.split("#", 1)[0]
        in_comment = start >= len(before_comment) and "#" in raw
        if in_comment:
            return possible, "comment_numeric_candidate", "LOW"
        prefix = before_comment[:start].casefold()
        if re.search(r"state_$", prefix):
            return ({"state"} & possible, "state_localisation_token", "HIGH")
        if re.search(r"(?:victory_points|vp)_$", prefix):
            return ({"province"} & possible, "victory_point_localisation_token", "HIGH")
        window = before_comment[
            max(0, start - 80) : start + len(str(value)) + 80
        ].casefold()
        has_state = bool(re.search(r"\bstate(?:_id)?\b", window))
        has_province = bool(re.search(r"\bprovince(?:_id|s)?\b", window))
        if has_state and not has_province and "state" in possible:
            return {"state"}, "state_keyword_lexical", "MEDIUM"
        if has_province and not has_state and "province" in possible:
            return {"province"}, "province_keyword_lexical", "MEDIUM"
        if len(possible) == 1:
            only = next(iter(possible))
            return possible, f"{only}_candidate_numeric", "LOW"
        return possible, "ambiguous_numeric_candidate", "LOW"

    def _three_way_inventory(self) -> None:
        if self.old_layer is None or self.original_layer is None:
            return
        relevant = set()
        for layer in (
            self.old_layer,
            self.original_layer,
            self.layer_by_name["vanilla"],
        ):
            relevant.update(
                relative
                for relative in layer.files
                if relative.startswith("map/") or relative.startswith("history/states/")
            )
        for relative in sorted(relevant):
            hashes: dict[str, str] = {}
            present: dict[str, str] = {}
            for label, layer in (
                ("old", self.old_layer),
                ("original", self.original_layer),
                ("target", self.layer_by_name["vanilla"]),
            ):
                if relative in layer.files:
                    data = self.read_bytes(layer, relative, "three_way_inventory")
                    hashes[label] = hashlib.sha256(data).hexdigest()
                    present[label] = "yes"
                else:
                    hashes[label] = ""
                    present[label] = "no"
            def relation(left: str, right: str) -> str:
                if not hashes[left] or not hashes[right]:
                    return "missing"
                return "same" if hashes[left] == hashes[right] else "different"
            self.three_way_rows.append(
                {
                    "relative_path": relative,
                    "old_present": present["old"],
                    "original_present": present["original"],
                    "target_present": present["target"],
                    "old_sha256": hashes["old"],
                    "original_sha256": hashes["original"],
                    "target_sha256": hashes["target"],
                    "old_vs_original": relation("old", "original"),
                    "old_vs_target": relation("old", "target"),
                    "original_vs_target": relation("original", "target"),
                }
            )

    def _add_limitations(self) -> None:
        self.add_finding(
            "INFO",
            "compatibility",
            "RUNTIME_COMPATIBILITY_UNPROVEN",
            evidence_grade="UNPROVEN",
            detail="Static inventory does not prove discovery, engine parsing, runtime evaluation, map rendering, save compatibility, or multiplayer synchronization.",
        )
        limitations = [
            (
                "EXACT_PATH_OVERLAY_LIMITATION",
                "VFS simulation uses exact relative-path replacement only; replace_path, launcher discovery, directory-specific merge rules, and platform case behavior are not modeled.",
            ),
            (
                "PARADOX_PARSER_LIMITATION",
                "The bounded lexer extracts top-level state/strategic_region ids and provinces blocks; it is not the HOI4 parser and does not validate arbitrary script scope or semantics.",
            ),
            (
                "GEOMETRY_LIMITATION",
                "RGB presence is checked, but connected components, coastal topology, pixel adjacency, railway continuity, coordinates, and inherited bitmap alignment are not proven.",
            ),
            (
                "REFERENCE_SCAN_LIMITATION",
                "General references are lexical candidates with explicit confidence; low-confidence numeric occurrences can be quantities, dates, comments, or unrelated IDs.",
            ),
            (
                "THREE_WAY_LIMITATION",
                "Three-way output requires manifest-verified V_OLD and HOK_ORIGINAL content, but their version/build labels remain user-supplied; the output compares file presence and SHA-256 only and does not derive or apply INTENDED_DELTA.",
            ),
        ]
        for code, detail in limitations:
            self.add_finding(
                "INFO", "limitation", code, evidence_grade="UNPROVEN", detail=detail
            )

    @staticmethod
    def _finding_sort_key(item: Finding) -> tuple[object, ...]:
        severity_order = {"ERROR": 0, "WARNING": 1, "INFO": 2}
        line = item.line if isinstance(item.line, int) else -1
        column = item.column if isinstance(item.column, int) else -1
        try:
            entity_numeric = int(item.entity_id)
        except (TypeError, ValueError):
            entity_numeric = -1
        return (
            severity_order.get(item.severity, 9),
            item.category,
            item.code,
            item.entity_type,
            entity_numeric,
            item.entity_id,
            item.source_layer,
            item.relative_path,
            line,
            column,
            item.detail,
        )

    def _reference_rows(self) -> list[dict[str, str]]:
        grouped: dict[tuple[object, ...], list[Occurrence]] = defaultdict(list)
        for occurrence in self.occurrences:
            if occurrence.entity_id not in self.candidates.get(occurrence.entity_type, {}):
                continue
            key = (
                occurrence.entity_type,
                occurrence.entity_id,
                occurrence.source_layer,
                occurrence.relative_path,
                occurrence.line,
                occurrence.column,
            )
            grouped[key].append(occurrence)

        confidence_order = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}
        rows: dict[tuple[object, ...], dict[str, str]] = {}
        for key, occurrences in grouped.items():
            occurrence = occurrences[0]
            classes = ";".join(
                sorted(self.candidates[occurrence.entity_type][occurrence.entity_id])
            )
            candidate_sources = ";".join(
                sorted(self.candidate_sources[occurrence.entity_type][occurrence.entity_id])
            )
            contexts = ";".join(sorted({item.context for item in occurrences}))
            confidence = max(
                (item.confidence for item in occurrences),
                key=lambda value: confidence_order.get(value, -1),
            )
            snippets = {item.snippet for item in occurrences if item.snippet}
            snippet = min(snippets, key=lambda value: (-len(value), value)) if snippets else ""
            source_layer = self.layer_by_name.get(occurrence.source_layer)
            if source_layer is None:
                effective, shadowed_by = "unknown", ""
            else:
                effective, shadowed_by = self._effective_status(
                    source_layer, occurrence.relative_path
                )
            rows[key] = {
                "entity_type": occurrence.entity_type,
                "entity_id": str(occurrence.entity_id),
                "candidate_class": classes,
                "candidate_source_layers": candidate_sources,
                "source_layer": occurrence.source_layer,
                "effective": effective,
                "shadowed_by": shadowed_by,
                "relative_path": occurrence.relative_path,
                "line": str(occurrence.line),
                "column": str(occurrence.column),
                "context": contexts,
                "confidence": confidence,
                "snippet": snippet,
            }
        return [rows[key] for key in sorted(rows)]

    @staticmethod
    def _write_tsv(path: Path, fieldnames: Sequence[str], rows: Iterable[dict[str, object]]) -> None:
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=fieldnames,
                delimiter="\t",
                lineterminator="\n",
                extrasaction="ignore",
            )
            writer.writeheader()
            for row in rows:
                writer.writerow(row)

    def write_output(self, output: Path) -> None:
        output = output.resolve()
        if output.exists():
            raise ScanError(f"output must not already exist: {output}")
        if not output.parent.is_dir():
            raise ScanError(f"output parent is not a directory: {output.parent}")
        temporary = Path(tempfile.mkdtemp(prefix=f".{output.name}.tmp-", dir=output.parent))
        try:
            findings = sorted(self.findings, key=self._finding_sort_key)
            finding_rows = [
                {
                    "severity": item.severity,
                    "category": item.category,
                    "code": item.code,
                    "evidence_grade": item.evidence_grade,
                    "entity_type": item.entity_type,
                    "entity_id": item.entity_id,
                    "source_layer": item.source_layer,
                    "relative_path": item.relative_path,
                    "line": item.line,
                    "column": item.column,
                    "detail": item.detail,
                }
                for item in findings
            ]
            self._write_tsv(
                temporary / "findings.tsv",
                (
                    "severity", "category", "code", "evidence_grade", "entity_type",
                    "entity_id", "source_layer", "relative_path", "line", "column", "detail",
                ),
                finding_rows,
            )
            input_rows = []
            for key in sorted(self.inputs):
                record = self.inputs[key]
                input_rows.append(
                    {
                        "layer": record.layer,
                        "relative_path": record.relative_path,
                        "source_path": record.source_path,
                        "size": record.size,
                        "sha256": record.sha256,
                        "effective": record.effective,
                        "shadowed_by": record.shadowed_by,
                        "roles": ";".join(sorted(record.roles)),
                    }
                )
            self._write_tsv(
                temporary / "inputs.tsv",
                ("layer", "relative_path", "source_path", "size", "sha256", "effective", "shadowed_by", "roles"),
                input_rows,
            )
            reference_rows = self._reference_rows()
            self._write_tsv(
                temporary / "references.tsv",
                (
                    "entity_type", "entity_id", "candidate_class", "candidate_source_layers",
                    "source_layer", "effective", "shadowed_by", "relative_path", "line",
                    "column", "context", "confidence", "snippet",
                ),
                reference_rows,
            )
            self._write_tsv(
                temporary / "three_way_files.tsv",
                (
                    "relative_path", "old_present", "original_present", "target_present",
                    "old_sha256", "original_sha256", "target_sha256",
                    "old_vs_original", "old_vs_target", "original_vs_target",
                ),
                self.three_way_rows,
            )

            severity_counts = Counter(item.severity for item in findings)
            code_counts = Counter(item.code for item in findings)
            summary = {
                "schema_version": 1,
                "tool": "map_fresh_scan",
                "tool_version": TOOL_VERSION,
                "roots": {
                    "vanilla": str(self.layer_by_name["vanilla"].root),
                    "dependency": str(self.layer_by_name["dependency"].root) if "dependency" in self.layer_by_name else None,
                    "mod": str(self.layer_by_name["mod"].root),
                    "old_vanilla": str(self.old_layer.root) if self.old_layer else None,
                    "hok_original": (
                        str(self.original_layer.root) if self.original_layer else None
                    ),
                },
                "old_vanilla_identity": self.old_vanilla_identity,
                "hok_original_identity": self.hok_original_identity,
                "vfs": {
                    "overlay_rule": "exact-relative-path",
                    "precedence_low_to_high": [layer.name for layer in self.layers],
                    "effective_file_count": len(self.effective),
                    "mod_excluded_top_levels": sorted(DEVELOPMENT_TOP_LEVELS),
                },
                "reference_row_semantics": (
                    "One row per entity type and physical token location; contexts from "
                    "multiple detectors are semicolon-joined and confidence is the highest "
                    "detector confidence. effective/shadowed_by describe the exact-path "
                    "overlay status of the source file."
                ),
                "runtime_compatibility": "UNPROVEN",
                "static_result": "FAIL" if severity_counts["ERROR"] else "PASS_WITH_LIMITATIONS",
                "three_way_status": "INVENTORY_ONLY" if self.old_layer else "BLOCKED",
                "three_way_reason": (
                    "Manifest-verified V_OLD and HOK_ORIGINAL plus the supplied V_TARGET file presence/SHA-256 relationships only; no semantic delta or merge is inferred."
                    if self.old_layer
                    else "Manifest-verified V_OLD and HOK_ORIGINAL roots were not supplied; three-way inventory is unavailable."
                ),
                "counts": {
                    "inputs_hashed": len(input_rows),
                    "findings": len(finding_rows),
                    "references": len(reference_rows),
                    "three_way_files": len(self.three_way_rows),
                    "findings_by_severity": dict(sorted(severity_counts.items())),
                    "findings_by_code": dict(sorted(code_counts.items())),
                    "candidate_province_ids": len(self.candidates["province"]),
                    "candidate_state_ids": len(self.candidates["state"]),
                },
                "parser_limitations": [
                    "Exact-relative-path overlay only; no replace_path or directory-specific engine merge semantics.",
                    "Bounded Paradox lexer, not the HOI4 parser.",
                    "No geometry connectivity, coordinate, coast, or railway-continuity proof.",
                    "Low-confidence lexical references may be unrelated numeric values.",
                    "Three-way inventory is hash-only and never derives or applies INTENDED_DELTA.",
                    "Old-vanilla and HOK_ORIGINAL manifests verify supplied content bytes; historical version/build labels remain user-supplied and independently unproven.",
                ],
                "output_files": [
                    "findings.tsv", "inputs.tsv", "references.tsv", "three_way_files.tsv", "summary.json"
                ],
            }
            (temporary / "summary.json").write_text(
                json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
                newline="\n",
            )
            if output.exists():
                raise ScanError(f"output appeared during scan; refusing to overwrite: {output}")
            temporary.rename(output)
        except Exception:
            if temporary.exists():
                shutil.rmtree(temporary)
            raise


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Create a deterministic, dependency-free static HOI4 map inventory. "
            "Inputs are opened read-only; the output directory must not exist."
        )
    )
    parser.add_argument("--vanilla-root", required=True, type=Path)
    parser.add_argument("--mod-root", required=True, type=Path)
    parser.add_argument("--dependency-root", type=Path)
    parser.add_argument("--old-vanilla-root", type=Path)
    parser.add_argument("--old-vanilla-manifest", type=Path)
    parser.add_argument("--old-vanilla-manifest-sha256")
    parser.add_argument("--old-vanilla-label")
    parser.add_argument("--original-root", type=Path)
    parser.add_argument("--original-manifest", type=Path)
    parser.add_argument("--original-manifest-sha256")
    parser.add_argument("--original-label")
    parser.add_argument("--output", required=True, type=Path)
    return parser


def _validate_output_location(
    output: Path,
    *,
    vanilla_root: Path,
    mod_root: Path,
    dependency_root: Path | None,
    old_vanilla_root: Path | None,
    original_root: Path | None,
) -> None:
    output = output.resolve()
    resolved_roots = {
        "vanilla": vanilla_root.resolve(),
        "mod": mod_root.resolve(),
    }
    if dependency_root is not None:
        resolved_roots["dependency"] = dependency_root.resolve()
    if old_vanilla_root is not None:
        resolved_roots["old_vanilla"] = old_vanilla_root.resolve()
    if original_root is not None:
        resolved_roots["hok_original"] = original_root.resolve()

    for name in ("vanilla", "dependency", "old_vanilla", "hok_original"):
        root = resolved_roots.get(name)
        if root is not None and output.is_relative_to(root):
            raise ScanError(f"output must not be inside the {name} input root: {output}")

    mod_root_resolved = resolved_roots["mod"]
    if output.is_relative_to(mod_root_resolved):
        allowed_root = (mod_root_resolved / ".local-artifacts").resolve()
        if not output.is_relative_to(allowed_root):
            raise ScanError(
                "output inside the mod root is allowed only below "
                f"{allowed_root}: {output}"
            )


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    output = args.output.resolve()
    if output.exists():
        print(f"error: output must not already exist: {output}", file=sys.stderr)
        return 2
    try:
        _validate_output_location(
            output,
            vanilla_root=args.vanilla_root,
            mod_root=args.mod_root,
            dependency_root=args.dependency_root,
            old_vanilla_root=args.old_vanilla_root,
            original_root=args.original_root,
        )
        scanner = MapScanner(
            vanilla_root=args.vanilla_root,
            mod_root=args.mod_root,
            dependency_root=args.dependency_root,
            old_vanilla_root=args.old_vanilla_root,
            old_vanilla_manifest=args.old_vanilla_manifest,
            old_vanilla_manifest_sha256=args.old_vanilla_manifest_sha256,
            old_vanilla_label=args.old_vanilla_label,
            original_root=args.original_root,
            original_manifest=args.original_manifest,
            original_manifest_sha256=args.original_manifest_sha256,
            original_label=args.original_label,
        )
        scanner.run()
        scanner.write_output(output)
    except ScanError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"error: filesystem operation failed: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
