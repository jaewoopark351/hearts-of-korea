"""Inspect or safely retarget a HOI4 local launcher descriptor.

``apply`` changes only the descriptor's single top-level ``path=`` line. It
requires the caller to provide the expected pre-change SHA-256 and a new backup
path, preventing an unnoticed launcher rewrite or accidental overwrite.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
from typing import Iterable


PATH_LINE = re.compile(
    r'^(?P<prefix>[^\S\r\n]*path[^\S\r\n]*=[^\S\r\n]*)'
    # ``\r`` belongs to a CRLF line ending and must remain in the match so a
    # byte-level rewrite preserves the descriptor's original newline style.
    r'"(?P<path>[^"\r\n]*)"(?P<suffix>[^\S\n]*)$',
    re.MULTILINE,
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _validate_project(project_root: Path) -> None:
    if not project_root.is_dir():
        raise ValueError(f"project root does not exist: {project_root}")
    if not (project_root / "descriptor.mod").is_file():
        raise ValueError(
            f"project descriptor.mod does not exist: {project_root / 'descriptor.mod'}"
        )


def _inspect_descriptor_bytes(
    descriptor: Path, project_root: Path, raw: bytes
) -> dict[str, object]:
    text = raw.decode("utf-8-sig")
    matches = list(PATH_LINE.finditer(text))
    if len(matches) != 1:
        raise ValueError(f"expected exactly one path line, found {len(matches)}")

    configured_path = matches[0].group("path")
    configured = Path(configured_path.replace("/", os.sep))
    try:
        configured_resolved = configured.resolve(strict=False)
    except OSError:
        configured_resolved = configured.absolute()
    project_resolved = project_root.resolve()
    return {
        "descriptor": str(descriptor.resolve()),
        "descriptor_sha256": hashlib.sha256(raw).hexdigest(),
        "configured_path": configured_path,
        "configured_path_exists": configured.exists(),
        "configured_path_resolved": str(configured_resolved),
        "project_root": str(project_resolved),
        "matches_project": configured_resolved == project_resolved,
    }


def inspect_descriptor(descriptor: Path, project_root: Path) -> dict[str, object]:
    if not descriptor.is_file():
        raise ValueError(f"launcher descriptor does not exist: {descriptor}")
    _validate_project(project_root)
    return _inspect_descriptor_bytes(descriptor, project_root, descriptor.read_bytes())


def _render_descriptor_bytes(raw: bytes, project_root: Path) -> bytes:
    has_bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig" if has_bom else "utf-8")
    matches = list(PATH_LINE.finditer(text))
    if len(matches) != 1:
        raise ValueError(f"expected exactly one path line, found {len(matches)}")

    match = matches[0]
    replacement = (
        f'{match.group("prefix")}"{project_root.resolve().as_posix()}"'
        f'{match.group("suffix")}'
    )
    updated = text[: match.start()] + replacement + text[match.end() :]
    encoded = updated.encode("utf-8")
    return (b"\xef\xbb\xbf" + encoded) if has_bom else encoded


def render_descriptor(descriptor: Path, project_root: Path) -> bytes:
    if not descriptor.is_file():
        raise ValueError(f"launcher descriptor does not exist: {descriptor}")
    _validate_project(project_root)
    return _render_descriptor_bytes(descriptor.read_bytes(), project_root)


def apply_descriptor(
    descriptor: Path,
    project_root: Path,
    expected_sha256: str,
    backup: Path,
) -> dict[str, object]:
    if not descriptor.is_file():
        raise ValueError(f"launcher descriptor does not exist: {descriptor}")
    _validate_project(project_root)
    raw = descriptor.read_bytes()
    before = _inspect_descriptor_bytes(descriptor, project_root, raw)
    actual_sha256 = str(before["descriptor_sha256"])
    if actual_sha256.lower() != expected_sha256.lower():
        raise ValueError(
            "descriptor changed since inspection: "
            f"expected {expected_sha256}, found {actual_sha256}"
        )
    if backup.exists():
        raise FileExistsError(f"refusing to overwrite backup: {backup}")
    if backup.resolve() == descriptor.resolve():
        raise ValueError("backup path must differ from descriptor path")

    updated = _render_descriptor_bytes(raw, project_root)
    descriptor_stat = descriptor.stat()
    backup.parent.mkdir(parents=True, exist_ok=True)
    with backup.open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    shutil.copymode(descriptor, backup)
    os.utime(
        backup,
        ns=(descriptor_stat.st_atime_ns, descriptor_stat.st_mtime_ns),
    )

    file_descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{descriptor.name}.", suffix=".tmp", dir=descriptor.parent
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(file_descriptor, "wb") as stream:
            stream.write(updated)
            stream.flush()
            os.fsync(stream.fileno())
        if descriptor.read_bytes() != raw:
            raise RuntimeError(
                "descriptor changed during apply; backup was preserved and no write was made"
            )
        os.replace(temporary, descriptor)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise

    after = inspect_descriptor(descriptor, project_root)
    if not after["matches_project"]:
        raise RuntimeError("post-write verification did not resolve to project root")
    return {
        "status": "PASS",
        "backup": str(backup.resolve()),
        "backup_sha256": sha256(backup),
        "before": before,
        "after": after,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("inspect", "apply"))
    parser.add_argument("--descriptor", required=True, type=Path)
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--expected-sha256")
    parser.add_argument("--backup", type=Path)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "inspect":
            result = inspect_descriptor(args.descriptor, args.project_root)
            result = {"status": "PASS", **result}
        else:
            if args.expected_sha256 is None or args.backup is None:
                raise ValueError("apply requires --expected-sha256 and --backup")
            result = apply_descriptor(
                args.descriptor,
                args.project_root,
                args.expected_sha256,
                args.backup,
            )
        exit_code = 0
    except (OSError, RuntimeError, ValueError) as error:
        result = {"status": "ERROR", "error": str(error)}
        exit_code = 2

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
