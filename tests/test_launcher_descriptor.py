from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from tools.launcher_descriptor import apply_descriptor, inspect_descriptor, sha256


class LauncherDescriptorTests(unittest.TestCase):
    def test_apply_changes_only_path_and_creates_backup(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            project = root / "project_name"
            project.mkdir()
            (project / "descriptor.mod").write_text('name="test"\n', encoding="utf-8")
            descriptor = root / "launcher.mod"
            original = (
                'name="test"\r\n'
                'path="C:/old path"\r\n'
                'supported_version="1.19.*"\r\n'
            )
            descriptor.write_bytes(original.encode("utf-8"))
            backup = root / "evidence" / "launcher.mod"

            result = apply_descriptor(
                descriptor, project, sha256(descriptor), backup
            )
            self.assertEqual(result["status"], "PASS")
            self.assertEqual(backup.read_bytes(), original.encode("utf-8"))
            updated_bytes = descriptor.read_bytes()
            self.assertIn(
                f'path="{project.resolve().as_posix()}"'.encode("utf-8"),
                updated_bytes,
            )
            self.assertIn(b'supported_version="1.19.*"', updated_bytes)
            self.assertEqual(updated_bytes.count(b"\r\n"), 3)
            self.assertTrue(inspect_descriptor(descriptor, project)["matches_project"])

    def test_apply_rejects_changed_input_and_existing_backup(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            project = root / "project"
            project.mkdir()
            (project / "descriptor.mod").write_text("", encoding="utf-8")
            descriptor = root / "launcher.mod"
            descriptor.write_text('path="C:/old"\n', encoding="utf-8")

            with self.assertRaises(ValueError):
                apply_descriptor(descriptor, project, "0" * 64, root / "backup.mod")

            backup = root / "backup.mod"
            backup.write_text("occupied", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                apply_descriptor(descriptor, project, sha256(descriptor), backup)


if __name__ == "__main__":
    unittest.main()
