#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Split sentences at ellipsis boundaries when followed by capital letters.

When spaCy treats an ellipsis followed by a capital letter as one sentence
(e.g., 'I thought... Never mind.'), this component splits them.

The ellipsis has been normalized to 'xellipsisthreex' at this point in the
pipeline, so we look for that pattern.

Example:
    Input:  ['I thoughtxellipsisthreex Never mind.']
    Output: ['I thoughtxellipsisthreex', 'Never mind.']

Note: After denormalization, 'xellipsisthreex' becomes '...'

Related GitHub Issue:
    #20 - Quote Attribution: edge cases with ?, !, and nested quotes
    https://github.com/craigtrim/fast-sentence-segment/issues/20
"""

import re
from typing import List

from fast_sentence_segment.core import BaseObject


# Pattern: ellipsis placeholder + space + capital letter
# This indicates a new sentence after the ellipsis
SPLIT_PATTERN = re.compile(r'(xellipsisthreex)(\s+)([A-Z])')


class EllipsisSentenceSplitter(BaseObject):
    """Split sentences at ellipsis + capital letter boundaries.

    When spaCy fails to split after an ellipsis followed by a capital
    letter, this splitter handles the split.

    Example:
        Input:  ['I thoughtxellipsisthreex Never mind.']
        Output: ['I thoughtxellipsisthreex', 'Never mind.']
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
        """Process a list of sentences, splitting at ellipsis + capital boundaries.

        Args:
            sentences: List of sentences

        Returns:
            List of sentences with ellipsis boundaries split
        """
        result = []

        for sent in sentences:
            # Split on pattern
            parts = SPLIT_PATTERN.split(sent)

            if len(parts) == 1:
                # No match, keep as-is
                result.append(sent)
            else:
                # Reassemble: parts = [before, ellipsis, space, capital, after, ...]
                i = 0
                while i < len(parts):
                    if i + 3 < len(parts):
                        # before + ellipsis
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
