# -*- coding: UTF-8 -*-
"""Quoted speech and text."""

from fast_sentence_segment import segment_text


class TestQuotedText:
    """Quoted speech and text."""

    def test_simple_quote(self):
        result = segment_text('He said "Hello there" to me.', flatten=True)
        assert result == ['He said "Hello there" to me.']

    def test_quote_with_period_inside(self):
        # Spurious trailing period after closing quote removed (issue #7)
        result = segment_text('"Hello." He waved.', flatten=True)
        assert result == ['"Hello."', 'He waved.']
