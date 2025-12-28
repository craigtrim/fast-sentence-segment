# -*- coding: UTF-8 -*-
"""Simple quoted text within sentences."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestSimpleQuotes:
    """Simple quoted text within sentences."""

    @pytest.mark.parametrize("text,expected", [
        # Quoted words
        ('He said "hello" to me.', ['He said "hello" to me.']),
        ("She called it 'brilliant' work.", ["She called it 'brilliant' work."]),

        # Multiple sentences, one with quote
        ('He said "hello" to me. I waved back.',
         ['He said "hello" to me.', 'I waved back.']),

        # Quote at beginning
        ('"Hello" was all he said.', ['"Hello" was all he said.']),

        # Quote at end
        ('The answer was simply "no".', ['The answer was simply "no".']),
    ])
    def test_simple_quotes(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
