#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Normalize Unicode tokens that affect sentence boundary detection.

Some Unicode characters look like ASCII punctuation but have different code
points. spaCy may not handle these consistently, causing false sentence splits.

This normalizer handles:
1. Unicode bullets (•, ⁃, ◦, ▪, etc.) - convert to standard list markers
2. Special abbreviation symbols (N°. for numero)
3. Other Unicode punctuation that impacts segmentation

Related GitHub Issues:
    #26 - Unicode Token Normalization (Bullets, Numero Sign)
    https://github.com/craigtrim/fast-sentence-segment/issues/26

    Golden Rule 37: "• 9. The first item • 10. The second item"
    Golden Rule 38: "⁃9. The first item ⁃10. The second item"
    Golden Rule 40: "You can find it at N°. 1026.253.553."
"""

import re
from typing import Dict, List, Tuple

from fast_sentence_segment.core import BaseObject


# Unicode bullet characters that should be treated as list markers
# Maps Unicode bullet → ASCII placeholder that won't trigger false splits
UNICODE_BULLETS: Dict[str, str] = {
    '•': 'xbulletx',      # U+2022 BULLET (most common)
    '⁃': 'xhyphenbulletx', # U+2043 HYPHEN BULLET
    '◦': 'xwhitebulletx', # U+25E6 WHITE BULLET
    '▪': 'xblacksqx',     # U+25AA BLACK SMALL SQUARE
    '▸': 'xtriangleRx',   # U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE
    '▹': 'xtriangleWx',   # U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE
    '●': 'xblackcirclex', # U+25CF BLACK CIRCLE
    '○': 'xwhitecirclex', # U+25CB WHITE CIRCLE
    '◆': 'xblackdiamondx',# U+25C6 BLACK DIAMOND
    '◇': 'xwhitediamondx',# U+25C7 WHITE DIAMOND
    '★': 'xblackstarx',   # U+2605 BLACK STAR
    '☆': 'xwhitestarx',   # U+2606 WHITE STAR
    '✓': 'xcheckx',       # U+2713 CHECK MARK
    '✔': 'xheavycheckx',  # U+2714 HEAVY CHECK MARK
    '✗': 'xballotxx',     # U+2717 BALLOT X
    '✘': 'xheavyballotxx',# U+2718 HEAVY BALLOT X
    '➢': 'xarrowheadx',   # U+27A2 THREE-D TOP-LIGHTED RIGHTWARDS ARROWHEAD
    '➤': 'xpointerx',     # U+27A4 BLACK RIGHTWARDS ARROWHEAD
    '›': 'xsingleguilx',  # U+203A SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
    '»': 'xdoubleguilx',  # U+00BB RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    '—': 'xemdashx',      # U+2014 EM DASH (when used as bullet)
    '–': 'xendashx',      # U+2013 EN DASH (when used as bullet)
}

# Special abbreviation patterns with Unicode characters
# N°. (numero sign) should not trigger a split at the period
# Pattern matches "N°." followed by space and digit
NUMERO_PATTERN = re.compile(r'N°\.(\s+)(\d)')
NUMERO_PLACEHOLDER = 'xnumerox'


class UnicodeTokenNormalizer(BaseObject):
    """Normalize Unicode tokens that affect sentence boundary detection.

    Handles Unicode bullets, special abbreviation symbols, and other
    characters that may cause incorrect sentence splits.

    Example bullets:
        Input:  "• First item • Second item"
        Norm:   "xbulletx First item xbulletx Second item"
        After:  "• First item" / "• Second item"

    Example numero:
        Input:  "N°. 1026.253.553"
        Norm:   "xnumerox1026.253.553"
        After:  "N°. 1026.253.553"
    """

    def __init__(self):
        """
        Created:
            04-Feb-2026
            craigtrim@gmail.com
        Reference:
            https://github.com/craigtrim/fast-sentence-segment/issues/26
        """
        BaseObject.__init__(self, __name__)

    def _normalize_bullets(self, text: str) -> str:
        """Replace Unicode bullets with ASCII placeholders.

        Args:
            text: Input text with Unicode bullets

        Returns:
            Text with bullets replaced by placeholders.
        """
        for bullet, placeholder in UNICODE_BULLETS.items():
            text = text.replace(bullet, placeholder)
        return text

    def _denormalize_bullets(self, text: str) -> str:
        """Restore ASCII placeholders back to Unicode bullets.

        Args:
            text: Text with placeholders

        Returns:
            Text with Unicode bullets restored.
        """
        for bullet, placeholder in UNICODE_BULLETS.items():
            text = text.replace(placeholder, bullet)
        return text

    def _normalize_numero(self, text: str) -> str:
        """Protect N°. pattern from false splits.

        "N°." is an abbreviation for "numero" (number). The period should
        not trigger a sentence split.

        Args:
            text: Input text that may contain N°.

        Returns:
            Text with N°. protected.
        """
        # Replace "N°. " with placeholder
        text = NUMERO_PATTERN.sub(rf'{NUMERO_PLACEHOLDER}\1\2', text)
        # Also handle "N°." at end of sentence or without following digit
        text = text.replace('N°.', NUMERO_PLACEHOLDER)
        return text

    def _denormalize_numero(self, text: str) -> str:
        """Restore N°. from placeholder.

        Args:
            text: Text with numero placeholder

        Returns:
            Text with N°. restored.
        """
        return text.replace(NUMERO_PLACEHOLDER, 'N°.')

    def _normalize(self, text: str) -> str:
        """Normalize all Unicode tokens.

        NOTE (2026-02-04): Unicode bullets are NOT normalized here.
        Normalizing bullets to placeholders causes issues with spaCy's
        sentence boundary detection. Instead, bullets are handled directly
        by ListItemSplitter which splits at bullet positions.

        Related: https://github.com/craigtrim/fast-sentence-segment/issues/26
        Golden Rules 37, 38

        Args:
            text: Input text

        Returns:
            Text with Unicode tokens normalized.
        """
        # NOTE: Bullets are NOT normalized - see docstring above
        # text = self._normalize_bullets(text)
        text = self._normalize_numero(text)
        return text

    def _denormalize(self, text: str) -> str:
        """Restore all Unicode tokens from placeholders.

        NOTE: Bullets are not normalized/denormalized - see _normalize docstring.

        Args:
            text: Text with placeholders

        Returns:
            Text with Unicode tokens restored.
        """
        # NOTE: Bullets are NOT denormalized - they weren't normalized
        # text = self._denormalize_bullets(text)
        text = self._denormalize_numero(text)
        return text

    def process(self, text: str, denormalize: bool = False) -> str:
        """Normalize or denormalize Unicode tokens.

        Args:
            text: Text to process
            denormalize: If True, restore placeholders to Unicode.
                         If False, replace Unicode with placeholders.

        Returns:
            Processed text.
        """
        if denormalize:
            return self._denormalize(text)
        return self._normalize(text)
