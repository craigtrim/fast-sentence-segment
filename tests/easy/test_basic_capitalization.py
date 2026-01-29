# -*- coding: UTF-8 -*-
"""Tests verifying sentence boundaries work with various capitalization."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestBasicCapitalization:
    """Tests verifying sentence boundaries work with various capitalization."""

    @pytest.mark.parametrize("text,expected", [
        # Normal capitalization
        ("Hello there. How are you?", ["Hello there.", "How are you?"]),

        # All caps sentence
        ("STOP RIGHT THERE. Do not move.",
         ["STOP RIGHT THERE.", "Do not move."]),

        # All lowercase (unusual but valid)
        ("hello there. how are you?", ["hello there.", "how are you?"]),

        # Mixed in same text
        ("WARNING! This is important. PAY ATTENTION!",
         ["WARNING!", "This is important.", "PAY ATTENTION!"]),
    ])
    def test_capitalization(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
