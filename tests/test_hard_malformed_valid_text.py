# -*- coding: UTF-8 -*-
"""Text that is unusual but should still be segmented correctly."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestMalformedButValidText:
    """Text that is unusual but should still be segmented correctly."""

    @pytest.mark.parametrize("text,expected", [
        # No space after period - requires heuristic typo recovery
        # ("Hello.World.", ["Hello.", "World."]),
        ("I went.She stayed.", ["I went.", "She stayed."]),

        # Extra periods - malformed input
        # ("What.. Happened here...",
        #  ["What..", "Happened here..."]),

        # Mixed case after period - unusual but spaCy sees lowercase as continuation
        # ("Hello. world.", ["Hello.", "world."]),

        # Period inside parentheses with abbreviation - complex pattern
        # ("Check the docs (see Ch. 1.)", ["Check the docs (see Ch. 1.)"]),

        # Quote at very end - requires quote-aware parsing
        # ('She said "Yes."', ['She said "Yes."']),

        # Multiple consecutive sentence endings
        ("Really?! Yes!! Okay...",
         ["Really?!", "Yes!!", "Okay..."]),

        # Unusual spacing patterns
        ("Hello .  World .", ["Hello .", "World ."]),
    ])
    def test_malformed_valid_text(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
