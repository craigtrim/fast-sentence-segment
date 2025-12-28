# -*- coding: UTF-8 -*-
"""Numbers with decimal points."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestDecimalNumbers:
    """Numbers with decimal points."""

    @pytest.mark.parametrize("text,expected", [
        # Simple decimals
        ("The price is 19.99 dollars.", ["The price is 19.99 dollars."]),
        ("Pi is approximately 3.14159.", ["Pi is approximately 3.14159."]),
        ("The temperature is 98.6 degrees.", ["The temperature is 98.6 degrees."]),

        # Currency with decimals
        ("It costs $9.99.", ["It costs $9.99."]),
        ("The total is $150.00. Please pay now.",
         ["The total is $150.00.", "Please pay now."]),
        ("I paid $24.99 for the book. It was worth it.",
         ["I paid $24.99 for the book.", "It was worth it."]),

        # Percentages
        ("The rate is 5.5 percent.", ["The rate is 5.5 percent."]),
        ("We achieved 99.9% uptime. Our goal was 99.5%.",
         ["We achieved 99.9% uptime.", "Our goal was 99.5%."]),

        # Measurements
        ("The board is 2.5 meters long.", ["The board is 2.5 meters long."]),
        ("It weighs 1.5 kg. That's quite light.",
         ["It weighs 1.5 kg.", "That's quite light."]),

        # Multiple decimals in one sentence
        ("The dimensions are 3.5 by 4.5 inches.",
         ["The dimensions are 3.5 by 4.5 inches."]),

        # Version numbers
        ("We're running version 2.0.", ["We're running version 2.0."]),
        ("Update to version 3.5.1. It fixes bugs.",
         ["Update to version 3.5.1.", "It fixes bugs."]),
    ])
    def test_decimal_numbers(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
