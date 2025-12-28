# -*- coding: UTF-8 -*-
"""Sentences with special characters and symbols."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestSpecialCharacters:
    """Sentences with special characters and symbols."""

    @pytest.mark.parametrize("text,expected", [
        # Ampersand
        ("Ben & Jerry's is popular.", ["Ben & Jerry's is popular."]),
        ("The firm is Johnson & Johnson. They make products.",
         ["The firm is Johnson & Johnson.", "They make products."]),

        # Plus sign
        ("The phone has 5G+ capability.", ["The phone has 5G+ capability."]),

        # Hash/pound
        ("Use #hashtag for social media.", ["Use #hashtag for social media."]),
        ("Tweet with #coding. People will see it.",
         ["Tweet with #coding.", "People will see it."]),

        # At symbol (not email)
        ("Meet @ the coffee shop.", ["Meet @ the coffee shop."]),

        # Slashes
        ("The price is $10/hour.", ["The price is $10/hour."]),
        ("Use TCP/IP for networking.", ["Use TCP/IP for networking."]),

        # Mixed - ext. 5. with following sentence
        # ("Contact R&D @ ext. 5. Ask for Dr. Smith.",
        #  ["Contact R&D @ ext. 5.", "Ask for Dr. Smith."]),
    ])
    def test_special_characters(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
