# -*- coding: UTF-8 -*-
"""Shared quote-tracking utilities for dialog and unwrap modules.

Provides common infrastructure for distinguishing dialog quotes from
apostrophes (contractions, possessives, and word-initial elisions).
Both dialog_formatter.py and unwrap_hard_wrapped_text.py depend on
these utilities for correct quote-parity tracking.

Related GitHub Issues:
    #13 - fix: Word-initial elision apostrophes ('cello, 'tis) counted as dialog quotes
    https://github.com/craigtrim/fast-sentence-segment/issues/13

    #29 - Augment single-quote normalization with missing apostrophe-like Unicode characters
    https://github.com/craigtrim/fast-sentence-segment/issues/29
"""

# Known elision words (case-insensitive).
# These are specific words where an apostrophe replaces omitted letters at the start.
# When an apostrophe precedes one of these words at a word boundary, it is an
# elision — not a dialog quote — and must not be counted for quote-parity tracking.
KNOWN_ELISION_WORDS = {
    # 'it' elisions
    "tis", "twas", "twere", "twill", "twould", "taint", "tother",
    # Archaic oaths (very specific words)
    "sblood", "sdeath", "swounds", "sbodikins", "slid", "strewth", "zounds",
    # Common elisions with a-/be- prefix dropped
    "bout", "bove", "cross", "fore", "fraid", "gainst", "live", "loft", "lone",
    "long", "mid", "midst", "mong", "mongst", "neath", "round", "sleep", "tween",
    "twixt", "wake", "ware", "way", "cause", "cuz", "coz", "hind", "low", "side",
    "yond", "cept", "scaped", "specially", "splain", "spect",
    # Cockney/dialect h-dropping (common words and their forms)
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


def is_elision(text: str, pos: int) -> bool:
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


def count_quotes(text: str, all_quotes: str, single_quotes: str) -> int:
    """Count actual quote characters in text, excluding apostrophes.

    Apostrophes in contractions (don't, can't), possessives (Jack's, Joselito's),
    and word-initial elisions ('tis, 'twas, 'cello, 'em) are NOT counted as quotes
    because they don't indicate dialog boundaries.

    A quote character is considered an apostrophe (not a quote) if:
    - It's preceded by a letter AND followed by a letter (mid-word: don't, Joselito's)
    - It's a word-initial elision ('tis, 'Twas, 'cello, '99)

    Args:
        text: The text to count quotes in.
        all_quotes: String of all quote characters to look for.
        single_quotes: String of single-quote characters (subset of all_quotes)
            used to identify potential apostrophes/elisions.

    Returns:
        Number of actual quote characters (not apostrophes).
    """
    count = 0
    for i, c in enumerate(text):
        if c not in all_quotes:
            continue

        # Check if this is a mid-word apostrophe (contraction/possessive)
        prev_is_letter = i > 0 and text[i - 1].isalpha()
        next_is_letter = i < len(text) - 1 and text[i + 1].isalpha()

        if prev_is_letter and next_is_letter:
            # Mid-word apostrophe (contraction/possessive) - don't count
            continue

        # Check if this is a word-initial elision
        prev_is_word_boundary = i == 0 or not text[i - 1].isalnum()
        if prev_is_word_boundary and c in single_quotes and is_elision(text, i):
            # Word-initial elision - don't count
            continue

        count += 1
    return count
