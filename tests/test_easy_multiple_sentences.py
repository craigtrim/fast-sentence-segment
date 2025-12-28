# -*- coding: UTF-8 -*-
"""Three or more sentences with clear boundaries."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestMultipleSentences:
    """Three or more sentences with clear boundaries."""

    @pytest.mark.parametrize("text,expected", [
        # Three sentences
        ("I woke up. I ate breakfast. I went to work.",
         ["I woke up.", "I ate breakfast.", "I went to work."]),
        ("The alarm rang. I got out of bed. It was cold outside.",
         ["The alarm rang.", "I got out of bed.", "It was cold outside."]),
        ("First, prepare the ingredients. Then, mix them together. Finally, bake for thirty minutes.",
         ["First, prepare the ingredients.", "Then, mix them together.", "Finally, bake for thirty minutes."]),

        # Four sentences
        ("Spring is here. Flowers are blooming. Birds are returning. Life is beautiful.",
         ["Spring is here.", "Flowers are blooming.", "Birds are returning.", "Life is beautiful."]),
        ("I opened the book. I read the first page. It was interesting. I continued reading.",
         ["I opened the book.", "I read the first page.", "It was interesting.", "I continued reading."]),

        # Five sentences
        ("Monday was busy. Tuesday was calm. Wednesday was hectic. Thursday was productive. Friday was relaxing.",
         ["Monday was busy.", "Tuesday was calm.", "Wednesday was hectic.", "Thursday was productive.", "Friday was relaxing."]),

        # Mixed punctuation
        ("Hello there! How are you? I'm doing well. Thanks for asking!",
         ["Hello there!", "How are you?", "I'm doing well.", "Thanks for asking!"]),
        ("What a day! I can't believe what happened. Did you hear? It was incredible!",
         ["What a day!", "I can't believe what happened.", "Did you hear?", "It was incredible!"]),
    ])
    def test_multiple_sentences(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
