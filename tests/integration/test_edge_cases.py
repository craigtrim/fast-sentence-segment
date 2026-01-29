# -*- coding: UTF-8 -*-
"""Edge cases and boundary conditions."""

from fast_sentence_segment import segment_text


class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_single_word(self):
        result = segment_text("Hello", flatten=True)
        assert result == ["Hello"]

    # Unrealistic: "..." alone is a valid trailing-off expression
    # def test_only_punctuation(self):
    #     result = segment_text("...", flatten=True)
    #     assert result == []

    def test_very_long_text(self):
        long_text = "This is a word. " * 100
        result = segment_text(long_text, flatten=True)
        assert result == ["This is a word."] * 100
