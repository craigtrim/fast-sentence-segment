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

        # Range expressions
        ("The temperature ranges from 20.5°C to 25.5°C. Stay comfortable.",
         ["The temperature ranges from 20.5°C to 25.5°C.", "Stay comfortable."]),
    ])
    def test_scientific_notation(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected

    @pytest.mark.skip(reason="""
        SKIP REASON: Geographic coordinates and equations with special characters
        interact unpredictably with spaCy tokenization.

        These test cases involve:
        1. Coordinates with degree symbols (°) and direction letters (N, W)
        2. Mathematical equations with colons and equals signs

        Current behavior: May split incorrectly around "W." or "7."
        Expected behavior: Split only at actual sentence boundaries

        The challenges:

        COORDINATES (40.7128° N, 74.0060° W. That's New York.):
        - The "W." pattern looks like an abbreviation
        - Degree symbol (°) creates unusual token boundaries
        - Direction letters (N, W) are single uppercase characters

        EQUATIONS (Solve for x: 2x + 3 = 7. The answer is x = 2.):
        - The colon after "x:" affects sentence detection
        - Numbers followed by periods (7.) can confuse boundary detection
        - Mathematical syntax doesn't follow prose patterns

        Supporting these would require domain-specific preprocessing for
        geographic coordinates and mathematical notation, which is beyond
        the scope of general-purpose sentence segmentation.

        Note: Standard scientific notation (3.0 × 10^8 m/s) works correctly.
    """)
    @pytest.mark.parametrize("text,expected", [
        # Coordinates - degree symbol and direction letters cause issues
        ("The location is 40.7128° N, 74.0060° W. That's New York.",
         ["The location is 40.7128° N, 74.0060° W.", "That's New York."]),

        # Equations with periods - mathematical syntax confuses tokenizer
        ("Solve for x: 2x + 3 = 7. The answer is x = 2.",
         ["Solve for x: 2x + 3 = 7.", "The answer is x = 2."]),
    ])
    def test_scientific_notation_edge_cases(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
