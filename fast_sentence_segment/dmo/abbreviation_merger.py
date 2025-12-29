#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Merge sentences that spaCy incorrectly split at abbreviation boundaries.

When spaCy incorrectly splits after an abbreviation (e.g., "ext. 5" becomes
["ext.", "5. Ask for help."]), this component merges them back together
using specific known patterns.

Reference: https://github.com/craigtrim/fast-sentence-segment/issues/3
"""

import re
from typing import List, Optional, Tuple

from fast_sentence_segment.core import BaseObject


# Patterns where spaCy incorrectly splits after an abbreviation.
# Format: (ending_pattern, extract_pattern)
#   - ending_pattern: regex to match end of current sentence
#   - extract_pattern: regex to extract the portion to merge from next sentence
#
# The extract_pattern MUST have a capture group for the portion to merge.
# Whatever is NOT captured remains as a separate sentence.

MERGE_PATTERNS: List[Tuple[str, str]] = [

    # ext. 5, Ext. 123, EXT. 42
    (r"(?i)\bext\.$", r"^(\d+\.?)\s*"),

    # no. 5, No. 42, NO. 100
    (r"(?i)\bno\.$", r"^(\d+\.?)\s*"),

    # vol. 3, Vol. 42, VOL. 1
    (r"(?i)\bvol\.$", r"^(\d+\.?)\s*"),

    # pt. 2, Pt. 1, PT. 3
    (r"(?i)\bpt\.$", r"^(\d+\.?)\s*"),

    # ch. 5, Ch. 10, CH. 3
    (r"(?i)\bch\.$", r"^(\d+\.?)\s*"),

    # sec. 3, Sec. 14, SEC. 2
    (r"(?i)\bsec\.$", r"^(\d+(?:\.\d+)?\.?)\s*"),

    # fig. 1, Fig. 3.2, FIG. 10
    (r"(?i)\bfig\.$", r"^(\d+(?:\.\d+)?\.?)\s*"),

    # p. 42, P. 100
    (r"(?i)\bp\.$", r"^(\d+\.?)\s*"),

    # pp. 42-50, PP. 100-110
    (r"(?i)\bpp\.$", r"^(\d+(?:-\d+)?\.?)\s*"),

    # art. 5, Art. 12, ART. 1
    (r"(?i)\bart\.$", r"^(\d+\.?)\s*"),

]


class AbbreviationMerger(BaseObject):
    """Merge sentences incorrectly split at abbreviation boundaries."""

    def __init__(self):
        """
        Created:
            27-Dec-2024
            craigtrim@gmail.com
        Reference:
            https://github.com/craigtrim/fast-sentence-segment/issues/3
        """
        BaseObject.__init__(self, __name__)
        # Compile patterns for efficiency
        self._patterns = [
            (re.compile(ending), re.compile(extract))
            for ending, extract in MERGE_PATTERNS
        ]

    def _try_merge(self, current: str, next_sent: str) -> Optional[Tuple[str, str]]:
        """Try to merge two sentences based on known patterns.

        Args:
            current: Current sentence
            next_sent: Next sentence

        Returns:
            Tuple of (merged_sentence, remainder) if merge needed, else None
        """
        current = current.strip()
        next_sent = next_sent.strip()

        for ending_pattern, extract_pattern in self._patterns:
            if ending_pattern.search(current):
                match = extract_pattern.match(next_sent)
                if match:
                    # Extract the portion to merge
                    extracted = match.group(1)
                    # Get the remainder (everything after the match)
                    remainder = next_sent[match.end():].strip()
                    # Build merged sentence
                    merged = current + " " + extracted
                    return (merged, remainder)

        return None

    def process(self, sentences: List[str]) -> List[str]:
        """Process a list of sentences, merging incorrectly split ones.

        Args:
            sentences: List of sentences from spaCy

        Returns:
            List of sentences with incorrect splits merged
        """
        if not sentences:
            return sentences

        result = []
        i = 0

        while i < len(sentences):
            current = sentences[i]

            # Check if we should merge with next sentence
            if i + 1 < len(sentences):
                next_sent = sentences[i + 1]
                merge_result = self._try_merge(current, next_sent)

                if merge_result:
                    merged, remainder = merge_result
                    result.append(merged)

                    # If there's a remainder, it becomes a new sentence to process
                    if remainder:
                        # Insert remainder back for processing
                        sentences = sentences[:i+2] + [remainder] + sentences[i+2:]
                        sentences[i+1] = remainder

                    i += 2
                    continue

            result.append(current)
            i += 1

        return result
