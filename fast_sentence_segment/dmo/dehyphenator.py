# -*- coding: UTF-8 -*-
"""Dehyphenate words split across lines.

Related GitHub Issue:
    #8 - Add dehyphenation support for words split across lines
    https://github.com/craigtrim/fast-sentence-segment/issues/8

When processing ebooks and scanned documents, words are often hyphenated
at line breaks for typesetting purposes. This module rejoins those words.
"""

import re

from fast_sentence_segment.core import BaseObject

# Pattern to match hyphenated word breaks at end of line:
# - A single hyphen (not -- em-dash)
# - Followed by newline and optional whitespace
# - Followed by a lowercase letter (continuation of word)
_HYPHEN_LINE_BREAK_PATTERN = re.compile(r'(?<!-)-\n\s*([a-z])')


class Dehyphenator(BaseObject):
    """Rejoin words that were hyphenated across line breaks."""

    def __init__(self):
        """Change Log

        Created:
            3-Feb-2026
            craigtrim@gmail.com
            *   add dehyphenation support for words split across lines
                https://github.com/craigtrim/fast-sentence-segment/issues/8
        """
        BaseObject.__init__(self, __name__)

    @staticmethod
    def process(input_text: str) -> str:
        """Rejoin words that were hyphenated across line breaks.

        Detects the pattern of a word fragment ending with a hyphen
        at the end of a line, followed by the word continuation
        starting with a lowercase letter on the next line.

        Examples:
            "bot-\\ntle" -> "bottle"
            "cham-\\n    bermaid" -> "chambermaid"

        Args:
            input_text: Text that may contain hyphenated line breaks.

        Returns:
            Text with hyphenated word breaks rejoined.
        """
        return _HYPHEN_LINE_BREAK_PATTERN.sub(r'\1', input_text)
