# -*- coding: UTF-8 -*-
"""Text containing list markers and bullets."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestListsAndBullets:
    """Text containing list markers and bullets."""

    @pytest.mark.parametrize("text,expected", [
        # Numbered inline list - unusual expected output (splits each number)
        # ("The steps are: 1. Plan. 2. Execute. 3. Review.",
        #  ["The steps are: 1.", "Plan.", "2.", "Execute.", "3.", "Review."]),

        # Bullet points as text
        ("• First item. • Second item. • Third item.",
         ["• First item.", "• Second item.", "• Third item."]),

        # Mixed bullets and text
        ("Consider these: a) cost, b) time, c) quality. Choose two.",
         ["Consider these: a) cost, b) time, c) quality.", "Choose two."]),

        # Roman numerals in lists
        ("Review: i) the introduction, ii) the methods, iii) the results.",
         ["Review: i) the introduction, ii) the methods, iii) the results."]),
    ])
    def test_lists_bullets(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
