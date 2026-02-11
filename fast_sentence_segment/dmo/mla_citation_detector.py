#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Heuristic-based MLA citation detector.

MLA citations have distinctive patterns that differ from APA:
- No parenthetical years like (2020)
- Multiple periods: "Author. Title. Publisher, Year."
- Specific name format: "LastName, FirstName."
- Publisher and year at end
- Specific keywords: "edited by", "vol.", "pp.", etc.

Instead of enumerating every MLA pattern, this detector uses heuristics
to calculate a probability score (0.0-1.0) that text is an MLA citation.
If confidence is high enough, we apply aggressive period normalization.

Related GitHub Issue:
    #34 - Citation middle initials and multi-sentence citations
    https://github.com/craigtrim/fast-sentence-segment/issues/34

Examples:
    "Hemingway, Ernest. The Sun Also Rises. Scribner, 1926."
    Score: ~0.8 (high confidence MLA)

    "Smith, J. (2020). Article Title."
    Score: ~0.2 (low confidence, likely APA due to parenthetical year)
"""

import re
from typing import Tuple

from fast_sentence_segment.core import BaseObject


class MlaCitationDetector(BaseObject):
    """Detect MLA citations using heuristic scoring.

    Calculates a probability score (0.0-1.0) that text is an MLA citation
    by checking for distinctive MLA features. If score exceeds threshold,
    applies aggressive period normalization.

    This overfitted approach works because MLA has very specific patterns
    that rarely appear in non-citation text.
    """

    def __init__(self, threshold: float = 0.6):
        """
        Args:
            threshold: Minimum probability score (0.0-1.0) to treat as MLA.
                      Default 0.6 means 60% confidence required.

        Created:
            11-Feb-2026
            craigtrim@gmail.com
        """
        BaseObject.__init__(self, __name__)
        self._threshold = threshold

    def calculate_probability(self, text: str) -> Tuple[float, dict]:
        """Calculate probability that text is an MLA citation.

        Uses multiple heuristic features to score the text. Each feature
        adds to the score if present. Final score is clamped to [0.0, 1.0].

        Args:
            text: Text to analyze

        Returns:
            Tuple of (score, features_dict) where score is 0.0-1.0 and
            features_dict shows which features matched (for debugging)
        """
        score = 0.0
        features = {}

        # Feature 1: Author name pattern "LastName, FirstName." (+0.3)
        # MLA always starts with author in this format
        # Examples: "Hemingway, Ernest.", "Morrison, Toni."
        author_pattern = r'^[A-Z][a-z]+,\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?\.(?:\s|$)'
        if re.search(author_pattern, text):
            score += 0.3
            features['author_name'] = True

        # Feature 2: NO parenthetical year (-0.3 if present)
        # MLA doesn't use (2020) format - that's APA
        # If we see (YYYY), strongly indicates NOT MLA
        if re.search(r'\(\d{4}\)', text):
            score -= 0.3
            features['has_parenthetical_year'] = True
        else:
            score += 0.2
            features['no_parenthetical_year'] = True

        # Feature 3: Ends with Publisher, Year pattern (+0.2)
        # MLA citations end with publisher and year
        # Examples: "Scribner, 1926.", "Norton, 2015."
        publisher_year_pattern = r',\s+[A-Z][A-Za-z\s&]+,\s+\d{4}\.$'
        if re.search(publisher_year_pattern, text):
            score += 0.2
            features['publisher_year_end'] = True

        # Feature 4: MLA-specific keywords (+0.15)
        # Common in MLA but rare in other citation styles
        mla_keywords = [
            'edited by', 'translated by', 'edited and translated by',
            'vol\.', 'no\.', 'pp\.', 'p\.',  # volume, number, pages
            'Rev\. ed\.', '5th ed\.', 'ed\.',  # edition markers
            'UP,',  # University Press abbreviation (Norton UP, Cambridge UP)
        ]
        keyword_matches = [kw for kw in mla_keywords if re.search(kw, text, re.IGNORECASE)]
        if keyword_matches:
            score += 0.15
            features['mla_keywords'] = keyword_matches

        # Feature 5: Quoted article title (+0.1)
        # MLA uses quotes for article titles: "Article Title."
        # Book titles are italicized in print but not marked in plain text
        quoted_title_pattern = r'"[A-Z][^"]+\."'
        if re.search(quoted_title_pattern, text):
            score += 0.1
            features['quoted_title'] = True

        # Feature 6: Multiple capital-period sequences (+0.1)
        # MLA has multiple sentences: "Author. Title. Publisher."
        # Need at least 3 to distinguish from regular sentences
        cap_period_count = len(re.findall(r'[A-Z][^.]*\.', text))
        if cap_period_count >= 3:
            score += 0.1
            features['multiple_periods'] = cap_period_count

        # Feature 7: Multi-author pattern with "and" (+0.1)
        # "Smith, John, and Mary Johnson."
        multi_author_pattern = r'[A-Z][a-z]+,\s+[A-Z][a-z]+,\s+and\s+[A-Z][a-z]+\s+[A-Z][a-z]+'
        if re.search(multi_author_pattern, text):
            score += 0.1
            features['multi_author'] = True

        # Feature 8: "et al." without parenthetical year (+0.05)
        # MLA uses "et al." differently than APA
        # "Johnson, Robert, et al." (no year follows immediately)
        et_al_pattern = r'et\s+al\.'
        if re.search(et_al_pattern, text) and not re.search(r'et\s+al\.\s*\(\d{4}\)', text):
            score += 0.05
            features['et_al_no_year'] = True

        # Clamp score to [0.0, 1.0]
        final_score = max(0.0, min(score, 1.0))

        return final_score, features

    def is_mla_citation(self, text: str) -> bool:
        """Check if text is likely an MLA citation.

        Args:
            text: Text to check

        Returns:
            True if probability score >= threshold, False otherwise
        """
        score, _ = self.calculate_probability(text)
        return score >= self._threshold

    def normalize_if_mla(self, text: str, placeholder: str = "xcitationprdx") -> str:
        """Normalize periods in text if detected as MLA citation.

        Uses aggressive overfitting: if MLA is detected with high confidence,
        replace ALL internal periods with placeholders except the final one.

        This works because we know MLA citations have multiple periods that
        should NOT be sentence boundaries.

        Args:
            text: Text to potentially normalize
            placeholder: Placeholder to use for periods

        Returns:
            Normalized text if MLA detected, otherwise unchanged text
        """
        score, features = self.calculate_probability(text)

        if score < self._threshold:
            return text

        # High confidence MLA - apply aggressive normalization
        # Strategy: Replace ALL periods except the final one
        # MLA has periods after author, title (in quotes), abbreviations, etc.

        # Use regex to replace periods NOT at the end
        # Match: period followed by (space OR quote OR comma OR parenthesis)
        # But NOT period at the very end
        import re

        # Replace periods that are NOT the final character
        # Match . followed by space, quote, comma, paren, etc.
        # Overfitted: we know it's MLA, so be aggressive
        normalized = re.sub(
            r'\.\s+',  # Period followed by whitespace
            f'{placeholder} ',
            text.rstrip('.')  # Remove final period temporarily
        )

        # Also replace periods followed by quotes or other punctuation
        # Common in MLA: "Title." or "Title.",
        normalized = re.sub(
            r'\.(?=["\',\)])',  # Period followed by quote, comma, or paren
            placeholder,
            normalized
        )

        # Restore final period if original had one
        if text.rstrip().endswith('.'):
            normalized = normalized.rstrip() + '.'

        return normalized
