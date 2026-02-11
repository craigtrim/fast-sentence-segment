#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Normalize citation patterns to prevent false sentence splits.

Citations in APA, MLA, and informal formats often have periods after author names
followed by parenthetical year information. spaCy treats these periods as sentence
boundaries, incorrectly splitting citations across multiple lines.

This normalizer detects citation patterns and replaces problematic periods with
placeholders to prevent false splits.

Common Citation Patterns:
    APA: "Matolino, Bernard. (2011). The Function..."
    MLA: "Hemingway, Ernest. The Sun Also Rises. Scribner, 1926."
    Informal: "By John Smith, March 15, 2023."

The core issue is: Author Name. (Year). Title
The period after "Name." should NOT be a sentence boundary.

Related GitHub Issue:
    #31 - APA citations incorrectly split leaving orphaned year fragments
    https://github.com/craigtrim/fast-sentence-segment/issues/31

Examples:
    Input:  "Matolino, Bernard. (2011). The Function."
    Problem: Splits into ["Matolino, Bernard.", "(2011).", "The Function."]
    Correct: ["Matolino, Bernard. (2011). The Function."]

Implementation Strategy:
    1. Detect pattern: Name. (Year)
    2. Replace period after Name with placeholder
    3. Let spaCy process the text
    4. Restore the period after processing
"""

import re
from typing import List, Tuple

from fast_sentence_segment.core import BaseObject


# Placeholder for period after author name in citations
# Uses lowercase word-like token that spaCy treats as regular text
PLACEHOLDER_CITATION_PERIOD = "xcitationprdx"

# Pattern to match month names in dates (within citations)
# Matches full month names that appear in date contexts
# Examples: "March 15", "December 31", "June 2020"
# We'll replace each month with a unique placeholder: "March" → "xmonthMarchx"
# This allows us to restore the exact month name during denormalization
MONTH_PATTERN = re.compile(
    r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\b'
)

# Pattern to match month placeholders during denormalization
# Matches: xmonthJanuaryx, xmonthMarchx, etc.
MONTH_PLACEHOLDER_PATTERN = re.compile(r'xmonth([A-Z][a-z]+)x')


# CORE PATTERN: Name. (Year). Title - The main issue from #31
# Matches: Author name ending with period, followed by (Year) with optional period
# Examples:
#   "Matolino, Bernard. (2011). Title"
#   "Smith, John. (2023). Work"
#   "Organization Name. (2020). Report"
#
# Pattern breakdown:
#   ([A-Z][A-Za-z\s,.&'-]+?)  - Author name (flexible, may include multiple words, commas, etc.)
#   \.                        - Period after author name (we'll replace with placeholder)
#   \s*                       - Optional whitespace
#   (\(\d{4}[a-z]?(?:,\s+\w+(?:\s+\d+)?)?\))  - Year with parentheses (with optional letter suffix like 2023a)
#   \.?                       - Optional period after year (we'll replace if present)
#   \s+                       - Whitespace before title
#   ([A-Z])                   - Start of title (capital letter)
CITATION_BASIC_PATTERN = re.compile(
    r"([A-Z][A-Za-z\s,.&'-]+?)\.\s*(\(\d{4}[a-z]?(?:,\s+\w+(?:\s+\d+)?)?\))\.?\s+([A-Z])"
)

# PATTERN: Organizational names with periods followed by year
# Handles: "U.S. Department. (2020). Report"
#          "N.A.S.A. (2022). Mission"
# This pattern requires at least two components to avoid matching single initials like "J."
# Matches: U.S. Department, N.A.S.A., U.K. Parliament, etc.
INSTITUTIONAL_CITATION_PATTERN = re.compile(
    r'([A-Z]\.(?:[A-Z]\.)+(?:\s+[A-Z][A-Za-z]+)+)\s*(\(\d{4}(?:,\s+\w+(?:\s+\d+)?)?\))\.?\s+([A-Z])'
)

# PATTERN: Citation with et al.
# "Smith, J., et al. (2020). Title"
ET_AL_CITATION_PATTERN = re.compile(
    r'([A-Z][A-Za-z]+,\s+[A-Z]\.(?:\s+[A-Z]\.)*,?\s+et\s+al)\.\s*(\(\d{4}(?:,\s+\w+(?:\s+\d+)?)?\))\.?\s+([A-Z])'
)

# PATTERN: Special dates (n.d., in press)
# "Author. (n.d.). Title"
# "Smith. (in press). Work"
SPECIAL_DATE_CITATION_PATTERN = re.compile(
    r"([A-Z][A-Za-z\s,.&'-]+?)\.\s*(\((?:n\.d\.|in\s+press|forthcoming)\))\.?\s+([A-Z])"
)

# PATTERN: Editor/Translator patterns
# "Smith, J. (Ed.). (2020). Title"
# "Brown, K. (Trans.). (2019). Work"
EDITOR_CITATION_PATTERN = re.compile(
    r"([A-Z][A-Za-z\s,.&'-]+?)\s+\((Ed\.|Eds\.|Trans\.)\)\.\s*(\(\d{4}(?:,\s+\w+(?:\s+\d+)?)?\))\.?\s+([A-Z])"
)

# PATTERN: MLA style author names
# "Hemingway, Ernest. The Sun Also Rises."
# Must be careful not to over-match regular sentences
# This pattern looks for: Capitalized Last, Capitalized First. Title.
MLA_AUTHOR_PATTERN = re.compile(
    r'([A-Z][a-z]+,\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\.\s+([A-Z][A-Za-z\s]+\.)'
)


class CitationNormalizer(BaseObject):
    """Normalize citation patterns to prevent sentence splits.

    Detects citation patterns like "Author. (Year). Title" and replaces
    the period after the author name with a placeholder that spaCy won't
    split on.

    This prevents APA, MLA, and informal citations from being incorrectly
    split across multiple lines.

    Example:
        Input:  "Matolino, Bernard. (2011). The Function."
        Norm:   "Matolino, Bernardxcitationprdx (2011). The Function."
        After:  "Matolino, Bernard. (2011). The Function."
    """

    def __init__(self):
        """
        Created:
            10-Feb-2026
            craigtrim@gmail.com
        Reference:
            https://github.com/craigtrim/fast-sentence-segment/issues/31
        """
        BaseObject.__init__(self, __name__)

    def _normalize(self, text: str) -> str:
        """Replace periods in citation patterns with placeholders.

        Processes text through multiple citation patterns, from most specific
        to most general, to avoid over-matching.

        Also normalizes month names to prevent spaCy from treating capitalized
        months as sentence boundaries.

        Args:
            text: Input text that may contain citations

        Returns:
            Text with citation periods replaced by placeholders.
        """
        # 0. Normalize month names FIRST (before any other processing)
        # Month names are capitalized and confuse spaCy's sentence boundary detection
        # "Johnson, A. (2020, March 15). Title" → "Johnson, A. (2020, xmonthMarchx 15). Title"
        # Each month gets a unique placeholder so we can restore it correctly later
        text = MONTH_PATTERN.sub(lambda m: f'xmonth{m.group(1)}x', text)

        # Process most specific patterns first

        # 1. Editor/Translator patterns (very specific)
        # "Smith, J. (Ed.). (2020). Title" → "Smith, J. (Ed.)xcitationprdx (2020)xcitationprdx Title"
        text = EDITOR_CITATION_PATTERN.sub(
            rf'\1 (\2){PLACEHOLDER_CITATION_PERIOD} \3{PLACEHOLDER_CITATION_PERIOD} \4',
            text
        )

        # 2. Et al. pattern (specific)
        # "Smith, J., et al. (2020). Title" → "Smith, J., et alxcitationprdx (2020)xcitationprdx Title"
        text = ET_AL_CITATION_PATTERN.sub(
            rf'\1{PLACEHOLDER_CITATION_PERIOD} \2{PLACEHOLDER_CITATION_PERIOD} \3',
            text
        )

        # 3. Special dates (n.d., in press)
        # "Author. (n.d.). Title" → "Authorxcitationprdx (n.d.)xcitationprdx Title"
        text = SPECIAL_DATE_CITATION_PATTERN.sub(
            rf'\1{PLACEHOLDER_CITATION_PERIOD} \2{PLACEHOLDER_CITATION_PERIOD} \3',
            text
        )

        # 4. Institutional names with abbreviations
        # "U.S. Department. (2020). Report" → "U.S. Departmentxcitationprdx (2020)xcitationprdx Report"
        text = INSTITUTIONAL_CITATION_PATTERN.sub(
            rf'\1{PLACEHOLDER_CITATION_PERIOD} \2{PLACEHOLDER_CITATION_PERIOD} \3',
            text
        )

        # 5. Core citation pattern - Name. (Year). Title
        # This is the main pattern from Issue #31
        # "Matolino, Bernard. (2011). Title" → "Matolino, Bernardxcitationprdx (2011)xcitationprdx Title"
        text = CITATION_BASIC_PATTERN.sub(
            rf'\1{PLACEHOLDER_CITATION_PERIOD} \2{PLACEHOLDER_CITATION_PERIOD} \3',
            text
        )

        # 6. MLA author pattern (least specific, so last)
        # "Hemingway, Ernest. The Sun" → "Hemingway, Ernestxcitationprdx The Sun"
        # Be conservative here to avoid false matches
        text = MLA_AUTHOR_PATTERN.sub(
            rf'\1{PLACEHOLDER_CITATION_PERIOD} \2',
            text
        )

        return text

    def _denormalize(self, text: str) -> str:
        """Restore placeholders back to periods and month names.

        Args:
            text: Text with placeholders

        Returns:
            Text with periods and month names restored.
        """
        # Restore month names first
        # "xmonthMarchx" → "March"
        text = MONTH_PLACEHOLDER_PATTERN.sub(lambda m: m.group(1), text)

        # Restore citation periods
        text = text.replace(PLACEHOLDER_CITATION_PERIOD, '.')

        return text

    def process(self, text: str, denormalize: bool = False) -> str:
        """Normalize or denormalize citation periods.

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
