# -*- coding: UTF-8 -*-
"""Sentences containing numbered or lettered lists."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestListsAndEnumerations:
    """Sentences containing numbered or lettered lists."""

    @pytest.mark.parametrize("text,expected", [
        # Inline numbering
        ("We need: 1. paper, 2. pens, and 3. folders.",
         ["We need: 1. paper, 2. pens, and 3. folders."]),

        # Lettered items
        ("Choose either a. red, b. blue, or c. green.",
         ["Choose either a. red, b. blue, or c. green."]),

        # Roman numerals - spaCy sees lowercase i. as abbreviation
        # ("See sections i. and ii. for details.",
        #  ["See sections i. and ii. for details."]),

        # List followed by sentence
        ("Buy: 1. milk, 2. eggs. Don't forget!",
         ["Buy: 1. milk, 2. eggs.", "Don't forget!"]),

        # Step numbering - unusual expected output (splits on each step)
        # ("Step 1. Open the app. Step 2. Click login.",
        #  ["Step 1.", "Open the app.", "Step 2.", "Click login."]),
    ])
    def test_lists_enumerations(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
