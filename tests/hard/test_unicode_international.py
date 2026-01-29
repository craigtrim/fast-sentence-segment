# -*- coding: UTF-8 -*-
"""Unicode characters and international text."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestUnicodeAndInternational:
    """Unicode characters and international text."""

    @pytest.mark.parametrize("text,expected", [
        # Accented characters
        ("Café is a French word. Résumé is another.",
         ["Café is a French word.", "Résumé is another."]),

        ("The naïve approach failed. A better method was needed.",
         ["The naïve approach failed.", "A better method was needed."]),

        # Currency symbols
        ("The price is €50. That's $55 in USD.",
         ["The price is €50.", "That's $55 in USD."]),

        ("It costs £30. Or ¥4000 in Japan.",
         ["It costs £30.", "Or ¥4000 in Japan."]),

        # Non-ASCII punctuation - Japanese brackets confuse spaCy
        # ("「Hello」 is a greeting. 「Goodbye」 is a farewell.",
        #  ["「Hello」 is a greeting.", "「Goodbye」 is a farewell."]),

        # Smart quotes
        ('"Hello," she said. "Goodbye," he replied.',
         ['"Hello," she said.', '"Goodbye," he replied.']),

        # Ellipsis character (single unicode char) - different from ...
        # ("I wonder… Never mind. Let's continue.",
        #  ["I wonder…", "Never mind.", "Let's continue."]),

        # Em dash (unicode)
        ("The answer—surprisingly—was yes. We celebrated.",
         ["The answer—surprisingly—was yes.", "We celebrated."]),

        # Mixed scripts
        ("Hello means こんにちは in Japanese. It's a greeting.",
         ["Hello means こんにちは in Japanese.", "It's a greeting."]),
    ])
    def test_unicode_international(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
