# -*- coding: UTF-8 -*-
"""Tests for quote normalization.

Related GitHub Issues:
    #5 - Normalize quotes and group open-quote sentences in unwrap mode
    https://github.com/craigtrim/fast-sentence-segment/issues/5

    #6 - Review findings from Issue #5
    https://github.com/craigtrim/fast-sentence-segment/issues/6
"""

import pytest
from fast_sentence_segment.dmo.normalize_quotes import normalize_quotes


class TestNormalizeDoubleQuotes:
    """Test unicode double quote normalization to ASCII "."""

    def test_left_double_quote(self):
        assert normalize_quotes('\u201cHello') == '"Hello'

    def test_right_double_quote(self):
        assert normalize_quotes('world\u201d') == 'world"'

    def test_left_and_right_double_quotes(self):
        assert normalize_quotes('\u201cHello, world.\u201d') == '"Hello, world."'

    def test_double_low_9_quote(self):
        assert normalize_quotes('\u201eHello\u201d') == '"Hello"'

    def test_double_high_reversed_9_quote(self):
        assert normalize_quotes('\u201fHello\u201d') == '"Hello"'

    def test_left_guillemet(self):
        assert normalize_quotes('\u00abHello\u00bb') == '"Hello"'

    def test_right_guillemet(self):
        assert normalize_quotes('\u00bbHello\u00ab') == '"Hello"'

    def test_double_prime(self):
        assert normalize_quotes('\u2033Hello\u2033') == '"Hello"'

    def test_reversed_double_prime(self):
        assert normalize_quotes('\u301dHello\u301e') == '"Hello"'

    def test_low_double_prime(self):
        assert normalize_quotes('\u301fHello\u301e') == '"Hello"'

    def test_fullwidth_quotation_mark(self):
        assert normalize_quotes('\uff02Hello\uff02') == '"Hello"'

    def test_mixed_double_variants(self):
        text = '\u201cShe said, \u00abHello.\u00bb\u201d'
        assert normalize_quotes(text) == '"She said, "Hello.""'

    def test_ascii_double_quotes_unchanged(self):
        text = '"Already ASCII quotes."'
        assert normalize_quotes(text) == text


class TestNormalizeSingleQuotes:
    """Test unicode single quote normalization to ASCII '."""

    def test_left_single_quote(self):
        assert normalize_quotes('\u2018Hello\u2019') == "'Hello'"

    def test_right_single_quote_apostrophe(self):
        assert normalize_quotes('It\u2019s') == "It's"

    def test_single_low_9_quote(self):
        assert normalize_quotes('\u201aHello\u2019') == "'Hello'"

    def test_single_high_reversed_9_quote(self):
        assert normalize_quotes('\u201bHello\u2019') == "'Hello'"

    def test_single_left_angle_quote(self):
        assert normalize_quotes('\u2039Hello\u203a') == "'Hello'"

    def test_prime(self):
        assert normalize_quotes('5\u2032') == "5'"

    def test_fullwidth_apostrophe(self):
        assert normalize_quotes('It\uff07s') == "It's"

    def test_grave_accent(self):
        assert normalize_quotes('\u0060Hello\u00b4') == "'Hello'"

    def test_acute_accent(self):
        assert normalize_quotes('caf\u00b4') == "caf'"

    def test_ascii_single_quotes_unchanged(self):
        text = "It's a contraction."
        assert normalize_quotes(text) == text


class TestNormalizeQuotesMixed:
    """Test mixed and edge cases."""

    def test_mixed_single_and_double(self):
        text = '\u201cIt\u2019s a test,\u201d she said.'
        assert normalize_quotes(text) == '"It\'s a test," she said.'

    def test_no_quotes_unchanged(self):
        text = 'No quotes here.'
        assert normalize_quotes(text) == text

    def test_empty_string(self):
        assert normalize_quotes('') == ''

    def test_multiline_text(self):
        text = '\u201cFirst line.\nSecond line.\u201d'
        expected = '"First line.\nSecond line."'
        assert normalize_quotes(text) == expected
