#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Normalize URLs to prevent periods from being appended at sentence boundaries.

URLs at the end of sentences were having periods incorrectly appended to them,
breaking the URL format. This normalizer detects URLs and replaces them with
placeholders during segmentation, then restores them afterward.

Examples:
    "Visit https://example.com" → stays as "Visit https://example.com"
    NOT "Visit https://example.com."

The normalizer uses a placeholder approach:
    1. Find all URLs in the text
    2. Replace each with a placeholder (xurl1x, xurl2x, etc.)
    3. Run segmentation on the placeholder text
    4. Restore the original URLs from placeholders

Related GitHub Issues:
    #32 - URLs incorrectly get periods appended at end
    https://github.com/craigtrim/fast-sentence-segment/issues/32
"""

import re
from typing import Dict

from fast_sentence_segment.core import BaseObject


# URL pattern that matches common URL schemes
# Matches two categories:
# 1. Standard URLs with ://
#    - http://, https://, ftp://, ftps://, ws://, wss://, file://
# 2. Special schemes with just :
#    - mailto:, tel:
#
# Captures the full URL including:
# - Scheme (http, https, mailto, tel, etc.)
# - Optional username:password@
# - Domain/IP (including subdomains, IPv4, IPv6 in brackets)
# - Optional port
# - Optional path
# - Optional query parameters
# - Optional fragment
#
# The pattern is designed to be permissive rather than strict, capturing
# URLs as they appear in real-world text while avoiding false positives.
#
# Pattern breakdown:
# - (?:...|...) - non-capturing group with two alternatives
# - First alternative: standard URLs with ://
#   - (?:https?|ftps?|wss?|file)://[^\s,;)\]}>]+
# - Second alternative: special schemes without ://
#   - (?:mailto|tel):[^\s,;)\]}>]+
#
# Character exclusions [^\s,;)\]}>]+:
# - \s: whitespace (end of URL)
# - ,;: separators (often after URLs in lists)
# - )\]}: closing brackets/parens (URLs in parentheses)
# - >: end of HTML/markdown links
#
# Note: The pattern may capture trailing periods. We handle this in _normalize()
# by checking if a captured URL ends with a period followed by whitespace/EOL
# (indicating a sentence boundary) and excluding that period from the URL.
#
# Related GitHub Issue:
#     #32 - URLs incorrectly get periods appended at end
#     https://github.com/craigtrim/fast-sentence-segment/issues/32
URL_PATTERN = re.compile(
    r'(?:(?:https?|ftps?|wss?|file)://[^\s,;)\]}>]+|(?:mailto|tel):[^\s,;)\]}>]+)',
    re.IGNORECASE
)


class UrlNormalizer(BaseObject):
    """Normalize URLs to prevent sentence-ending periods from being appended.

    Uses a placeholder approach:
    1. Normalize: Replace URLs with placeholders (xurl1x, xurl2x, ...)
    2. Segment: Run sentence segmentation on placeholder text
    3. Denormalize: Restore original URLs from placeholders

    Example:
        Input:  "Visit https://example.com"
        Norm:   "Visit xurl1x"
        After:  "Visit https://example.com"
    """

    def __init__(self):
        """
        Created:
            10-Feb-2026
            craigtrim@gmail.com
        Reference:
            https://github.com/craigtrim/fast-sentence-segment/issues/32
        """
        BaseObject.__init__(self, __name__)
        # Instance-level storage for URL mappings
        # Key: placeholder (e.g., "xurl1x")
        # Value: original URL
        self._url_map: Dict[str, str] = {}

    def _normalize(self, text: str) -> str:
        """Replace URLs with placeholders.

        Finds all URLs in the text and replaces them with numbered
        placeholders. Stores the mapping for later restoration.

        Special handling for trailing periods:
        - If a URL match ends with a period followed by whitespace/EOL,
          we treat that period as sentence punctuation, not part of the URL
        - E.g., "Visit https://example.com. Next" → "Visit xurl1x. Next"
          (preserves the sentence-boundary period)

        Args:
            text: Input text that may contain URLs

        Returns:
            Text with URLs replaced by placeholders (xurl1x, xurl2x, ...).
        """
        # Clear any previous mappings
        self._url_map.clear()

        # Find all URLs and replace with placeholders
        url_counter = 1

        def replace_url(match):
            nonlocal url_counter
            url = match.group(0)

            # Check if URL ends with period followed by whitespace/end
            # This indicates the period is sentence punctuation, not part of the URL
            match_end = match.end()
            if url.endswith('.') and (match_end >= len(text) or text[match_end:match_end+1].isspace()):
                # Strip the trailing period from the URL
                url = url[:-1]
                # The period will remain in the text after replacement
                placeholder = f"xurl{url_counter}x"
                self._url_map[placeholder] = url
                url_counter += 1
                return f"{placeholder}."

            # Normal case: no trailing period issue
            placeholder = f"xurl{url_counter}x"
            self._url_map[placeholder] = url
            url_counter += 1
            return placeholder

        return URL_PATTERN.sub(replace_url, text)

    def _denormalize(self, text: str) -> str:
        """Restore placeholders back to original URLs.

        Args:
            text: Text with URL placeholders

        Returns:
            Text with original URLs restored.
        """
        # Replace all placeholders with their original URLs
        result = text
        for placeholder, original_url in self._url_map.items():
            result = result.replace(placeholder, original_url)
        return result

    def process(self, text: str, denormalize: bool = False) -> str:
        """Normalize or denormalize URLs.

        Args:
            text: Text to process
            denormalize: If True, restore placeholders to URLs.
                         If False, replace URLs with placeholders.

        Returns:
            Processed text.
        """
        if denormalize:
            return self._denormalize(text)
        return self._normalize(text)
