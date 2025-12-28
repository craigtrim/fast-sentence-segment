# -*- coding: UTF-8 -*-
"""Whitespace handling."""

from fast_sentence_segment import segment_text


class TestWhitespace:
    """Whitespace handling."""

    def test_double_space_as_delimiter(self):
        result = segment_text("First sentence.  Second sentence.", flatten=True)
        assert result == ["First sentence.", "Second sentence."]

    def test_leading_trailing_whitespace(self):
        result = segment_text("   Hello world.   ", flatten=True)
        assert result == ["Hello world."]

    def test_multiple_spaces_as_delimiter(self):
        # Multiple spaces are treated as sentence delimiter
        result = segment_text("Hello    world.", flatten=True)
        assert result == ["Hello. world."]
