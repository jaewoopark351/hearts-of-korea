from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from tools.dependency_overlap import audit


class DependencyOverlapTests(unittest.TestCase):
    def test_reports_paths_and_localisation_keys_without_runtime_claim(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            mod = root / "mod"
            dependency = root / "dependency"
            vanilla = root / "vanilla"
            for item in (mod, dependency, vanilla):
                (item / "localisation").mkdir(parents=True)

            relative = Path("localisation") / "names_l_korean.yml"
            (mod / relative).write_text(
                '\ufeffl_korean:\n KEY_SHARED:0 "mod"\n', encoding="utf-8"
            )
            (dependency / relative).write_text(
                '\ufeffl_korean:\n KEY_SHARED: "dependency"\n', encoding="utf-8"
            )
            (vanilla / relative).write_text(
                '\ufeffl_korean:\n KEY_VANILLA:0 "vanilla"\n', encoding="utf-8"
            )
            output = root / "output"

            result = audit(mod, dependency, vanilla, output)
            self.assertEqual(result["runtime_compatibility"], "UNPROVEN")
            self.assertEqual(result["dependency_vs_mod_path_overlaps"], 1)
            self.assertEqual(result["dependency_vs_vanilla_path_overlaps"], 1)
            self.assertEqual(
                result["distinct_dependency_vs_mod_localisation_keys"], 1
            )
            written = json.loads(
                (output / "summary.json").read_text(encoding="utf-8")
            )
            self.assertEqual(written["status"], "PASS")

            with self.assertRaises(FileExistsError):
                audit(mod, dependency, vanilla, output)

            for unsafe in (
                vanilla / "audit-output",
                dependency / "audit-output",
                mod / "localisation" / "audit-output",
            ):
                with self.subTest(output=unsafe), self.assertRaises(ValueError):
                    audit(mod, dependency, vanilla, unsafe)
                self.assertFalse(unsafe.exists())

            allowed = mod / ".local-artifacts" / "dependency-audit"
            allowed.parent.mkdir()
            self.assertEqual(
                audit(mod, dependency, vanilla, allowed)["status"], "PASS"
            )


if __name__ == "__main__":
    unittest.main()
