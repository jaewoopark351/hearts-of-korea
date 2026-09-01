"""Create and verify deterministic SHA-256 manifests for evidence baselines.

The tool is deliberately dependency-free. It reads directories or ZIP files,
never mutates the source, and refuses to overwrite an existing manifest.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys
from typing import BinaryIO, Iterable, Iterator, NamedTuple
import zipfile


CHUNK_SIZE = 1024 * 1024
HEADER = "sha256\tbytes\tpath"
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


class Entry(NamedTuple):
    sha256: str
    size: int
    path: str


def _normalise_relative_path(value: str) -> str:
    candidate = PurePosixPath(value.replace("\\", "/"))
    if (
        candidate.is_absolute()
        or ".." in candidate.parts
        or candidate.as_posix() in {"", "."}
    ):
        raise ValueError(f"unsafe manifest path: {value}")
    for part in candidate.parts:
        basename = part.split(".", 1)[0].casefold()
        if (
            ":" in part
            or part.endswith((" ", "."))
            or basename in _WINDOWS_RESERVED_BASENAMES
            or any(ord(character) < 32 for character in part)
        ):
            raise ValueError(f"unsafe manifest path: {value}")
    return candidate.as_posix()


def _hash_stream(stream: BinaryIO) -> tuple[str, int]:
    digest = hashlib.sha256()
    size = 0
    while True:
        chunk = stream.read(CHUNK_SIZE)
        if not chunk:
            break
        digest.update(chunk)
        size += len(chunk)
    return digest.hexdigest(), size


def _iter_directory(root: Path) -> Iterator[Entry]:
    if not root.is_dir():
        raise ValueError(f"directory source does not exist: {root}")

    files = sorted(
        (path for path in root.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(root).as_posix().casefold(),
    )
    seen: set[str] = set()
    for path in files:
        relative = _normalise_relative_path(path.relative_to(root).as_posix())
        key = relative.casefold()
        if key in seen:
            raise ValueError(
                f"duplicate directory path (case-insensitive): {relative}"
            )
        seen.add(key)
        with path.open("rb") as stream:
            sha256, size = _hash_stream(stream)
        yield Entry(sha256, size, relative)


def _iter_zip(path: Path) -> Iterator[Entry]:
    if not path.is_file():
        raise ValueError(f"ZIP source does not exist: {path}")

    with zipfile.ZipFile(path, "r") as archive:
        members: list[tuple[str, zipfile.ZipInfo]] = []
        seen: set[str] = set()
        for member in archive.infolist():
            if member.is_dir():
                continue
            relative = _normalise_relative_path(member.filename)
            key = relative.casefold()
            if key in seen:
                raise ValueError(
                    f"duplicate ZIP member path (case-insensitive): {relative}"
                )
            seen.add(key)
            members.append((relative, member))

        for relative, member in sorted(
            members, key=lambda item: item[0].casefold()
        ):
            with archive.open(member, "r") as stream:
                sha256, size = _hash_stream(stream)
            yield Entry(sha256, size, relative)


def iter_source(source: Path) -> Iterator[Entry]:
    if source.is_dir():
        yield from _iter_directory(source)
        return
    if source.is_file() and zipfile.is_zipfile(source):
        yield from _iter_zip(source)
        return
    raise ValueError(f"source must be a directory or ZIP file: {source}")


def read_manifest(path: Path) -> list[Entry]:
    if not path.is_file():
        raise ValueError(f"manifest does not exist: {path}")

    entries: list[Entry] = []
    seen: set[str] = set()
    with path.open("r", encoding="utf-8", newline="") as stream:
        header = stream.readline().rstrip("\r\n")
        if header != HEADER:
            raise ValueError(f"unexpected manifest header: {header}")

        for line_number, raw_line in enumerate(stream, start=2):
            line = raw_line.rstrip("\r\n")
            if not line:
                raise ValueError(f"blank manifest row at line {line_number}")
            columns = line.split("\t")
            if len(columns) != 3:
                raise ValueError(f"invalid manifest row at line {line_number}")

            sha256, size_text, raw_path = columns
            if len(sha256) != 64 or any(
                character not in "0123456789abcdefABCDEF" for character in sha256
            ):
                raise ValueError(f"invalid SHA-256 at line {line_number}")
            try:
                size = int(size_text)
            except ValueError as error:
                raise ValueError(
                    f"invalid byte size at line {line_number}"
                ) from error
            if size < 0:
                raise ValueError(f"negative byte size at line {line_number}")

            relative = _normalise_relative_path(raw_path)
            key = relative.casefold()
            if key in seen:
                raise ValueError(
                    f"duplicate manifest path at line {line_number}: {relative}"
                )
            seen.add(key)
            entries.append(Entry(sha256.lower(), size, relative))
    return entries


def write_manifest(source: Path, output: Path) -> dict[str, object]:
    if output.exists():
        raise FileExistsError(f"refusing to overwrite existing manifest: {output}")

    entries = list(iter_source(source))
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8", newline="") as stream:
        stream.write(f"{HEADER}\n")
        for entry in entries:
            stream.write(f"{entry.sha256}\t{entry.size}\t{entry.path}\n")

    manifest_sha256 = hashlib.sha256(output.read_bytes()).hexdigest()
    return {
        "status": "PASS",
        "source": str(source.resolve()),
        "manifest": str(output.resolve()),
        "files": len(entries),
        "bytes": sum(entry.size for entry in entries),
        "manifest_sha256": manifest_sha256,
    }


def verify_manifest(source: Path, manifest: Path) -> tuple[dict[str, object], int]:
    expected_entries = read_manifest(manifest)
    actual_entries = list(iter_source(source))

    # Evidence bundles keep their own manifest in the source directory. The
    # manifest cannot hash itself, so omit exactly that file during verification.
    if source.is_dir():
        try:
            manifest_relative = _normalise_relative_path(
                manifest.resolve().relative_to(source.resolve()).as_posix()
            ).casefold()
        except ValueError:
            manifest_relative = None
        if manifest_relative is not None:
            actual_entries = [
                entry
                for entry in actual_entries
                if entry.path.casefold() != manifest_relative
            ]

    expected = {entry.path.casefold(): entry for entry in expected_entries}
    actual = {entry.path.casefold(): entry for entry in actual_entries}

    missing = [expected[key].path for key in sorted(expected.keys() - actual.keys())]
    extra = [actual[key].path for key in sorted(actual.keys() - expected.keys())]
    mismatches: list[dict[str, object]] = []
    for key in sorted(expected.keys() & actual.keys()):
        expected_entry = expected[key]
        actual_entry = actual[key]
        if (
            expected_entry.size != actual_entry.size
            or expected_entry.sha256 != actual_entry.sha256
        ):
            mismatches.append(
                {
                    "path": expected_entry.path,
                    "actual_path": actual_entry.path,
                    "expected_bytes": expected_entry.size,
                    "actual_bytes": actual_entry.size,
                    "expected_sha256": expected_entry.sha256,
                    "actual_sha256": actual_entry.sha256,
                }
            )

    passed = not missing and not extra and not mismatches
    result: dict[str, object] = {
        "status": "PASS" if passed else "FAIL",
        "source": str(source.resolve()),
        "manifest": str(manifest.resolve()),
        "expected_files": len(expected_entries),
        "actual_files": len(actual_entries),
        "expected_bytes": sum(entry.size for entry in expected_entries),
        "actual_bytes": sum(entry.size for entry in actual_entries),
        "missing": missing,
        "extra": extra,
        "mismatches": mismatches,
    }
    return result, 0 if passed else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    create = subparsers.add_parser(
        "create", help="create a new deterministic manifest"
    )
    create.add_argument("--source", required=True, type=Path)
    create.add_argument("--output", required=True, type=Path)

    verify = subparsers.add_parser(
        "verify", help="verify a directory or ZIP against a manifest"
    )
    verify.add_argument("--source", required=True, type=Path)
    verify.add_argument("--manifest", required=True, type=Path)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "create":
            result = write_manifest(args.source, args.output)
            exit_code = 0
        else:
            result, exit_code = verify_manifest(args.source, args.manifest)
    except (OSError, ValueError, zipfile.BadZipFile) as error:
        result = {"status": "ERROR", "error": str(error)}
        exit_code = 2

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
