#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Merge sentences that were incorrectly split inside quotes.

When spaCy splits at a period inside a quoted passage, this component
detects unclosed quotes and merges sentences back together.

Example:
    Input:  ['"First thing.', 'Second thing," she said.']
    Output: ['"First thing. Second thing," she said.']

Related GitHub Issue:
    #20 - Quote Attribution: edge cases with ?, !, and nested quotes
    https://github.com/craigtrim/fast-sentence-segment/issues/20
"""

from typing import List

from fast_sentence_segment.core import BaseObject


# All quote characters (opening and closing)
# Using unicode escapes: \u201c = " (left double), \u201d = " (right double)
# \u2018 = ' (left single), \u2019 = ' (right single)
OPEN_QUOTES = {'"', "'", '\u201c', '\u2018'}
CLOSE_QUOTES = {'"', "'", '\u201d', '\u2019'}


def _count_quotes(text: str) -> dict:
    """Count opening and closing quotes in text.

    For straight quotes (" and '), they can be either opening or closing,
    so we count them as ambiguous and use parity.
    """
    straight_double = text.count('"')
    straight_single = text.count("'")

    # Curly quotes are unambiguous (using unicode escapes for reliability)
    # \u201c = " (left double), \u201d = " (right double)
    # \u2018 = ' (left single), \u2019 = ' (right single)
    open_double_curly = text.count('\u201c')
    close_double_curly = text.count('\u201d')
    open_single_curly = text.count('\u2018')
    close_single_curly = text.count('\u2019')

    return {
        'straight_double': straight_double,
        'straight_single': straight_single,
        'open_double_curly': open_double_curly,
        'close_double_curly': close_double_curly,
        'open_single_curly': open_single_curly,
        'close_single_curly': close_single_curly,
    }


def _has_unclosed_quote(text: str) -> bool:
    """Check if text has an unclosed quote.

    Uses simple heuristic: odd number of double quotes, or
    more opening curly double quotes than closing.

    NOTE: We only track double quotes, not single quotes, because single
    quotes are commonly used as apostrophes in contractions (e.g., "Let's",
    "don't", "it's") which would cause false positives.
    """
    counts = _count_quotes(text)

    # Check straight double quotes (odd = unclosed)
    if counts['straight_double'] % 2 == 1:
        return True

    # Check curly double quotes
    if counts['open_double_curly'] > counts['close_double_curly']:
        return True

    return False


def _closes_quote(text: str) -> bool:
    """Check if text closes a quote (contains closing quote character)."""
    for char in CLOSE_QUOTES:
        if char in text:
            return True
    return False


class UnclosedQuoteMerger(BaseObject):
    """Merge sentences split inside quotes.

    When spaCy incorrectly splits at a period inside a quoted passage,
    this merger detects the unclosed quote and merges with subsequent
    sentences until the quote is closed.

    Example:
        Input:  ['"First thing.', 'Second thing," she said.']
        Output: ['"First thing. Second thing," she said.']
    """

    def __init__(self):
        """
        Created:
            03-Feb-2026
            craigtrim@gmail.com
        Reference:
            https://github.com/craigtrim/fast-sentence-segment/issues/20
        """
        BaseObject.__init__(self, __name__)

    def process(self, sentences: List[str]) -> List[str]:
        """Process a list of sentences, merging those split inside quotes.

        Args:
            sentences: List of sentences

        Returns:
            List of sentences with quote splits merged
        """
        if not sentences:
            return sentences

        result = []
        i = 0

        while i < len(sentences):
            current = sentences[i]

            # Check if current sentence has an unclosed quote
            if _has_unclosed_quote(current):
                # Merge with subsequent sentences until quote is closed
                merged = current
                j = i + 1

                while j < len(sentences):
                    next_sent = sentences[j]
                    merged = merged + ' ' + next_sent

                    # Check if the quote is now closed
                    if not _has_unclosed_quote(merged):
                        break
                    j += 1

                result.append(merged)
                i = j + 1
            else:
                result.append(current)
                i += 1

        return result
