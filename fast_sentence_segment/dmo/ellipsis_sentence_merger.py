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

Special case: Conjunction + Capital I (Issue #22)
    When spaCy incorrectly splits after a conjunction before "I" (pronoun):
    Input:  ['I wanted toxellipsisthreex but', "I couldn't."]
    Output: ["I wanted toxellipsisthreex but I couldn't"]

Related GitHub Issues:
    #19 - Ellipsis Handling
    https://github.com/craigtrim/fast-sentence-segment/issues/19

    #22 - Capital I pronoun causes false sentence splits after ellipsis
    https://github.com/craigtrim/fast-sentence-segment/issues/22
"""

import re
from typing import List

from fast_sentence_segment.core import BaseObject


# Pattern: ends with ellipsis placeholder
ENDS_WITH_ELLIPSIS = re.compile(r'xellipsisthreex\s*$')

# Pattern: contains ellipsis placeholder anywhere
CONTAINS_ELLIPSIS = re.compile(r'xellipsis')

# Pattern: ends with a coordinating conjunction (often signals incomplete split)
# Used to detect cases like "I wanted to... but" + "I couldn't" (Issue #22)
# Reference: https://github.com/craigtrim/fast-sentence-segment/issues/22
ENDS_WITH_CONJUNCTION = re.compile(r'\b(but|and|or|yet|so|nor|for)\s*$', re.IGNORECASE)

# Pattern: starts with lowercase letter
STARTS_LOWERCASE = re.compile(r'^[a-z]')

# Pattern: starts with capital I (pronoun, not new sentence)
STARTS_WITH_I = re.compile(r'^I\b')


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

        Merges in these cases:
        1. Current ends with ellipsis and next starts with lowercase
           Lowercase after ellipsis indicates continuation, not a new sentence.
           E.g., ['so...', 'yeah.'] -> ['so... yeah.']
        2. Current contains ellipsis, ends with conjunction, next starts with I
           E.g., ['I wanted to... but', "I couldn't."] -> ["I wanted to... but I couldn't"]
        """
        # Case 1: ends with ellipsis + next starts lowercase
        # Lowercase is always continuation, even if it has a period at the end
        if ENDS_WITH_ELLIPSIS.search(current) and STARTS_LOWERCASE.match(next_sent):
            return True

        # Case 2: contains ellipsis, ends with conjunction, next starts with I
        # This handles cases like "I wanted to... but" being wrongly split from "I couldn't"
        if (CONTAINS_ELLIPSIS.search(current) and
                ENDS_WITH_CONJUNCTION.search(current) and
                STARTS_WITH_I.match(next_sent)):
            return True

        return False

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
                next_sent = sentences[i + 1]

                # Strip trailing period from next sentence ONLY if:
                # 1. This is a conjunction + I case (the period was likely added by us)
                # 2. NOT if it's a lowercase continuation (the period may be original)
                if (ENDS_WITH_CONJUNCTION.search(current) and
                        STARTS_WITH_I.match(next_sent) and
                        next_sent.endswith('.') and
                        not next_sent.endswith('...')):
                    # Strip period from "I couldn't." when merging with "but"
                    if len(next_sent) >= 2 and next_sent[-2] != '.':
                        next_sent = next_sent[:-1]

                # Merge with next sentence
                merged = current + ' ' + next_sent
                result.append(merged)
                i += 2
            else:
                result.append(current)
                i += 1

        return result
