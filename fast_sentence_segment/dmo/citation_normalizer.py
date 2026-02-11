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
from fast_sentence_segment.dmo.mla_citation_detector import MlaCitationDetector


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

# PATTERN: Citation with retrieval information
# "Smith, J. (2023). Digital Article. Retrieved from https://..."
# "Brown, A. (2022). Report. Available from http://..."
# "Jones, K. (2021). Study. Accessed at https://..."
# The period after the title (Article, Report, Study) should not cause a split
# Hardcoded retrieval keywords (overfitted approach per user guidance)
RETRIEVAL_KEYWORDS = r'(?:Retrieved|Available|Accessed|Downloaded|Obtained|Found|Located)'
RETRIEVAL_CITATION_PATTERN = re.compile(
    rf'\.\s+({RETRIEVAL_KEYWORDS}\s+(?:from|at|on))\s+'
)

# PATTERN: Citation followed directly by URL
# "Brown, A. (2022). Online Research. https://doi.org/..."
# "Smith, J. (2023). Web Article. http://example.com"
# The period before the URL should not cause a split
# NOTE: URLs are already replaced with placeholders (xurl1x, xurl2x, etc.)
# by UrlNormalizer which runs BEFORE CitationNormalizer in the pipeline
URL_CITATION_PATTERN = re.compile(
    r'\.\s+(?=xurl\d+x)'
)

# PATTERN: APA journal article - Title followed by journal name with volume/issue
# "Johnson, A. (2021). Article Title. Journal of Research, 15(3), 123-145."
# "Smith, J. (2020). Study Results. International Journal, 28(2), 45-67."
# The period after the article title should not split before the journal name
# Overfitted pattern: Matches period before journal name (identified by volume/page indicators)
# Format: ". [Capital Word]+" followed eventually by ", digits"
# Uses lookahead to detect journal format without consuming the volume/issue/page info
JOURNAL_ARTICLE_PATTERN = re.compile(
    r'\.\s+(?=[A-Z][A-Za-z\s&]+,\s+\d+)'
)

# PATTERN: APA chapter/proceeding with "In"
# "Smith, J. (2020). Chapter Title. In K. Brown (Ed.), Book Title (pp. 25-50)."
# "Brown, K. (2020). Paper Title. In Proceedings of the Conference (pp. 100-110)."
# The period before "In" should not cause a split
# Common in edited books and conference proceedings
IN_EDITOR_PATTERN = re.compile(
    r'\.\s+(In\s+)'
)

# PATTERN: APA dissertation/thesis/report with parenthetical type indicator
# "Johnson, P. (2021). Title (Doctoral dissertation). University Name."
# "Garcia, M. (2020). Title (Master's thesis). University Name."
# "APA. (2019). Title (Report No. 123). Publisher."
# The period after the parenthetical type indicator should not cause a split
# Overfitted to common academic publication types
PARENTHETICAL_TYPE_PATTERN = re.compile(
    r'(\((?:Doctoral dissertation|Master\'s thesis|Report No\.\s*\d+)\))\.\s+([A-Z])'
)

# PATTERN: Retrieved with date (extended retrieval pattern)
# "Blog Post. Retrieved June 15, 2023, from URL"
# "Article. Retrieved January 1, 2020, from URL"
# Extends RETRIEVAL_CITATION_PATTERN to handle dates between Retrieved and from
# Format: ". Retrieved Month Day, Year, from"
RETRIEVAL_WITH_DATE_PATTERN = re.compile(
    rf'\.\s+(Retrieved\s+\w+\s+\d{{1,2}},\s+\d{{4}},\s+from)\s+'
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
        # MLA citation detector for heuristic-based detection
        self._mla_detector = MlaCitationDetector(threshold=0.6)

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

        # 0.5. Check for MLA citations using heuristic detector (Issue #36)
        # MLA citations are fundamentally different from APA and have 3-5+ periods
        # in various positions. Instead of maintaining 50+ patterns, we use a
        # heuristic classifier that calculates confidence score based on 8 features.
        #
        # If high confidence MLA detected (score ≥ 0.6), apply aggressive normalization:
        # replace ALL internal periods with placeholders except the final one.
        #
        # Why early return? MLA and APA are mutually exclusive. If we detect MLA
        # with high confidence, skip APA patterns entirely for performance.
        #
        # Examples:
        #   "Hemingway, Ernest. The Sun Also Rises. Scribner, 1926."
        #   → "Hemingway, Ernestxcitationprdx The Sun Also Risesxcitationprdx Scribner, 1926."
        #
        #   'Williams, P. "Article Title." Journal, vol. 15, no. 3, 2020, pp. 123-145.'
        #   → 'Williams, Pxcitationprdx "Article Titlexcitationprdx" Journal, volxcitationprdx 15...'
        #
        # Related: Issue #36 - Heuristic-Based MLA Citation Detector
        # See: https://github.com/craigtrim/fast-sentence-segment/issues/36
        mla_normalized = self._mla_detector.normalize_if_mla(text, PLACEHOLDER_CITATION_PERIOD)
        if mla_normalized != text:
            # MLA detected and normalized - return early, skip APA patterns
            return mla_normalized

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

        # 7. Citations with retrieval information
        # After processing basic citation patterns, handle multi-sentence citations
        # "Title. Retrieved from URL" → "Titlexcitationprdx Retrieved from URL"
        # "Title. Available at URL" → "Titlexcitationprdx Available at URL"
        text = RETRIEVAL_CITATION_PATTERN.sub(
            rf'{PLACEHOLDER_CITATION_PERIOD} \1 ',
            text
        )

        # 8. Citations followed directly by URL
        # "Title. https://..." → "Titlexcitationprdx https://..."
        # "Title. doi:..." → "Titlexcitationprdx doi:..."
        # Using lookahead so we don't consume the URL itself
        text = URL_CITATION_PATTERN.sub(
            PLACEHOLDER_CITATION_PERIOD + ' ',
            text
        )

        # 9. APA journal articles - Title followed by journal name
        # "Article Title. Journal of Research, 15(3), 123-145." → "Article Titlexcitationprdx Journal of Research, 15(3), 123-145."
        # Overfitted to journal citation format with volume/issue numbers
        # Using lookahead so we don't consume the journal name
        text = JOURNAL_ARTICLE_PATTERN.sub(
            PLACEHOLDER_CITATION_PERIOD + ' ',
            text
        )

        # 10. APA chapter/proceeding with "In"
        # "Chapter Title. In K. Brown (Ed.)" → "Chapter Titlexcitationprdx In K. Brown (Ed.)"
        # Common in edited books and conference proceedings
        text = IN_EDITOR_PATTERN.sub(
            rf'{PLACEHOLDER_CITATION_PERIOD} \1',
            text
        )

        # 11. APA dissertation/thesis/report with parenthetical type
        # "(Doctoral dissertation). University Name" → "(Doctoral dissertation)xcitationprdx University Name"
        # Keeps dissertation/report metadata together with publisher
        text = PARENTHETICAL_TYPE_PATTERN.sub(
            rf'\1{PLACEHOLDER_CITATION_PERIOD} \2',
            text
        )

        # 12. Retrieved with date (extended retrieval pattern)
        # "Blog Post. Retrieved June 15, 2023, from URL" → "Blog Postxcitationprdx Retrieved June 15, 2023, from URL"
        # Handles date between Retrieved and from
        text = RETRIEVAL_WITH_DATE_PATTERN.sub(
            rf'{PLACEHOLDER_CITATION_PERIOD} \1 ',
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
