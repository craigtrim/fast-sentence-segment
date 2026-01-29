# -*- coding: UTF-8 -*-
"""Normalize unicode quote variants to ASCII equivalents.

E-texts use a variety of quote characters (curly/smart quotes, unicode
variants, primes, guillemets). This module normalizes all quote variants
to their standard ASCII equivalents: double quote (") and single
quote/apostrophe (').

Related GitHub Issues:
    #5 - Normalize quotes and group open-quote sentences in unwrap mode
    https://github.com/craigtrim/fast-sentence-segment/issues/5

    #6 - Review findings from Issue #5
    https://github.com/craigtrim/fast-sentence-segment/issues/6
"""

import re

# Unicode double quote variants to normalize to ASCII " (U+0022).
#
# U+201C  " LEFT DOUBLE QUOTATION MARK
# U+201D  " RIGHT DOUBLE QUOTATION MARK
# U+201E  „ DOUBLE LOW-9 QUOTATION MARK
# U+201F  ‟ DOUBLE HIGH-REVERSED-9 QUOTATION MARK
# U+00AB  « LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
# U+00BB  » RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
# U+2033  ″ DOUBLE PRIME
# U+301D  〝 REVERSED DOUBLE PRIME QUOTATION MARK
# U+301E  〞 DOUBLE PRIME QUOTATION MARK
# U+301F  〟 LOW DOUBLE PRIME QUOTATION MARK
# U+FF02  ＂ FULLWIDTH QUOTATION MARK
DOUBLE_QUOTE_PATTERN = re.compile(
    '[\u201c\u201d\u201e\u201f\u00ab\u00bb\u2033\u301d\u301e\u301f\uff02]'
)

# Unicode single quote variants to normalize to ASCII ' (U+0027).
#
# U+2018  ' LEFT SINGLE QUOTATION MARK
# U+2019  ' RIGHT SINGLE QUOTATION MARK
# U+201A  ‚ SINGLE LOW-9 QUOTATION MARK
# U+201B  ‛ SINGLE HIGH-REVERSED-9 QUOTATION MARK
# U+2039  ‹ SINGLE LEFT-POINTING ANGLE QUOTATION MARK
# U+203A  › SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
# U+2032  ′ PRIME
# U+FF07  ＇ FULLWIDTH APOSTROPHE
# U+0060  ` GRAVE ACCENT (used as opening quote in some e-texts)
# U+00B4  ´ ACUTE ACCENT (used as closing quote in some e-texts)
SINGLE_QUOTE_PATTERN = re.compile(
    '[\u2018\u2019\u201a\u201b\u2039\u203a\u2032\uff07\u0060\u00b4]'
)


def normalize_quotes(text: str) -> str:
    """Replace all unicode quote variants with their ASCII equivalents.

    Double quote variants are normalized to ASCII " (U+0022).
    Single quote variants are normalized to ASCII ' (U+0027).

    Args:
        text: Input text potentially containing unicode quotes.

    Returns:
        Text with all quote variants replaced by ASCII equivalents.

    Example:
        >>> normalize_quotes('\u201cHello,\u201d she said.')
        '"Hello," she said.'
        >>> normalize_quotes('It\u2019s fine.')
        "It's fine."

    Related GitHub Issues:
        #5 - Normalize quotes and group open-quote sentences in unwrap mode
        https://github.com/craigtrim/fast-sentence-segment/issues/5

        #6 - Review findings from Issue #5
        https://github.com/craigtrim/fast-sentence-segment/issues/6
    """
    text = DOUBLE_QUOTE_PATTERN.sub('"', text)
    text = SINGLE_QUOTE_PATTERN.sub("'", text)
    return text
