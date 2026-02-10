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
from fast_sentence_segment.dmo.abbreviations import SENTENCE_ENDING_ABBREVIATIONS, COUNTRY_ABBREV_PROPER_NOUNS, TITLE_ABBREVIATIONS


# Country/organization abbreviations that need special handling
COUNTRY_ABBREVIATIONS = {"U.S.", "U.K.", "U.N.", "E.U.", "U.S.A."}

# Title abbreviations that should not trigger sentence splits when they follow other abbreviations
# e.g., "a.m. Mr. Smith" should NOT split between "a.m." and "Mr."
_TITLE_ABBREV_SET = set(TITLE_ABBREVIATIONS)


# Set for O(1) lookup
_PROPER_NOUN_SET = set(COUNTRY_ABBREV_PROPER_NOUNS)


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

    def _is_country_abbrev_with_proper_noun(self, sentence: str, match: re.Match) -> bool:
        """Check if this is a country abbreviation followed by a proper noun.

        Args:
            sentence: The sentence being processed
            match: The regex match object

        Returns:
            True if this is a country abbreviation followed by a proper noun
            (indicating we should NOT split here)
        """
        abbrev = match.group(1)
        if abbrev not in COUNTRY_ABBREVIATIONS:
            return False

        # Get the word following the abbreviation
        # match.group(2) is the capital letter that starts the next word
        rest_of_sentence = sentence[match.end(1):].strip()
        if not rest_of_sentence:
            return False

        # Extract the first word after the abbreviation
        first_word_match = re.match(r'([A-Z][a-zA-Z]*)', rest_of_sentence)
        if not first_word_match:
            return False

        first_word = first_word_match.group(1)
        return first_word in _PROPER_NOUN_SET

    def _is_followed_by_another_abbreviation(self, sentence: str, match: re.Match) -> bool:
        """Check if the capital letter after this abbreviation starts another abbreviation.

        e.g., "U.S. U.S." or "U.S. U.K." - should NOT split between them.

        Args:
            sentence: The sentence being processed
            match: The regex match object

        Returns:
            True if the next word is another country abbreviation (don't split)
        """
        # Get text after the matched abbreviation
        rest_of_sentence = sentence[match.end(1):].strip()
        if not rest_of_sentence:
            return False

        # Check if the next word matches any known country abbreviation pattern
        for abbrev in COUNTRY_ABBREVIATIONS:
            if rest_of_sentence.startswith(abbrev):
                return True

        return False

    def _is_followed_by_title_abbrev(self, sentence: str, match: re.Match) -> bool:
        """Check if the abbreviation is followed by a title abbreviation at sentence start.

        e.g., "At 5 a.m. Mr. Smith went to the bank." - should NOT split
        but "He left at 6 P.M. Mr. Smith then went." - SHOULD split

        Only prevents split when:
        1. The next word is a title abbreviation (Mr., Dr., etc.)
        2. AND the abbreviation appears near the START of the sentence
           (suggesting the title is the subject of the sentence, not a new sentence)

        Args:
            sentence: The sentence being processed
            match: The regex match object

        Returns:
            True if we should NOT split here
        """
        # Get the text following the matched abbreviation
        rest_of_sentence = sentence[match.end(1):].strip()
        if not rest_of_sentence:
            return False

        # Check if the next word (including potential period) is a title abbreviation
        next_word_match = re.match(r'([A-Z][a-zA-Z]*\.?)', rest_of_sentence)
        if not next_word_match:
            return False

        next_word = next_word_match.group(1)
        if next_word not in _TITLE_ABBREV_SET:
            return False

        # Only prevent split if the abbreviation is near the start of the sentence
        # (indicating the title is the subject, not a new sentence)
        text_before = sentence[:match.start()].strip()

        # If very little text before the abbreviation (< 15 chars or just prepositional phrase),
        # likely the title is the subject - don't split
        # Examples where we DON'T split:
        #   "At 5 a.m. Mr." - text_before = "At 5"
        #   "The 9 a.m. Mr." - text_before = "The 9"
        # Examples where we DO split:
        #   "He left at 6 P.M. Mr." - text_before = "He left at 6"
        #   "The bank closed at 5 p.m. Dr." - text_before = "The bank closed at 5"

        # Heuristic: if text_before contains a verb (has more than just prep + number),
        # it's likely a complete thought and we should split
        if len(text_before) > 15:
            return False  # Enough text before - likely complete sentence, DO split

        # Check if text_before looks like just a time phrase (preposition + number)
        # e.g., "At 5", "By 9", "The 3"
        time_phrase_pattern = re.compile(r'^(?:at|by|the|around|about|until|before|after)\s+\d', re.IGNORECASE)
        if time_phrase_pattern.match(text_before):
            return True  # Just a time phrase, don't split

        return False  # Default: allow split

    def _split_sentence(self, sentence: str) -> List[str]:
        """Split a single sentence at abbreviation boundaries.

        Args:
            sentence: A sentence that may contain abbreviation boundaries

        Returns:
            List of one or more sentences
        """
        results = []
        remaining = sentence
        search_start = 0

        while True:
            match = self._pattern.search(remaining, search_start)
            if not match:
                if remaining.strip():
                    results.append(remaining.strip())
                break

            # Check if this is a country abbreviation followed by a proper noun
            if self._is_country_abbrev_with_proper_noun(remaining, match):
                # Don't split here, continue searching after this match
                search_start = match.end()
                continue

            # Check if this is followed by another abbreviation
            # e.g., "U.S. U.S." or "U.S. U.K." should not split between them
            if self._is_followed_by_another_abbreviation(remaining, match):
                search_start = match.end()
                continue

            # Check if this abbreviation is followed by a title abbreviation
            # e.g., "a.m. Mr. Smith" should not split between "a.m." and "Mr."
            if self._is_followed_by_title_abbrev(remaining, match):
                search_start = match.end()
                continue

            split_pos = match.end(1)

            before = remaining[:split_pos].strip()
            if before:
                results.append(before)

            remaining = remaining[split_pos:].strip()
            search_start = 0  # Reset search start for the new remaining string

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
