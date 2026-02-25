#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Normalize inline list markers to prevent false sentence splits.

This module protects list markers (like "1." "1.)" "a." "i.") from being
split by spaCy. Uses word-like placeholders that spaCy treats as regular
tokens, not punctuation.

Reference: https://github.com/craigtrim/fast-sentence-segment/issues/18
"""

import re
from typing import List, Tuple

from fast_sentence_segment.core import BaseObject


# Roman numeral patterns (lowercase and uppercase) - limited to common ones (i-xxxix)
# NOTE: x{1,2} requires at least 1 x to avoid matching empty string (Issue #21)
# Previously x{0,2}i{0,3} could match empty string, causing `. . .` to be
# incorrectly treated as three Roman numeral list markers instead of ellipsis.
# Reference: https://github.com/craigtrim/fast-sentence-segment/issues/21
ROMAN_LOWER = r'(?:i{1,3}|iv|vi{0,3}|ix|x{1,2}i{0,3}|x{1,2}iv|x{1,2}ix)'
ROMAN_UPPER = r'(?:I{1,3}|IV|VI{0,3}|IX|X{1,2}I{0,3}|X{1,2}IV|X{1,2}IX)'

# Placeholder format: short lowercase tokens that spaCy won't split on
# Format: xlm{marker}x where marker keeps digits as-is for brevity
# Example: "1.)" -> "xlm1dpx", "10." -> "xlm10dx"
# Note: Long placeholders like "listmarkeronedotparenend" confuse spaCy's
# statistical sentence boundary detection, so we use shorter forms.
PLACEHOLDER_PREFIX = "xlm"
PLACEHOLDER_SUFFIX = "x"


class ListMarkerNormalizer(BaseObject):
    """Normalize list markers to prevent spaCy from splitting on them.

    Uses deterministic placeholders that encode the marker type and value,
    allowing stateless denormalization.
    """

    def __init__(self):
        """
        Created:
            03-Feb-2026
            craigtrim@gmail.com
            *   Protect inline list markers from false splits
                https://github.com/craigtrim/fast-sentence-segment/issues/18
        """
        BaseObject.__init__(self, __name__)

    def _marker_to_placeholder(self, marker: str) -> str:
        """Convert a list marker to a deterministic placeholder.

        Encodes the marker type and value in the placeholder so it can
        be restored without maintaining state. Uses short codes to avoid
        confusing spaCy's sentence boundary detection.

        Examples:
            "1." -> "xlm1dx"
            "1.)" -> "xlm1dpx"
            "a." -> "xlmadx"
            "A." -> "xlmuadx" (u prefix for uppercase)
            "ii)" -> "xlmiipx"
        """
        # Preserve case info: uppercase letters get 'u' prefix
        encoded = ""
        for char in marker:
            if char.isupper():
                encoded += 'u' + char.lower()
            else:
                encoded += char

        # Encode punctuation with single letters
        encoded = encoded.replace('.)', 'dp')  # Period+paren combo first
        encoded = encoded.replace('.', 'd')     # d for dot
        encoded = encoded.replace(')', 'p')     # p for paren

        return f"{PLACEHOLDER_PREFIX}{encoded}{PLACEHOLDER_SUFFIX}"

    def _placeholder_to_marker(self, placeholder: str) -> str:
        """Convert a placeholder back to the original list marker.

        Examples:
            "xlm1dx" -> "1."
            "xlm1dpx" -> "1.)"
            "xlmadx" -> "a."
            "xlmuadx" -> "A."
            "xlmiipx" -> "ii)"
        """
        # Extract the encoded part
        if not placeholder.startswith(PLACEHOLDER_PREFIX):
            return placeholder
        if not placeholder.endswith(PLACEHOLDER_SUFFIX):
            return placeholder

        encoded = placeholder[len(PLACEHOLDER_PREFIX):-len(PLACEHOLDER_SUFFIX)]

        # Decode punctuation first (order matters: dp before d and p)
        decoded = encoded
        decoded = decoded.replace('dp', '.)')  # Period+paren combo first
        decoded = decoded.replace('d', '.')    # d for dot
        decoded = decoded.replace('p', ')')    # p for paren

        # Restore uppercase: 'u' followed by letter means uppercase
        result = ""
        i = 0
        while i < len(decoded):
            if decoded[i] == 'u' and i + 1 < len(decoded) and decoded[i + 1].isalpha():
                result += decoded[i + 1].upper()
                i += 2
            else:
                result += decoded[i]
                i += 1

        return result

    def _find_markers(self, text: str) -> List[Tuple[int, int, str]]:
        """Find all list markers in text.

        Returns:
            List of (start_pos, end_pos, marker_text) tuples
        """
        markers = []

        # Patterns to match list markers
        patterns = [
            # 1.) style: number + period + paren (must be followed by space)
            r'(\d{1,3}\.\))(?=\s)',

            # 1) style: number + paren (no period)
            r'(?:^|(?<=\s))(\d{1,3}\))(?=\s)',

            # 1.1. style: nested numbering
            r'(?:^|(?<=\s))(\d{1,3}\.\d{1,3}\.)(?=\s)',

            # 1. style: number + period (at start or after whitespace)
            r'(?:^|(?<=\s))(\d{1,3}\.)(?=\s)',

            # a. style: lowercase letter + period
            # Lookahead requires space + letter/bracket, NOT digit.
            # This excludes citation abbreviations like "p. 5" (page 5) or
            # "n. 3" (note 3) which look identical to list markers but are
            # followed by numbers. Real list items start with text, e.g. "a. First".
            # Related: issue #47 – p. in citations was decoded as ")." due to
            # the 'p' → ')' substitution in the ListMarkerNormalizer codec.
            r'(?:^|(?<=\s))([a-z]\.)(?=\s[a-zA-Z\(\[\{])',

            # A. style: uppercase letter + period (same digit-exclusion logic)
            r'(?:^|(?<=\s))([A-Z]\.)(?=\s[a-zA-Z\(\[\{])',

            # a) style: letter + paren
            r'(?:^|(?<=\s))([a-zA-Z]\))(?=\s)',

            # i. ii. iii. style: lowercase roman + period
            rf'(?:^|(?<=\s))({ROMAN_LOWER}\.)(?=\s)',

            # I. II. III. style: uppercase roman + period
            rf'(?:^|(?<=\s))({ROMAN_UPPER}\.)(?=\s)',

            # i) ii) style: roman + paren
            rf'(?:^|(?<=\s))({ROMAN_LOWER}\))(?=\s)',
        ]

        for pat in patterns:
            for match in re.finditer(pat, text):
                markers.append((match.start(1), match.end(1), match.group(1)))

        # Sort by position and remove duplicates
        markers = sorted(set(markers), key=lambda x: x[0])
        return markers

    def _count_markers(self, text: str) -> int:
        """Count how many list markers are in the text."""
        return len(self._find_markers(text))

    def _get_marker_type(self, marker: str) -> str:
        """Classify a marker by its type."""
        if re.match(r'\d+\.\)', marker):
            return 'num_dot_paren'
        if re.match(r'\d+\)', marker):
            return 'num_paren'
        if re.match(r'\d+\.', marker):
            return 'num_dot'
        if re.match(r'\d+\.\d+\.', marker):
            return 'nested'
        if re.match(r'[a-z]\.', marker):
            return 'alpha_lower_dot'
        if re.match(r'[A-Z]\.', marker):
            return 'alpha_upper_dot'
        if re.match(r'[a-zA-Z]\)', marker):
            return 'alpha_paren'
        if re.match(rf'{ROMAN_LOWER}\)', marker):
            return 'roman_lower_paren'
        if re.match(rf'{ROMAN_LOWER}\.', marker):
            return 'roman_lower_dot'
        if re.match(rf'{ROMAN_UPPER}\.', marker):
            return 'roman_upper_dot'
        return 'other'

    def _normalize(self, text: str) -> str:
        """Replace list markers with word-like placeholders.

        Only normalizes if the text appears to contain a real list (2+ markers of same type).
        """
        # Only normalize if we have multiple markers (looks like a list)
        if self._count_markers(text) < 2:
            return text

        markers = self._find_markers(text)
        if not markers:
            return text

        # Check if markers are of consistent type
        # Don't normalize if markers are mixed types (e.g., "p." and "10)" are different)
        marker_types = [self._get_marker_type(m[2]) for m in markers]
        type_counts = {}
        for t in marker_types:
            type_counts[t] = type_counts.get(t, 0) + 1

        # Need at least 2 markers of the same type
        max_same_type = max(type_counts.values()) if type_counts else 0
        if max_same_type < 2:
            return text

        # Replace from end to start to preserve indices
        result = text
        for start, end, marker in reversed(markers):
            placeholder = self._marker_to_placeholder(marker)
            result = result[:start] + placeholder + result[end:]

        return result

    def _denormalize(self, text: str) -> str:
        """Restore placeholders back to original list markers."""
        # Find all placeholders in the text (now includes digits)
        pattern = re.compile(rf'{PLACEHOLDER_PREFIX}[a-z0-9]+{PLACEHOLDER_SUFFIX}')

        result = text
        for match in pattern.finditer(text):
            placeholder = match.group(0)
            original = self._placeholder_to_marker(placeholder)
            result = result.replace(placeholder, original)

        return result

    def process(self, text: str, denormalize: bool = False) -> str:
        """Normalize or denormalize list markers.

        Args:
            text: Text to process
            denormalize: If True, restore placeholders to markers.
                         If False, replace markers with placeholders.

        Returns:
            Processed text with markers normalized or restored.
        """
        if denormalize:
            return self._denormalize(text)
        return self._normalize(text)
