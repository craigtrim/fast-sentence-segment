#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Merge sentences incorrectly split at parenthetical boundaries.

When a sentence contains a parenthetical comment that ends with punctuation,
spaCy may incorrectly split at the closing parenthesis. This merger detects
and corrects such false splits.

Pattern:
    "... (comment ending with period.) lowercase continuation"
    Should be ONE sentence, not two.

Example:
    Input:  ["He teaches (He worked as an engineer.)", "at the university."]
    Output: ["He teaches (He worked as an engineer.) at the university."]

Related GitHub Issues:
    Golden Rule 21 - Parenthetical sentence handling
    https://github.com/craigtrim/fast-sentence-segment/issues/26

Technical Notes:
    - spaCy sees period inside parentheses as sentence boundary
    - Following lowercase text indicates continuation, not new sentence
    - Must check for closing paren + period pattern: `.)` or `.)`
"""

import re
from typing import List

from fast_sentence_segment.core import BaseObject


class ParentheticalMerger(BaseObject):
    """Merge sentences incorrectly split at parenthetical boundaries.

    Detects patterns where:
    1. First sentence ends with `.)`
    2. Second sentence starts with lowercase letter

    These should be merged as they're one continuous sentence with
    a parenthetical comment.
    """

    def __init__(self):
        """
        Created:
            04-Feb-2026
            craigtrim@gmail.com
        Reference:
            Golden Rule 21
            https://github.com/craigtrim/fast-sentence-segment/issues/26
        """
        BaseObject.__init__(self, __name__)

    def _should_merge(self, current: str, next_sent: str) -> bool:
        """Check if two sentences should be merged.

        Args:
            current: Current sentence
            next_sent: Following sentence

        Returns:
            True if sentences should be merged (parenthetical split)
        """
        # Strip whitespace for checking
        current = current.rstrip()
        next_sent = next_sent.lstrip()

        if not current or not next_sent:
            return False

        # Pattern 1: Current ends with .) and next starts with lowercase
        # Example: "... (comment.)" + "at the university"
        if current.endswith('.)'):
            # Check if next sentence starts with lowercase letter
            # Also allow lowercase after certain connecting words
            first_char = next_sent[0] if next_sent else ''
            if first_char.islower():
                return True

        # Pattern 2: Current ends with .) followed by more punctuation
        # Example: "... (comment.)." (SpacyDocSegmenter might add period)
        if current.endswith('.).'):
            first_char = next_sent[0] if next_sent else ''
            if first_char.islower():
                return True

        # Pattern 3: Current ends with ?!) or !!) - question/exclaim in parens
        if current.endswith('?)') or current.endswith('!)'):
            first_char = next_sent[0] if next_sent else ''
            if first_char.islower():
                return True

        return False

    def _merge_sentences(self, current: str, next_sent: str) -> str:
        """Merge two sentences into one.

        Handles cleanup of spurious punctuation that may have been added.

        Args:
            current: Current sentence
            next_sent: Following sentence

        Returns:
            Merged sentence
        """
        current = current.rstrip()
        next_sent = next_sent.lstrip()

        # Remove spurious trailing period if present after closing paren
        # "... (comment.)." -> "... (comment.)"
        if current.endswith('.).'):
            current = current[:-1]

        return f"{current} {next_sent}"

    def process(self, sentences: List[str]) -> List[str]:
        """Process list of sentences, merging parenthetical splits.

        Args:
            sentences: List of sentences that may have incorrect splits

        Returns:
            List of sentences with parenthetical splits corrected
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
                    # Merge and continue
                    merged = self._merge_sentences(current, next_sent)
                    result.append(merged)
                    i += 2  # Skip next sentence since we merged it
                    continue

            # No merge needed, add current sentence as-is
            result.append(current)
            i += 1

        return result
