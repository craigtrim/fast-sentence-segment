# -*- coding: UTF-8 -*-
"""Two sentence inputs with clear boundaries."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestTwoSentences:
    """Two sentence inputs with clear boundaries."""

    @pytest.mark.parametrize("text,expected", [
        # Two declarative sentences
        ("Hello world. Goodbye world.",
         ["Hello world.", "Goodbye world."]),
        ("I went to the store. I bought some milk.",
         ["I went to the store.", "I bought some milk."]),
        ("The sun is shining. The birds are singing.",
         ["The sun is shining.", "The birds are singing."]),
        ("She opened the door. He walked inside.",
         ["She opened the door.", "He walked inside."]),
        ("First we eat. Then we sleep.",
         ["First we eat.", "Then we sleep."]),

        # Declarative + Question
        ("I went home. Did you come too?",
         ["I went home.", "Did you come too?"]),
        ("The movie was great. Have you seen it?",
         ["The movie was great.", "Have you seen it?"]),
        ("I finished my homework. Can we play now?",
         ["I finished my homework.", "Can we play now?"]),

        # Declarative + Exclamation
        ("I won the lottery. I can't believe it!",
         ["I won the lottery.", "I can't believe it!"]),
        ("The package arrived. Finally!",
         ["The package arrived.", "Finally!"]),
        ("She said yes. Amazing!",
         ["She said yes.", "Amazing!"]),

        # Question + Declarative
        ("What time is it? I need to know.",
         ["What time is it?", "I need to know."]),
        ("Where is my phone? I left it here.",
         ["Where is my phone?", "I left it here."]),

        # Question + Question
        ("How are you? How was your day?",
         ["How are you?", "How was your day?"]),
        ("What happened? Why are you crying?",
         ["What happened?", "Why are you crying?"]),

        # Exclamation + Declarative
        ("Watch out! There's a car coming.",
         ["Watch out!", "There's a car coming."]),
        ("Surprise! We threw you a party.",
         ["Surprise!", "We threw you a party."]),

        # Exclamation + Exclamation
        ("Stop! Don't do that!",
         ["Stop!", "Don't do that!"]),
        ("Hurry up! We're going to be late!",
         ["Hurry up!", "We're going to be late!"]),
    ])
    def test_two_sentences(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
