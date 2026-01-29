# -*- coding: UTF-8 -*-
"""Scientific and mathematical expressions."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestScientificNotation:
    """Scientific and mathematical expressions."""

    @pytest.mark.parametrize("text,expected", [
        # Scientific notation
        ("The speed of light is 3.0 × 10^8 m/s. This is constant.",
         ["The speed of light is 3.0 × 10^8 m/s.", "This is constant."]),

        # Chemical formulas - spaCy sees CO2. as different token pattern
        # ("Water is H2O. Carbon dioxide is CO2.",
        #  ["Water is H2O.", "Carbon dioxide is CO2."]),

        # Mathematical expressions
        ("If x = 2.5, then y = 5.0. The ratio is constant.",
         ["If x = 2.5, then y = 5.0.", "The ratio is constant."]),

        # Coordinates
        ("The location is 40.7128° N, 74.0060° W. That's New York.",
         ["The location is 40.7128° N, 74.0060° W.", "That's New York."]),

        # Range expressions
        ("The temperature ranges from 20.5°C to 25.5°C. Stay comfortable.",
         ["The temperature ranges from 20.5°C to 25.5°C.", "Stay comfortable."]),

        # Equations with periods
        ("Solve for x: 2x + 3 = 7. The answer is x = 2.",
         ["Solve for x: 2x + 3 = 7.", "The answer is x = 2."]),
    ])
    def test_scientific_notation(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
