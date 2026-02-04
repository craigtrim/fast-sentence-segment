#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Merge sentences that spaCy incorrectly split at quote attribution boundaries.

When spaCy incorrectly splits after a closing quote followed by lowercase text
(e.g., '"Are you sure?" she asked.' becomes ['"Are you sure?"', 'she asked.']),
this component merges them back together.

The key insight is that when a quote ends with punctuation and the next word
is lowercase, it's typically attribution ("she said") not a new sentence.

Related GitHub Issue:
    #20 - Quote Attribution: edge cases with ?, !, and nested quotes
    https://github.com/craigtrim/fast-sentence-segment/issues/20

Reference: pySBD Golden Rules 24-26
"""

import re
from typing import List

from fast_sentence_segment.core import BaseObject


# All quote characters (straight and curly)
QUOTE_CHARS = '"\'"\'""'''

# Pattern to detect if a sentence ends with punctuation inside/before a closing quote
# Matches: ?" or !" or .' or ." (with possible variations of quote characters)
ENDS_WITH_QUOTE_PUNCT = re.compile(
    r'[.?!][' + re.escape(QUOTE_CHARS) + r']\s*$'
)

# Pattern to detect if a sentence starts with a lowercase letter
STARTS_LOWERCASE = re.compile(r'^[a-z]')


class QuoteAttributionMerger(BaseObject):
    """Merge sentences incorrectly split at quote attribution boundaries.

    When spaCy splits a sentence after a closing quote but before lowercase
    attribution text, this merger puts them back together.

    Example:
        Input:  ['"Are you sure?"', 'she asked.']
        Output: ['"Are you sure?" she asked.']
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

    def _should_merge(self, current: str, next_sent: str) -> bool:
        """Check if two sentences should be merged.

        Merge when:
        1. Current sentence ends with punctuation + closing quote
        2. Next sentence starts with lowercase

        Args:
            current: Current sentence
            next_sent: Next sentence

        Returns:
            True if sentences should be merged
        """
        current = current.strip()
        next_sent = next_sent.strip()

        if not current or not next_sent:
            return False

        # Check if current ends with punctuation + quote
        if not ENDS_WITH_QUOTE_PUNCT.search(current):
            return False

        # Check if next starts with lowercase
        if not STARTS_LOWERCASE.match(next_sent):
            return False

        return True

    def process(self, sentences: List[str]) -> List[str]:
        """Process a list of sentences, merging quote attributions.

        Args:
            sentences: List of sentences from spaCy

        Returns:
            List of sentences with quote attributions merged
        """
        if not sentences or len(sentences) < 2:
            return sentences

        result = []
        i = 0

        while i < len(sentences):
            current = sentences[i]

            # Check if we should merge with next sentence
            if i + 1 < len(sentences):
                next_sent = sentences[i + 1]

                if self._should_merge(current, next_sent):
                    # Merge the sentences
                    merged = current.rstrip() + " " + next_sent.lstrip()
                    result.append(merged)
                    i += 2
                    continue

            result.append(current)
            i += 1

        return result
