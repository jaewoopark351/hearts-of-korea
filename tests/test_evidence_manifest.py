from __future__ import annotations

from pathlib import Path
import tempfile
import unittest
import zipfile

from tools.evidence_manifest import read_manifest, verify_manifest, write_manifest


class EvidenceManifestTests(unittest.TestCase):
    def test_directory_and_zip_verify_against_same_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            source.mkdir()
            (source / "a.txt").write_bytes(b"alpha")
            (source / "nested").mkdir()
            (source / "nested" / "b.bin").write_bytes(b"\x00\x01\x02")

            manifest = root / "manifest.tsv"
            result = write_manifest(source, manifest)
            self.assertEqual(result["files"], 2)
            self.assertEqual(
                [entry.path for entry in read_manifest(manifest)],
                ["a.txt", "nested/b.bin"],
            )
            self.assertEqual(verify_manifest(source, manifest)[0]["status"], "PASS")
            self.assertEqual(verify_manifest(source, manifest)[1], 0)

            archive = root / "source.zip"
            with zipfile.ZipFile(archive, "w") as output:
                output.write(source / "a.txt", "a.txt")
                output.write(source / "nested" / "b.bin", "nested/b.bin")
            self.assertEqual(verify_manifest(archive, manifest)[0]["status"], "PASS")
            self.assertEqual(verify_manifest(archive, manifest)[1], 0)

    def test_verify_reports_changed_missing_and_extra_files(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            source.mkdir()
            (source / "changed.txt").write_text("before", encoding="utf-8")
            (source / "missing.txt").write_text("present", encoding="utf-8")
            manifest = root / "manifest.tsv"
            write_manifest(source, manifest)

            (source / "changed.txt").write_text("after", encoding="utf-8")
            (source / "missing.txt").unlink()
            (source / "extra.txt").write_text("extra", encoding="utf-8")

            result, exit_code = verify_manifest(source, manifest)
            self.assertEqual((result["status"], exit_code), ("FAIL", 1))
            self.assertEqual(result["missing"], ["missing.txt"])
            self.assertEqual(result["extra"], ["extra.txt"])
            self.assertEqual(
                [item["path"] for item in result["mismatches"]], ["changed.txt"]
            )

    def test_create_refuses_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            source.mkdir()
            output = root / "manifest.tsv"
            output.write_text("existing", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                write_manifest(source, output)

    def test_windows_unsafe_manifest_paths_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            manifest = Path(temporary) / "unsafe.tsv"
            for unsafe in (
                "foo/C:/escape.txt",
                "foo/data:stream",
                "CON.txt",
                "CONOUT$",
                "nested/LPT².log",
                "nested/COM9.log",
                "trailing-dot./file.txt",
                "trailing-space /file.txt",
            ):
                with self.subTest(path=unsafe):
                    manifest.write_text(
                        f"sha256\tbytes\tpath\n{'0' * 64}\t0\t{unsafe}\n",
                        encoding="utf-8",
                        newline="\n",
                    )
                    with self.assertRaises(ValueError):
                        read_manifest(manifest)


if __name__ == "__main__":
    unittest.main()
