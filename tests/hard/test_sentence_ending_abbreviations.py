# -*- coding: UTF-8 -*-
"""Sentences that end with abbreviations (ambiguous boundaries)."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestSentenceEndingAbbreviations:
    """Sentences that end with abbreviations (ambiguous boundaries)."""

    @pytest.mark.parametrize("text,expected", [
        # Ending with etc.
        ("We bought apples, oranges, etc. The store was crowded.",
         ["We bought apples, oranges, etc.", "The store was crowded."]),

        # Ending with Inc./Corp.
        ("She works at Google Inc. He works at Microsoft Corp.",
         ["She works at Google Inc.", "He works at Microsoft Corp."]),

        # Ending with Jr./Sr.
        ("I met John Smith Jr. His father is John Smith Sr.",
         ["I met John Smith Jr.", "His father is John Smith Sr."]),

        # Ending with Ph.D./M.D.
        ("She earned her Ph.D. Her brother earned his M.D.",
         ["She earned her Ph.D.", "Her brother earned his M.D."]),

        # Ending with U.S./U.K.
        ("He moved to the U.S. She moved to the U.K.",
         ["He moved to the U.S.", "She moved to the U.K."]),

        # Ending with time
        ("The show starts at 8 p.m. The doors open at 7 p.m.",
         ["The show starts at 8 p.m.", "The doors open at 7 p.m."]),

        # Ending with vs.
        ("It's quality vs. quantity. Choose wisely.",
         ["It's quality vs. quantity.", "Choose wisely."]),
    ])
    def test_sentence_ending_abbreviations(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
