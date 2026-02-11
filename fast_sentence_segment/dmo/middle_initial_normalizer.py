#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Normalize middle initials in names to prevent false sentence splits.

Names with middle initials like "Albert I. Jones" or "John F. Kennedy" have
a single capital letter followed by a period. spaCy often treats this period
as a sentence boundary, splitting incorrectly.

This normalizer detects common name patterns with middle initials and replaces
the period with a placeholder to prevent false splits.

Pattern: FirstName M. LastName
- FirstName: Capitalized word (1+ letters)
- M.: Single capital letter followed by period
- LastName: Capitalized word (1+ letters)

Examples:
    "Albert I. Jones" → "Albert IxmidinitialprdxJones"
    "John F. Kennedy" → "John FxmidinitialprdxKennedy"

Related GitHub Issues:
    #25 - Middle Initial Pattern in Names (Albert I. Jones)
    https://github.com/craigtrim/fast-sentence-segment/issues/25

    Golden Rule 42: "We make a good team, you and I. Did you see Albert I. Jones yesterday?"
    Should split at "I." (pronoun, sentence end) but NOT at "I." (middle initial)
"""

import re
from typing import List, Tuple

from fast_sentence_segment.core import BaseObject


# Placeholder for period after middle initial
# Uses lowercase word-like token that spaCy treats as regular text
PLACEHOLDER_PERIOD = "xmidinitialprdx"


# Pattern to match names with middle initials
# Structure: Capitalized word + space + single capital + period + space + Capitalized word
# Examples: "Albert I. Jones", "John F. Kennedy", "Mary J. Smith"
#
# Breakdown:
#   ([A-Z][a-z]+)       - FirstName: capital + lowercase letters
#   \s+                 - whitespace
#   ([A-Z])             - Middle initial: single capital letter
#   \.                  - period after initial
#   \s+                 - whitespace
#   ([A-Z][a-z]+)       - LastName: capital + lowercase letters
#
# NOTE: This won't catch ALL names (e.g., "O'Brien", hyphenated names) but
# catches the common pattern. We're intentionally not over-fitting here.
MIDDLE_INITIAL_PATTERN = re.compile(
    r'([A-Z][a-z]+)\s+([A-Z])\.(\s+)([A-Z][a-z]+)'
)

# Pattern for multiple middle initials like "J. R. R. Tolkien"
# Matches: initial + period + space + initial + period (repeated)
MULTIPLE_INITIALS_PATTERN = re.compile(
    r'([A-Z])\.(\s+)([A-Z])\.(\s+)([A-Z]\.?)(\s+)([A-Z][a-z]+)'
)

# Pattern for "FirstName A. B. LastName" (two middle initials)
TWO_INITIALS_PATTERN = re.compile(
    r'([A-Z][a-z]+)\s+([A-Z])\.(\s+)([A-Z])\.(\s+)([A-Z][a-z]+)'
)

# Pattern for citation-style initials: "LastName, A. B. C. (Year)"
# Matches initials after comma in academic citations (APA, MLA, etc.)
# Examples: "Smith, J. R. (2020)", "Jones, A. B. C. (2019)"
# Breakdown:
#   ([A-Z][a-z]+)           - LastName: capital + lowercase letters
#   ,\s+                    - comma + whitespace
#   ([A-Z]\.)               - First initial: capital + period
#   (?:\s+[A-Z]\.)*         - Additional initials (zero or more): space + capital + period
#   \s+\(                   - space + opening paren (start of year)
CITATION_INITIALS_PATTERN = re.compile(
    r'([A-Z][a-z]+),\s+([A-Z]\.)(\s+[A-Z]\.)*\s+\('
)


class MiddleInitialNormalizer(BaseObject):
    """Normalize middle initials in names to prevent sentence splits.

    Detects patterns like "Albert I. Jones" and replaces the period after
    the middle initial with a placeholder that spaCy won't split on.

    Example:
        Input:  "Did you see Albert I. Jones yesterday?"
        Norm:   "Did you see Albert IxmidinitialprdxJones yesterday?"
        After:  "Did you see Albert I. Jones yesterday?"
    """

    def __init__(self):
        """
        Created:
            04-Feb-2026
            craigtrim@gmail.com
        Reference:
            https://github.com/craigtrim/fast-sentence-segment/issues/25
        """
        BaseObject.__init__(self, __name__)

    def _normalize(self, text: str) -> str:
        """Replace periods after middle initials with placeholders.

        Args:
            text: Input text that may contain names with middle initials

        Returns:
            Text with middle initial periods replaced by placeholders.
        """
        # Handle citation-style initials first (most specific pattern)
        # "Williams, P. R. K. (2019)" → "Williams, Pxmidinitialprdx Rxmidinitialprdx K. (2019)"
        # IMPORTANT: We preserve the last period before the parenthesis because the
        # CitationNormalizer needs it to detect the citation pattern
        def replace_citation_initials(match):
            lastname = match.group(1)
            # Get all the initials (including the ones captured in group 3)
            initials_text = match.group(0)[len(lastname)+2:-2]  # Skip "LastName, " and " ("
            # Replace all periods EXCEPT the last one with placeholders
            # Split by periods, replace periods in between, keep last one
            parts = initials_text.split('.')
            if len(parts) > 1:
                # Replace periods between initials but not the final one
                normalized_initials = PLACEHOLDER_PERIOD.join(parts[:-1]) + '.'
            else:
                normalized_initials = initials_text
            return f"{lastname}, {normalized_initials} ("

        text = CITATION_INITIALS_PATTERN.sub(replace_citation_initials, text)

        # Handle multiple initials first (most specific pattern)
        # "J. R. R. Tolkien" → "JxmidinitialprdxRxmidinitialprdxR. Tolkien"
        # (We leave the last initial with its period if followed by title like Jr.)
        text = MULTIPLE_INITIALS_PATTERN.sub(
            rf'\1{PLACEHOLDER_PERIOD}\2\3{PLACEHOLDER_PERIOD}\4\5\6\7',
            text
        )

        # Handle two initials: "John F. X. Smith"
        text = TWO_INITIALS_PATTERN.sub(
            rf'\1 \2{PLACEHOLDER_PERIOD}\3\4{PLACEHOLDER_PERIOD}\5\6',
            text
        )

        # Handle single middle initial: "Albert I. Jones"
        # Replacement keeps structure: FirstName Initial<placeholder>Space LastName
        text = MIDDLE_INITIAL_PATTERN.sub(
            rf'\1 \2{PLACEHOLDER_PERIOD}\3\4',
            text
        )

        return text

    def _denormalize(self, text: str) -> str:
        """Restore placeholders back to periods.

        Args:
            text: Text with placeholders

        Returns:
            Text with periods restored.
        """
        return text.replace(PLACEHOLDER_PERIOD, '.')

    def process(self, text: str, denormalize: bool = False) -> str:
        """Normalize or denormalize middle initial periods.

        Args:
            text: Text to process
            denormalize: If True, restore placeholders to periods.
                         If False, replace periods with placeholders.

        Returns:
            Processed text.
        """
        if denormalize:
            return self._denormalize(text)
        return self._normalize(text)
