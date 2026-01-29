# -*- coding: UTF-8 -*-
"""Basic sentence segmentation tests."""

from fast_sentence_segment import segment_text


class TestBasicSegmentation:
    """Basic sentence segmentation tests."""

    def test_single_sentence(self):
        result = segment_text("Hello world.", flatten=True)
        assert result == ["Hello world."]

    def test_two_sentences(self):
        result = segment_text("Hello world. Goodbye world.", flatten=True)
        assert result == ["Hello world.", "Goodbye world."]

    def test_three_sentences(self):
        result = segment_text("One. Two. Three.", flatten=True)
        assert result == ["One.", "Two.", "Three."]

    def test_no_period_preserved(self):
        result = segment_text("Hello world", flatten=True)
        assert result == ["Hello world"]
