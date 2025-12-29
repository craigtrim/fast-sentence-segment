#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Split sentences at abbreviation boundaries.

When spaCy fails to detect a sentence boundary after an abbreviation
(e.g., "I woke at 6 a.m. It was dark."), this component splits the
sentence by detecting the pattern: abbreviation + space + Capital letter.

Reference: https://github.com/craigtrim/fast-sentence-segment/issues/3
"""

import re
from typing import List

from fast_sentence_segment.core import BaseObject
from fast_sentence_segment.dmo.abbreviations import SENTENCE_ENDING_ABBREVIATIONS


class AbbreviationSplitter(BaseObject):
    """Split sentences at abbreviation boundaries."""

    def __init__(self):
        """
        Created:
            27-Dec-2024
            craigtrim@gmail.com
        Reference:
            https://github.com/craigtrim/fast-sentence-segment/issues/3
        """
        BaseObject.__init__(self, __name__)
        self._pattern = self._build_pattern()

    def _build_pattern(self) -> re.Pattern:
        """Build regex pattern to match abbreviation + capital letter.

        Pattern matches:
        - A known sentence-ending abbreviation (escaped for regex)
        - Followed by one or more spaces
        - Followed by a capital letter (start of new sentence)

        Note: Title abbreviations (Dr., Mr., etc.) are excluded because
        they are typically followed by names, not new sentences.

        Returns:
            Compiled regex pattern
        """
        escaped_abbrevs = [re.escape(abbr) for abbr in SENTENCE_ENDING_ABBREVIATIONS]
        abbrev_pattern = "|".join(escaped_abbrevs)
        pattern = rf"({abbrev_pattern})\s+([A-Z])"
        return re.compile(pattern)

    def _split_sentence(self, sentence: str) -> List[str]:
        """Split a single sentence at abbreviation boundaries.

        Args:
            sentence: A sentence that may contain abbreviation boundaries

        Returns:
            List of one or more sentences
        """
        results = []
        remaining = sentence

        while True:
            match = self._pattern.search(remaining)
            if not match:
                if remaining.strip():
                    results.append(remaining.strip())
                break

            split_pos = match.end(1)

            before = remaining[:split_pos].strip()
            if before:
                results.append(before)

            remaining = remaining[split_pos:].strip()

        return results if results else [sentence]

    def process(self, sentences: List[str]) -> List[str]:
        """Process a list of sentences, splitting at abbreviation boundaries.

        Args:
            sentences: List of sentences from spaCy

        Returns:
            List of sentences with abbreviation boundaries properly split
        """
        result = []
        for sentence in sentences:
            split_sentences = self._split_sentence(sentence)
            result.extend(split_sentences)
        return result
