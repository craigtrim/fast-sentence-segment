# -*- coding: UTF-8 -*-
"""Unwrap hard-wrapped text (e.g., Project Gutenberg e-texts).

Joins lines within paragraphs into continuous strings while
preserving paragraph boundaries (blank lines). Also dehyphenates
words that were split across lines for typesetting.

Related GitHub Issues:
    #8 - Add dehyphenation support for words split across lines
    https://github.com/craigtrim/fast-sentence-segment/issues/8

    #12 - Unwrap fails when hard-wrap splits across blank line
    https://github.com/craigtrim/fast-sentence-segment/issues/12

    #14 - Make unwrap quote-aware to join text across blank lines inside open quotes
    https://github.com/craigtrim/fast-sentence-segment/issues/14
"""

import re

from fast_sentence_segment.dmo.quote_utils import (
    KNOWN_ELISION_WORDS,
    is_elision as _is_elision_impl,
    count_quotes as _count_quotes_impl,
)

# Quote characters to track for dialog detection.
# unwrap_hard_wrapped_text runs BEFORE normalize_quotes() in the pipeline,
# so it must recognize both ASCII and Unicode quote variants directly.
#
# Related GitHub Issue:
#     #29 - Augment single-quote normalization with missing Unicode characters
#     https://github.com/craigtrim/fast-sentence-segment/issues/29
DOUBLE_QUOTES = '"""\u201c\u201d'  # " " " " "
SINGLE_QUOTES = (
    "'''"           # ASCII straight quotes
    "\u2018\u2019"  # LEFT/RIGHT SINGLE QUOTATION MARK
    "\u201a\u201b"  # SINGLE LOW-9 / HIGH-REVERSED-9
    "\u2039\u203a"  # SINGLE ANGLE QUOTES
    "\u2032\u2035"  # PRIME / REVERSED PRIME
    "\uff07"        # FULLWIDTH APOSTROPHE
    "\u0060\u00b4"  # GRAVE ACCENT / ACUTE ACCENT
    "\u02b9\u02bc"  # MODIFIER LETTER PRIME / APOSTROPHE
    "\u02c8"        # MODIFIER LETTER VERTICAL LINE
    "\u055a"        # ARMENIAN APOSTROPHE
    "\u05f3"        # HEBREW GERESH
    "\u07f4\u07f5"  # NKO APOSTROPHES
    "\u1fbf\u1fbd"  # GREEK PSILI / KORONIS
    "\ua78c"        # LATIN SALTILLO
)
ALL_QUOTES = DOUBLE_QUOTES + SINGLE_QUOTES

# Pattern to match hyphenated word breaks at end of line:
# - A single hyphen (not -- em-dash)
# - Followed by newline and optional whitespace
# - Followed by a lowercase letter (continuation of word)
_HYPHEN_LINE_BREAK_PATTERN = re.compile(r'(?<!-)-\n\s*([a-z])')


def _is_elision(text: str, pos: int) -> bool:
    """Check if apostrophe at position is a word-initial elision.

    Delegates to shared implementation in quote_utils.

    Args:
        text: The full text.
        pos: Position of the apostrophe character.

    Returns:
        True if this appears to be an elision, not a dialog quote.
    """
    return _is_elision_impl(text, pos)


def _count_quotes(text: str) -> int:
    """Count actual quote characters in text, excluding apostrophes.

    Delegates to shared implementation in quote_utils.
    Uses this module's ALL_QUOTES and SINGLE_QUOTES constants
    (which include Unicode variants for the pre-normalization path).
    """
    return _count_quotes_impl(text, ALL_QUOTES, SINGLE_QUOTES)


def _is_inside_open_quote(text: str) -> bool:
    """Check if text ends with an unclosed quote.

    Counts quote characters (excluding apostrophes) and returns True
    if the count is odd, meaning there's an open quote.

    Args:
        text: The text to check.

    Returns:
        True if there's an unclosed quote at the end of text.
    """
    return _count_quotes(text) % 2 == 1

# Characters that indicate end of sentence
_SENTENCE_END_PUNCT = {'.', '?', '!'}


def _ends_with_sentence_punct(text: str) -> bool:
    """Check if text ends with sentence-ending punctuation.

    Handles trailing quotes/parens: 'He said "Hello."' -> True
    Handles ellipsis: 'He wondered...' -> True

    Args:
        text: The text to check.

    Returns:
        True if text ends with . ? ! or ... (possibly followed by quotes/parens).
    """
    if not text:
        return False

    # Strip trailing whitespace and quotes/parens (including curly quotes)
    stripped = text.rstrip()
    trailing_chars = {'"', "'", ')', ']', '\u201d', '\u2019'}  # " ' ) ] " '
    while stripped and stripped[-1] in trailing_chars:
        stripped = stripped[:-1]

    if not stripped:
        return False

    return stripped[-1] in _SENTENCE_END_PUNCT


def _dehyphenate_block(block: str) -> str:
    """Remove hyphens from words split across lines.

    Detects the pattern of a word fragment ending with a hyphen
    at the end of a line, followed by the word continuation
    starting with a lowercase letter on the next line.

    Examples:
        "bot-\\ntle" -> "bottle"
        "cham-\\n    bermaid" -> "chambermaid"

    Args:
        block: A paragraph block that may contain hyphenated line breaks.

    Returns:
        The block with hyphenated word breaks rejoined.
    """
    return _HYPHEN_LINE_BREAK_PATTERN.sub(r'\1', block)


def unwrap_hard_wrapped_text(text: str) -> str:
    """Unwrap hard-wrapped paragraphs into continuous lines.

    Splits on blank lines to identify paragraphs, then joins
    lines within each paragraph into a single string with
    single spaces. Also dehyphenates words that were split
    across lines for typesetting purposes.

    Special handling for spurious blank lines (issue #12):
    When a single blank line appears mid-sentence (previous line
    doesn't end with .?! and next line starts lowercase), the
    text is joined rather than treated as a paragraph break.

    Quote-aware joining (issue #14):
    When we're inside an open quote (odd number of quote characters),
    join across blank lines even if the previous line ends with
    sentence punctuation and the next starts uppercase. This keeps
    multi-sentence dialog together.

    Examples:
        >>> unwrap_hard_wrapped_text("a bot-\\ntle of wine")
        'a bottle of wine'
        >>> unwrap_hard_wrapped_text("line one\\nline two")
        'line one line two'
        >>> unwrap_hard_wrapped_text("His colour\\n\\nmounted;")
        'His colour mounted;'
        >>> unwrap_hard_wrapped_text("'First.\\n\\nSecond.'")
        "'First. Second.'"

    Args:
        text: Raw text with hard-wrapped lines.

    Returns:
        Text with paragraphs unwrapped into continuous strings,
        separated by double newlines, with hyphenated words rejoined.
    """
    lines = text.splitlines()
    paragraphs: list[list[str]] = []
    current_para_lines: list[str] = []
    blank_line_count = 0

    for line in lines:
        stripped = line.strip()

        if not stripped:
            # Blank line (or whitespace-only)
            blank_line_count += 1
        else:
            # Non-blank line
            if current_para_lines and blank_line_count > 0:
                # We have previous content and saw blank line(s)
                # Build the current paragraph text to check ending
                prev_para = ' '.join(ln.strip() for ln in current_para_lines if ln.strip())

                # Issue #12: Join across single blank line if:
                # 1. Exactly one blank line
                # 2. Previous paragraph doesn't end with sentence punctuation
                # 3. Current line starts with lowercase
                issue_12_join = (
                    blank_line_count == 1
                    and prev_para
                    and not _ends_with_sentence_punct(prev_para)
                    and stripped[0].islower()
                )

                # Issue #14: Join across blank line if inside open quote
                # Even if previous ends with sentence punct and next starts uppercase,
                # we should join if we're inside an unclosed quote
                issue_14_join = (
                    blank_line_count == 1
                    and prev_para
                    and _is_inside_open_quote(prev_para)
                )

                should_join = issue_12_join or issue_14_join

                if should_join:
                    # Treat as continuation of current paragraph
                    current_para_lines.append(line)
                else:
                    # Finish current paragraph, start new one
                    paragraphs.append(current_para_lines)
                    current_para_lines = [line]
            else:
                # No blank lines seen, add to current paragraph
                current_para_lines.append(line)

            blank_line_count = 0

    # Don't forget the last paragraph
    if current_para_lines:
        paragraphs.append(current_para_lines)

    # Process each paragraph: dehyphenate and join lines
    unwrapped = []
    for para_lines in paragraphs:
        block = '\n'.join(para_lines)
        # First, dehyphenate words split across lines
        block = _dehyphenate_block(block)
        # Then join remaining lines with spaces
        joined_lines = block.splitlines()
        joined = ' '.join(ln.strip() for ln in joined_lines if ln.strip())
        # Normalize multiple spaces to single space (OCR artifacts, formatting)
        while '  ' in joined:
            joined = joined.replace('  ', ' ')
        if joined:
            unwrapped.append(joined)

    return '\n\n'.join(unwrapped)
