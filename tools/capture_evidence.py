"""Copy one new, self-verifying run evidence bundle without touching sources.

Each ``--file`` value is ``relative/bundle/name=absolute/source/path``. The
destination must not exist. Source timestamps are preserved, metadata and a
deterministic SHA-256 manifest are written, and an incomplete temporary bundle
is removed if capture fails. The manifest detects later changes; filesystem
immutability or WORM retention must be provided separately.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path, PurePosixPath
import shutil
import sys
import tempfile
from typing import Iterable

try:
    from tools.evidence_manifest import write_manifest
except ModuleNotFoundError:  # Direct execution from the tools directory.
    from evidence_manifest import write_manifest


_RESERVED_BUNDLE_PATHS = {"capture.json", "sha256sums.tsv"}
_WINDOWS_RESERVED_BASENAMES = {
    "con",
    "prn",
    "aux",
    "nul",
    "conin$",
    "conout$",
    "clock$",
    *(f"com{number}" for number in range(1, 10)),
    *(f"lpt{number}" for number in range(1, 10)),
    "com¹",
    "com²",
    "com³",
    "lpt¹",
    "lpt²",
    "lpt³",
}


def _pair(value: str) -> tuple[str, str]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("expected NAME=VALUE")
    name, item_value = value.split("=", 1)
    if not name or not item_value:
        raise argparse.ArgumentTypeError("expected non-empty NAME=VALUE")
    return name, item_value


def _safe_relative(value: str) -> Path:
    candidate = PurePosixPath(value.replace("\\", "/"))
    if (
        candidate.is_absolute()
        or ".." in candidate.parts
        or candidate.as_posix() in {"", "."}
    ):
        raise ValueError(f"unsafe bundle path: {value}")
    for part in candidate.parts:
        basename = part.split(".", 1)[0].casefold()
        if (
            ":" in part
            or part.endswith((" ", "."))
            or basename in _WINDOWS_RESERVED_BASENAMES
            or any(ord(character) < 32 for character in part)
        ):
            raise ValueError(f"unsafe bundle path: {value}")
    return Path(*candidate.parts)


def capture_bundle(
    output: Path,
    files: list[tuple[str, str]],
    metadata: list[tuple[str, str]],
) -> dict[str, object]:
    if output.exists():
        raise FileExistsError(f"refusing to overwrite evidence bundle: {output}")

    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(
        tempfile.mkdtemp(prefix=f".{output.name}.tmp-", dir=output.parent)
    )
    try:
        seen_paths: set[str] = set()
        captured_files: list[dict[str, object]] = []
        for raw_bundle_path, raw_source in files:
            relative = _safe_relative(raw_bundle_path)
            bundle_path = relative.as_posix()
            path_key = bundle_path.casefold()
            if path_key in seen_paths or path_key in _RESERVED_BUNDLE_PATHS:
                raise ValueError(f"duplicate bundle path: {bundle_path}")
            seen_paths.add(path_key)

            source = Path(raw_source)
            if not source.is_file():
                raise ValueError(f"evidence source is not a file: {source}")
            source_stat = source.stat()

            destination = temporary / relative
            temporary_resolved = temporary.resolve()
            destination_resolved = destination.resolve(strict=False)
            if (
                destination_resolved == temporary_resolved
                or not destination_resolved.is_relative_to(temporary_resolved)
            ):
                raise ValueError(f"unsafe bundle destination: {bundle_path}")
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
            destination_stat = destination.stat()
            captured_files.append(
                {
                    "bundle_path": bundle_path,
                    "source": str(source.resolve()),
                    "source_bytes": source_stat.st_size,
                    "source_mtime_ns": source_stat.st_mtime_ns,
                    "captured_bytes": destination_stat.st_size,
                    "captured_mtime_ns": destination_stat.st_mtime_ns,
                }
            )

        metadata_values: dict[str, str] = {}
        for key, value in metadata:
            if key in metadata_values:
                raise ValueError(f"duplicate metadata key: {key}")
            metadata_values[key] = value

        capture = {
            "captured_at_utc": datetime.now(timezone.utc).isoformat(),
            "metadata": metadata_values,
            "files": captured_files,
        }
        (temporary / "capture.json").write_text(
            json.dumps(capture, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="",
        )
        manifest_result = write_manifest(
            temporary, temporary / "SHA256SUMS.tsv"
        )
        temporary.rename(output)
        return {
            "status": "PASS",
            "output": str(output.resolve()),
            "captured_files": len(captured_files),
            "bundle_manifest_sha256": manifest_result["manifest_sha256"],
        }
    except Exception:
        shutil.rmtree(temporary, ignore_errors=True)
        raise


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--file", action="append", default=[], type=_pair)
    parser.add_argument("--metadata", action="append", default=[], type=_pair)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        result = capture_bundle(args.output, args.file, args.metadata)
        exit_code = 0
    except (OSError, ValueError) as error:
        result = {"status": "ERROR", "error": str(error)}
        exit_code = 2

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
