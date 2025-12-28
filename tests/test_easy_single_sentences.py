# -*- coding: UTF-8 -*-
"""Single sentence inputs - should return a list with one element."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestSingleSentences:
    """Single sentence inputs - should return a list with one element."""

    @pytest.mark.parametrize("text,expected", [
        # Simple declarative sentences
        ("Hello world.", ["Hello world."]),
        ("The cat sat on the mat.", ["The cat sat on the mat."]),
        ("I love programming.", ["I love programming."]),
        ("Python is a great language.", ["Python is a great language."]),
        ("The quick brown fox jumps over the lazy dog.",
         ["The quick brown fox jumps over the lazy dog."]),

        # Questions
        ("How are you?", ["How are you?"]),
        ("What is your name?", ["What is your name?"]),
        ("Where did you go yesterday?", ["Where did you go yesterday?"]),
        ("Why is the sky blue?", ["Why is the sky blue?"]),
        ("Can you help me with this?", ["Can you help me with this?"]),

        # Exclamations
        ("Stop right there!", ["Stop right there!"]),
        ("What a beautiful day!", ["What a beautiful day!"]),
        ("I can't believe it!", ["I can't believe it!"]),
        ("Help!", ["Help!"]),
        ("Congratulations on your success!", ["Congratulations on your success!"]),

        # Single word sentences
        ("Yes.", ["Yes."]),
        ("No.", ["No."]),
        ("Maybe.", ["Maybe."]),
        ("Hello.", ["Hello."]),
        ("Goodbye.", ["Goodbye."]),
    ])
    def test_single_sentence(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
