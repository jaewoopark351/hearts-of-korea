from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from tools.capture_evidence import capture_bundle
from tools.evidence_manifest import verify_manifest


class CaptureEvidenceTests(unittest.TestCase):
    def test_capture_is_new_and_self_verifying(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source.log"
            source.write_bytes(b"evidence\n")
            output = root / "bundle"

            result = capture_bundle(
                output,
                [("logs/error.log", str(source))],
                [("run_id", "D-PRE")],
            )
            self.assertEqual(result["status"], "PASS")
            self.assertEqual((output / "logs" / "error.log").read_bytes(), b"evidence\n")
            metadata = json.loads(
                (output / "capture.json").read_text(encoding="utf-8")
            )
            self.assertEqual(metadata["metadata"]["run_id"], "D-PRE")
            self.assertEqual(
                verify_manifest(output, output / "SHA256SUMS.tsv")[0]["status"],
                "PASS",
            )
            self.assertEqual(
                verify_manifest(output, output / "SHA256SUMS.tsv")[1], 0
            )

            with self.assertRaises(FileExistsError):
                capture_bundle(output, [], [])

    def test_windows_unsafe_bundle_paths_are_rejected_without_output(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source.log"
            source.write_bytes(b"evidence\n")

            for index, unsafe in enumerate(
                (
                    "foo/C:/escape.txt",
                    "foo/data:stream",
                    "CON.txt",
                    "CONIN$",
                    "nested/COM¹.log",
                    "nested/LPT9.log",
                    "trailing-dot./file.txt",
                    "trailing-space /file.txt",
                )
            ):
                output = root / f"bundle-{index}"
                with self.subTest(path=unsafe), self.assertRaises(ValueError):
                    capture_bundle(output, [(unsafe, str(source))], [])
                self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
