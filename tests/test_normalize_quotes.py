# -*- coding: UTF-8 -*-
"""Tests for quote normalization.

Related GitHub Issue:
    #5 - Normalize quotes and group open-quote sentences in unwrap mode
    https://github.com/craigtrim/fast-sentence-segment/issues/5
"""

import pytest
from fast_sentence_segment.dmo.normalize_quotes import normalize_quotes


class TestNormalizeQuotes:
    """Test unicode double quote normalization to ASCII."""

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

    def test_mixed_variants(self):
        text = '\u201cShe said, \u00abHello.\u00bb\u201d'
        assert normalize_quotes(text) == '"She said, "Hello.""'

    def test_no_quotes_unchanged(self):
        text = 'No quotes here.'
        assert normalize_quotes(text) == text

    def test_ascii_quotes_unchanged(self):
        text = '"Already ASCII quotes."'
        assert normalize_quotes(text) == text

    def test_single_quotes_unchanged(self):
        text = "It's a contraction."
        assert normalize_quotes(text) == text

    def test_empty_string(self):
        assert normalize_quotes('') == ''

    def test_multiline_text(self):
        text = '\u201cFirst line.\nSecond line.\u201d'
        expected = '"First line.\nSecond line."'
        assert normalize_quotes(text) == expected
