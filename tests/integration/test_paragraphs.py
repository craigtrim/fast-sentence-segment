# -*- coding: UTF-8 -*-
"""Test paragraph-aware segmentation (the core feature)."""

from fast_sentence_segment import segment_text


class TestParagraphs:
    """Test paragraph-aware segmentation (the core feature)."""

    def test_single_paragraph(self):
        result = segment_text("First sentence. Second sentence.")
        assert result == [["First sentence.", "Second sentence."]]

    def test_two_paragraphs(self):
        text = "First paragraph sentence one. Sentence two.\n\nSecond paragraph here."
        result = segment_text(text)
        assert result == [
            ["First paragraph sentence one.", "Sentence two."],
            ["Second paragraph here."]
        ]

    def test_three_paragraphs(self):
        text = "Para one.\n\nPara two.\n\nPara three."
        result = segment_text(text)
        assert result == [
            ["Para one."],
            ["Para two."],
            ["Para three."]
        ]

    def test_flatten_collapses_paragraphs(self):
        text = "Para one.\n\nPara two."
        flat = segment_text(text, flatten=True)
        nested = segment_text(text, flatten=False)
        assert flat == ["Para one.", "Para two."]
        assert nested == [["Para one."], ["Para two."]]
