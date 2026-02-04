#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Normalize Ellipses to prevent them being stripped by cleanup routines.

This module handles all ellipsis patterns:
- Spaced ellipsis: . . .
- Spaced four-dot: . . . . (ellipsis + sentence boundary)
- Unspaced four-dot: .... (ellipsis + sentence boundary)
- Unspaced three-dot: ...
- Unicode ellipsis: …
- Bracketed ellipsis: [...]

Reference:
    GitHub Issue #3 - Original ellipsis handling
    GitHub Issue #19 - Comprehensive ellipsis patterns (Golden Rules 43-48)
"""

import re
from fast_sentence_segment.core import BaseObject


# Unique placeholders that won't be affected by spacing normalization
# Using lowercase alphabetic tokens - spaCy treats ALL-CAPS as sentence endings!
PLACEHOLDER_SPACED_FOUR = "xellipsisfourspacedx"
PLACEHOLDER_SPACED_THREE = "xellipsisthreespacedx"
PLACEHOLDER_FOUR = "xellipsisfourx"
PLACEHOLDER_THREE = "xellipsisthreex"
PLACEHOLDER_UNICODE = "xellipsisunicodex"
PLACEHOLDER_UNICODE_PERIOD = "xellipsisunicodeperiodx"  # …. pattern
PLACEHOLDER_BRACKET = "xellipsisbracketx"

# For backward compatibility
PLACEHOLDER = PLACEHOLDER_THREE

# Patterns ordered by specificity (longest/most specific first)
# Spaced four-dot: . . . . (with sentence boundary after)
# IMPORTANT: Require whitespace before first dot to avoid consuming
# a sentence-ending period. "compounds. . . . The" should be treated as
# "compounds." (sentence end) + ". . ." (ellipsis), NOT as ". . . ." (four-dot).
# Related: Golden Rule 48
SPACED_FOUR_DOT = re.compile(r'(?<=\s)\. \. \. \.(?=\s|$)')
# Spaced three-dot: . . .
# IMPORTANT: Must NOT match when preceded by a word character (letter/digit).
# "compounds. . . . The" should NOT match the first dot as part of ellipsis.
# The pattern (?<!\w) ensures we don't start matching after a word character.
# However, we DO want to match after punctuation or whitespace.
# Related: Golden Rule 48
SPACED_THREE_DOT = re.compile(r'(?<![a-zA-Z0-9])\. \. \.')
# Bracketed ellipsis: [...]
BRACKET_ELLIPSIS = re.compile(r'\[\.\.\.\]')
# Five or more dots (treat as four-dot boundary)
FIVE_PLUS_DOTS = re.compile(r'\.{5,}')
# Four dots: ....
FOUR_DOT = re.compile(r'\.{4}')
# Three dots: ...
THREE_DOT = re.compile(r'\.{3}')
# Unicode ellipsis + period: …. (sentence boundary, like ....)
UNICODE_ELLIPSIS_PERIOD = re.compile(r'…\.')
# Unicode ellipsis: …
UNICODE_ELLIPSIS = re.compile(r'…')


class EllipsisNormalizer(BaseObject):
    """Normalize Ellipses to prevent them being stripped by cleanup routines.

    Handles three-dot, four-dot, spaced, and unicode ellipsis patterns.
    Four-dot patterns indicate sentence boundaries (ellipsis + period).
    Three-dot patterns indicate continuation (no sentence boundary).
    """

    def __init__(self):
        """
        Created:
            27-Dec-2024
            craigtrim@gmail.com
            *   preserve ellipses through the pipeline
                https://github.com/craigtrim/fast-sentence-segment/issues/3
        Updated:
            03-Feb-2026
            craigtrim@gmail.com
            *   comprehensive ellipsis handling for Golden Rules compliance
                https://github.com/craigtrim/fast-sentence-segment/issues/19
        """
        BaseObject.__init__(self, __name__)

    def _normalize(self, input_text: str) -> str:
        """Replace ellipsis patterns with placeholders.

        Order matters: process longer/more specific patterns first.

        Four-dot patterns (spaced or unspaced) are sentence boundaries.
        Three-dot patterns are continuations (unless followed by capital).
        """
        # Bracketed ellipsis [...] - protect entirely
        input_text = BRACKET_ELLIPSIS.sub(PLACEHOLDER_BRACKET, input_text)

        # Spaced four-dot followed by space and capital: . . . . Capital
        # → marks sentence boundary (add period for spaCy to split on)
        # IMPORTANT: Require whitespace before first dot to avoid consuming
        # sentence-ending period. See SPACED_FOUR_DOT comment.
        # Related: Golden Rule 48
        spaced_four_boundary = re.compile(r'(?<=\s)\. \. \. \.(\s+)([A-Z])')
        input_text = spaced_four_boundary.sub(
            PLACEHOLDER_SPACED_FOUR + r'.\1\2',
            input_text
        )

        # Remaining spaced four-dot: . . . .
        input_text = SPACED_FOUR_DOT.sub(PLACEHOLDER_SPACED_FOUR, input_text)

        # Spaced three-dot: . . . → placeholder (continuation)
        input_text = SPACED_THREE_DOT.sub(PLACEHOLDER_SPACED_THREE, input_text)

        # Five or more dots followed by space and capital → boundary
        five_plus_boundary = re.compile(r'\.{5,}(\s+)([A-Z])')
        input_text = five_plus_boundary.sub(
            PLACEHOLDER_FOUR + r'.\1\2',
            input_text
        )
        # Remaining five or more dots
        input_text = FIVE_PLUS_DOTS.sub(PLACEHOLDER_FOUR, input_text)

        # Four dots followed by space and capital: .... Capital → boundary
        four_dot_boundary = re.compile(r'\.{4}(\s+)([A-Z])')
        input_text = four_dot_boundary.sub(
            PLACEHOLDER_FOUR + r'.\1\2',
            input_text
        )
        # Remaining four dots
        input_text = FOUR_DOT.sub(PLACEHOLDER_FOUR, input_text)

        # Unicode ellipsis + period: …. → treat as four-dot (sentence boundary)
        # Must be processed BEFORE regular unicode ellipsis
        unicode_period_boundary = re.compile(r'…\.(\s+)([A-Z])')
        input_text = unicode_period_boundary.sub(
            PLACEHOLDER_UNICODE_PERIOD + r'.\1\2',
            input_text
        )
        input_text = UNICODE_ELLIPSIS_PERIOD.sub(PLACEHOLDER_UNICODE_PERIOD, input_text)

        # Unicode ellipsis followed by space and capital: … Capital → boundary
        # EXCEPT: "I" as pronoun is NOT a new sentence (common in dialogue: "I… I can't")
        # The [A-HJ-Z] pattern excludes capital I to avoid false splits
        # Reference: https://github.com/craigtrim/fast-sentence-segment/issues/22
        unicode_boundary = re.compile(r'…(\s+)([A-HJ-Z])')  # Excludes I
        input_text = unicode_boundary.sub(
            PLACEHOLDER_UNICODE + r'.\1\2',
            input_text
        )
        # Unicode ellipsis: … → placeholder (continuation)
        input_text = UNICODE_ELLIPSIS.sub(PLACEHOLDER_UNICODE, input_text)

        # Three dots: ... → always treat as continuation (no sentence boundary)
        # Unlike four-dots, three-dots don't include the terminal period
        # Sentence boundary after ... should be determined by spaCy, not us
        input_text = THREE_DOT.sub(PLACEHOLDER_THREE, input_text)

        return input_text

    def _denormalize(self, input_text: str) -> str:
        """Restore placeholders back to original ellipsis patterns.

        For patterns where we added a period for boundary detection,
        we need to remove it since the original pattern already includes
        the terminal punctuation.
        """
        # Spaced four-dot with added period → just spaced four-dot
        input_text = input_text.replace(PLACEHOLDER_SPACED_FOUR + '.', '. . . .')
        # Spaced four-dot (no added period)
        input_text = input_text.replace(PLACEHOLDER_SPACED_FOUR, '. . . .')

        # Spaced three-dot (continuation)
        input_text = input_text.replace(PLACEHOLDER_SPACED_THREE, '. . .')

        # Four-dot with added period → just four-dot
        input_text = input_text.replace(PLACEHOLDER_FOUR + '.', '....')
        # Four-dot (no added period)
        input_text = input_text.replace(PLACEHOLDER_FOUR, '....')

        # Unicode ellipsis + period with added period → just unicode ellipsis + period
        input_text = input_text.replace(PLACEHOLDER_UNICODE_PERIOD + '.', '….')
        # Unicode ellipsis + period (no added period)
        input_text = input_text.replace(PLACEHOLDER_UNICODE_PERIOD, '….')

        # Unicode ellipsis with added period → just unicode ellipsis
        input_text = input_text.replace(PLACEHOLDER_UNICODE + '.', '…')
        # Unicode ellipsis (no added period)
        input_text = input_text.replace(PLACEHOLDER_UNICODE, '…')

        # Bracketed ellipsis
        input_text = input_text.replace(PLACEHOLDER_BRACKET, '[...]')

        # Three-dot with added period for boundary → just ellipsis
        input_text = input_text.replace(PLACEHOLDER_THREE + '.', '...')

        # Three-dot (continuation)
        input_text = input_text.replace(PLACEHOLDER_THREE, '...')

        return input_text

    def process(self,
                input_text: str,
                denormalize: bool = False) -> str:
        """Normalize or denormalize ellipsis patterns.

        Args:
            input_text: Text to process
            denormalize: If True, restore placeholders to ellipses.
                         If False, replace ellipses with placeholders.

        Returns:
            Processed text with ellipses normalized or restored.
        """
        if denormalize:
            return self._denormalize(input_text)
        return self._normalize(input_text)
