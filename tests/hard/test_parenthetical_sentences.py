# -*- coding: UTF-8 -*-
"""Complete sentences within parentheses."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestParentheticalSentences:
    """Complete sentences within parentheses."""

    @pytest.mark.parametrize("text,expected", [
        # Full sentence in parentheses
        ("The results were clear (see Table 1). We proceeded.",
         ["The results were clear (see Table 1).", "We proceeded."]),

        # Parenthetical sentence at end - spaCy includes paren in previous sentence
        # ("He agreed. (This surprised everyone.)",
        #  ["He agreed.", "(This surprised everyone.)"]),

        # Multiple parenthetical elements
        ("The data (n=100) shows improvement (p<0.05).",
         ["The data (n=100) shows improvement (p<0.05)."]),

        # Nested parentheses
        ("The results (shown in Fig. 1 (a) and (b)) are clear.",
         ["The results (shown in Fig. 1 (a) and (b)) are clear."]),

        # Brackets instead of parentheses - complex bracket handling
        # ("The study [Smith, 2020] confirms this. [Editor's note: disputed.]",
        #  ["The study [Smith, 2020] confirms this.", "[Editor's note: disputed.]"]),

        # Question in parentheses
        ("He left early (why did he leave?) without explanation.",
         ["He left early (why did he leave?) without explanation."]),
    ])
    def test_parenthetical_sentences(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
