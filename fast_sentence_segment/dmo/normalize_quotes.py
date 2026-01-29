# -*- coding: UTF-8 -*-
"""Normalize unicode double quote variants to ASCII double quotes.

E-texts use a variety of double quote characters (curly/smart quotes,
unicode variants). This module normalizes all double quote variants
to the standard ASCII double quote character (").

Related GitHub Issue:
    #5 - Normalize quotes and group open-quote sentences in unwrap mode
    https://github.com/craigtrim/fast-sentence-segment/issues/5
"""

import re

# Unicode double quote variants to normalize to ASCII "
# Covers: left/right double quotation marks, low-9, high-reversed-9,
# and left/right-pointing double angle quotation marks (guillemets).
DOUBLE_QUOTE_PATTERN = re.compile(
    '[\u201c\u201d\u201e\u201f\u00ab\u00bb]'
)


def normalize_quotes(text: str) -> str:
    """Replace all unicode double quote variants with ASCII double quote.

    Normalizes the following characters to ASCII " (U+0022):
        - U+201C  left double quotation mark
        - U+201D  right double quotation mark
        - U+201E  double low-9 quotation mark
        - U+201F  double high-reversed-9 quotation mark
        - U+00AB  left-pointing double angle quotation mark
        - U+00BB  right-pointing double angle quotation mark

    Args:
        text: Input text potentially containing unicode double quotes.

    Returns:
        Text with all double quote variants replaced by ASCII ".

    Example:
        >>> normalize_quotes('\u201cHello,\u201d she said.')
        '"Hello," she said.'
    """
    return DOUBLE_QUOTE_PATTERN.sub('"', text)
