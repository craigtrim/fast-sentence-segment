# -*- coding: UTF-8 -*-
"""Tests for Issue #29: Unicode apostrophe-like character normalization.

Validates that 11 additional non-combining Unicode characters that can represent
apostrophes in real-world text are correctly normalized to ASCII ' (U+0027).

These characters appear in e-texts, OCR output, transliteration, and multilingual
documents. If they reach _count_quotes() un-normalized, they won't match the
ASCII apostrophe that _is_elision() and the mid-word apostrophe check expect,
causing them to be miscounted as dialog quotes and corrupting quote-parity
tracking.

Related GitHub Issues:
    #29 - Augment single-quote normalization with 13 missing apostrophe-like characters
    https://github.com/craigtrim/fast-sentence-segment/issues/29

    #6 - Review findings from Issue #5
    https://github.com/craigtrim/fast-sentence-segment/issues/6

    #13 - fix: Word-initial elision apostrophes counted as dialog quotes
    https://github.com/craigtrim/fast-sentence-segment/issues/13
"""

import pytest

from fast_sentence_segment.dmo.normalize_quotes import normalize_quotes


# ==============================================================================
# SECTION 1: Individual character normalization — high-value characters
# ==============================================================================


class TestModifierLetterApostrophe:
    """U+02BC MODIFIER LETTER APOSTROPHE — the Unicode-recommended apostrophe.

    This is the single most important character in Issue #29. It is the
    Unicode-correct character for apostrophe-as-letter (contractions, elisions,
    possessives). Produced by standards-aware software, some keyboards, and
    used in Welsh, Hawaiian, and English e-texts.
    """

    def test_contraction_dont(self):
        """don\u02BCt → don't"""
        assert normalize_quotes("don\u02BCt") == "don't"

    def test_contraction_cant(self):
        """can\u02BCt → can't"""
        assert normalize_quotes("can\u02BCt") == "can't"

    def test_contraction_wont(self):
        """won\u02BCt → won't"""
        assert normalize_quotes("won\u02BCt") == "won't"

    def test_contraction_its(self):
        """it\u02BCs → it's"""
        assert normalize_quotes("it\u02BCs") == "it's"

    def test_contraction_im(self):
        """I\u02BCm → I'm"""
        assert normalize_quotes("I\u02BCm") == "I'm"

    def test_contraction_youre(self):
        """you\u02BCre → you're"""
        assert normalize_quotes("you\u02BCre") == "you're"

    def test_possessive(self):
        """Jack\u02BCs → Jack's"""
        assert normalize_quotes("Jack\u02BCs") == "Jack's"

    def test_elision_tis(self):
        """\u02BCtis → 'tis"""
        assert normalize_quotes("\u02BCtis") == "'tis"

    def test_elision_twas(self):
        """\u02BCTwas → 'Twas"""
        assert normalize_quotes("\u02BCTwas") == "'Twas"

    def test_elision_cello(self):
        """\u02BCcello → 'cello"""
        assert normalize_quotes("\u02BCcello") == "'cello"

    def test_elision_em(self):
        """give \u02BCem → give 'em"""
        assert normalize_quotes("give \u02BCem") == "give 'em"

    def test_hawaiian_word(self):
        """Hawai\u02BCi → Hawai'i"""
        assert normalize_quotes("Hawai\u02BCi") == "Hawai'i"

    def test_welsh_word(self):
        """Cymru\u02BCr → Cymru'r"""
        assert normalize_quotes("Cymru\u02BCr") == "Cymru'r"

    def test_full_sentence(self):
        """Full sentence with modifier letter apostrophe."""
        text = "She said, \"I don\u02BCt know what\u02BCs happening.\""
        expected = "She said, \"I don't know what's happening.\""
        assert normalize_quotes(text) == expected

    def test_multiple_in_sentence(self):
        """Multiple modifier letter apostrophes in one sentence."""
        text = "I\u02BCm sure it\u02BCs Jack\u02BCs fault"
        expected = "I'm sure it's Jack's fault"
        assert normalize_quotes(text) == expected

    def test_standalone(self):
        """Standalone U+02BC normalizes to ASCII apostrophe."""
        assert normalize_quotes("\u02BC") == "'"


class TestReversedPrime:
    """U+2035 REVERSED PRIME — complement of U+2032 (already handled).

    Appears in mathematical and technical text. Since the forward prime
    is already normalized, the reversed prime should be too for consistency.
    """

    def test_standalone(self):
        assert normalize_quotes("\u2035") == "'"

    def test_in_contraction(self):
        assert normalize_quotes("don\u2035t") == "don't"

    def test_in_elision(self):
        assert normalize_quotes("\u2035tis a fine day") == "'tis a fine day"

    def test_in_sentence(self):
        text = "It\u2035s been a long day."
        expected = "It's been a long day."
        assert normalize_quotes(text) == expected


class TestModifierLetterPrime:
    """U+02B9 MODIFIER LETTER PRIME — used in transliteration (e.g., Cyrillic)."""

    def test_standalone(self):
        assert normalize_quotes("\u02B9") == "'"

    def test_in_contraction(self):
        assert normalize_quotes("don\u02B9t") == "don't"

    def test_in_possessive(self):
        assert normalize_quotes("Stephen\u02B9s") == "Stephen's"

    def test_in_elision(self):
        assert normalize_quotes("give \u02B9em the goods") == "give 'em the goods"

    def test_in_sentence(self):
        text = "I\u02B9ve seen it before."
        expected = "I've seen it before."
        assert normalize_quotes(text) == expected


class TestLatinSaltillo:
    """U+A78C LATIN SMALL LETTER SALTILLO — Nahuatl and Mesoamerican languages."""

    def test_standalone(self):
        assert normalize_quotes("\uA78C") == "'"

    def test_in_contraction(self):
        assert normalize_quotes("don\uA78Ct") == "don't"

    def test_in_possessive(self):
        assert normalize_quotes("Joselito\uA78Cs") == "Joselito's"

    def test_in_elision(self):
        assert normalize_quotes("\uA78Ctwas the night") == "'twas the night"

    def test_in_sentence(self):
        text = "She can\uA78Ct believe what\uA78Cs happening."
        expected = "She can't believe what's happening."
        assert normalize_quotes(text) == expected


# ==============================================================================
# SECTION 2: Individual character normalization — medium-value characters
# ==============================================================================


class TestModifierLetterVerticalLine:
    """U+02C8 MODIFIER LETTER VERTICAL LINE — IPA transcription bleed-through."""

    def test_standalone(self):
        assert normalize_quotes("\u02C8") == "'"

    def test_in_contraction(self):
        assert normalize_quotes("don\u02C8t") == "don't"

    def test_in_sentence(self):
        text = "It\u02C8s a lovely day."
        expected = "It's a lovely day."
        assert normalize_quotes(text) == expected


class TestArmenianApostrophe:
    """U+055A ARMENIAN APOSTROPHE — Armenian language text."""

    def test_standalone(self):
        assert normalize_quotes("\u055A") == "'"

    def test_in_contraction(self):
        assert normalize_quotes("don\u055At") == "don't"

    def test_in_sentence(self):
        text = "It\u055As happened before."
        expected = "It's happened before."
        assert normalize_quotes(text) == expected


class TestHebrewGeresh:
    """U+05F3 HEBREW PUNCTUATION GERESH — Hebrew text."""

    def test_standalone(self):
        assert normalize_quotes("\u05F3") == "'"

    def test_in_contraction(self):
        assert normalize_quotes("don\u05F3t") == "don't"

    def test_in_sentence(self):
        text = "We\u05F3ve arrived."
        expected = "We've arrived."
        assert normalize_quotes(text) == expected


class TestNkoHighToneApostrophe:
    """U+07F4 NKO HIGH TONE APOSTROPHE — West African languages (NKo script)."""

    def test_standalone(self):
        assert normalize_quotes("\u07F4") == "'"

    def test_in_contraction(self):
        assert normalize_quotes("don\u07F4t") == "don't"

    def test_in_sentence(self):
        text = "She\u07F4s coming tomorrow."
        expected = "She's coming tomorrow."
        assert normalize_quotes(text) == expected


class TestNkoLowToneApostrophe:
    """U+07F5 NKO LOW TONE APOSTROPHE — West African languages (NKo script)."""

    def test_standalone(self):
        assert normalize_quotes("\u07F5") == "'"

    def test_in_contraction(self):
        assert normalize_quotes("don\u07F5t") == "don't"

    def test_in_sentence(self):
        text = "They\u07F5re almost done."
        expected = "They're almost done."
        assert normalize_quotes(text) == expected


class TestGreekPsili:
    """U+1FBF GREEK PSILI (smooth breathing) — Greek polytonic text."""

    def test_standalone(self):
        assert normalize_quotes("\u1FBF") == "'"

    def test_in_contraction(self):
        assert normalize_quotes("don\u1FBFt") == "don't"

    def test_in_sentence(self):
        text = "He\u1FBFs been waiting."
        expected = "He's been waiting."
        assert normalize_quotes(text) == expected


class TestGreekKoronis:
    """U+1FBD GREEK KORONIS (crasis) — Greek polytonic text."""

    def test_standalone(self):
        assert normalize_quotes("\u1FBD") == "'"

    def test_in_contraction(self):
        assert normalize_quotes("don\u1FBDt") == "don't"

    def test_in_sentence(self):
        text = "I\u1FBDll be there soon."
        expected = "I'll be there soon."
        assert normalize_quotes(text) == expected


# ==============================================================================
# SECTION 3: Mixed character tests — multiple new chars in same text
# ==============================================================================


class TestMixedNewCharacters:
    """Tests with multiple new Unicode characters in the same text."""

    def test_two_different_new_chars(self):
        """Two different new characters in one sentence."""
        text = "I\u02BCm sure it\u2035s fine."
        expected = "I'm sure it's fine."
        assert normalize_quotes(text) == expected

    def test_new_char_with_existing_char(self):
        """New character mixed with already-handled character."""
        text = "\u2018Hello,\u2019 she said. \u201cI don\u02BCt know.\u201d"
        expected = "'Hello,' she said. \"I don't know.\""
        assert normalize_quotes(text) == expected

    def test_three_different_new_chars(self):
        """Three different new characters."""
        text = "don\u02BCt won\u02B9t can\uA78Ct"
        expected = "don't won't can't"
        assert normalize_quotes(text) == expected

    def test_new_and_old_single_quotes(self):
        """Mix of new and existing single quote variants."""
        text = "It\u2019s and it\u02BCs and it\u00B4s"
        expected = "It's and it's and it's"
        assert normalize_quotes(text) == expected

    def test_all_eleven_new_chars_sequential(self):
        """All 11 new characters appearing sequentially."""
        chars = [
            "\u2035",  # REVERSED PRIME
            "\u02B9",  # MODIFIER LETTER PRIME
            "\u02BC",  # MODIFIER LETTER APOSTROPHE
            "\u02C8",  # MODIFIER LETTER VERTICAL LINE
            "\u055A",  # ARMENIAN APOSTROPHE
            "\u05F3",  # HEBREW PUNCTUATION GERESH
            "\u07F4",  # NKO HIGH TONE APOSTROPHE
            "\u07F5",  # NKO LOW TONE APOSTROPHE
            "\u1FBF",  # GREEK PSILI
            "\u1FBD",  # GREEK KORONIS
            "\uA78C",  # LATIN SMALL LETTER SALTILLO
        ]
        for char in chars:
            assert normalize_quotes(char) == "'", (
                f"U+{ord(char):04X} should normalize to ASCII apostrophe"
            )


# ==============================================================================
# SECTION 4: Contraction normalization across all 11 new characters
# ==============================================================================


class TestContractionNormalizationAllChars:
    """Verify every new character normalizes correctly in common contractions.

    This is a systematic sweep: for each of the 11 new characters, test that
    "don{char}t" normalizes to "don't". This ensures the regex character class
    is complete.
    """

    @pytest.mark.parametrize("char,name", [
        ("\u2035", "REVERSED PRIME"),
        ("\u02B9", "MODIFIER LETTER PRIME"),
        ("\u02BC", "MODIFIER LETTER APOSTROPHE"),
        ("\u02C8", "MODIFIER LETTER VERTICAL LINE"),
        ("\u055A", "ARMENIAN APOSTROPHE"),
        ("\u05F3", "HEBREW PUNCTUATION GERESH"),
        ("\u07F4", "NKO HIGH TONE APOSTROPHE"),
        ("\u07F5", "NKO LOW TONE APOSTROPHE"),
        ("\u1FBF", "GREEK PSILI"),
        ("\u1FBD", "GREEK KORONIS"),
        ("\uA78C", "LATIN SMALL LETTER SALTILLO"),
    ])
    def test_dont_contraction(self, char, name):
        """don{char}t should normalize to don't for {name}."""
        assert normalize_quotes(f"don{char}t") == "don't", (
            f"U+{ord(char):04X} ({name}) failed in contraction"
        )

    @pytest.mark.parametrize("char,name", [
        ("\u2035", "REVERSED PRIME"),
        ("\u02B9", "MODIFIER LETTER PRIME"),
        ("\u02BC", "MODIFIER LETTER APOSTROPHE"),
        ("\u02C8", "MODIFIER LETTER VERTICAL LINE"),
        ("\u055A", "ARMENIAN APOSTROPHE"),
        ("\u05F3", "HEBREW PUNCTUATION GERESH"),
        ("\u07F4", "NKO HIGH TONE APOSTROPHE"),
        ("\u07F5", "NKO LOW TONE APOSTROPHE"),
        ("\u1FBF", "GREEK PSILI"),
        ("\u1FBD", "GREEK KORONIS"),
        ("\uA78C", "LATIN SMALL LETTER SALTILLO"),
    ])
    def test_its_contraction(self, char, name):
        """it{char}s should normalize to it's for {name}."""
        assert normalize_quotes(f"it{char}s") == "it's", (
            f"U+{ord(char):04X} ({name}) failed in contraction"
        )

    @pytest.mark.parametrize("char,name", [
        ("\u2035", "REVERSED PRIME"),
        ("\u02B9", "MODIFIER LETTER PRIME"),
        ("\u02BC", "MODIFIER LETTER APOSTROPHE"),
        ("\u02C8", "MODIFIER LETTER VERTICAL LINE"),
        ("\u055A", "ARMENIAN APOSTROPHE"),
        ("\u05F3", "HEBREW PUNCTUATION GERESH"),
        ("\u07F4", "NKO HIGH TONE APOSTROPHE"),
        ("\u07F5", "NKO LOW TONE APOSTROPHE"),
        ("\u1FBF", "GREEK PSILI"),
        ("\u1FBD", "GREEK KORONIS"),
        ("\uA78C", "LATIN SMALL LETTER SALTILLO"),
    ])
    def test_possessive(self, char, name):
        """Jack{char}s should normalize to Jack's for {name}."""
        assert normalize_quotes(f"Jack{char}s") == "Jack's", (
            f"U+{ord(char):04X} ({name}) failed in possessive"
        )


# ==============================================================================
# SECTION 5: Elision normalization across all 11 new characters
# ==============================================================================


class TestElisionNormalizationAllChars:
    """Verify every new character normalizes correctly in elisions."""

    @pytest.mark.parametrize("char,name", [
        ("\u2035", "REVERSED PRIME"),
        ("\u02B9", "MODIFIER LETTER PRIME"),
        ("\u02BC", "MODIFIER LETTER APOSTROPHE"),
        ("\u02C8", "MODIFIER LETTER VERTICAL LINE"),
        ("\u055A", "ARMENIAN APOSTROPHE"),
        ("\u05F3", "HEBREW PUNCTUATION GERESH"),
        ("\u07F4", "NKO HIGH TONE APOSTROPHE"),
        ("\u07F5", "NKO LOW TONE APOSTROPHE"),
        ("\u1FBF", "GREEK PSILI"),
        ("\u1FBD", "GREEK KORONIS"),
        ("\uA78C", "LATIN SMALL LETTER SALTILLO"),
    ])
    def test_tis_elision(self, char, name):
        """{char}tis should normalize to 'tis for {name}."""
        assert normalize_quotes(f"{char}tis a fine day") == "'tis a fine day", (
            f"U+{ord(char):04X} ({name}) failed in 'tis elision"
        )

    @pytest.mark.parametrize("char,name", [
        ("\u2035", "REVERSED PRIME"),
        ("\u02B9", "MODIFIER LETTER PRIME"),
        ("\u02BC", "MODIFIER LETTER APOSTROPHE"),
        ("\u02C8", "MODIFIER LETTER VERTICAL LINE"),
        ("\u055A", "ARMENIAN APOSTROPHE"),
        ("\u05F3", "HEBREW PUNCTUATION GERESH"),
        ("\u07F4", "NKO HIGH TONE APOSTROPHE"),
        ("\u07F5", "NKO LOW TONE APOSTROPHE"),
        ("\u1FBF", "GREEK PSILI"),
        ("\u1FBD", "GREEK KORONIS"),
        ("\uA78C", "LATIN SMALL LETTER SALTILLO"),
    ])
    def test_em_elision(self, char, name):
        """give {char}em should normalize to give 'em for {name}."""
        assert normalize_quotes(f"give {char}em") == "give 'em", (
            f"U+{ord(char):04X} ({name}) failed in 'em elision"
        )

    @pytest.mark.parametrize("char,name", [
        ("\u2035", "REVERSED PRIME"),
        ("\u02B9", "MODIFIER LETTER PRIME"),
        ("\u02BC", "MODIFIER LETTER APOSTROPHE"),
        ("\u02C8", "MODIFIER LETTER VERTICAL LINE"),
        ("\u055A", "ARMENIAN APOSTROPHE"),
        ("\u05F3", "HEBREW PUNCTUATION GERESH"),
        ("\u07F4", "NKO HIGH TONE APOSTROPHE"),
        ("\u07F5", "NKO LOW TONE APOSTROPHE"),
        ("\u1FBF", "GREEK PSILI"),
        ("\u1FBD", "GREEK KORONIS"),
        ("\uA78C", "LATIN SMALL LETTER SALTILLO"),
    ])
    def test_cello_elision(self, char, name):
        """the {char}cello should normalize to the 'cello for {name}."""
        assert normalize_quotes(f"the {char}cello") == "the 'cello", (
            f"U+{ord(char):04X} ({name}) failed in 'cello elision"
        )


# ==============================================================================
# SECTION 6: Existing characters still work (regression)
# ==============================================================================


class TestExistingCharsStillWork:
    """Verify that existing single-quote characters are unaffected by the change."""

    def test_left_single_quote(self):
        assert normalize_quotes("\u2018Hello\u2019") == "'Hello'"

    def test_right_single_quote_contraction(self):
        assert normalize_quotes("It\u2019s") == "It's"

    def test_single_low_9(self):
        assert normalize_quotes("\u201atest") == "'test"

    def test_single_high_reversed_9(self):
        assert normalize_quotes("\u201btest") == "'test"

    def test_single_left_angle(self):
        assert normalize_quotes("\u2039test\u203a") == "'test'"

    def test_prime(self):
        assert normalize_quotes("5\u2032") == "5'"

    def test_fullwidth_apostrophe(self):
        assert normalize_quotes("It\uFF07s") == "It's"

    def test_grave_accent(self):
        assert normalize_quotes("\u0060Hello\u00B4") == "'Hello'"

    def test_acute_accent(self):
        assert normalize_quotes("caf\u00B4") == "caf'"

    def test_ascii_unchanged(self):
        assert normalize_quotes("It's a test.") == "It's a test."


# ==============================================================================
# SECTION 7: Double quote normalization unaffected (regression)
# ==============================================================================


class TestDoubleQuotesUnaffected:
    """Verify double-quote normalization is not broken by the changes."""

    def test_curly_double_quotes(self):
        assert normalize_quotes("\u201cHello\u201d") == '"Hello"'

    def test_guillemets(self):
        assert normalize_quotes("\u00abBonjour\u00bb") == '"Bonjour"'

    def test_fullwidth(self):
        assert normalize_quotes("\uFF02Test\uFF02") == '"Test"'

    def test_ascii_double_unchanged(self):
        assert normalize_quotes('"Already ASCII"') == '"Already ASCII"'


# ==============================================================================
# SECTION 8: Real-world text scenarios with new characters
# ==============================================================================


class TestRealWorldScenarios:
    """Real-world text scenarios where these characters might appear."""

    def test_unicode_aware_word_processor_output(self):
        """Text from a word processor that uses U+02BC for apostrophes."""
        text = "I\u02BCm not sure what\u02BCs going on. She can\u02BCt believe it."
        expected = "I'm not sure what's going on. She can't believe it."
        assert normalize_quotes(text) == expected

    def test_transliterated_text_with_modifier_prime(self):
        """Transliterated text using modifier letter prime."""
        text = "The scholar\u02B9s work on Dostoevski\u02B9s novels"
        expected = "The scholar's work on Dostoevski's novels"
        assert normalize_quotes(text) == expected

    def test_ocr_output_mixed_apostrophes(self):
        """OCR output that produces inconsistent apostrophe characters."""
        text = "don\u02BCt and can\u2035t and won\u02B9t"
        expected = "don't and can't and won't"
        assert normalize_quotes(text) == expected

    def test_multilingual_document(self):
        """Document mixing English with Hawaiian place names."""
        text = "The Hawai\u02BCi conference on O\u02BCahu was wonderful."
        expected = "The Hawai'i conference on O'ahu was wonderful."
        assert normalize_quotes(text) == expected

    def test_ipa_bleed_through(self):
        """IPA vertical line appearing in place of apostrophe."""
        text = "He said he\u02C8d come back."
        expected = "He said he'd come back."
        assert normalize_quotes(text) == expected

    def test_ebook_with_saltillo(self):
        """E-text using Latin saltillo for apostrophes."""
        text = "\uA78CTwas brillig and the slithy toves."
        expected = "'Twas brillig and the slithy toves."
        assert normalize_quotes(text) == expected

    def test_full_paragraph_mixed_sources(self):
        """Full paragraph with characters from different sources."""
        text = (
            "\u02BCTwas the night before Christmas. "
            "The children couldn\u02BCt sleep. "
            "\"Santa\u02B9s coming!\" they whispered. "
            "Their father\uA78Cs patience was wearing thin."
        )
        expected = (
            "'Twas the night before Christmas. "
            "The children couldn't sleep. "
            "\"Santa's coming!\" they whispered. "
            "Their father's patience was wearing thin."
        )
        assert normalize_quotes(text) == expected

    def test_dialog_with_new_apostrophe_chars(self):
        """Dialog using U+02BC throughout."""
        text = (
            "\u201cI don\u02BCt think that\u02BCs right,\u201d "
            "she said. \u201cIt\u02BCs Jack\u02BCs fault.\u201d"
        )
        expected = (
            "\"I don't think that's right,\" "
            "she said. \"It's Jack's fault.\""
        )
        assert normalize_quotes(text) == expected


# ==============================================================================
# SECTION 9: Edge cases
# ==============================================================================


class TestEdgeCases:
    """Edge cases for the new character normalization."""

    def test_empty_string(self):
        assert normalize_quotes("") == ""

    def test_only_new_apostrophe_chars(self):
        """String of only new apostrophe characters."""
        assert normalize_quotes("\u02BC\u02B9\u2035") == "'''"

    def test_new_char_at_start_of_string(self):
        assert normalize_quotes("\u02BCtis") == "'tis"

    def test_new_char_at_end_of_string(self):
        assert normalize_quotes("test\u02BC") == "test'"

    def test_consecutive_new_chars(self):
        """Two new chars in a row (unusual but should still normalize)."""
        assert normalize_quotes("\u02BC\u02BC") == "''"

    def test_new_char_between_digits(self):
        """New char between digits (e.g., measurement notation)."""
        assert normalize_quotes("5\u2035") == "5'"

    def test_new_char_before_newline(self):
        """New char before newline."""
        assert normalize_quotes("test\u02BC\nmore") == "test'\nmore"

    def test_new_char_in_multiline(self):
        """New chars in multiline text."""
        text = "Line one: don\u02BCt\nLine two: can\u02B9t\nLine three: won\uA78Ct"
        expected = "Line one: don't\nLine two: can't\nLine three: won't"
        assert normalize_quotes(text) == expected

    def test_no_quotes_unchanged(self):
        """Text without any quotes passes through unchanged."""
        text = "No quotes here at all."
        assert normalize_quotes(text) == text

    def test_ascii_apostrophe_unchanged(self):
        """ASCII apostrophe (U+0027) is NOT changed."""
        text = "It's already ASCII."
        assert normalize_quotes(text) == text


# ==============================================================================
# SECTION 10: Combining characters — documented decision to skip
# ==============================================================================


class TestCombiningCharactersSkipped:
    """Document that combining characters U+0313 and U+0315 are NOT normalized.

    These are combining diacritics from Greek polytonic text. They attach to
    the preceding base character rather than standing alone. Normalizing them
    via simple regex substitution would strip the diacritic but leave the base
    character, which may or may not be desired. They are vanishingly rare in
    the English e-texts this library targets.

    Related GitHub Issue:
        #29, Task 2 — Evaluate combining characters
        https://github.com/craigtrim/fast-sentence-segment/issues/29

    Decision: Skip. Document as known limitation.
    """

    def test_combining_comma_above_not_normalized(self):
        """U+0313 COMBINING COMMA ABOVE is intentionally NOT normalized.

        This is a combining character that attaches to the preceding base
        character. Simple regex substitution would strip only the diacritic.
        """
        # U+0313 is a combining character — it modifies the preceding char
        # We intentionally do NOT normalize it
        text = "a\u0313"  # 'a' with combining comma above
        result = normalize_quotes(text)
        # The combining character should pass through unchanged
        assert "\u0313" in result or result == text

    def test_combining_comma_above_right_not_normalized(self):
        """U+0315 COMBINING COMMA ABOVE RIGHT is intentionally NOT normalized.

        Same reasoning as U+0313 — combining character, not standalone.
        """
        text = "a\u0315"  # 'a' with combining comma above right
        result = normalize_quotes(text)
        assert "\u0315" in result or result == text
