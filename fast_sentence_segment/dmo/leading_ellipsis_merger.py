#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Merge standalone ellipsis with the following sentence.

When an ellipsis appears as its own "sentence" (e.g., ". . ."), it should be
merged with the following sentence as a "leading ellipsis" - indicating
omitted text at the start of a quotation or continuation.

Example:
    Input:  ["compounds.", ". . .", "The practice was not abandoned."]
    Output: ["compounds.", ". . . The practice was not abandoned."]

This is a specific edge-case handler for Golden Rule 48 and similar patterns.
The rule is: a standalone ellipsis (just dots, possibly with periods) should
be attached to the FOLLOWING sentence, not the preceding one.

Related: Golden Rule 48
https://github.com/craigtrim/fast-sentence-segment/issues/26
"""

import re
from typing import List

from fast_sentence_segment.core import BaseObject


# Pattern to detect standalone ellipsis sentences
# Matches sentences that are ONLY ellipsis (with optional surrounding whitespace)
# Handles: ". . .", "...", ". . . .", "....", and variants
STANDALONE_ELLIPSIS = re.compile(
    r'^[\s]*[\.\s]+[\s]*$'  # Only dots and spaces
)

# More specific: exactly 3 or 4 dots with optional spaces
ELLIPSIS_ONLY = re.compile(
    r'^[\s]*\.[\s]*\.[\s]*\.[\s]*(\.)?[\s]*$'
)


class LeadingEllipsisMerger(BaseObject):
    """Merge standalone ellipsis with the following sentence.

    When a sentence is just an ellipsis (". . ." or "..."), merge it with
    the following sentence to create a "leading ellipsis" that indicates
    omitted text at the start of a quoted/continued passage.
    """

    def __init__(self):
        """
        Created:
            04-Feb-2026
            craigtrim@gmail.com
        Reference:
            Golden Rule 48
            https://github.com/craigtrim/fast-sentence-segment/issues/26
        """
        BaseObject.__init__(self, __name__)

    def _is_standalone_ellipsis(self, text: str) -> bool:
        """Check if text is just an ellipsis.

        Args:
            text: Text to check

        Returns:
            True if text is only an ellipsis pattern
        """
        text = text.strip()
        if not text:
            return False

        # Check if it's only dots and spaces
        if ELLIPSIS_ONLY.match(text):
            return True

        return False

    def process(self, sentences: List[str]) -> List[str]:
        """Process list of sentences, merging standalone ellipsis appropriately.

        Handles two cases:
        1. Leading ellipsis: ". . ." + "Next sentence" → ". . . Next sentence"
        2. Trailing ellipsis: "Sentence." + ". . ." (at end) → "Sentence. . . ."

        Args:
            sentences: List of sentences that may have standalone ellipsis

        Returns:
            List of sentences with ellipsis merged appropriately
        """
        if not sentences or len(sentences) < 2:
            return sentences

        # First pass: Merge leading ellipsis (ellipsis followed by content)
        result = []
        i = 0
        while i < len(sentences):
            current = sentences[i]

            # Check if current is a standalone ellipsis with following content
            if self._is_standalone_ellipsis(current) and i + 1 < len(sentences):
                next_sent = sentences[i + 1]
                # Only merge if next sentence has real content (not just ellipsis)
                if not self._is_standalone_ellipsis(next_sent):
                    merged = f"{current.strip()} {next_sent.strip()}"
                    result.append(merged)
                    i += 2
                    continue

            result.append(current)
            i += 1

        # Second pass: Merge trailing ellipsis (content followed by ellipsis at end)
        if len(result) >= 2 and self._is_standalone_ellipsis(result[-1]):
            # Last sentence is standalone ellipsis - merge with preceding
            trailing = result.pop()
            result[-1] = f"{result[-1].rstrip()} {trailing.strip()}"

        return result
