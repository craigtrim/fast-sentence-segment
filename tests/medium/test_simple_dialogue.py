# -*- coding: UTF-8 -*-
"""Basic dialogue with quotation marks."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestSimpleDialogue:
    """Basic dialogue with quotation marks."""

    @pytest.mark.parametrize("text,expected", [
        # Said with period inside quotes
        ('"Hello," she said.', ['"Hello," she said.']),
        ('"Goodbye," he replied.', ['"Goodbye," he replied.']),

        # Full sentence in quotes followed by attribution
        ('"I am leaving now," she announced.',
         ['"I am leaving now," she announced.']),

        # Question in quotes
        ('"Are you coming?" she asked.',
         ['"Are you coming?" she asked.']),

        # Complex: exclamation in quotes with attribution
        # ('"Watch out!" he shouted.',
        #  ['"Watch out!" he shouted.']),

        # Complex: period inside closing quote
        # ('She said, "I agree."', ['She said, "I agree."']),
        # ('He replied, "That sounds good."',
        #  ['He replied, "That sounds good."']),

        # Complex: two dialogue sentences
        # ('"Hello," she said. "How are you?"',
        #  ['"Hello," she said.', '"How are you?"']),
        # ('"I agree," he nodded. "Let\'s proceed."',
        #  ['"I agree," he nodded.', '"Let\'s proceed."']),
    ])
    def test_simple_dialogue(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
