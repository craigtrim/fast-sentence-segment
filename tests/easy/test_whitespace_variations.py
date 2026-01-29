# -*- coding: UTF-8 -*-
"""Tests with various whitespace patterns between sentences."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestWhitespaceVariations:
    """Tests with various whitespace patterns between sentences."""

    @pytest.mark.parametrize("text,expected", [
        # Single space between sentences
        ("Hello. World.", ["Hello.", "World."]),

        # Multiple spaces between sentences
        ("Hello.  World.", ["Hello.", "World."]),
        ("Hello.   World.", ["Hello.", "World."]),

        # Leading whitespace
        ("  Hello. World.", ["Hello.", "World."]),
        (" Hello. World.", ["Hello.", "World."]),

        # Trailing whitespace
        ("Hello. World.  ", ["Hello.", "World."]),
        ("Hello. World. ", ["Hello.", "World."]),

        # Mixed whitespace
        ("  Hello.   World.  ", ["Hello.", "World."]),

        # Tab characters
        ("Hello.\tWorld.", ["Hello.", "World."]),
        ("Hello.\t\tWorld.", ["Hello.", "World."]),

        # Newlines as sentence separators
        ("Hello.\nWorld.", ["Hello.", "World."]),
        ("Hello.\n\nWorld.", ["Hello.", "World."]),
        ("Line one.\nLine two.\nLine three.",
         ["Line one.", "Line two.", "Line three."]),
    ])
    def test_whitespace_variations(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
