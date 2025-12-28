# -*- coding: UTF-8 -*-
"""Simple sentences containing numbers."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestBasicNumbers:
    """Simple sentences containing numbers."""

    @pytest.mark.parametrize("text,expected", [
        # Cardinal numbers
        ("I have 5 apples.", ["I have 5 apples."]),
        ("There are 100 people here.", ["There are 100 people here."]),
        ("She is 25 years old.", ["She is 25 years old."]),

        # Ordinal numbers
        ("This is my 1st attempt.", ["This is my 1st attempt."]),
        ("He finished in 3rd place.", ["He finished in 3rd place."]),

        # Multiple sentences with numbers
        ("I have 3 cats. She has 2 dogs.",
         ["I have 3 cats.", "She has 2 dogs."]),
        ("There are 50 states. Each has its own capital.",
         ["There are 50 states.", "Each has its own capital."]),

        # Years
        ("The year is 2024.", ["The year is 2024."]),
        ("She was born in 1990.", ["She was born in 1990."]),
        ("World War 2 ended in 1945. Many lives were lost.",
         ["World War 2 ended in 1945.", "Many lives were lost."]),
    ])
    def test_basic_numbers(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
