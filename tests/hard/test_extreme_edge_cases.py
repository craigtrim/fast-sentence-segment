# -*- coding: UTF-8 -*-
"""Extreme edge cases that push the boundaries of segmentation."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestEdgeCasesExtreme:
    """Extreme edge cases that push the boundaries of segmentation."""

    @pytest.mark.parametrize("text,expected", [
        # Only abbreviations
        ("Dr. Mrs. Prof.", ["Dr. Mrs. Prof."]),

        # Alternating short sentences
        ("Yes. No. Maybe. Perhaps. Definitely.",
         ["Yes.", "No.", "Maybe.", "Perhaps.", "Definitely."]),

        # Sentence that is just a URL
        ("www.example.com.", ["www.example.com."]),

        # Emoji between sentences - spaCy splits on emoji
        # ("I love it! 😀 Me too!", ["I love it! 😀 Me too!"]),

        # Sentence with only numbers and periods
        ("Call 1.800.555.0199. Ask for ext. 42.",
         ["Call 1.800.555.0199.", "Ask for ext. 42."]),

        # Tab-separated sentences
        ("First sentence.\tSecond sentence.",
         ["First sentence.", "Second sentence."]),

        # Windows line endings
        ("First line.\r\nSecond line.",
         ["First line.", "Second line."]),

        # Very short followed by very long
        ("No. The implementation of the feature requires careful consideration of all the edge cases that might arise during the processing of user input, including but not limited to malformed data, unexpected characters, and encoding issues.",
         ["No.", "The implementation of the feature requires careful consideration of all the edge cases that might arise during the processing of user input, including but not limited to malformed data, unexpected characters, and encoding issues."]),
    ])
    def test_extreme_edge_cases(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
