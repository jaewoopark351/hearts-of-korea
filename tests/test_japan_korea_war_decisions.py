import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DECISION_FILE = ROOT / "common" / "decisions" / "JAP.txt"
CATEGORY_FILE = (
    ROOT
    / "common"
    / "decisions"
    / "categories"
    / "JAP_HoK_decision_category.txt"
)
EVENT_FILE = ROOT / "events" / "korea.txt"
STATE_FILE = ROOT / "history" / "states" / "525-South Korea.txt"
FOCUS_FILE = ROOT / "common" / "national_focus" / "korea.txt"
AI_FILE = ROOT / "common" / "ai_strategy" / "KOR.txt"


def read_text(path: Path) -> str:
    return path.read_bytes().decode("utf-8-sig")


def extract_block(text: str, key: str) -> str:
    matches = list(
        re.finditer(
            rf"(?m)^[ \t]*{re.escape(key)}[ \t]*=[ \t]*\{{",
            text,
        )
    )
    if len(matches) != 1:
        raise AssertionError(f"expected one {key} block, found {len(matches)}")

    start = matches[0].start()
    opening_brace = text.find("{", matches[0].start(), matches[0].end())
    depth = 0
    in_string = False
    in_comment = False
    escaped = False

    for index in range(opening_brace, len(text)):
        char = text[index]

        if in_comment:
            if char in "\r\n":
                in_comment = False
            continue

        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue

        if char == "#":
            in_comment = True
        elif char == '"':
            in_string = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[start : index + 1]

    raise AssertionError(f"unterminated {key} block")


class JapanKoreaWarDecisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.decisions = read_text(DECISION_FILE)
        cls.category = read_text(CATEGORY_FILE)
        cls.events = read_text(EVENT_FILE)

    def test_restores_only_warning_and_ultimatum_decisions(self) -> None:
        category = extract_block(self.decisions, "JAP_war_on_korea_category")
        direct_decisions = set(
            re.findall(r"(?m)^\t(jap_[a-zA-Z0-9_]+)\s*=\s*\{", category)
        )
        self.assertEqual(
            direct_decisions,
            {"jap_warning_to_korea", "jap_ultimatum_to_korea"},
        )

        forbidden = {
            "jap_more_divisions_for_AI_JAP",
            "jap_attack_Rhee_korea",
            "jap_gain_core_on_north_sakhalin",
            "JAP_gain_core_on_north_sakhalin_category",
        }
        restored_source = category + "\n" + self.category
        for identifier in forbidden:
            self.assertNotIn(identifier, restored_source)

    def test_warning_contract(self) -> None:
        category = extract_block(self.decisions, "JAP_war_on_korea_category")
        warning = extract_block(category, "jap_warning_to_korea")

        self.assertIn("date > 1939.1.10", warning)
        self.assertIn("date < 1939.1.15", warning)
        self.assertIn("cost = 0", warning)
        self.assertIn("fire_only_once = yes", warning)
        self.assertEqual(
            len(re.findall(r"id\s*=\s*kor_events\.20\b", warning, re.IGNORECASE)),
            1,
        )
        self.assertIn("set_global_flag = jap_warning_to_korea_flag", warning)

    def test_ultimatum_contract(self) -> None:
        category = extract_block(self.decisions, "JAP_war_on_korea_category")
        ultimatum = extract_block(category, "jap_ultimatum_to_korea")

        self.assertIn("has_global_flag = jap_warning_to_korea_flag", ultimatum)
        self.assertIn("date > 1939.6.25", ultimatum)
        self.assertIn("cost = 0", ultimatum)
        self.assertIn("fire_only_once = yes", ultimatum)
        self.assertEqual(
            len(re.findall(r"id\s*=\s*kor_events\.16\b", ultimatum, re.IGNORECASE)),
            1,
        )
        self.assertIn("set_global_flag = jap_ultimatum_to_korea_flag", ultimatum)

    def test_category_uses_unique_japan_scope(self) -> None:
        metadata = extract_block(self.category, "JAP_war_on_korea_category")
        self.assertIn("icon = military_operation", metadata)
        self.assertIn("original_tag = JAP", metadata)
        self.assertEqual(
            len(
                re.findall(
                    r"(?m)^\s*JAP_war_on_korea_category\s*=\s*\{",
                    self.category,
                )
            ),
            1,
        )

    def test_ultimatum_event_creates_the_state_525_wargoal(self) -> None:
        event_match = re.search(
            r"(?is)\bid\s*=\s*kor_events\.16\b(?P<body>.*?)"
            r"\bid\s*=\s*kor_events\.17\b",
            self.events,
        )
        self.assertIsNotNone(event_match)
        event = event_match.group("body")

        self.assertIn("is_triggered_only = yes", event)
        self.assertIn("create_wargoal", event)
        self.assertIn("type = take_state_focus", event)
        self.assertIn("target = KOR", event)
        self.assertRegex(event, r"generator\s*=\s*\{\s*525\s*\}")

    def test_required_korea_dependencies_remain_registered(self) -> None:
        focuses = read_text(FOCUS_FILE)
        state = read_text(STATE_FILE)
        ai = read_text(AI_FILE)

        for focus_id in (
            "KOR_anticommunism_agreement_signed",
            "KOR_urihwangsilsaranghoe",
            "KOR_korea_in_the_world",
        ):
            self.assertEqual(
                len(re.findall(rf"(?m)^\s*id\s*=\s*{focus_id}\s*$", focuses)),
                1,
            )

        self.assertEqual(len(re.findall(r"(?m)^\s*id\s*=\s*525\s*$", state)), 1)
        self.assertIn("owner = KOR", state)
        self.assertIn("Japanese_want_annex_korea_since_they_fail", ai)
        self.assertIn("type = prepare_for_war", ai)
        self.assertIn("id = KOR", ai)


if __name__ == "__main__":
    unittest.main()
