# -*- coding: UTF-8 -*-
"""Unusual or complex punctuation patterns."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestComplexPunctuation:
    """Unusual or complex punctuation patterns."""

    @pytest.mark.parametrize("text,expected", [
        # Multiple punctuation marks
        ("What?! You can't be serious!",
         ["What?!", "You can't be serious!"]),

        ("Really?? I don't believe it!!",
         ["Really??", "I don't believe it!!"]),

        # Interrobang style
        ("You did what?! That's insane!",
         ["You did what?!", "That's insane!"]),

        # Dash usage
        ("He arrived—finally—at noon. We had been waiting.",
         ["He arrived—finally—at noon.", "We had been waiting."]),

        ("The answer—if there is one—remains unclear.",
         ["The answer—if there is one—remains unclear."]),

        # Mixed dash and period
        ("Wait—what? Never mind. I understand now.",
         ["Wait—what?", "Never mind.", "I understand now."]),

        # Colon followed by quote - requires quote-aware parsing
        # ('He said: "I disagree." She nodded.',
        #  ['He said: "I disagree."', 'She nodded.']),

        # Semicolon near sentence end
        ("Read chapter one; then read two. Quiz tomorrow.",
         ["Read chapter one; then read two.", "Quiz tomorrow."]),
    ])
    def test_complex_punctuation(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
