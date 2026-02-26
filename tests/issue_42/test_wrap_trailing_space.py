# -*- coding: UTF-8 -*-
"""Unit tests for NewlinesToPeriods with trailing spaces before the newline.

These are the cases where the line ending has trailing whitespace BEFORE the
newline. Combined with any indent on the continuation line, this can create
an even larger gap. After the fix, `line.strip()` removes both trailing spaces
on the first line and leading spaces on the second, producing a clean single-
space join.

Variants covered:
  - single trailing space + no indent:     "word \nword"
  - single trailing space + 4-space:       "word \n    word"
  - two trailing spaces + no indent:       "word  \nword"
  - two trailing spaces + 4-space indent:  "word  \n    word"

Currently FAILING for indented variants (documents desired post-fix behavior).

Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
"""

from fast_sentence_segment.dmo.newlines_to_periods import NewlinesToPeriods


class TestWrapTrailingSpace:
    """Hard-wrapped lines with trailing whitespace before the newline."""

    # ---------------------------------------------------------------- single trailing space + no indent

    def test_one_trailing_no_indent_01(self):
        assert NewlinesToPeriods.process("She walked down the long \ncorridor.") == "She walked down the long corridor."

    def test_one_trailing_no_indent_02(self):
        assert NewlinesToPeriods.process("He opened the heavy oak \ndoor slowly.") == "He opened the heavy oak door slowly."

    def test_one_trailing_no_indent_03(self):
        assert NewlinesToPeriods.process("The sun was setting \nbehind the mountains.") == "The sun was setting behind the mountains."

    def test_one_trailing_no_indent_04(self):
        assert NewlinesToPeriods.process("A cold wind swept across \nthe courtyard.") == "A cold wind swept across the courtyard."

    def test_one_trailing_no_indent_05(self):
        assert NewlinesToPeriods.process("Rain had been falling \nsince early morning.") == "Rain had been falling since early morning."

    def test_one_trailing_no_indent_06(self):
        assert NewlinesToPeriods.process("The minister resigned \namid allegations.") == "The minister resigned amid allegations."

    def test_one_trailing_no_indent_07(self):
        assert NewlinesToPeriods.process("The reaction was complete \nafter sixty minutes.") == "The reaction was complete after sixty minutes."

    def test_one_trailing_no_indent_08(self):
        assert NewlinesToPeriods.process("The army crossed the river \nat dawn.") == "The army crossed the river at dawn."

    def test_one_trailing_no_indent_09(self):
        assert NewlinesToPeriods.process("The contract shall be \ngoverned by English law.") == "The contract shall be governed by English law."

    def test_one_trailing_no_indent_10(self):
        assert NewlinesToPeriods.process("Assist in the business \ndepartment.") == "Assist in the business department."

    def test_one_trailing_no_indent_11(self):
        assert NewlinesToPeriods.process("The advertising \ndepartment was on the third floor.") == "The advertising department was on the third floor."

    def test_one_trailing_no_indent_12(self):
        assert NewlinesToPeriods.process("She managed the marketing \nteam for ten years.") == "She managed the marketing team for ten years."

    def test_one_trailing_no_indent_13(self):
        assert NewlinesToPeriods.process("Apply to the Personnel \nManager before Friday.") == "Apply to the Personnel Manager before Friday."

    def test_one_trailing_no_indent_14(self):
        assert NewlinesToPeriods.process("Bake in a preheated oven at \n180 degrees.") == "Bake in a preheated oven at 180 degrees."

    def test_one_trailing_no_indent_15(self):
        assert NewlinesToPeriods.process("The committee reviewed all \nsubmitted applications.") == "The committee reviewed all submitted applications."

    # ---------------------------------------------------------------- single trailing space + 4-space indent

    def test_one_trailing_4space_01(self):
        result = NewlinesToPeriods.process("She walked down the long \n    corridor.")
        assert "long.corridor" not in result
        assert result == "She walked down the long corridor."

    def test_one_trailing_4space_02(self):
        result = NewlinesToPeriods.process("assist in the business \n    department during the holidays.")
        assert "business.department" not in result
        assert result == "assist in the business department during the holidays."

    def test_one_trailing_4space_03(self):
        result = NewlinesToPeriods.process("The sun was setting behind \n    the mountains.")
        assert "behind.the" not in result
        assert result == "The sun was setting behind the mountains."

    def test_one_trailing_4space_04(self):
        result = NewlinesToPeriods.process("He opened the heavy oak \n    door slowly.")
        assert "oak.door" not in result
        assert result == "He opened the heavy oak door slowly."

    def test_one_trailing_4space_05(self):
        result = NewlinesToPeriods.process("A cold wind swept across \n    the courtyard.")
        assert "across.the" not in result
        assert result == "A cold wind swept across the courtyard."

    def test_one_trailing_4space_06(self):
        result = NewlinesToPeriods.process("Rain had been falling since \n    early morning.")
        assert "since.early" not in result
        assert result == "Rain had been falling since early morning."

    def test_one_trailing_4space_07(self):
        result = NewlinesToPeriods.process("The minister resigned amid \n    allegations of misconduct.")
        assert "amid.allegations" not in result
        assert result == "The minister resigned amid allegations of misconduct."

    def test_one_trailing_4space_08(self):
        result = NewlinesToPeriods.process("The reaction was complete after \n    sixty minutes.")
        assert "after.sixty" not in result
        assert result == "The reaction was complete after sixty minutes."

    def test_one_trailing_4space_09(self):
        result = NewlinesToPeriods.process("The army crossed the river at \n    dawn.")
        assert "at.dawn" not in result
        assert result == "The army crossed the river at dawn."

    def test_one_trailing_4space_10(self):
        result = NewlinesToPeriods.process("The advertising \n    department was on the third floor.")
        assert "advertising.department" not in result
        assert result == "The advertising department was on the third floor."

    def test_one_trailing_4space_11(self):
        result = NewlinesToPeriods.process("She managed the marketing \n    team for ten years.")
        assert "marketing.team" not in result
        assert result == "She managed the marketing team for ten years."

    def test_one_trailing_4space_12(self):
        result = NewlinesToPeriods.process("Apply to the Personnel \n    Manager before Friday.")
        assert "Personnel.Manager" not in result
        assert result == "Apply to the Personnel Manager before Friday."

    def test_one_trailing_4space_13(self):
        result = NewlinesToPeriods.process("The health \n    department issued a warning.")
        assert "health.department" not in result
        assert result == "The health department issued a warning."

    def test_one_trailing_4space_14(self):
        result = NewlinesToPeriods.process("The finance \n    committee approved the budget.")
        assert "finance.committee" not in result
        assert result == "The finance committee approved the budget."

    def test_one_trailing_4space_15(self):
        result = NewlinesToPeriods.process("The foreign \n    office sent a telegram.")
        assert "foreign.office" not in result
        assert result == "The foreign office sent a telegram."

    # ---------------------------------------------------------------- two trailing spaces + no indent

    def test_two_trailing_no_indent_01(self):
        assert NewlinesToPeriods.process("She walked down the long  \ncorridor.") == "She walked down the long corridor."

    def test_two_trailing_no_indent_02(self):
        assert NewlinesToPeriods.process("He opened the heavy  \ndoor slowly.") == "He opened the heavy door slowly."

    def test_two_trailing_no_indent_03(self):
        assert NewlinesToPeriods.process("The sun was setting  \nbehind the mountains.") == "The sun was setting behind the mountains."

    def test_two_trailing_no_indent_04(self):
        assert NewlinesToPeriods.process("assist in the business  \ndepartment.") == "assist in the business department."

    def test_two_trailing_no_indent_05(self):
        assert NewlinesToPeriods.process("The advertising  \ndepartment was on the third floor.") == "The advertising department was on the third floor."

    def test_two_trailing_no_indent_06(self):
        assert NewlinesToPeriods.process("The fire  \nstation was nearby.") == "The fire station was nearby."

    def test_two_trailing_no_indent_07(self):
        assert NewlinesToPeriods.process("The post  \noffice opened at nine.") == "The post office opened at nine."

    def test_two_trailing_no_indent_08(self):
        assert NewlinesToPeriods.process("The night  \nwatchman made his rounds.") == "The night watchman made his rounds."

    def test_two_trailing_no_indent_09(self):
        assert NewlinesToPeriods.process("She could not find  \nthe key anywhere.") == "She could not find the key anywhere."

    def test_two_trailing_no_indent_10(self):
        assert NewlinesToPeriods.process("He stared at the portrait  \nfor a long time.") == "He stared at the portrait for a long time."

    # ---------------------------------------------------------------- two trailing spaces + 4-space indent

    def test_two_trailing_4space_01(self):
        result = NewlinesToPeriods.process("assist in the business  \n    department.")
        assert "business.department" not in result
        assert result == "assist in the business department."

    def test_two_trailing_4space_02(self):
        result = NewlinesToPeriods.process("The advertising  \n    department was on the third floor.")
        assert "advertising.department" not in result
        assert result == "The advertising department was on the third floor."

    def test_two_trailing_4space_03(self):
        result = NewlinesToPeriods.process("She walked down the long  \n    corridor.")
        assert "long.corridor" not in result
        assert result == "She walked down the long corridor."

    def test_two_trailing_4space_04(self):
        result = NewlinesToPeriods.process("He opened the heavy oak  \n    door slowly.")
        assert "oak.door" not in result
        assert result == "He opened the heavy oak door slowly."

    def test_two_trailing_4space_05(self):
        result = NewlinesToPeriods.process("The night  \n    watchman made his rounds.")
        assert "night.watchman" not in result
        assert result == "The night watchman made his rounds."

    def test_two_trailing_4space_06(self):
        result = NewlinesToPeriods.process("The foreign  \n    office sent a telegram.")
        assert "foreign.office" not in result
        assert result == "The foreign office sent a telegram."

    def test_two_trailing_4space_07(self):
        result = NewlinesToPeriods.process("The finance  \n    committee approved.")
        assert "finance.committee" not in result
        assert result == "The finance committee approved."

    def test_two_trailing_4space_08(self):
        result = NewlinesToPeriods.process("The health  \n    department issued a warning.")
        assert "health.department" not in result
        assert result == "The health department issued a warning."

    def test_two_trailing_4space_09(self):
        result = NewlinesToPeriods.process("The fire  \n    station was nearby.")
        assert "fire.station" not in result
        assert result == "The fire station was nearby."

    def test_two_trailing_4space_10(self):
        result = NewlinesToPeriods.process("The post  \n    office opened at nine.")
        assert "post.office" not in result
        assert result == "The post office opened at nine."

    # ---------------------------------------------------------------- trailing space + 2-space indent

    def test_one_trailing_2space_01(self):
        result = NewlinesToPeriods.process("assist in the business \n  department.")
        assert "business.department" not in result
        assert result == "assist in the business department."

    def test_one_trailing_2space_02(self):
        result = NewlinesToPeriods.process("the advertising \n  department.")
        assert "advertising.department" not in result
        assert result == "the advertising department."

    def test_one_trailing_2space_03(self):
        result = NewlinesToPeriods.process("the marketing \n  team.")
        assert "marketing.team" not in result
        assert result == "the marketing team."

    # ---------------------------------------------------------------- trailing space + tab indent

    def test_one_trailing_tab_01(self):
        result = NewlinesToPeriods.process("assist in the business \n\tdepartment.")
        assert "business.department" not in result
        assert result == "assist in the business department."

    def test_one_trailing_tab_02(self):
        result = NewlinesToPeriods.process("the advertising \n\tdepartment.")
        assert "advertising.department" not in result
        assert result == "the advertising department."

    def test_one_trailing_tab_03(self):
        result = NewlinesToPeriods.process("the fire \n\tstation.")
        assert "fire.station" not in result
        assert result == "the fire station."

    # ---------------------------------------------------------------- many trailing spaces

    def test_many_trailing_no_indent_01(self):
        assert NewlinesToPeriods.process("She walked down     \nthe corridor.") == "She walked down the corridor."

    def test_many_trailing_no_indent_02(self):
        assert NewlinesToPeriods.process("assist in the business     \ndepartment.") == "assist in the business department."

    def test_many_trailing_4space_01(self):
        result = NewlinesToPeriods.process("assist in the business     \n    department.")
        assert "business.department" not in result
        assert result == "assist in the business department."

    def test_many_trailing_4space_02(self):
        result = NewlinesToPeriods.process("the advertising     \n    department.")
        assert "advertising.department" not in result
        assert result == "the advertising department."
