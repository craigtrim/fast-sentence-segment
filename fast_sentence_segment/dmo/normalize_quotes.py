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

    #29 - Augment single-quote normalization with missing Unicode characters
    https://github.com/craigtrim/fast-sentence-segment/issues/29
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
# --- Original 10 characters (issues #5, #6) ---
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
#
# --- 11 additional apostrophe-like characters (issue #29) ---
# U+2035  ‵ REVERSED PRIME (math/technical text; complement of U+2032)
# U+02B9  ʹ MODIFIER LETTER PRIME (transliteration, e.g., Cyrillic)
# U+02BC  ʼ MODIFIER LETTER APOSTROPHE (Unicode-correct apostrophe-as-letter;
#            used in Welsh, Hawaiian, and standards-aware English e-texts)
# U+02C8  ˈ MODIFIER LETTER VERTICAL LINE (IPA transcription bleed-through)
# U+055A  ՚ ARMENIAN APOSTROPHE
# U+05F3  ׳ HEBREW PUNCTUATION GERESH
# U+07F4  ߴ NKO HIGH TONE APOSTROPHE (West African languages)
# U+07F5  ߵ NKO LOW TONE APOSTROPHE (West African languages)
# U+1FBF  ᾿ GREEK PSILI — smooth breathing (Greek polytonic text)
# U+1FBD  ᾽ GREEK KORONIS — crasis (Greek polytonic text)
# U+A78C  ꞌ LATIN SMALL LETTER SALTILLO (Nahuatl, Mesoamerican languages)
#
# NOTE: Combining characters U+0313 (COMBINING COMMA ABOVE) and U+0315
# (COMBINING COMMA ABOVE RIGHT) are intentionally excluded. They are
# diacritics that attach to the preceding base character, not standalone
# apostrophe substitutes. Simple regex substitution would strip only the
# diacritic mark. They are also vanishingly rare in the English e-texts
# this library targets. See issue #29, task 2 for discussion.
SINGLE_QUOTE_PATTERN = re.compile(
    '['
    '\u2018\u2019\u201a\u201b'  # curly single quotes
    '\u2039\u203a'              # single angle quotes
    '\u2032\u2035'              # prime and reversed prime
    '\uff07'                    # fullwidth apostrophe
    '\u0060\u00b4'              # grave and acute accents
    '\u02b9\u02bc\u02c8'        # modifier letters (prime, apostrophe, vertical line)
    '\u055a'                    # Armenian apostrophe
    '\u05f3'                    # Hebrew geresh
    '\u07f4\u07f5'              # NKo apostrophes
    '\u1fbf\u1fbd'              # Greek psili and koronis
    '\ua78c'                    # Latin saltillo
    ']'
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
