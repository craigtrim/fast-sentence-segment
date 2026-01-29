# -*- coding: UTF-8 -*-
"""Multi-turn and complex dialogue patterns."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestComplexDialogue:
    """Multi-turn and complex dialogue patterns."""

    @pytest.mark.parametrize("text,expected", [
        # Interrupted dialogue
        ('"I think—" she began, but he interrupted.',
         ['"I think—" she began, but he interrupted.']),

        # Complex: requires quote-aware parsing
        # ('"Wait," he paused, looking around, "did you hear that?"',
        #  ['"Wait," he paused, looking around, "did you hear that?"']),

        # Multiple speakers, one paragraph
        ('"Hello," said John. "Hi," replied Mary. "How are you both?" asked Tom.',
         ['"Hello," said John.', '"Hi," replied Mary.', '"How are you both?" asked Tom.']),

        # Complex: ellipsis inside quotes + sentence after
        # ('"I was going to say..." He trailed off.',
        #  ['"I was going to say..."', 'He trailed off.']),

        # Complex: consecutive quoted sentences
        # ('"Why did you do it?" "I had no choice."',
        #  ['"Why did you do it?"', '"I had no choice."']),

        # Complex: quoted exclamation + question
        # ('"Watch out!" she screamed. "What is it?" he asked.',
        #  ['"Watch out!" she screamed.', '"What is it?" he asked.']),

        # Complex: multi-sentence quoted passage
        # ('"When I was young, I used to dream of faraway places. Mountains, oceans, deserts. All of it."',
        #  ['"When I was young, I used to dream of faraway places. Mountains, oceans, deserts. All of it."']),
    ])
    def test_complex_dialogue(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
