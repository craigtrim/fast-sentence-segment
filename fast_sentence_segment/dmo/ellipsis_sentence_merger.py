#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Merge sentences that were incorrectly split at ellipsis boundaries.

When spaCy splits at an ellipsis followed by a lowercase letter
(e.g., 'She said... but she didn't' becomes ['She said...', 'but she didn't']),
this component merges them back together.

The ellipsis has been normalized to 'xellipsisthreex' at this point in the
pipeline, so we look for that pattern.

Example:
    Input:  ['She saidxellipsisthreex', 'but she didn\\'t.']
    Output: ['She saidxellipsisthreex but she didn\\'t.']

Note: After denormalization, 'xellipsisthreex' becomes '...'

Related GitHub Issue:
    #20 - Quote Attribution: edge cases with ?, !, and nested quotes
    https://github.com/craigtrim/fast-sentence-segment/issues/20
"""

import re
from typing import List

from fast_sentence_segment.core import BaseObject


# Pattern: ends with ellipsis placeholder
ENDS_WITH_ELLIPSIS = re.compile(r'xellipsisthreex\s*$')

# Pattern: starts with lowercase letter
STARTS_LOWERCASE = re.compile(r'^[a-z]')


class EllipsisSentenceMerger(BaseObject):
    """Merge sentences incorrectly split at ellipsis + lowercase boundaries.

    When spaCy splits after an ellipsis followed by a lowercase
    letter, this merger joins them back together.

    Example:
        Input:  ['She saidxellipsisthreex', 'but she didn\\'t.']
        Output: ['She saidxellipsisthreex but she didn\\'t.']
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

        Returns True if current ends with ellipsis and next starts with lowercase.
        """
        if not ENDS_WITH_ELLIPSIS.search(current):
            return False
        if not STARTS_LOWERCASE.match(next_sent):
            return False
        return True

    def process(self, sentences: List[str]) -> List[str]:
        """Process a list of sentences, merging those split at ellipsis + lowercase.

        Args:
            sentences: List of sentences

        Returns:
            List of sentences with ellipsis splits merged
        """
        if not sentences:
            return sentences

        result = []
        i = 0

        while i < len(sentences):
            current = sentences[i]

            # Check if we should merge with the next sentence
            if i + 1 < len(sentences) and self._should_merge(current, sentences[i + 1]):
                # Merge with next sentence
                merged = current + ' ' + sentences[i + 1]
                result.append(merged)
                i += 2
            else:
                result.append(current)
                i += 1

        return result
