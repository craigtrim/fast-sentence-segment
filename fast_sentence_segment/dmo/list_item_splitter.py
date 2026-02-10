#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Split sentences at list item boundaries.

When text contains inline lists like "1. First 2. Second 3. Third",
this component splits them into individual list items.

Reference: https://github.com/craigtrim/fast-sentence-segment/issues/18
"""

import re
from typing import List, Tuple

from fast_sentence_segment.core import BaseObject


# Bullet characters that indicate list items
# Note: Hyphen (-) is NOT included as it conflicts with phone numbers and hyphenated words
# Only use clear bullet/symbol characters
BULLET_CHARS = r'[•⁃\*‣→☐☑]'

# Extended Unicode bullet pattern for direct splitting
# These are bullets that should trigger direct list splitting (not through spaCy)
# Related: https://github.com/craigtrim/fast-sentence-segment/issues/26
UNICODE_BULLET_PATTERN = r'[•⁃◦▪▸▹●○◆◇★☆✓✔✗✘➢➤›»]'

# Roman numeral patterns (lowercase and uppercase)
ROMAN_LOWER = r'(?:i{1,3}|iv|vi{0,3}|ix|xi{0,3})'
ROMAN_UPPER = r'(?:I{1,3}|IV|VI{0,3}|IX|XI{0,3})'

# List marker patterns - these are the patterns we'll split on
# Each pattern captures the full marker including any trailing space
# Note: (?:\s+|\.?$) allows matching followed by space OR at end of string (with optional period)
LIST_PATTERNS = [
    # 1.) style - number + period + paren
    r'(\d{1,3}\.\))(?:\s+|\.?$)',

    # 1) style - number + paren (no period)
    r'(\d{1,3}\))(?:\s+|\.?$)',

    # 1. style - number + period (but not decimals like 3.14)
    # Must be preceded by whitespace or start of string to avoid matching decimals
    r'(?:^|(?<=\s))(\d{1,3}\.)(?:\s+|\.?$)',

    # 1.1. style - nested numbering
    r'(?:^|(?<=\s))(\d{1,3}\.\d{1,3}\.)(?:\s+|\.?$)',

    # a. b. c. style - lowercase letter + period
    r'(?:^|(?<=\s))([a-z]\.)(?:\s+|\.?$)',

    # A. B. C. style - uppercase letter + period
    r'(?:^|(?<=\s))([A-Z]\.)(?:\s+|\.?$)',

    # a) b) c) style - letter + paren
    r'(?:^|(?<=\s))([a-zA-Z]\))(?:\s+|\.?$)',

    # i. ii. iii. style - lowercase roman numerals
    rf'(?:^|(?<=\s))({ROMAN_LOWER}\.)(?:\s+|\.?$)',

    # I. II. III. style - uppercase roman numerals
    rf'(?:^|(?<=\s))({ROMAN_UPPER}\.)(?:\s+|\.?$)',

    # i) ii) iii) style - roman with paren
    rf'(?:^|(?<=\s))({ROMAN_LOWER}\))(?:\s+|\.?$)',

    # Bullet characters (•, -, *, etc.)
    rf'({BULLET_CHARS})\s*',
]

# Combine all patterns into one regex
# This pattern matches any list marker followed by content
COMBINED_PATTERN = re.compile('|'.join(LIST_PATTERNS))


class ListItemSplitter(BaseObject):
    """Split sentences containing inline lists into individual list items."""

    def __init__(self):
        """
        Created:
            03-Feb-2026
            craigtrim@gmail.com
            *   Handle inline lists as sentence boundaries
                https://github.com/craigtrim/fast-sentence-segment/issues/18
        """
        BaseObject.__init__(self, __name__)

    def _find_list_markers(self, text: str) -> List[Tuple[int, int, str]]:
        """Find all list markers in text.

        Args:
            text: Input text to search

        Returns:
            List of (start_pos, end_pos, marker) tuples
        """
        # Title keywords that precede numbered sections (Issue #30)
        # These should NOT be treated as list markers
        TITLE_KEYWORDS = {
            "Part", "Module", "Week", "Chapter", "Section",
            "Step", "Phase", "Unit", "Level", "Stage",
            # Abbreviated forms
            "Ch.", "Sec.", "Mod.", "Vol.", "Pt."
        }

        markers = []
        for match in COMBINED_PATTERN.finditer(text):
            # Get the first non-None group (the actual marker)
            marker = None
            for g in match.groups():
                if g is not None:
                    marker = g
                    break
            if marker:
                # Check if this marker is preceded by a title keyword (Issue #30)
                # e.g., "Part 2." should not be treated as a list item
                start_pos = match.start()
                if start_pos > 0:
                    # Look back to see if there's a title keyword right before this
                    text_before = text[:start_pos].strip()
                    # Check if text_before ends with a title keyword
                    is_titled_number = False
                    for keyword in TITLE_KEYWORDS:
                        if text_before.lower().endswith(keyword.lower()):
                            is_titled_number = True
                            break

                    if is_titled_number:
                        # Skip this marker - it's part of a numbered title
                        continue

                markers.append((match.start(), match.end(), marker))
        return markers

    def _is_likely_list(self, text: str, markers: List[Tuple[int, int, str]]) -> bool:
        """Determine if the markers represent a real list vs false positives.

        Args:
            text: The full text
            markers: List of found markers

        Returns:
            True if this looks like a real standalone list that should be split
        """
        if len(markers) < 2:
            return False

        # Check if this is an embedded list in a sentence
        # (connected by commas, "and", "or") - don't split these
        text_lower = text.lower()

        # Pattern: list items separated by ", N. item, and N. item"
        # e.g., "We need: 1. paper, 2. pens, and 3. folders."
        # These are inline lists within sentences - don't split
        if ', and ' in text_lower or ', or ' in text_lower:
            return False

        # Pattern: "either a. X, b. Y, or c. Z"
        if 'either ' in text_lower and ' or ' in text_lower:
            return False

        # Check if list items are separated by commas - indicates inline list, don't split
        # e.g., "a) cost, b) time, c) quality" or "1. paper, 2. pens, 3. folders"
        # Look for comma AT THE END of text between markers (right before next marker)
        for i in range(len(markers) - 1):
            between = text[markers[i][1]:markers[i + 1][0]].strip()
            # If the text between markers ends with comma, it's an inline list
            if between.endswith(','):
                return False

        # Check if list is inside parentheses - don't split
        # e.g., "The options (1. red 2. blue 3. green) are available."
        if markers:
            first_marker_start = markers[0][0]
            last_marker_end = markers[-1][1]
            # Look for opening paren before first marker
            text_before = text[:first_marker_start]
            text_after = text[last_marker_end:]
            # Check for unclosed paren before first marker
            open_paren_count = text_before.count('(') - text_before.count(')')
            if open_paren_count > 0:
                # There's an unclosed paren before the list
                # Check if there's content after the last marker (before closing paren)
                if ')' in text_after:
                    return False  # List is inside parentheses, don't split

        # Check if markers are of similar type (all numbers, all letters, all bullets)
        marker_types = []
        for _, _, marker in markers:
            if re.match(r'\d+\.?\)?', marker):
                marker_types.append('number')
            elif re.match(r'[a-z]\.?\)?', marker, re.IGNORECASE):
                marker_types.append('letter')
            elif re.match(rf'{ROMAN_LOWER}\.?\)?', marker) or re.match(rf'{ROMAN_UPPER}\.?\)?', marker):
                marker_types.append('roman')
            elif re.match(BULLET_CHARS, marker):
                marker_types.append('bullet')
            else:
                marker_types.append('other')

        # Require at least 2 markers of the same type to consider it a real list
        # This prevents false positives like "p. 10)" from being split
        if marker_types:
            most_common = max(set(marker_types), key=marker_types.count)
            same_type_count = marker_types.count(most_common)
            # Must have at least 2 markers of same type AND >50% consistency
            if same_type_count < 2:
                return False
            return same_type_count >= len(markers) * 0.5

        return True

    def _split_at_markers(self, text: str, markers: List[Tuple[int, int, str]]) -> List[str]:
        """Split text at list marker positions.

        Args:
            text: Input text
            markers: List of (start_pos, end_pos, marker) tuples

        Returns:
            List of text segments, each starting with a list marker
        """
        if not markers:
            return [text]

        results = []
        last_end = 0
        prefix_for_first = ""

        for i, (start, end, marker) in enumerate(markers):
            # For the first marker, check if there's text before it
            if i == 0:
                if start > 0:
                    prefix = text[:start].strip()
                    # If prefix ends with colon, it's an intro - attach to first item
                    # e.g., "The steps are: 1. First" -> "The steps are: 1. First"
                    if prefix.endswith(':'):
                        prefix_for_first = prefix + " "
                    elif prefix:
                        # Otherwise, treat as separate item
                        results.append(prefix)
                # Start tracking from this marker
                last_end = start
            else:
                # Add the segment from the previous marker to this one
                segment = text[last_end:start].strip()
                if segment:
                    # Add prefix to first segment if we have one
                    if prefix_for_first:
                        segment = prefix_for_first + segment
                        prefix_for_first = ""
                    results.append(segment)
                last_end = start

        # Add the final segment
        final_segment = text[last_end:].strip()
        if final_segment:
            # Add prefix to final segment if not already used
            if prefix_for_first:
                final_segment = prefix_for_first + final_segment
            results.append(final_segment)

        return results

    def _split_sentence(self, sentence: str) -> List[str]:
        """Split a single sentence at list item boundaries.

        Args:
            sentence: A sentence that may contain list items

        Returns:
            List of one or more sentences/list items
        """
        # Find all list markers
        markers = self._find_list_markers(sentence)

        # If we don't have at least 2 markers, don't split
        if not self._is_likely_list(sentence, markers):
            return [sentence]

        # Strip trailing period that was artificially added by spaCy
        # if the original list items didn't have terminal punctuation
        # BUT don't strip if it ends with an abbreviation (a.m., p.m., etc.)
        text = sentence
        if text.endswith('.') and markers:
            # Don't strip if text ends with common abbreviations
            common_abbrevs = ('a.m.', 'p.m.', 'A.M.', 'P.M.',
                              'Dr.', 'Mr.', 'Mrs.', 'Ms.', 'Jr.', 'Sr.',
                              'etc.', 'vs.', 'i.e.', 'e.g.')
            ends_with_abbrev = any(text.endswith(abbr) for abbr in common_abbrevs)
            if not ends_with_abbrev:
                # Check if the last marker's content doesn't end with punctuation
                last_marker_end = markers[-1][1]
                content_after_last_marker = text[last_marker_end:].strip()
                # If the content doesn't naturally end with terminal punctuation
                # (other than the artificially added period), strip it
                if content_after_last_marker.endswith('.'):
                    # Check if there's any other terminal punct before the final period
                    content_without_final = content_after_last_marker[:-1].rstrip()
                    if content_without_final and content_without_final[-1] not in '.?!':
                        text = text[:-1]

        # Split at marker positions
        return self._split_at_markers(text, markers)

    def _is_lone_marker(self, text: str) -> bool:
        """Check if text is just a list marker with no content.

        Examples of lone markers: "A.", "1.", "ii)", "•"
        Also handles cases where spaCy adds extra periods: "A.." -> still a lone marker

        NOTE: Single "I." and "i." are explicitly excluded because they are
        too ambiguous - "I." could be the pronoun "I" ending a sentence,
        and "i." is commonly used in text. Only treat multi-character roman
        numerals (ii., iii., iv., etc.) as list markers.
        """
        text = text.strip()
        # Handle spaCy adding trailing periods (e.g., "1.)." from "xlm1dpx.")
        # Strip trailing period if the text ends with punctuation + period
        # e.g., "1.)." -> "1.)", "A.." -> "A."
        if len(text) > 2 and text.endswith('.') and text[-2] in '.)]':
            text = text[:-1]

        # IMPORTANT: Exclude "I." and "i." - too ambiguous
        # "I." could be pronoun "I" ending a sentence
        # Only treat multi-character roman numerals as markers
        if text.lower() in ('i.', 'i)'):
            return False

        # Check against all list patterns
        patterns = [
            r'^(\d{1,3}\.\))$',      # 1.)
            r'^(\d{1,3}\))$',        # 1)
            r'^(\d{1,3}\.)$',        # 1.
            r'^([a-zA-Z]\.)$',       # a. or A.
            r'^([a-zA-Z]\))$',       # a) or A)
            rf'^({ROMAN_LOWER}\.)$', # ii. iii. etc (i. excluded above)
            rf'^({ROMAN_UPPER}\.)$', # II. III. etc (I. excluded above)
            rf'^({ROMAN_LOWER}\))$', # ii) iii) etc (i) excluded above)
            rf'^({BULLET_CHARS})$',  # bullets
        ]
        for pat in patterns:
            if re.match(pat, text):
                return True
        return False

    def _ends_with_lone_marker(self, text: str) -> bool:
        """Check if text ends with a lone marker (with possible extra period).

        Examples: "The steps are: 1.." -> True (ends with "1.." lone marker)
                  "The steps are: 1. First step" -> False (has content after marker)
                  "See Table 1)." -> False (table reference, not list marker)
                  "you and I." -> False (pronoun I, not a marker)

        NOTE: Excludes " I." and " i." at end because these are typically:
        - Pronoun "I" at end of sentence ("you and I.")
        - NOT a list marker (roman numeral i would need more context)
        Related: https://github.com/craigtrim/fast-sentence-segment/issues/25
        """
        text = text.strip()

        # IMPORTANT: Exclude " I." and " i." - these are pronouns, not markers
        # "We make a good team, you and I." should NOT be treated as ending with marker
        # Related to Golden Rule 42 and issue #25
        if re.search(r'\s[Ii]\.\.?$', text):
            return False

        # Common reference patterns that should NOT be treated as list markers
        # e.g., "Table 1", "Figure 2", "Section 3", "Appendix A"
        reference_words = r'(?:Table|Figure|Fig|Section|Appendix|Chapter|Part|Item|Step|Page|Ref|No|Number|#)'
        # Check if text ends with a reference pattern
        if re.search(rf'{reference_words}\s+\d+\)?\.?$', text, re.IGNORECASE):
            return False

        # Look for patterns at the end of the text
        # Handle possible extra period from spaCy
        patterns = [
            r'[\s:]\d{1,3}\.\)\.?$',   # ends with " 1.)." or ": 1.)"
            r'[\s:]\d{1,3}\)\.?$',     # ends with " 1)." or ": 1)"
            r'[\s:]\d{1,3}\.\.?$',     # ends with " 1.." or ": 1."
            r'[\s:][a-zA-Z]\.\.?$',    # ends with " a.." or ": A."
            r'[\s:][a-zA-Z]\)\.?$',    # ends with " a)." or ": a)"
        ]
        for pat in patterns:
            if re.search(pat, text):
                return True
        return False

    def _extract_trailing_marker(self, text: str) -> Tuple[str, str]:
        """Extract a trailing lone marker from the end of text.

        Returns (prefix_text, marker) if found, otherwise (text, "")
        """
        text = text.strip()
        # Look for trailing marker patterns
        patterns = [
            r'^(.*[\s:])((\d{1,3}\.\))\.?)$',   # "prefix: 1.)." or "prefix 1.)"
            r'^(.*[\s:])((\d{1,3}\))\.?)$',     # "prefix: 1)." or "prefix 1)"
            r'^(.*[\s:])((\d{1,3}\.)\.?)$',     # "prefix: 1.." or "prefix 1."
            r'^(.*[\s:])(([a-zA-Z]\.)\.?)$',    # "prefix: a.." or "prefix a."
            r'^(.*[\s:])(([a-zA-Z]\))\.?)$',    # "prefix: a)." or "prefix a)"
        ]
        for pat in patterns:
            match = re.match(pat, text)
            if match:
                prefix = match.group(1).rstrip()
                marker = match.group(2)
                # Clean up marker (remove extra trailing period)
                if marker.endswith('..'):
                    marker = marker[:-1]
                return (prefix, marker)
        return (text, "")

    def _merge_lone_markers(self, sentences: List[str]) -> List[str]:
        """Merge sentences that are just list markers with the next sentence.

        When spaCy incorrectly splits "A. First item" into ["A.", "First item"],
        this method merges them back together. Also handles spaCy adding extra
        periods, e.g., ["A..", "First item"] -> ["A. First item"].

        Also handles sentences that END with a lone marker:
        ["The steps are: 1..", "First step"] -> ["The steps are: 1. First step"]
        """
        if not sentences:
            return sentences

        result = []
        i = 0
        while i < len(sentences):
            current = sentences[i]

            # Case 1: Sentence is JUST a lone marker
            if self._is_lone_marker(current) and i + 1 < len(sentences):
                next_sent = sentences[i + 1]
                # Clean up the marker (remove extra periods from spaCy)
                marker = current.strip()
                # Handle patterns like "1.)." -> "1.)" or "A.." -> "A."
                if len(marker) > 2 and marker.endswith('.') and marker[-2] in '.)]':
                    marker = marker[:-1]
                merged = f"{marker} {next_sent}"
                result.append(merged)
                i += 2  # Skip the next sentence since we merged it

            # Case 2: Sentence ENDS with a lone marker (e.g., "The steps are: 1..")
            # But NOT if the prefix itself starts with a list marker
            # (that means it's "1.) First 2.)." which should be split, not merged)
            elif self._ends_with_lone_marker(current) and i + 1 < len(sentences):
                prefix, marker = self._extract_trailing_marker(current)
                next_sent = sentences[i + 1]
                # Check if prefix starts with a marker (indicating it's a list item)
                prefix_markers = self._find_list_markers(prefix)
                prefix_starts_with_marker = prefix_markers and prefix_markers[0][0] == 0
                if marker and not prefix_starts_with_marker:
                    # Merge: "The steps are:" + "1." + "First step"
                    merged = f"{prefix} {marker} {next_sent}"
                    result.append(merged)
                    i += 2
                else:
                    result.append(current)
                    i += 1
            else:
                result.append(current)
                i += 1
        return result

    def _strip_artificial_periods(self, items: List[str]) -> List[str]:
        """Strip trailing periods that were artificially added by spaCy.

        SpacyDocSegmenter adds periods to sentences without terminal punctuation.
        For list items, we detect artificial periods by looking at whether ANY
        list item lacks terminal punctuation - if so, periods on other items
        are likely artificial and should be stripped for consistency.

        Exception: Never strip periods that are part of abbreviations (a.m., p.m., etc.)
        """
        if not items:
            return items

        # Common abbreviations that shouldn't have their periods stripped
        common_abbrevs = ('a.m.', 'p.m.', 'A.M.', 'P.M.',
                          'Dr.', 'Mr.', 'Mrs.', 'Ms.', 'Jr.', 'Sr.',
                          'etc.', 'vs.', 'i.e.', 'e.g.')

        # Find list items (items that start with a marker)
        has_marker = []
        for item in items:
            item = item.strip()
            markers = self._find_list_markers(item)
            has_marker.append(markers and markers[0][0] == 0)

        marker_indices = [i for i, has in enumerate(has_marker) if has]
        if not marker_indices:
            return items

        # Check if any list item lacks terminal punctuation (excluding abbreviations)
        # If so, strip periods from all list items for consistency
        has_no_period = False
        for i in marker_indices:
            item = items[i].strip()
            # Check terminal punctuation (but abbreviations count as having punctuation)
            ends_with_punct = item.endswith(('.', '?', '!'))
            ends_with_abbrev = any(item.endswith(abbr) for abbr in common_abbrevs)
            if not ends_with_punct and not ends_with_abbrev:
                has_no_period = True
                break

        if not has_no_period:
            # All items have terminal punctuation, keep them
            return items

        # At least one item has no terminal punctuation,
        # so strip trailing periods from items that have them (except abbreviations)
        result = []
        for i, item in enumerate(items):
            item = item.strip()
            if has_marker[i] and item.endswith('.'):
                # Don't strip if it ends with an abbreviation
                ends_with_abbrev = any(item.endswith(abbr) for abbr in common_abbrevs)
                if not ends_with_abbrev:
                    # Strip the trailing period (likely artificial)
                    item = item[:-1]
            result.append(item)
        return result

    def _split_unicode_bullet_list(self, text: str) -> List[str]:
        """Split text at Unicode bullet positions.

        When text contains 2+ Unicode bullets, split directly at those positions
        rather than relying on spaCy (which may mishandle them).

        This handles patterns like:
            "• 9. First • 10. Second" → ["• 9. First", "• 10. Second"]

        Related: https://github.com/craigtrim/fast-sentence-segment/issues/26
        Golden Rules 37, 38

        Args:
            text: Input text that may contain Unicode bullets

        Returns:
            List of items split at bullet positions
        """
        # Count Unicode bullets
        bullets = re.findall(UNICODE_BULLET_PATTERN, text)
        if len(bullets) < 2:
            return [text]

        # Split at bullet positions (lookahead to keep bullet with following content)
        items = re.split(rf'(?={UNICODE_BULLET_PATTERN})', text)
        items = [item.strip() for item in items if item.strip()]
        return items

    def _has_unicode_bullet_list(self, text: str) -> bool:
        """Check if text contains a Unicode bullet list (2+ bullets).

        Args:
            text: Input text

        Returns:
            True if text has 2+ Unicode bullets (indicates inline list)
        """
        bullets = re.findall(UNICODE_BULLET_PATTERN, text)
        return len(bullets) >= 2

    def process(self, sentences: List[str]) -> List[str]:
        """Process a list of sentences, splitting at list item boundaries.

        Args:
            sentences: List of sentences from earlier processing

        Returns:
            List of sentences with list items properly split
        """
        # First pass: Handle Unicode bullet lists directly
        # This is done before merge/split iterations because Unicode bullets
        # may have been mangled by spaCy and need direct handling.
        # Related: https://github.com/craigtrim/fast-sentence-segment/issues/26
        expanded = []
        for sentence in sentences:
            if self._has_unicode_bullet_list(sentence):
                # Split directly at bullet positions
                expanded.extend(self._split_unicode_bullet_list(sentence))
            else:
                expanded.append(sentence)
        sentences = expanded

        # Iteratively merge lone markers and split until stable
        # This handles complex cases where merge creates new items that need splitting
        max_iterations = 5  # Safety limit
        for _ in range(max_iterations):
            # Merge lone markers with following sentence
            sentences = self._merge_lone_markers(sentences)

            # Split each sentence at list markers
            new_result = []
            for sentence in sentences:
                split_items = self._split_sentence(sentence)
                new_result.extend(split_items)

            # Check if we've reached stability
            if new_result == sentences:
                break
            sentences = new_result

        # Strip artificial trailing periods from list items
        result = self._strip_artificial_periods(sentences)

        return result
