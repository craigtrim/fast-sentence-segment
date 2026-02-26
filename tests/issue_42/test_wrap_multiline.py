# -*- coding: UTF-8 -*-
"""Unit tests for NewlinesToPeriods with multiple consecutive hard-wrapped lines.

These tests cover 3, 4, and 5 consecutive hard-wrapped lines (single `\n`,
no blank lines), with and without indent on continuation lines. After the fix,
every newline must produce a single space join regardless of how many consecutive
wrapped lines appear.

Currently FAILING for indented variants (documents desired post-fix behavior).

Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
"""

from fast_sentence_segment.dmo.newlines_to_periods import NewlinesToPeriods


class TestWrapMultiline:
    """Multiple consecutive hard-wrapped lines with various indent patterns."""

    # ---------------------------------------------------------------- 3 lines, no indent

    def test_three_no_indent_01(self):
        inp = "Young men to assist in the\nbusiness department during\nthe Christmas holidays."
        assert NewlinesToPeriods.process(inp) == "Young men to assist in the business department during the Christmas holidays."

    def test_three_no_indent_02(self):
        inp = "She walked down the long\ncorridor towards the room\nat the end of the hall."
        assert NewlinesToPeriods.process(inp) == "She walked down the long corridor towards the room at the end of the hall."

    def test_three_no_indent_03(self):
        inp = "The committee met on three\nseparate occasions to discuss\nthe proposed legislation."
        assert NewlinesToPeriods.process(inp) == "The committee met on three separate occasions to discuss the proposed legislation."

    def test_three_no_indent_04(self):
        inp = "He had lived in the town\nfor twenty years without\nonce feeling at home."
        assert NewlinesToPeriods.process(inp) == "He had lived in the town for twenty years without once feeling at home."

    def test_three_no_indent_05(self):
        inp = "The delegation arrived\nhaving already agreed\non their main position."
        assert NewlinesToPeriods.process(inp) == "The delegation arrived having already agreed on their main position."

    def test_three_no_indent_06(self):
        inp = "She had always hoped\nto travel but never\nfound the opportunity."
        assert NewlinesToPeriods.process(inp) == "She had always hoped to travel but never found the opportunity."

    def test_three_no_indent_07(self):
        inp = "The final report was\nsubmitted to the committee\non the morning of the deadline."
        assert NewlinesToPeriods.process(inp) == "The final report was submitted to the committee on the morning of the deadline."

    def test_three_no_indent_08(self):
        inp = "Investigators say the\nfire broke out in\nthe early hours of the morning."
        assert NewlinesToPeriods.process(inp) == "Investigators say the fire broke out in the early hours of the morning."

    def test_three_no_indent_09(self):
        inp = "Results were analysed\nusing a standard\nregression model."
        assert NewlinesToPeriods.process(inp) == "Results were analysed using a standard regression model."

    def test_three_no_indent_10(self):
        inp = "The party of the\nfirst part agrees\nto deliver by Friday."
        assert NewlinesToPeriods.process(inp) == "The party of the first part agrees to deliver by Friday."

    # ---------------------------------------------------------------- 3 lines, 4-space indent

    def test_three_4space_01(self):
        inp = "Young men to assist in the\n    business department during\n    the Christmas holidays."
        assert NewlinesToPeriods.process(inp) == "Young men to assist in the business department during the Christmas holidays."

    def test_three_4space_02(self):
        inp = "She walked down the long\n    corridor towards the room\n    at the end of the hall."
        assert NewlinesToPeriods.process(inp) == "She walked down the long corridor towards the room at the end of the hall."

    def test_three_4space_03(self):
        inp = "The committee met on three\n    separate occasions to discuss\n    the proposed legislation."
        assert NewlinesToPeriods.process(inp) == "The committee met on three separate occasions to discuss the proposed legislation."

    def test_three_4space_04(self):
        inp = "He had lived in the town\n    for twenty years without\n    once feeling at home."
        assert NewlinesToPeriods.process(inp) == "He had lived in the town for twenty years without once feeling at home."

    def test_three_4space_05(self):
        result = NewlinesToPeriods.process(
            "assist in the business\n    department during\n    the Christmas holidays."
        )
        assert "business.department" not in result
        assert "department.during" not in result
        assert result == "assist in the business department during the Christmas holidays."

    def test_three_4space_06(self):
        inp = "She had always hoped\n    to travel but never\n    found the opportunity."
        assert NewlinesToPeriods.process(inp) == "She had always hoped to travel but never found the opportunity."

    def test_three_4space_07(self):
        inp = "The final report was\n    submitted to the committee\n    on the deadline morning."
        assert NewlinesToPeriods.process(inp) == "The final report was submitted to the committee on the deadline morning."

    def test_three_4space_08(self):
        inp = "Results were analysed\n    using a standard\n    regression model."
        assert NewlinesToPeriods.process(inp) == "Results were analysed using a standard regression model."

    def test_three_4space_09(self):
        result = NewlinesToPeriods.process(
            "the advertising\n    department on\n    the third floor."
        )
        assert "advertising.department" not in result
        assert "department.on" not in result
        assert result == "the advertising department on the third floor."

    def test_three_4space_10(self):
        inp = "Apply to the Business\n    Manager between\n    9 and 10 a.m."
        assert NewlinesToPeriods.process(inp) == "Apply to the Business Manager between 9 and 10 a.m."

    # ---------------------------------------------------------------- 4 lines, no indent

    def test_four_no_indent_01(self):
        inp = "Wanted: A number of bright\nyoung men to assist in\nthe business department\nduring the holidays."
        assert NewlinesToPeriods.process(inp) == "Wanted: A number of bright young men to assist in the business department during the holidays."

    def test_four_no_indent_02(self):
        inp = "She walked down the long\ncorridor towards the room\nat the end of the hall\nand knocked."
        assert NewlinesToPeriods.process(inp) == "She walked down the long corridor towards the room at the end of the hall and knocked."

    def test_four_no_indent_03(self):
        inp = "The committee met on\nthree occasions to\ndiscuss the proposed\nlegislation."
        assert NewlinesToPeriods.process(inp) == "The committee met on three occasions to discuss the proposed legislation."

    def test_four_no_indent_04(self):
        inp = "He had lived in the\ntown for twenty years\nwithout once feeling\ntruly at home."
        assert NewlinesToPeriods.process(inp) == "He had lived in the town for twenty years without once feeling truly at home."

    def test_four_no_indent_05(self):
        inp = "The sun had set\nand the streets\nwere empty and\ncold."
        assert NewlinesToPeriods.process(inp) == "The sun had set and the streets were empty and cold."

    # ---------------------------------------------------------------- 4 lines, 4-space indent

    def test_four_4space_01(self):
        inp = "Wanted: A number of bright\n    young men to assist in\n    the business department\n    during the holidays."
        assert NewlinesToPeriods.process(inp) == "Wanted: A number of bright young men to assist in the business department during the holidays."

    def test_four_4space_02(self):
        result = NewlinesToPeriods.process(
            "assist in the\n    business department\n    during the\n    Christmas holidays."
        )
        assert "the.business" not in result
        assert "business.department" not in result
        assert "department.during" not in result
        assert result == "assist in the business department during the Christmas holidays."

    def test_four_4space_03(self):
        inp = "She walked down\n    the long corridor\n    towards the room\n    at the end."
        assert NewlinesToPeriods.process(inp) == "She walked down the long corridor towards the room at the end."

    def test_four_4space_04(self):
        inp = "The committee met\n    on three separate\n    occasions to\n    discuss the bill."
        assert NewlinesToPeriods.process(inp) == "The committee met on three separate occasions to discuss the bill."

    def test_four_4space_05(self):
        inp = "He had lived in\n    the town for\n    twenty years\n    without respite."
        assert NewlinesToPeriods.process(inp) == "He had lived in the town for twenty years without respite."

    # ---------------------------------------------------------------- 5 lines, no indent

    def test_five_no_indent_01(self):
        inp = "Wanted: A number of\nbright young men to\nassist in the business\ndepartment during the\nChristmas holidays."
        assert NewlinesToPeriods.process(inp) == "Wanted: A number of bright young men to assist in the business department during the Christmas holidays."

    def test_five_no_indent_02(self):
        inp = "She walked down\nthe long corridor\ntowards the room\nat the end of\nthe hall."
        assert NewlinesToPeriods.process(inp) == "She walked down the long corridor towards the room at the end of the hall."

    def test_five_no_indent_03(self):
        inp = "The committee met\non three occasions\nto discuss the\nproposed new\nlegislation."
        assert NewlinesToPeriods.process(inp) == "The committee met on three occasions to discuss the proposed new legislation."

    # ---------------------------------------------------------------- 5 lines, 4-space indent

    def test_five_4space_01(self):
        inp = "Wanted: A number of\n    bright young men to\n    assist in the business\n    department during the\n    Christmas holidays."
        assert NewlinesToPeriods.process(inp) == "Wanted: A number of bright young men to assist in the business department during the Christmas holidays."

    def test_five_4space_02(self):
        result = NewlinesToPeriods.process(
            "assist in the\n    business\n    department\n    during the\n    holidays."
        )
        assert "the.business" not in result
        assert "business.department" not in result
        assert result == "assist in the business department during the holidays."

    # ---------------------------------------------------------------- mixed indent levels

    def test_mixed_indent_3line_01(self):
        # First continuation has 4-space, second has 2-space
        inp = "She walked down the long\n    corridor towards the\n  room at the end."
        assert NewlinesToPeriods.process(inp) == "She walked down the long corridor towards the room at the end."

    def test_mixed_indent_3line_02(self):
        # No indent on first continuation, 4-space on second
        inp = "She walked down the long\ncorridor towards the\n    room at the end."
        assert NewlinesToPeriods.process(inp) == "She walked down the long corridor towards the room at the end."

    def test_mixed_indent_3line_03(self):
        # Tab on first continuation, 4-space on second
        inp = "assist in the business\n\tdepartment during\n    the holidays."
        result = NewlinesToPeriods.process(inp)
        assert "business.department" not in result
        assert "department.during" not in result
        assert result == "assist in the business department during the holidays."

    # ---------------------------------------------------------------- dreiser full passage (3 lines)

    def test_dreiser_full_passage(self):
        inp = (
            "Wanted: A number of bright young men to assist in the business\n"
            "    department during the Christmas holidays. Promotion possible.\n"
            "    Apply to Business Manager between 9 and 10 a.m."
        )
        result = NewlinesToPeriods.process(inp)
        assert "business.department" not in result
        assert "possible.Apply" not in result
        assert "possible.apply" not in result
        assert result == (
            "Wanted: A number of bright young men to assist in the business "
            "department during the Christmas holidays. Promotion possible. "
            "Apply to Business Manager between 9 and 10 a.m."
        )
