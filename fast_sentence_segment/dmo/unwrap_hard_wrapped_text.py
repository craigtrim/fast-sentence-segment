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

# Quote characters to track for dialog detection
# Includes straight and curly/smart quotes
DOUBLE_QUOTES = '"""\u201c\u201d'  # " " " " "
SINGLE_QUOTES = "'''\u2018\u2019"  # ' ' ' ' '
ALL_QUOTES = DOUBLE_QUOTES + SINGLE_QUOTES

# Known elision words where an apostrophe replaces omitted letters at word start
# These should NOT be counted as dialog quotes
KNOWN_ELISION_WORDS = {
    # 'it' elisions
    "tis", "twas", "twere", "twill", "twould", "taint", "tother",
    # Archaic oaths
    "sblood", "sdeath", "swounds", "sbodikins", "slid", "strewth", "zounds",
    # Common elisions with a-/be- prefix dropped
    "bout", "bove", "cross", "fore", "fraid", "gainst", "live", "loft", "lone",
    "long", "mid", "midst", "mong", "mongst", "neath", "round", "sleep", "tween",
    "twixt", "wake", "ware", "way", "cause", "cuz", "coz", "hind", "low", "side",
    "yond", "cept", "scaped", "specially", "splain", "spect",
    # Cockney/dialect h-dropping
    "e", "em", "er", "ere", "im", "is", "ave", "avin", "ead", "ear", "eard",
    "eart", "eaven", "eavens", "eavy", "eck", "edge", "eel", "eight", "ell",
    "elp", "en", "ero", "igh", "ill", "imself", "int", "it", "itch", "obby",
    "old", "ole", "oliday", "oller", "ollow", "oly", "ome", "onest", "oney",
    "onor", "onour", "ood", "ook", "oop", "ope", "orizon", "orn", "orrible",
    "orse", "ospital", "ot", "otel", "our", "ouse", "ow", "owever", "uge",
    "undred", "ungry", "unt", "urry", "urt", "usband", "alf", "all", "am",
    "and", "andsome", "appen", "appy", "ard", "arm", "at", "ate",
    # Cockney th-dropping
    "ese", "ey", "ose", "ough", "rough",
    # Other prefix elisions
    "count", "fter", "gain", "gin", "less", "nother", "nough", "nuff", "pears",
    "pon", "prentice", "scuse", "spite", "spose", "stead", "tarnal", "tend",
    "thout", "til", "till", "un",
    # Modern colloquial
    "kay", "sup", "dya", "ja", "yer", "copter",
    # Musical
    "cello",
    # 'member (remember)
    "member",
}

# Pattern to match hyphenated word breaks at end of line:
# - A single hyphen (not -- em-dash)
# - Followed by newline and optional whitespace
# - Followed by a lowercase letter (continuation of word)
_HYPHEN_LINE_BREAK_PATTERN = re.compile(r'(?<!-)-\n\s*([a-z])')


def _is_elision(text: str, pos: int) -> bool:
    """Check if apostrophe at position is a word-initial elision.

    Elisions like 'tis, 'twas, 'cello, 'em replace omitted letters at word start.
    Dialog quotes like 'Hello!' surround quoted speech.

    Args:
        text: The full text.
        pos: Position of the apostrophe character.

    Returns:
        True if this appears to be an elision, not a dialog quote.
    """
    if pos >= len(text) - 1:
        return False

    next_char = text[pos + 1]

    # If followed by a digit, it's a year abbreviation ('99, '20s)
    if next_char.isdigit():
        return True

    # Extract the word after the apostrophe (letters only, up to non-letter)
    word_start = pos + 1
    word_end = word_start
    while word_end < len(text) and text[word_end].isalpha():
        word_end += 1

    if word_end == word_start:
        return False  # No letters after apostrophe

    word = text[word_start:word_end].lower()

    # Check if it's a known elision word
    return word in KNOWN_ELISION_WORDS


def _count_quotes(text: str) -> int:
    """Count actual quote characters in text, excluding apostrophes.

    Apostrophes in contractions (don't, can't), possessives (Jack's, Joselito's),
    and word-initial elisions ('tis, 'twas, 'cello, 'em) are NOT counted as quotes
    because they don't indicate dialog boundaries.

    A quote character is considered an apostrophe (not a quote) if:
    - It's preceded by a letter AND followed by a letter (mid-word: don't, Joselito's)
    - It's a word-initial elision ('tis, 'Twas, 'cello, '99)

    Args:
        text: The text to count quotes in.

    Returns:
        Number of actual quote characters (not apostrophes).
    """
    count = 0
    for i, c in enumerate(text):
        if c not in ALL_QUOTES:
            continue

        # Check if this is a mid-word apostrophe (contraction/possessive)
        prev_is_letter = i > 0 and text[i - 1].isalpha()
        next_is_letter = i < len(text) - 1 and text[i + 1].isalpha()

        if prev_is_letter and next_is_letter:
            # Mid-word apostrophe (contraction/possessive) - don't count
            continue

        # Check if this is a word-initial elision
        prev_is_word_boundary = i == 0 or not text[i - 1].isalnum()
        if prev_is_word_boundary and c in SINGLE_QUOTES and _is_elision(text, i):
            # Word-initial elision - don't count
            continue

        count += 1
    return count


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
