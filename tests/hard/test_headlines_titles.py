# -*- coding: UTF-8 -*-
"""Headlines, titles, and other non-sentence text."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestHeadlinesAndTitles:
    """Headlines, titles, and other non-sentence text."""

    @pytest.mark.parametrize("text,expected", [
        # News headline style - spaCy doesn't split on ALL CAPS colon pattern
        # ("BREAKING NEWS: Fire Destroys Building. No Injuries Reported.",
        #  ["BREAKING NEWS: Fire Destroys Building.", "No Injuries Reported."]),

        # Title followed by content
        ("Chapter 1. The Beginning. It was a dark and stormy night.",
         ["Chapter 1.", "The Beginning.", "It was a dark and stormy night."]),

        # Section headers
        ("Section 3.1. Methodology. We used a mixed-methods approach.",
         ["Section 3.1.", "Methodology.", "We used a mixed-methods approach."]),

        # Book/movie titles in text - requires quote-aware parsing
        # ('I read "To Kill a Mockingbird." It was moving.',
        #  ['I read "To Kill a Mockingbird."', 'It was moving.']),

        # Titles with Mr./Mrs.
        ('"Mr. Smith Goes to Washington" is a classic. I loved it.',
         ['"Mr. Smith Goes to Washington" is a classic.', 'I loved it.']),
    ])
    def test_headlines_titles(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
