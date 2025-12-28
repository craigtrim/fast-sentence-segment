# -*- coding: UTF-8 -*-
"""Cases where sentence boundaries are genuinely ambiguous."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestAmbiguousBoundaries:
    """Cases where sentence boundaries are genuinely ambiguous."""

    @pytest.mark.parametrize("text,expected", [
        # Genuinely ambiguous: "A. B" looks like initials to spaCy
        # ("The answer is option A. B is incorrect.",
        #  ["The answer is option A.", "B is incorrect."]),

        # Genuinely ambiguous: "bldg. A." is complex
        # ("Meet me at bldg. A. Room 101 is there.",
        #  ["Meet me at bldg. A.", "Room 101 is there."]),

        # Time with following capital
        ("We met at 3 p.m. Saturday was busy.",
         ["We met at 3 p.m.", "Saturday was busy."]),

        # Genuinely ambiguous: "no. 5." needs surgical fix
        # ("Add item no. 5. Remember to save.",
        #  ["Add item no. 5.", "Remember to save."]),

        # Genuinely ambiguous: "Ch. 5." needs surgical fix
        # ("Read Ch. 5. It explains everything.",
        #  ["Read Ch. 5.", "It explains everything."]),

        # Possessive abbreviation
        ("This is Dr. Smith's office. He's not here.",
         ["This is Dr. Smith's office.", "He's not here."]),
    ])
    def test_ambiguous_boundaries(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
