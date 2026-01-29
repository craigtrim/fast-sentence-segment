# -*- coding: UTF-8 -*-
"""Sentences with basic internal punctuation."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestBasicPunctuation:
    """Sentences with basic internal punctuation."""

    @pytest.mark.parametrize("text,expected", [
        # Commas
        ("I bought apples, oranges, and bananas.",
         ["I bought apples, oranges, and bananas."]),
        ("Well, I suppose so.", ["Well, I suppose so."]),
        ("After dinner, we watched a movie.",
         ["After dinner, we watched a movie."]),

        # Colons in simple contexts
        ("Here is the answer: yes.", ["Here is the answer: yes."]),
        ("I need three things: paper, pen, and ink.",
         ["I need three things: paper, pen, and ink."]),

        # Semicolons
        ("I came; I saw; I conquered.", ["I came; I saw; I conquered."]),
        ("The sun set; darkness fell.", ["The sun set; darkness fell."]),

        # Hyphens
        ("It was a well-known fact.", ["It was a well-known fact."]),
        ("The twenty-five year old man arrived.",
         ["The twenty-five year old man arrived."]),

        # Apostrophes
        ("I can't do this.", ["I can't do this."]),
        ("She's the one who called.", ["She's the one who called."]),
        ("It's John's book.", ["It's John's book."]),
    ])
    def test_basic_punctuation(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
