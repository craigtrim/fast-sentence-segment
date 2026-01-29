# -*- coding: UTF-8 -*-
"""Tests for paragraph segmentation.

The PerformParagraphSegmentation component splits text into paragraphs
on double-newline boundaries.
"""

import pytest
from fast_sentence_segment.svc.perform_paragraph_segmentation import (
    PerformParagraphSegmentation,
)


@pytest.fixture
def segmenter():
    return PerformParagraphSegmentation()


class TestBasicParagraphSplit:
    """Split text on double-newline boundaries."""

    def test_two_paragraphs(self, segmenter):
        text = "First paragraph.\n\nSecond paragraph."
        result = segmenter.process(text)
        assert result == ["First paragraph.", "Second paragraph."]

    def test_three_paragraphs(self, segmenter):
        text = "One.\n\nTwo.\n\nThree."
        result = segmenter.process(text)
        assert result == ["One.", "Two.", "Three."]

    def test_single_paragraph(self, segmenter):
        text = "Just one paragraph."
        result = segmenter.process(text)
        assert result == ["Just one paragraph."]


class TestWhitespaceHandling:
    """Whitespace around paragraphs is stripped."""

    def test_leading_trailing_whitespace(self, segmenter):
        text = "  First.  \n\n  Second.  "
        result = segmenter.process(text)
        assert result == ["First.", "Second."]

    def test_multiple_blank_lines(self, segmenter):
        """Multiple blank lines still split into paragraphs."""
        text = "First.\n\n\n\nSecond."
        result = segmenter.process(text)
        # Split on \n\n produces ["First.", "", "Second."] -- empties filtered
        assert "First." in result
        assert "Second." in result

    def test_single_newline_no_split(self, segmenter):
        """Single newline does NOT split into paragraphs."""
        text = "Line one.\nLine two."
        result = segmenter.process(text)
        assert len(result) == 1


class TestErrorHandling:
    """Error handling for invalid input."""

    def test_empty_string_raises(self, segmenter):
        with pytest.raises(ValueError):
            segmenter.process("")

    def test_none_raises(self, segmenter):
        with pytest.raises((ValueError, TypeError)):
            segmenter.process(None)
