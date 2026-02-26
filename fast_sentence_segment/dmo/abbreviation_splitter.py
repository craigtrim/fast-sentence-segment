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

# Compound abbreviations where a SENTENCE_ENDING_ABBREVIATION appears as the
# second word.  The key is the abbreviation (lowercase), the value is the set
# of words that immediately precede it to form a recognized compound.
# Example: "in ext." (in extenso) — ext. is in SENTENCE_ENDING_ABBREVIATIONS
# but when preceded by "in" it forms a compound Latin abbreviation and must
# not trigger a sentence split.
_COMPOUND_SECOND_WORDS: dict = {
    "ext.": {"in"},
}

# Entity-suffix abbreviations that only end sentences when they appear
# after a company name (i.e., preceded by a proper noun).  When preceded
# by a preposition, article, or appearing at sentence-initial position,
# they are used as reference abbreviations and must NOT trigger a split.
#
# Examples that SHOULD split:
#   "Apple Inc. They are hiring."  (Inc. follows proper noun "Apple")
#   "Microsoft Corp. We use their products."
#
# Examples that should NOT split:
#   "Inc. Week 7 is referenced..."  (sentence-initial — not a sentence end)
#   "Per Inc. Smith 2024..."        (preceded by preposition "Per")
#   "consistent with Inc. Week 3." (preceded by preposition "with")
_ENTITY_SUFFIX_ABBREVS = frozenset({"Inc.", "Corp.", "Ltd.", "Co.", "Bros."})

# Measurement / reference abbreviations (approx., dept.) that appear before
# capitalized continuations in reference contexts ("approx. Week 7",
# "dept. Smith") and must NOT trigger splits in those positions.
# Unlike _ENTITY_SUFFIX_ABBREVS, these CAN follow articles at sentence end
# (e.g. "Contact the dept. Human resources will respond."), so the guard
# excludes articles (a/an/the) from the non-split set.
_MEASUREMENT_ABBREVS = frozenset({"approx.", "dept."})

# Non-split preceding words for _MEASUREMENT_ABBREVS — mirrors
# _NON_SPLIT_PRECEDING_WORDS but without "a", "an", "the" so that
# "the dept." at sentence end is still allowed to split.
_MEASUREMENT_NON_SPLIT_WORDS = frozenset({
    "and", "or", "but", "nor", "yet", "so",
    "in", "on", "at", "by", "to", "of", "for", "as", "via", "re",
    "per", "with", "from", "into", "onto", "upon", "about", "above",
    "across", "after", "against", "along", "amid", "among", "around",
    "before", "behind", "below", "beneath", "beside", "between", "beyond",
    "despite", "down", "during", "except", "inside", "near", "off",
    "outside", "over", "past", "since", "than", "throughout", "toward",
    "through", "under", "until", "unto", "up", "within", "without",
    "not", "also", "even", "only", "just", "both", "either", "neither",
    "see", "note", "specifically", "particularly", "especially",
    "including", "excluding", "containing", "covering",
})

# Words that, when immediately preceding an entity suffix abbreviation,
# indicate it is NOT ending a company name → do NOT split.
# Includes prepositions, articles, conjunctions, and other function words.
_NON_SPLIT_PRECEDING_WORDS = frozenset({
    "a", "an", "the",
    "and", "or", "but", "nor", "yet", "so",
    "in", "on", "at", "by", "to", "of", "for", "as", "via", "re",
    "per", "with", "from", "into", "onto", "upon", "about", "above",
    "across", "after", "against", "along", "amid", "among", "around",
    "before", "behind", "below", "beneath", "beside", "between", "beyond",
    "despite", "down", "during", "except", "inside", "near", "off",
    "outside", "over", "past", "since", "than", "throughout", "toward",
    "through", "under", "until", "unto", "up", "within", "without",
    "not", "also", "even", "only", "just", "both", "either", "neither",
    "see", "note", "specifically", "particularly", "especially",
    "including", "excluding", "containing", "covering",
})


# Punctuation tokens that, when they are the last "word" before an entity-suffix
# abbreviation, indicate the abbreviation is inside a parenthetical or em-dash
# phrase and must NOT trigger a sentence split.
# e.g. "Results (Inc. Week 3)..." or "The results — Inc. Week 9 — are conclusive."
_NON_SPLIT_PRECEDING_TOKENS = frozenset({
    "(", "—", "–",          # open paren, em-dash, en-dash
})

# Time abbreviations — when one of these is immediately followed by a day-of-week
# name, the day name is a continuation of the time phrase and must NOT trigger
# a split.  e.g. "The meeting is at 9 a.m. Monday." stays as one sentence.
_TIME_ABBREVS = frozenset({"a.m.", "p.m.", "A.M.", "P.M."})

# Days of the week — used together with _TIME_ABBREVS to block splits of the
# form "at 9 a.m. Monday" or "by 5 p.m. Friday".
_DAYS_OF_WEEK = frozenset({
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",
})

# Connector words that, when immediately following a day-of-week name after a
# time abbreviation, indicate a time qualifier continuation rather than the
# start of an independent clause.  e.g. "at 9 a.m. Monday and Tuesday." stays
# together, but "at 3 p.m. Saturday was busy." splits at p.m.
_TIME_QUALIFIER_CONNECTORS = frozenset({
    "and", "or", "but", "nor",
    "at", "from", "to", "through", "between",
    "morning", "afternoon", "evening",
})

# Set for O(1) lookup
_PROPER_NOUN_SET = set(COUNTRY_ABBREV_PROPER_NOUNS)

# Pattern to detect proof-ending abbreviations (q.e.d., Q.E.D.) that appear at
# the END of a sentence preceded by terminal punctuation (a period from a prior
# clause, e.g. "...implies R. q.e.d.").  These always form their own sentence.
#
# The pattern matches: <terminal-period> <whitespace> <proof-ender> <end-of-string>
# Capture group 1 = the proof-ender itself (e.g. "q.e.d.").
#
# Related GitHub Issue:
#     #47 - Abbreviations with trailing periods cause false sentence splits
#     https://github.com/craigtrim/fast-sentence-segment/issues/47
_PROOF_ENDER_PATTERN = re.compile(
    r'\.\s+(q\.e\.d\.|Q\.E\.D\.)\s*$',
    re.IGNORECASE,
)


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

    def _is_entity_abbrev_non_split(self, sentence: str, match: re.Match) -> bool:
        """Check if an entity suffix abbreviation is in a non-sentence-ending position.

        Inc., Corp., Ltd., Co., Bros. can end sentences when they follow a
        company name (e.g., "Apple Inc. They love it.").  However, they must
        NOT trigger a split when:
          - they appear at sentence-initial position (no preceding text), or
          - they are preceded by a preposition, article, or other function word
            (indicating they are used as reference abbreviations rather than
            company-name suffixes).

        Args:
            sentence: The sentence being processed
            match: The regex match object

        Returns:
            True if we should NOT split here
        """
        abbrev = match.group(1)
        if abbrev not in _ENTITY_SUFFIX_ABBREVS:
            return False  # Only applies to entity suffix abbreviations

        text_before = sentence[:match.start()].rstrip()
        if not text_before:
            return True  # Sentence-initial — cannot be ending a company name

        words = text_before.split()
        last_word = words[-1].lower() if words else ""
        if not last_word:
            return True  # No preceding word — treat as sentence-initial

        # If preceded by a known function/preposition word → don't split.
        # Also strip any leading open-paren or dash that may be attached
        # (e.g. "(see" in "The rule (see Inc. Week 7)" → stripped = "see").
        if last_word in _NON_SPLIT_PRECEDING_WORDS:
            return True
        stripped_last = last_word.lstrip("(—–")
        if stripped_last in _NON_SPLIT_PRECEDING_WORDS:
            return True

        # If preceded by an em-dash, en-dash, or open-paren → inside a parenthetical
        # phrase — do not split. e.g. "Results (Inc. Week 3)" or "— Inc. Week 9 —"
        if words[-1] in _NON_SPLIT_PRECEDING_TOKENS:
            return True

        # If preceded by a lowercase word (any word not Title-Case) → don't split
        # This catches multi-word preposition phrases like "consistent with"
        if words[-1][0].islower():
            return True

        return False  # Preceded by a capitalized proper noun → allow split

    def _is_measurement_abbrev_non_split(self, sentence: str, match: re.Match) -> bool:
        """Check if a measurement/reference abbreviation is in a non-sentence-ending position.

        approx. and dept. appear before capitalized words in reference contexts
        (e.g. "approx. Week 7", "Per dept. Smith") and must NOT split there.
        Unlike Inc./Corp./Ltd., they CAN follow articles at sentence end
        (e.g. "Contact the dept. Human resources will respond."), so articles
        are excluded from the non-split preceding-word set.

        Args:
            sentence: The sentence being processed
            match: The regex match object

        Returns:
            True if we should NOT split here
        """
        abbrev = match.group(1)
        if abbrev not in _MEASUREMENT_ABBREVS:
            return False

        text_before = sentence[:match.start()].rstrip()
        if not text_before:
            return True  # Sentence-initial → always a reference, never a sentence end

        words = text_before.split()
        last_word = words[-1].lower() if words else ""
        if last_word in _MEASUREMENT_NON_SPLIT_WORDS:
            return True
        # Strip leading paren/dash attached to the preceding word (e.g. "(approx.")
        stripped_last = last_word.lstrip("(—–")
        if stripped_last in _MEASUREMENT_NON_SPLIT_WORDS:
            return True
        # Standalone paren/dash token → inside a parenthetical phrase
        if words[-1] in _NON_SPLIT_PRECEDING_TOKENS:
            return True
        # Colon / semicolon context: when the text before ends with ":" or ";",
        # the abbreviation is introduced by a clause connector and is NOT a
        # sentence end.
        # e.g. "The rule is: approx. Week 7" → do NOT split at approx.
        # e.g. "Two sources agree; approx. Week 3..." → do NOT split at approx.
        if text_before.endswith(':') or text_before.endswith(';'):
            return True
        return False

    def _is_part_of_compound_abbrev(self, sentence: str, match: re.Match) -> bool:
        """Check if the matched abbreviation is the second word of a compound abbreviation.

        For example, "in ext." (in extenso) is a compound Latin abbreviation.
        Even though "ext." is in SENTENCE_ENDING_ABBREVIATIONS, when it is
        preceded by "in" it should not trigger a sentence split.

        Args:
            sentence: The sentence being processed
            match: The regex match object

        Returns:
            True if we should NOT split here (part of a compound abbreviation)
        """
        abbrev = match.group(1).lower()
        preceding_words = _COMPOUND_SECOND_WORDS.get(abbrev)
        if not preceding_words:
            return False

        text_before = sentence[:match.start()].rstrip()
        if not text_before:
            return False

        last_word = text_before.split()[-1].lower()
        if last_word in preceding_words:
            return True
        # Strip leading paren/dash (e.g. "(in ext." → last_word = "(in" → "in")
        return last_word.lstrip("(—–") in preceding_words

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

    def _is_time_abbrev_before_day(self, sentence: str, match: re.Match) -> bool:
        """Check if a time abbreviation is immediately followed by a day-of-week name.

        e.g. "The meeting is at 9 a.m. Monday." — 'Monday' is part of the time
        phrase, not the start of a new sentence.  Splitting here would produce
        the nonsense fragment "Monday." as a standalone sentence.

        However, if the day name is followed by an independent predicate
        (e.g. "Saturday was busy."), then the day IS the subject of a new
        sentence and a split SHOULD occur.

        Args:
            sentence: The sentence being processed
            match: The regex match object

        Returns:
            True if we should NOT split here (time abbrev + day name as qualifier)
        """
        abbrev = match.group(1)
        if abbrev not in _TIME_ABBREVS:
            return False

        # match.group(2) is the capital letter that opens the next word.
        # Extract the full next word to check against day names.
        rest = sentence[match.start(2):]
        word_match = re.match(r'([A-Za-z]+)', rest)
        if not word_match:
            return False

        next_word = word_match.group(1)
        if next_word not in _DAYS_OF_WEEK:
            return False

        # The day name is present.  Now check if it is a time qualifier
        # (day name alone or followed by a connector) or an independent clause
        # subject (day name followed by a predicate).
        # e.g. "at 9 a.m. Monday."             → qualifier → no split
        # e.g. "at 9 a.m. Monday and Tuesday." → qualifier → no split
        # e.g. "at 3 p.m. Saturday was busy."  → new sentence → split
        rest_after_day = rest[word_match.end():].strip()
        if rest_after_day and rest_after_day != '.':
            next_word_match = re.match(r'([A-Za-z]+)', rest_after_day)
            if next_word_match:
                first_word_after_day = next_word_match.group(1).lower()
                if first_word_after_day not in _TIME_QUALIFIER_CONNECTORS:
                    # Independent predicate follows — allow the split
                    return False

        return True

    def _split_sentence(self, sentence: str) -> List[str]:
        """Split a single sentence at abbreviation boundaries.

        Args:
            sentence: A sentence that may contain abbreviation boundaries

        Returns:
            List of one or more sentences
        """
        # Special case: proof-ending abbreviations (q.e.d., Q.E.D.) that appear
        # at the very end of a sentence, preceded by a sentence-terminal period.
        # e.g. "...implies R. q.e.d." → ["...implies R.", "q.e.d."]
        # spaCy does not split here because q.e.d. starts with a lowercase letter,
        # so we handle it explicitly before the main pattern loop.
        proof_match = _PROOF_ENDER_PATTERN.search(sentence)
        if proof_match:
            before = sentence[:proof_match.start() + 1].strip()  # up to and including the period
            after = sentence[proof_match.start(1):].strip()        # the proof-ender itself
            if before and after:
                # Recursively split the "before" part in case it contains other abbreviation splits
                parts = self._split_sentence(before)
                parts.append(after)
                return parts

        results = []
        remaining = sentence
        search_start = 0

        while True:
            match = self._pattern.search(remaining, search_start)
            if not match:
                if remaining.strip():
                    results.append(remaining.strip())
                break

            # Check if this is an entity-suffix abbreviation (Inc., Corp., etc.)
            # in a non-sentence-ending position (sentence-initial or after
            # a preposition/article) — do not split.
            if self._is_entity_abbrev_non_split(remaining, match):
                search_start = match.end()
                continue

            # Check if this is a measurement/reference abbreviation (approx., dept.)
            # in a non-sentence-ending position — do not split.
            if self._is_measurement_abbrev_non_split(remaining, match):
                search_start = match.end()
                continue

            # Check if this is a time abbreviation (a.m., p.m.) immediately
            # followed by a day-of-week name — time phrase, not sentence end.
            if self._is_time_abbrev_before_day(remaining, match):
                search_start = match.end()
                continue

            # Check if this abbreviation is the second word of a compound Latin
            # abbreviation (e.g., "in ext." = in extenso) — do not split.
            if self._is_part_of_compound_abbrev(remaining, match):
                search_start = match.end()
                continue

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
