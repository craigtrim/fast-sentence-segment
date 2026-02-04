#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Split sentences at quote closing boundaries when followed by capital letters.

When spaCy treats a closing quote followed by a capital letter as one sentence
(e.g., '"We should go to the U.S." Dr. Smith suggested.'), this component
splits them into separate sentences.

This is the inverse of QuoteAttributionMerger - it handles cases where
the word after the quote is capitalized (new sentence) rather than
lowercase (attribution).

Related GitHub Issue:
    #20 - Quote Attribution: edge cases with ?, !, and nested quotes
    https://github.com/craigtrim/fast-sentence-segment/issues/20
"""

import re
from typing import List

from fast_sentence_segment.core import BaseObject


# All quote characters (straight and curly)
QUOTE_CHARS = '"\'"\'""'''

# Pattern to split: punctuation + closing quote + space + capital letter
# Captures: (everything before including quote) (space) (capital and rest)
# The pattern looks for: ." or !" or ?" followed by space and capital
# Also handles ellipsis placeholder (xellipsisthreex) followed by quote
SPLIT_PATTERN = re.compile(
    r'([.?!][' + re.escape(QUOTE_CHARS) + r']|xellipsisthreex[' + re.escape(QUOTE_CHARS) + r'])(\s+)([A-Z])'
)


class QuoteClosingSplitter(BaseObject):
    """Split sentences at quote closing + capital letter boundaries.

    When spaCy fails to split after a closing quote followed by a capital
    letter, this splitter handles the split.

    Example:
        Input:  ['"We should go." Dr. Smith suggested.']
        Output: ['"We should go."', 'Dr. Smith suggested.']
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
        """Process a list of sentences, splitting at quote + capital boundaries.

        Args:
            sentences: List of sentences

        Returns:
            List of sentences with quote closings split
        """
        result = []

        for sent in sentences:
            # Split on pattern, keeping punctuation with first part
            parts = SPLIT_PATTERN.split(sent)

            if len(parts) == 1:
                # No match, keep as-is
                result.append(sent)
            else:
                # Reassemble: parts = [before, punct+quote, space, capital, after, ...]
                i = 0
                while i < len(parts):
                    if i + 3 < len(parts):
                        # before + punct+quote
                        segment = parts[i] + parts[i + 1]
                        if segment.strip():
                            result.append(segment.strip())
                        # Prepend capital to next part
                        parts[i + 4] = parts[i + 3] + parts[i + 4] if i + 4 < len(parts) else parts[i + 3]
                        i += 4
                    else:
                        if parts[i].strip():
                            result.append(parts[i].strip())
                        i += 1

        return [s for s in result if s]
