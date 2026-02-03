# -*- coding: UTF-8 -*-
"""Unwrap hard-wrapped text (e.g., Project Gutenberg e-texts).

Joins lines within paragraphs into continuous strings while
preserving paragraph boundaries (blank lines). Also dehyphenates
words that were split across lines for typesetting.

Related GitHub Issue:
    #8 - Add dehyphenation support for words split across lines
    https://github.com/craigtrim/fast-sentence-segment/issues/8
"""

import re

# Pattern to match hyphenated word breaks at end of line:
# - A single hyphen (not -- em-dash)
# - Followed by newline and optional whitespace
# - Followed by a lowercase letter (continuation of word)
_HYPHEN_LINE_BREAK_PATTERN = re.compile(r'(?<!-)-\n\s*([a-z])')


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

    Examples:
        >>> unwrap_hard_wrapped_text("a bot-\\ntle of wine")
        'a bottle of wine'
        >>> unwrap_hard_wrapped_text("line one\\nline two")
        'line one line two'

    Args:
        text: Raw text with hard-wrapped lines.

    Returns:
        Text with paragraphs unwrapped into continuous strings,
        separated by double newlines, with hyphenated words rejoined.
    """
    blocks = re.split(r'\n\s*\n', text)
    unwrapped = []

    for block in blocks:
        # First, dehyphenate words split across lines
        block = _dehyphenate_block(block)
        # Then join remaining lines with spaces
        lines = block.splitlines()
        joined = ' '.join(line.strip() for line in lines if line.strip())
        if joined:
            unwrapped.append(joined)

    return '\n\n'.join(unwrapped)
