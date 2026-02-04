#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Split sentences at ? and ! followed by capital letter """


import re
from typing import List

from fast_sentence_segment.core import BaseObject
from fast_sentence_segment.dmo.abbreviations import EXCLAMATION_COMPANY_NAMES


# Pattern: ? or ! followed by space and capital letter
BOUNDARY_PATTERN = re.compile(r'([?!])(\s+)([A-Z])')

# Build pattern to match company names with exclamation marks
# This pattern matches the company name INCLUDING the "!"
# Uses word boundary \b to avoid matching "e!" inside "Hide!"
_COMPANY_PATTERN = re.compile(
    r'\b(' + '|'.join(re.escape(name) for name in EXCLAMATION_COMPANY_NAMES) + r')',
    re.IGNORECASE
)


class QuestionExclamationSplitter(BaseObject):
    """ Split sentences at ? and ! followed by capital letter """

    def __init__(self):
        """
        Created:
            27-Dec-2024
            craigtrim@gmail.com
            *   spaCy doesn't always split on ? and ! boundaries
                https://github.com/craigtrim/fast-sentence-segment/issues/3
        """
        BaseObject.__init__(self, __name__)

    def _protect_company_names(self, text: str) -> tuple:
        """Replace company names with placeholders to prevent false splits.

        Args:
            text: Input text that may contain company names with "!"

        Returns:
            Tuple of (modified text, list of (placeholder, original) pairs)
        """
        replacements = []
        result = text

        for i, match in enumerate(_COMPANY_PATTERN.finditer(text)):
            placeholder = f"__COMPANY_{i}__"
            original = match.group(0)
            replacements.append((placeholder, original))

        # Apply replacements in reverse order to maintain positions
        for placeholder, original in reversed(replacements):
            result = result.replace(original, placeholder, 1)

        return result, replacements

    def _restore_company_names(self, text: str, replacements: list) -> str:
        """Restore company names from placeholders.

        Args:
            text: Text with placeholders
            replacements: List of (placeholder, original) pairs

        Returns:
            Text with company names restored
        """
        result = text
        for placeholder, original in replacements:
            result = result.replace(placeholder, original)
        return result

    def process(self, sentences: List[str]) -> List[str]:
        """Split sentences that contain ? or ! followed by capital letter.

        Args:
            sentences: List of sentences from earlier processing

        Returns:
            List of sentences with ? and ! boundaries split
        """
        result = []
        for sent in sentences:
            # Protect company names with "!" from being split
            protected, replacements = self._protect_company_names(sent)

            # Split on pattern, keeping the punctuation with the first part
            parts = BOUNDARY_PATTERN.split(protected)
            if len(parts) == 1:
                result.append(sent)
            else:
                # Reassemble: parts = [before, punct, space, capital, after, ...]
                i = 0
                while i < len(parts):
                    if i + 3 < len(parts):
                        # before + punct
                        segment = parts[i] + parts[i + 1]
                        # Restore company names in this segment
                        segment = self._restore_company_names(segment, replacements)
                        result.append(segment)
                        # capital + rest will be handled in next iteration
                        parts[i + 4] = parts[i + 3] + parts[i + 4] if i + 4 < len(parts) else parts[i + 3]
                        i += 4
                    else:
                        if parts[i].strip():
                            # Restore company names in final segment
                            segment = self._restore_company_names(parts[i], replacements)
                            result.append(segment)
                        i += 1

        return [s.strip() for s in result if s.strip()]
