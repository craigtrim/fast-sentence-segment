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

    def _is_standalone_title(self, text: str) -> bool:
        """Check if text is a standalone numbered title.

        A standalone title is a short sentence matching the pattern:
        [Keyword] [Number].

        Must NOT have text before the keyword (e.g., "Assignment Module 3." is NOT standalone)

        Examples: "Part 8.", "Chapter 17.", "Module III."

        Args:
            text: Text to check

        Returns:
            True if text is a standalone numbered title
        """
        text = text.strip()

        # Check each keyword
        for keyword in TITLE_KEYWORDS:
            # Pattern: keyword + whitespace + number + period (case-insensitive)
            # MUST start at the beginning (no text before keyword)
            pattern = rf"^\s*{re.escape(keyword)}\s+(\d+|[IVXLCDMivxlcdm]+|[A-Za-z])\.?\s*$"
            if re.match(pattern, text, re.IGNORECASE):
                return True

        return False

    def _looks_like_title(self, text: str) -> bool:
        """Check if text looks like a standalone title (not a descriptive sentence).

        Heuristic: Short (1-4 words), title case. May or may not end with period.
        Examples: "The Beginning.", "Introduction", "Overview", "Introduction to Economics"

        Args:
            text: Text to check

        Returns:
            True if text looks like a title
        """
        text = text.strip()

        # Remove trailing period if present for word counting
        text_for_analysis = text[:-1] if text.endswith('.') else text

        # Count words (split on whitespace)
        words = text_for_analysis.split()
        if len(words) > 4:
            return False

        # Check if title case (first letter of each word is uppercase)
        # Allow for common lowercase words like "a", "the", "of", "to"
        lowercase_allowed = {'a', 'an', 'the', 'of', 'in', 'on', 'at', 'to', 'for'}
        for i, word in enumerate(words):
            if not word:
                continue
            # First word must be capitalized
            if i == 0 and not word[0].isupper():
                return False
            # Other words: either capitalized or in allowed lowercase set
            if i > 0 and not (word[0].isupper() or word.lower() in lowercase_allowed):
                return False

        return True

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

        # Case 1: Current is a standalone numbered title (e.g., "Part 8.")
        # Merge with next sentence UNLESS next sentence is also a title
        if self._is_standalone_title(current):
            # Special case: "Week N." patterns are ALWAYS separate sentences
            # This is an overfitted solution for common academic/course patterns
            # Related GitHub Issue:
            #     https://github.com/craigtrim/fast-sentence-segment/issues/30
            if re.match(r'^Week\s+\d{1,2}\.?$', current, re.IGNORECASE):
                return None

            # Don't merge if next is also a title (e.g., "The Beginning.")
            if self._looks_like_title(next_sent):
                return None

            merged = current + " " + next_sent
            return (merged, "")

        # Case 2: Current sentence ends with title keyword, next starts with number
        # e.g., ["Part", "2. (May 6, 2008)"]
        keyword_match = self._ending_with_keyword.search(current)
        if keyword_match:
            # Next sentence must start with a number
            number_result = self._extract_number(next_sent)
            if number_result:
                number_part, remainder = number_result

                # Build merged sentence: "Keyword Number."
                merged = current + " " + number_part

                return (merged, remainder.strip())

        # Case 3: Current contains a numbered title pattern and next starts with metadata delimiter
        # e.g., ["Part 2. (May 6, 2008)", "[Video File]"]
        # This handles cases where spaCy splits metadata in brackets from the numbered title
        # Pattern to match numbered title in current sentence
        numbered_title_in_current = r'\b(Part|Chapter|Module|Section|Week|Step|Phase|Unit|Level|Stage)\s+(\d+|[IVXLCDMivxlcdm]+|[A-Za-z])\.'
        if re.search(numbered_title_in_current, current, re.IGNORECASE):
            # Check if next sentence starts with metadata delimiters
            # Common patterns: [Video File], (Additional info), <tag>, etc.
            if next_sent and next_sent[0] in '([{<':
                # Merge them together
                merged = current + " " + next_sent
                return (merged, "")

        return None

    def process(self, sentences: List[str]) -> List[str]:
        """Process a list of sentences, merging numbered title splits.

        Args:
            sentences: List of sentences from spaCy

        Returns:
            List of sentences with numbered title splits merged
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
                merge_result = self._try_merge(current, next_sent)

                if merge_result:
                    merged, remainder = merge_result
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

        return result
