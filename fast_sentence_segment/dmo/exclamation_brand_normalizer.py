#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Normalize exclamation marks in brand names to prevent false sentence splits.

spaCy and the QuestionExclamationSplitter split on "!" followed by a capital
letter. However, some brand names include "!" as part of the name:
- Yahoo! → spaCy splits "She works at Yahoo! In marketing" incorrectly

This normalizer replaces the "!" in brand names with a placeholder BEFORE
spaCy processes the text, preventing false splits.

Related GitHub Issues:
    #27 - Exclamation Mark in Company Names (Yahoo!, Yum!)
    https://github.com/craigtrim/fast-sentence-segment/issues/27

    Golden Rule 41: "She works at Yahoo! in the accounting department."
    Should NOT split at "Yahoo!"
"""

import re
from typing import List, Tuple

from fast_sentence_segment.core import BaseObject
from fast_sentence_segment.dmo.abbreviations import EXCLAMATION_COMPANY_NAMES


# Placeholder that looks like a word (spaCy won't split on it)
PLACEHOLDER_EXCLAIM = "xexclaimx"
PLACEHOLDER_QUESTION = "xqmarkx"


class ExclamationBrandNormalizer(BaseObject):
    """Normalize exclamation/question marks in brand names to prevent splits.

    Replaces "!" and "?" in known brand names with placeholders that spaCy
    treats as regular word characters. After segmentation, the placeholders
    are restored to original punctuation.

    Example:
        Normalize: "Yahoo!" → "Yahooxexclaimx"
        After segmentation: "Yahooxexclaimx" → "Yahoo!"
    """

    def __init__(self):
        """
        Created:
            04-Feb-2026
            craigtrim@gmail.com
        Reference:
            https://github.com/craigtrim/fast-sentence-segment/issues/27
        """
        BaseObject.__init__(self, __name__)
        self._patterns = self._build_patterns()

    def _build_patterns(self) -> List[Tuple[re.Pattern, str]]:
        """Build regex patterns for each brand name.

        Returns:
            List of (pattern, replacement) tuples.
            Pattern matches the brand name, replacement has placeholder.
        """
        patterns = []
        for name in EXCLAMATION_COMPANY_NAMES:
            # Create replacement with placeholder
            if '!' in name:
                replacement = name.replace('!', PLACEHOLDER_EXCLAIM)
            elif '?' in name:
                replacement = name.replace('?', PLACEHOLDER_QUESTION)
            else:
                continue

            # Pattern matches the brand name (case-insensitive)
            # Use word boundary to avoid partial matches inside other words
            pattern = re.compile(
                r'\b' + re.escape(name),
                re.IGNORECASE
            )
            patterns.append((pattern, replacement))

        return patterns

    def _normalize(self, text: str) -> str:
        """Replace brand name punctuation with placeholders.

        Args:
            text: Input text that may contain brand names with ! or ?

        Returns:
            Text with brand name punctuation replaced by placeholders.
        """
        for pattern, replacement in self._patterns:
            text = pattern.sub(replacement, text)
        return text

    def _denormalize(self, text: str) -> str:
        """Restore placeholders back to original punctuation.

        Also handles spurious periods added by SpacyDocSegmenter when the
        placeholder is at the end of a sentence. For example:
            "Jeopardyxexclaimx." → "Jeopardy!" (not "Jeopardy!.")

        The ! and ? are already terminal punctuation, so no extra period needed.

        Related: https://github.com/craigtrim/fast-sentence-segment/issues/27

        Args:
            text: Text with placeholders

        Returns:
            Text with original punctuation restored.
        """
        # Handle placeholder + spurious period (added by SpacyDocSegmenter)
        # "xexclaimx." → "!" (the ! is terminal punctuation, no extra period needed)
        text = text.replace(PLACEHOLDER_EXCLAIM + '.', '!')
        text = text.replace(PLACEHOLDER_QUESTION + '.', '?')
        # Handle regular placeholders (not at sentence end)
        text = text.replace(PLACEHOLDER_EXCLAIM, '!')
        text = text.replace(PLACEHOLDER_QUESTION, '?')
        return text

    def process(self, text: str, denormalize: bool = False) -> str:
        """Normalize or denormalize brand name punctuation.

        Args:
            text: Text to process
            denormalize: If True, restore placeholders to punctuation.
                         If False, replace punctuation with placeholders.

        Returns:
            Processed text.
        """
        if denormalize:
            return self._denormalize(text)
        return self._normalize(text)
