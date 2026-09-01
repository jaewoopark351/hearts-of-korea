"""Audit file and localisation-key overlap without claiming runtime support."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import tempfile
from typing import Iterable


LOCALISATION_KEY = re.compile(r"^\s*([^\s#][^:]*?):(?:\d+)?\s+")
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


def _inventory(
    root: Path, excluded_top_levels: set[str] | frozenset[str] | None = None
) -> dict[str, tuple[str, Path]]:
    if not root.is_dir():
        raise ValueError(f"root does not exist: {root}")

    excluded = {value.casefold() for value in (excluded_top_levels or set())}
    inventory: dict[str, tuple[str, Path]] = {}
    for path in sorted(
        (item for item in root.rglob("*") if item.is_file()),
        key=lambda item: item.relative_to(root).as_posix().casefold(),
    ):
        relative = PurePosixPath(path.relative_to(root).as_posix()).as_posix()
        parts = PurePosixPath(relative).parts
        if parts and parts[0].casefold() in excluded:
            continue
        key = relative.casefold()
        if key in inventory:
            raise ValueError(
                f"case-insensitive path collision in {root}: {relative}"
            )
        inventory[key] = (relative, path)
    return inventory


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _localisation_keys(root: Path) -> dict[str, list[tuple[str, int, str]]]:
    keys: dict[str, list[tuple[str, int, str]]] = {}
    localisation = root / "localisation"
    if not localisation.is_dir():
        return keys

    for path in sorted(
        localisation.rglob("*.yml"),
        key=lambda item: item.relative_to(root).as_posix().casefold(),
    ):
        relative = path.relative_to(root).as_posix()
        try:
            lines = path.read_text(encoding="utf-8-sig").splitlines()
        except UnicodeDecodeError as error:
            raise ValueError(
                f"localisation is not UTF-8/BOM readable: {path}"
            ) from error
        for line_number, line in enumerate(lines, start=1):
            match = LOCALISATION_KEY.match(line)
            if not match:
                continue
            key = match.group(1).strip()
            keys.setdefault(key, []).append((relative, line_number, line.strip()))
    return keys


def _write_tsv(path: Path, header: list[str], rows: list[list[object]]) -> None:
    with path.open("x", encoding="utf-8", newline="") as stream:
        stream.write("\t".join(header) + "\n")
        for row in rows:
            cleaned = [
                str(value).replace("\t", " ").replace("\r", " ").replace("\n", " ")
                for value in row
            ]
            stream.write("\t".join(cleaned) + "\n")


def audit(
    mod_root: Path,
    dependency_root: Path,
    vanilla_root: Path,
    output: Path,
) -> dict[str, object]:
    output = output.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite audit output: {output}")
    if not output.parent.is_dir():
        raise ValueError(f"audit output parent is not a directory: {output.parent}")
    resolved_roots = {
        "mod": mod_root.resolve(),
        "dependency": dependency_root.resolve(),
        "vanilla": vanilla_root.resolve(),
    }
    for name in ("dependency", "vanilla"):
        if output.is_relative_to(resolved_roots[name]):
            raise ValueError(f"audit output must not be inside {name} input root")
    if output.is_relative_to(resolved_roots["mod"]):
        allowed = (resolved_roots["mod"] / ".local-artifacts").resolve()
        if not output.is_relative_to(allowed):
            raise ValueError(
                f"audit output inside mod root is allowed only below {allowed}"
            )

    mod_files = _inventory(mod_root, DEVELOPMENT_TOP_LEVELS)
    dependency_files = _inventory(dependency_root)
    vanilla_files = _inventory(vanilla_root)
    temporary = Path(
        tempfile.mkdtemp(prefix=f".{output.name}.tmp-", dir=output.parent)
    )

    try:
        result = _write_audit(
            mod_root,
            dependency_root,
            vanilla_root,
            temporary,
            mod_files,
            dependency_files,
            vanilla_files,
        )
        if output.exists():
            raise FileExistsError(
                f"audit output appeared during scan; refusing to overwrite: {output}"
            )
        temporary.rename(output)
        return result
    except Exception:
        if temporary.exists():
            shutil.rmtree(temporary)
        raise


def _write_audit(
    mod_root: Path,
    dependency_root: Path,
    vanilla_root: Path,
    output: Path,
    mod_files: dict[str, tuple[str, Path]],
    dependency_files: dict[str, tuple[str, Path]],
    vanilla_files: dict[str, tuple[str, Path]],
) -> dict[str, object]:

    path_rows: list[list[object]] = []
    overlap_counts = {"dependency_vs_mod": 0, "dependency_vs_vanilla": 0}
    overlap_by_top_directory: dict[str, int] = {}
    for comparison, other_files in (
        ("dependency_vs_mod", mod_files),
        ("dependency_vs_vanilla", vanilla_files),
    ):
        for key in sorted(dependency_files.keys() & other_files.keys()):
            dependency_path, dependency_file = dependency_files[key]
            other_path, other_file = other_files[key]
            dependency_hash = _sha256(dependency_file)
            other_hash = _sha256(other_file)
            path_rows.append(
                [
                    comparison,
                    dependency_path,
                    other_path,
                    dependency_file.stat().st_size,
                    other_file.stat().st_size,
                    dependency_hash,
                    other_hash,
                    dependency_hash == other_hash,
                ]
            )
            overlap_counts[comparison] += 1
            if comparison == "dependency_vs_vanilla":
                top = PurePosixPath(dependency_path).parts[0]
                overlap_by_top_directory[top] = (
                    overlap_by_top_directory.get(top, 0) + 1
                )

    _write_tsv(
        output / "path_overlaps.tsv",
        [
            "comparison",
            "dependency_path",
            "other_path",
            "dependency_bytes",
            "other_bytes",
            "dependency_sha256",
            "other_sha256",
            "identical",
        ],
        path_rows,
    )

    dependency_keys = _localisation_keys(dependency_root)
    mod_keys = _localisation_keys(mod_root)
    shared_keys = sorted(dependency_keys.keys() & mod_keys.keys())
    localisation_rows: list[list[object]] = []
    for key in shared_keys:
        for dependency_path, dependency_line, _ in dependency_keys[key]:
            for mod_path, mod_line, _ in mod_keys[key]:
                localisation_rows.append(
                    [key, dependency_path, dependency_line, mod_path, mod_line]
                )
    _write_tsv(
        output / "localisation_key_overlaps.tsv",
        ["key", "dependency_path", "dependency_line", "mod_path", "mod_line"],
        localisation_rows,
    )

    dependency_paths = [item[0] for item in dependency_files.values()]
    summary: dict[str, object] = {
        "status": "PASS",
        "scope": "static_overlap_only",
        "runtime_compatibility": "UNPROVEN",
        "mod_root": str(mod_root.resolve()),
        "dependency_root": str(dependency_root.resolve()),
        "vanilla_root": str(vanilla_root.resolve()),
        "dependency_files": len(dependency_files),
        "dependency_vs_mod_path_overlaps": overlap_counts["dependency_vs_mod"],
        "dependency_vs_vanilla_path_overlaps": overlap_counts[
            "dependency_vs_vanilla"
        ],
        "dependency_vs_vanilla_overlap_by_top_directory": dict(
            sorted(overlap_by_top_directory.items())
        ),
        "distinct_dependency_vs_mod_localisation_keys": len(shared_keys),
        "localisation_overlap_rows": len(localisation_rows),
        "dependency_has_map_files": any(
            path.casefold().startswith("map/") for path in dependency_paths
        ),
        "dependency_has_history_files": any(
            path.casefold().startswith("history/") for path in dependency_paths
        ),
    }
    (output / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="",
    )
    return summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mod-root", required=True, type=Path)
    parser.add_argument("--dependency-root", required=True, type=Path)
    parser.add_argument("--vanilla-root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        result = audit(
            args.mod_root, args.dependency_root, args.vanilla_root, args.output
        )
        exit_code = 0
    except (OSError, ValueError) as error:
        result = {"status": "ERROR", "error": str(error)}
        exit_code = 2

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
