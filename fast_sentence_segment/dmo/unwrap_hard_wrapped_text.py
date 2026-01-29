# -*- coding: UTF-8 -*-
"""Unwrap hard-wrapped text (e.g., Project Gutenberg e-texts).

Joins lines within paragraphs into continuous strings while
preserving paragraph boundaries (blank lines).
"""

import re


def unwrap_hard_wrapped_text(text: str) -> str:
    """Unwrap hard-wrapped paragraphs into continuous lines.

    Splits on blank lines to identify paragraphs, then joins
    lines within each paragraph into a single string with
    single spaces.

    Args:
        text: Raw text with hard-wrapped lines.

    Returns:
        Text with paragraphs unwrapped into continuous strings,
        separated by double newlines.
    """
    blocks = re.split(r'\n\s*\n', text)
    unwrapped = []

    for block in blocks:
        lines = block.splitlines()
        joined = ' '.join(line.strip() for line in lines if line.strip())
        if joined:
            unwrapped.append(joined)

    return '\n\n'.join(unwrapped)
