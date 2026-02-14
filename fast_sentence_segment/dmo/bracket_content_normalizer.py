#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Normalize bracketed content to prevent false sentence splits.

Square brackets [...] are used for references, citations, notes, and editorial
comments. The content inside brackets should never be split, regardless of
internal punctuation like periods, commas, or semicolons.

This normalizer protects bracketed content by replacing it with placeholders
before spaCy processes the text, then restoring it afterwards.

Examples:
    "[Fig. 1.]" → "xbracketFigdot1dotx"
    "[p. 42.]" → "xbracketpdot42dotx"

Common patterns protected:
    - Figure references: [Fig. 1.], [Figure 2.1.]
    - Page references: [p. 42.], [pp. 10-20.]
    - Citations: [Smith 2020.], [refs. 1, 2, 3.]
    - Editorial notes: [sic.], [emphasis added.]
    - See-also references: [see note 1.], [cf. Chapter 2.]

Related GitHub Issue:
    #37 - Period Before Closing Punctuation
    https://github.com/craigtrim/fast-sentence-segment/issues/37
"""

import re
import base64
from fast_sentence_segment.core import BaseObject


class BracketContentNormalizer(BaseObject):
    """Normalize bracketed content to prevent sentence splits.

    Detects patterns like "[Fig. 1.]" and replaces the entire bracketed
    content with a placeholder that spaCy won't split.

    Example:
        Input:  "The data supports this [Fig. 1.]. Analysis continued."
        Norm:   "The data supports this xbracketW0ZpZy4gMS5dxend. Analysis continued."
        After:  "The data supports this [Fig. 1.]. Analysis continued."
    """

    def __init__(self):
        """
        Created:
            13-Feb-2026
            craigtrim@gmail.com
        Reference:
            https://github.com/craigtrim/fast-sentence-segment/issues/37
        """
        BaseObject.__init__(self, __name__)

    def _encode_bracket(self, bracket_text: str) -> str:
        """Encode bracket content into a placeholder.

        Args:
            bracket_text: The full bracket text including [ and ]

        Returns:
            A placeholder that encodes the original bracket text
        """
        # Use URL-safe base64 (uses - and _ instead of + and /)
        # This avoids character replacement issues
        encoded = base64.urlsafe_b64encode(bracket_text.encode('utf-8')).decode('ascii')
        # Remove padding '=' characters
        encoded = encoded.replace('=', '')
        return f"xbracket{encoded}xend"

    def _decode_placeholder(self, placeholder: str) -> str:
        """Decode a placeholder back to original bracket text.

        Args:
            placeholder: The placeholder created by _encode_bracket

        Returns:
            The original bracket text
        """
        # Extract the encoded part between xbracket and xend
        encoded = placeholder[8:-4]  # Remove 'xbracket' prefix and 'xend' suffix
        # Add back padding if needed for base64 decoding
        while len(encoded) % 4 != 0:
            encoded += '='
        # Decode using URL-safe base64
        return base64.urlsafe_b64decode(encoded.encode('ascii')).decode('utf-8')

    def _normalize(self, text: str) -> str:
        """Replace bracketed content with placeholders.

        Args:
            text: Input text that may contain bracketed content

        Returns:
            Text with bracketed content replaced by placeholders.
        """
        def replace_bracket(match):
            """Replace a single bracketed section with a placeholder."""
            return self._encode_bracket(match.group(0))

        # Pattern: [ followed by any characters (non-greedy) followed by ]
        # Non-greedy .*? ensures we match individual brackets, not from [ to last ]
        bracket_pattern = re.compile(r'\[.*?\]')
        text = bracket_pattern.sub(replace_bracket, text)

        return text

    def _denormalize(self, text: str) -> str:
        """Restore placeholders back to original bracketed content.

        Args:
            text: Text with placeholders

        Returns:
            Text with bracketed content restored.
        """
        # Find all bracket placeholders
        placeholder_pattern = re.compile(r'xbracket[A-Za-z0-9]+xend')

        def restore_bracket(match):
            """Restore a single placeholder to its original bracket text."""
            return self._decode_placeholder(match.group(0))

        text = placeholder_pattern.sub(restore_bracket, text)
        return text

    def process(self, text: str, denormalize: bool = False) -> str:
        """Normalize or denormalize bracketed content.

        Args:
            text: Text to process
            denormalize: If True, restore placeholders to bracketed content.
                         If False, replace bracketed content with placeholders.

        Returns:
            Processed text.
        """
        if denormalize:
            return self._denormalize(text)
        return self._normalize(text)
