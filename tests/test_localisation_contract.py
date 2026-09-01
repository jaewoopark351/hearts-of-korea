from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import re
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LOCALISATION_ROOT = PROJECT_ROOT / "localisation"
UTF8_BOM = b"\xef\xbb\xbf"
LANGUAGES = {
    "english": ("_l_english.yml", "l_english:"),
    "korean": ("_l_korean.yml", "l_korean:"),
}
LOCALISATION_KEY = re.compile(r"^\s*([^#:\s]+):(?:\d+)?(?:\s|$)")


def language_files(language: str) -> list[Path]:
    return sorted((LOCALISATION_ROOT / language).rglob("*.yml"))


def count_unescaped_double_quotes(line: str) -> int:
    count = 0
    preceding_backslashes = 0

    for character in line:
        if character == '"' and preceding_backslashes % 2 == 0:
            count += 1
        if character == "\\":
            preceding_backslashes += 1
        else:
            preceding_backslashes = 0

    return count


class LocalisationContractTests(unittest.TestCase):
    def test_language_trees_have_one_to_one_paths(self) -> None:
        english_files = language_files("english")
        korean_files = language_files("korean")

        self.assertEqual(len(english_files), 18)
        self.assertEqual(len(korean_files), 18)
        self.assertTrue(
            all(path.name.endswith("_l_english.yml") for path in english_files)
        )
        self.assertTrue(
            all(path.name.endswith("_l_korean.yml") for path in korean_files)
        )

        english_root = LOCALISATION_ROOT / "english"
        korean_root = LOCALISATION_ROOT / "korean"
        expected_korean_paths = {
            relative.with_name(
                relative.name.removesuffix("_l_english.yml") + "_l_korean.yml"
            )
            for path in english_files
            for relative in (path.relative_to(english_root),)
        }
        actual_korean_paths = {
            path.relative_to(korean_root) for path in korean_files
        }
        self.assertEqual(actual_korean_paths, expected_korean_paths)

    def test_files_have_utf8_bom_and_exact_language_header(self) -> None:
        for language, (suffix, header) in LANGUAGES.items():
            for path in language_files(language):
                with self.subTest(language=language, path=path):
                    raw = path.read_bytes()
                    self.assertTrue(raw.startswith(UTF8_BOM))
                    text = raw.decode("utf-8-sig")
                    self.assertEqual(text.splitlines()[0], header)
                    self.assertTrue(path.name.endswith(suffix))

    def test_korean_copies_differ_only_in_header(self) -> None:
        english_root = LOCALISATION_ROOT / "english"
        korean_root = LOCALISATION_ROOT / "korean"

        for english_path in language_files("english"):
            relative = english_path.relative_to(english_root)
            korean_relative = relative.with_name(
                relative.name.removesuffix("_l_english.yml") + "_l_korean.yml"
            )
            korean_path = korean_root / korean_relative
            with self.subTest(path=relative):
                english_bytes = english_path.read_bytes()
                expected_korean_bytes = english_bytes.replace(
                    b"l_english:", b"l_korean:", 1
                )
                self.assertEqual(korean_path.read_bytes(), expected_korean_bytes)

    def test_lines_have_zero_or_two_unescaped_double_quotes(self) -> None:
        for language in LANGUAGES:
            root = LOCALISATION_ROOT / language
            for path in language_files(language):
                text = path.read_bytes().decode("utf-8-sig")
                for line_number, line in enumerate(text.splitlines(), start=1):
                    with self.subTest(
                        language=language,
                        path=path.relative_to(root),
                        line=line_number,
                    ):
                        self.assertIn(count_unescaped_double_quotes(line), (0, 2))

    def test_keys_are_unique_within_each_language_tree(self) -> None:
        for language, (_, header) in LANGUAGES.items():
            locations: dict[str, list[str]] = defaultdict(list)
            root = LOCALISATION_ROOT / language

            for path in language_files(language):
                text = path.read_bytes().decode("utf-8-sig")
                for line_number, line in enumerate(text.splitlines(), start=1):
                    if line == header or line.lstrip().startswith("#"):
                        continue
                    match = LOCALISATION_KEY.match(line)
                    if match:
                        locations[match.group(1)].append(
                            f"{path.relative_to(root)}:{line_number}"
                        )

            duplicates = {
                key: found_at
                for key, found_at in locations.items()
                if len(found_at) > 1
            }
            self.assertEqual(duplicates, {}, msg=f"{language}: {duplicates}")


if __name__ == "__main__":
    unittest.main()
