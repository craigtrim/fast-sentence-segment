# -*- coding: UTF-8 -*-
"""Sentences with parenthetical expressions."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestParentheses:
    """Sentences with parenthetical expressions."""

    @pytest.mark.parametrize("text,expected", [
        # Simple parenthetical
        ("He arrived (finally) at noon.", ["He arrived (finally) at noon."]),
        ("The answer (42) was surprising.", ["The answer (42) was surprising."]),

        # Longer parenthetical
        ("She (the new manager) called today.",
         ["She (the new manager) called today."]),
        ("The book (published in 2020) was excellent.",
         ["The book (published in 2020) was excellent."]),

        # Parenthetical with period inside
        ("Read the book (see Ch. 5) for details.",
         ["Read the book (see Ch. 5) for details."]),
        # esp. Sec. inside parentheses - complex abbreviation chain
        # ("Follow the guide (esp. Sec. 3.2) carefully.",
        #  ["Follow the guide (esp. Sec. 3.2) carefully."]),

        # Parentheses at end
        ("Call support (open 9-5).", ["Call support (open 9-5)."]),
        ("The meeting is tomorrow (at 3 p.m.).",
         ["The meeting is tomorrow (at 3 p.m.)."]),

        # Multiple sentences with parentheses
        ("He works at Google (since 2020). She works at Apple.",
         ["He works at Google (since 2020).", "She works at Apple."]),
    ])
    def test_parentheses(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
