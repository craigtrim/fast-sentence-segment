# -*- coding: UTF-8 -*-
"""Various punctuation marks."""

from fast_sentence_segment import segment_text


class TestPunctuation:
    """Various punctuation marks."""

    def test_question_mark(self):
        result = segment_text("How are you? I am fine.", flatten=True)
        assert result == ["How are you?", "I am fine."]

    def test_exclamation(self):
        result = segment_text("Wow! That is amazing.", flatten=True)
        assert result == ["Wow!", "That is amazing."]

    def test_multiple_question_marks(self):
        # ??? followed by capital letter is a sentence boundary
        result = segment_text("What??? Are you serious?", flatten=True)
        assert result == ["What???", "Are you serious?"]

    def test_ellipsis(self):
        # Ellipsis followed by capital letter is a sentence boundary, but ... is preserved
        result = segment_text("Well... I think so.", flatten=True)
        assert result == ["Well...", "I think so."]
