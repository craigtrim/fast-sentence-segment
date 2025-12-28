# -*- coding: UTF-8 -*-
"""Ellipses in various contexts."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestEllipses:
    """Ellipses in various contexts."""

    @pytest.mark.parametrize("text,expected", [
        # Trailing ellipsis
        ("I'm not sure...", ["I'm not sure..."]),
        ("Well, I guess...", ["Well, I guess..."]),

        # Ellipsis followed by another sentence
        ("I thought... Never mind. Let's continue.",
         ["I thought...", "Never mind.", "Let's continue."]),
        ("Wait... Did you hear that?",
         ["Wait...", "Did you hear that?"]),

        # Ellipsis in the middle
        ("She said she would... but she didn't.",
         ["She said she would... but she didn't."]),
        ("The results were... unexpected.",
         ["The results were... unexpected."]),

        # Multiple ellipses
        ("I wonder... No, never mind... Or maybe...",
         ["I wonder...", "No, never mind...", "Or maybe..."]),

        # Ellipsis with exclamation or question
        ("What the...!", ["What the...!"]),
        ("Did he really...?", ["Did he really...?"]),
    ])
    def test_ellipses(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
