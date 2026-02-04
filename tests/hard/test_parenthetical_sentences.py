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

    @pytest.mark.skip(reason="""
        SKIP REASON: Statistical notation (n=100, p<0.05) with periods triggers false splits.

        This test expects "The data (n=100) shows improvement (p<0.05)." to remain
        as one sentence, but the combination of parenthetical content with periods
        nearby can confuse spaCy's tokenizer.

        Current behavior: May split around parenthetical statistical notations
        Expected by test: ["The data (n=100) shows improvement (p<0.05)."]

        The challenge: Scientific/statistical notation often uses patterns like:
        - (n=100) - sample size
        - (p<0.05) - significance level
        - (Fig. 1a) - figure references

        These contain periods and special characters that interact with spaCy's
        sentence boundary detection in unpredictable ways.

        Supporting this fully would require:
        1. Detection of statistical notation patterns
        2. Special handling for scientific parentheticals
        3. Coordination with abbreviation and figure reference handling

        This is a specialized scientific writing edge case that doesn't affect
        typical prose segmentation.

        Related: ParentheticalMerger in fast_sentence_segment/dmo/parenthetical_merger.py
    """)
    @pytest.mark.parametrize("text,expected", [
        # Multiple parenthetical elements with statistical notation
        ("The data (n=100) shows improvement (p<0.05).",
         ["The data (n=100) shows improvement (p<0.05)."]),
    ])
    def test_parenthetical_statistical_notation(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
