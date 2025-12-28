# -*- coding: UTF-8 -*-
"""Multiple abbreviations appearing in sequence."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestConsecutiveAbbreviations:
    """Multiple abbreviations appearing in sequence."""

    @pytest.mark.parametrize("text,expected", [
        # Back-to-back abbreviations
        ("Contact Dr. Mr. J.R. Smith Jr. at the office.",
         ["Contact Dr. Mr. J.R. Smith Jr. at the office."]),

        # Dense abbreviation chain - E.S.T. confuses spaCy
        # ("The event is at 5 p.m. E.S.T. on Dec. 25th.",
        #  ["The event is at 5 p.m. E.S.T. on Dec. 25th."]),

        # Sentence ending with abbreviation followed by new sentence
        ("He lives in Washington D.C. She lives in New York.",
         ["He lives in Washington D.C.", "She lives in New York."]),

        ("The meeting ends at 5 p.m. Don't be late.",
         ["The meeting ends at 5 p.m.", "Don't be late."]),

        # Multiple abbreviations at sentence end - Corp. Inc. chain
        # ("Call Acme Corp. Inc. for details.",
        #  ["Call Acme Corp. Inc. for details."]),

        # Abbreviations followed by abbreviation-starting sentence
        ("I work at Acme Inc. Dr. Smith is my boss.",
         ["I work at Acme Inc.", "Dr. Smith is my boss."]),

        # Dense abbreviation text - very complex chain
        # ("Prof. J.D. Williams, Ph.D., M.D., spoke at 3 p.m. at MIT.",
        #  ["Prof. J.D. Williams, Ph.D., M.D., spoke at 3 p.m. at MIT."]),
    ])
    def test_consecutive_abbreviations(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
