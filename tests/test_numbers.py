# -*- coding: UTF-8 -*-
"""Numbers with decimals should NOT trigger splits."""

from fast_sentence_segment import segment_text


class TestNumbers:
    """Numbers with decimals should NOT trigger splits."""

    def test_currency(self):
        result = segment_text("The price is $4.50 today.", flatten=True)
        assert result == ["The price is $4.50 today."]

    def test_decimal(self):
        result = segment_text("Pi is approximately 3.14159 in value.", flatten=True)
        assert result == ["Pi is approximately 3.14159 in value."]

    def test_percentage(self):
        result = segment_text("Growth was 5.5% last year.", flatten=True)
        assert result == ["Growth was 5.5% last year."]
