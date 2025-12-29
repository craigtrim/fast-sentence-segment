#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Merge sentences incorrectly split when a title abbreviation is followed by a
single-word name ending in punctuation.

When the question/exclamation splitter splits "Dr. Who?" into ["Dr.", "Who?"],
this component merges them back together because a title + single capitalized
word is almost certainly a name, not two sentences.

Examples that should be merged:
    ["Dr.", "Who?"] -> ["Dr. Who?"]
    ["Mr.", "T!"] -> ["Mr. T!"]
    ["Do you like Dr.", "Who?"] -> ["Do you like Dr. Who?"]

Examples that should NOT be merged:
    ["Dr.", "Where did he go?"] -> stays split (multi-word sentence)
    ["Dr.", "who can help."] -> stays split (lowercase = not a name)

Reference: https://github.com/craigtrim/fast-sentence-segment/issues/3
"""

import re
from typing import List, Optional, Tuple

from fast_sentence_segment.core import BaseObject
from fast_sentence_segment.dmo.abbreviations import TITLE_ABBREVIATIONS


# Subset of titles that commonly precede names (not geographic like Mt., St.)
PERSONAL_TITLES: List[str] = [
    "Dr.",
    "Mr.",
    "Mrs.",
    "Ms.",
    "Prof.",
    "Sr.",
    "Jr.",
    "Rev.",
    "Gen.",
    "Col.",
    "Capt.",
    "Lt.",
    "Sgt.",
    "Rep.",
    "Sen.",
    "Gov.",
    "Pres.",
    "Hon.",
]


class TitleNameMerger(BaseObject):
    """Merge sentences incorrectly split at title + single-word name boundaries."""

    def __init__(self):
        """
        Created:
            28-Dec-2024
            craigtrim@gmail.com
        Reference:
            https://github.com/craigtrim/fast-sentence-segment/issues/3
        """
        BaseObject.__init__(self, __name__)

        # Build pattern to match sentences ending with a title abbreviation
        # Escape dots in abbreviations for regex
        escaped_titles = [re.escape(t) for t in PERSONAL_TITLES]
        titles_pattern = "|".join(escaped_titles)
        self._ending_with_title = re.compile(rf"({titles_pattern})$", re.IGNORECASE)

        # Pattern to match a single capitalized word followed by sentence-ending punctuation
        # at the START of a sentence (may have more content after)
        # Matches: "Who?", "Who? More text", "T!", "T! More", "Who?." (with trailing period), etc.
        # Captures the word+punctuation part for extraction
        # Note: The spaCy segmenter may add a trailing period to sentences ending in ?/!
        self._single_word_with_punct = re.compile(r"^([A-Z][a-zA-Z\-]*[?!]+\.?)\s*(.*)$")

    def _try_merge(self, current: str, next_sent: str) -> Optional[Tuple[str, str]]:
        """Try to merge two sentences if they match the title + single-word name pattern.

        Args:
            current: Current sentence (may end with title abbreviation)
            next_sent: Next sentence (may start with single-word name with punctuation)

        Returns:
            Tuple of (merged_sentence, remainder) if merge needed, else None
        """
        current = current.strip()
        next_sent = next_sent.strip()

        # Current sentence must end with a title abbreviation
        if not self._ending_with_title.search(current):
            return None

        # Next sentence must start with a single capitalized word with ?/! punctuation
        match = self._single_word_with_punct.match(next_sent)
        if not match:
            return None

        # Extract the name part and any remainder
        name_part = match.group(1)
        remainder = match.group(2).strip() if match.group(2) else ""

        # Clean up trailing period from name if present (added by spaCy)
        if name_part.endswith('?.') or name_part.endswith('!.'):
            name_part = name_part[:-1]

        merged = current + " " + name_part
        return (merged, remainder)

    def process(self, sentences: List[str]) -> List[str]:
        """Process a list of sentences, merging title + single-word name splits.

        Args:
            sentences: List of sentences

        Returns:
            List of sentences with title+name splits merged
        """
        if not sentences or len(sentences) < 2:
            return sentences

        # Work with a mutable copy
        sentences = list(sentences)
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

                    # If there's a remainder, replace next_sent with it for further processing
                    if remainder:
                        sentences[i + 1] = remainder
                        i += 1  # Move to process the remainder (now at i+1, will be i after increment)
                    else:
                        i += 2  # Skip both merged sentences
                    continue

            result.append(current)
            i += 1

        return result
