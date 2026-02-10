#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Merge sentences that spaCy incorrectly split at numbered title boundaries.

When spaCy incorrectly splits after a numbered title like "Part 2." or
"Chapter IV.", this component merges them back together with the following
content, treating the numbered title as an introductory phrase rather than
a complete sentence.

Examples:
    ["Try crossing this street!!", "Part", "2. (May 6, 2008)"]
    -> ["Try crossing this street!!", "Part 2. (May 6, 2008)"]

    ["Chapter 1.", "The Beginning.", "It was dark."]
    -> ["Chapter 1.", "The Beginning.", "It was dark."]  (stays separate)

Reference: https://github.com/craigtrim/fast-sentence-segment/issues/30
"""

import re
from typing import List, Optional, Tuple

from fast_sentence_segment.core import BaseObject


# Full-word title keywords that precede numbers
# Format: Case-insensitive keywords that introduce numbered sections
TITLE_KEYWORDS: List[str] = [
    "Part",
    "Module",
    "Week",
    "Chapter",
    "Section",
    "Step",
    "Phase",
    "Unit",
    "Level",
    "Stage",
]


class NumberedTitleMerger(BaseObject):
    """Merge sentences incorrectly split at numbered title boundaries."""

    def __init__(self):
        """
        Created:
            10-Feb-2025
            craigtrim@gmail.com
        Reference:
            https://github.com/craigtrim/fast-sentence-segment/issues/30
        """
        BaseObject.__init__(self, __name__)

        # Build pattern to match keywords at end of sentence
        # Escape for regex and join with |
        keywords_pattern = "|".join(TITLE_KEYWORDS)

        # Match keyword at end of sentence (case-insensitive)
        # Can be preceded by other text
        self._ending_with_keyword = re.compile(
            rf"\b({keywords_pattern})$",
            re.IGNORECASE
        )

        # Pattern for numbered portions at start of next sentence
        # Matches:
        # - Arabic numerals: 1., 2., 10., 123.
        # - Roman numerals: I., II., III., IV., V., etc.
        # - Letters: A., B., C., etc.
        # - Optionally followed by more content

        # Arabic: \d+\.
        # Roman: I{1,3}|IV|V|VI{0,3}|IX|X{1,3}|XL|L|XC|C{1,3}|CD|D|CM|M{1,3}
        # (simplified to common cases: I-XX, L, C, D, M)
        # Letter: [A-Z]

        self._number_pattern = re.compile(
            r"^(\d+\.)"  # Arabic numeral + period
            r"|^([IVX]+\.)"  # Roman numeral + period (basic set)
            r"|^([A-Z]\.)"  # Single uppercase letter + period
            , re.IGNORECASE
        )

        # More comprehensive Roman numeral pattern for validation
        # Covers I (1) through M (1000) and common combinations
        self._roman_numeral = re.compile(
            r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",
            re.IGNORECASE
        )

    def _is_valid_roman_numeral(self, text: str) -> bool:
        """Check if text is a valid Roman numeral.

        Args:
            text: Text to check (without trailing period)

        Returns:
            True if valid Roman numeral, False otherwise
        """
        if not text:
            return False
        return bool(self._roman_numeral.match(text.upper()))

    def _extract_number(self, text: str) -> Optional[Tuple[str, str]]:
        """Extract number portion from start of text.

        Args:
            text: Text starting with potential number

        Returns:
            Tuple of (number_part, remainder) if found, else None
            number_part includes the trailing period
        """
        text = text.strip()

        # Try Arabic numeral (most common)
        match = re.match(r"^(\d+\.)\s*(.*)", text)
        if match:
            return (match.group(1), match.group(2))

        # Try Roman numeral
        match = re.match(r"^([IVXLCDMivxlcdm]+\.)\s*(.*)", text)
        if match:
            roman_part = match.group(1)[:-1]  # Remove period for validation
            if self._is_valid_roman_numeral(roman_part):
                return (match.group(1), match.group(2))

        # Try single letter
        match = re.match(r"^([A-Z]\.)\s*(.*)", text, re.IGNORECASE)
        if match:
            return (match.group(1), match.group(2))

        return None

    def _try_merge(self, current: str, next_sent: str) -> Optional[Tuple[str, str]]:
        """Try to merge two sentences if they match the numbered title pattern.

        Args:
            current: Current sentence (may end with title keyword)
            next_sent: Next sentence (may start with number)

        Returns:
            Tuple of (merged_sentence, remainder) if merge needed, else None
        """
        current = current.strip()
        next_sent = next_sent.strip()

        # Current sentence must end with a title keyword
        keyword_match = self._ending_with_keyword.search(current)
        if not keyword_match:
            return None

        # Next sentence must start with a number
        number_result = self._extract_number(next_sent)
        if not number_result:
            return None

        number_part, remainder = number_result

        # Build merged sentence: "Keyword Number."
        merged = current + " " + number_part

        return (merged, remainder.strip())

    def process(self, sentences: List[str]) -> List[str]:
        """Process a list of sentences, merging numbered title splits.

        Args:
            sentences: List of sentences from spaCy

        Returns:
            List of sentences with numbered title splits merged
        """
        # DEBUG: Log input
        import sys
        print(f"\n[NumberedTitleMerger] Input ({len(sentences)} sentences):", file=sys.stderr)
        for idx, sent in enumerate(sentences):
            print(f"  [{idx}]: {repr(sent)}", file=sys.stderr)

        if not sentences or len(sentences) < 2:
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
                    print(f"[NumberedTitleMerger] MERGED: {repr(current)} + {repr(next_sent)} -> {repr(merged)}", file=sys.stderr)
                    result.append(merged)

                    # If there's a remainder, it becomes a new sentence to process
                    if remainder:
                        # Replace next sentence with remainder for further processing
                        sentences[i + 1] = remainder
                        i += 1  # Move to process the remainder
                    else:
                        i += 2  # Skip both merged sentences
                    continue

            result.append(current)
            i += 1

        print(f"[NumberedTitleMerger] Output ({len(result)} sentences):", file=sys.stderr)
        for idx, sent in enumerate(result):
            print(f"  [{idx}]: {repr(sent)}", file=sys.stderr)

        return result
