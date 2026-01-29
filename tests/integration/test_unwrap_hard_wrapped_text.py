# -*- coding: UTF-8 -*-
"""Tests for unwrap_hard_wrapped_text and segment_text(unwrap=True)."""

import pytest

from fast_sentence_segment.dmo.unwrap_hard_wrapped_text import unwrap_hard_wrapped_text
from fast_sentence_segment import segment_text


class TestUnwrapHardWrappedText:

    def test_basic_unwrap(self):
        text = "This is a line\nthat continues here."
        result = unwrap_hard_wrapped_text(text)
        assert result == "This is a line that continues here."

    def test_indented_lines(self):
        text = "      I am bound to say that in\n      all the accounts which you have been so good"
        result = unwrap_hard_wrapped_text(text)
        assert result == "I am bound to say that in all the accounts which you have been so good"

    def test_paragraph_boundaries_preserved(self):
        text = "First paragraph line one.\nFirst paragraph line two.\n\nSecond paragraph line one.\nSecond paragraph line two."
        result = unwrap_hard_wrapped_text(text)
        assert result == "First paragraph line one. First paragraph line two.\n\nSecond paragraph line one. Second paragraph line two."

    def test_multiple_blank_lines(self):
        text = "Paragraph one.\n\n\nParagraph two."
        result = unwrap_hard_wrapped_text(text)
        assert result == "Paragraph one.\n\nParagraph two."

    def test_empty_lines_with_whitespace(self):
        text = "Paragraph one.\n   \nParagraph two."
        result = unwrap_hard_wrapped_text(text)
        assert result == "Paragraph one.\n\nParagraph two."

    def test_no_wrapping_passthrough(self):
        text = "A single line of text."
        result = unwrap_hard_wrapped_text(text)
        assert result == "A single line of text."

    def test_blank_lines_only(self):
        text = "\n\n\n"
        result = unwrap_hard_wrapped_text(text)
        assert result == ""


class TestSegmentTextUnwrap:

    def test_unwrap_false_preserves_existing_behavior(self):
        text = "      I am bound to say that in\n      all the accounts"
        result_default = segment_text(text, flatten=True)
        result_no_unwrap = segment_text(text, flatten=True, unwrap=False)
        assert result_default == result_no_unwrap

    def test_unwrap_fixes_hard_wrapped_gutenberg(self):
        text = (
            '      "I am bound to say that in\n'
            '      all the accounts which you have been so good as to give of my own\n'
            '      small achievements you have habitually underrated your own\n'
            '      abilities. It may be that you are not yourself luminous, but you\n'
            '      are a conductor of light. Some people without possessing genius\n'
            '      have a remarkable power of stimulating it. I confess, my dear\n'
            '      fellow, that I am very much in your debt."'
        )
        result = segment_text(text, flatten=True, unwrap=True)

        # No spurious periods from line joins
        for sentence in result:
            assert ".a" not in sentence.lower(), f"Spurious period found: {sentence}"
            assert ".s" not in sentence.lower() or "Mrs." in sentence or "Mr." in sentence, f"Spurious period found: {sentence}"

        # Should contain "bound to say that in all" without a period break
        full = ' '.join(result)
        assert "that in all" in full

    def test_unwrap_multi_paragraph_gutenberg(self):
        text = (
            '      "Well, Watson, what do you make of it?"\n'
            '\n'
            '      Holmes was sitting with his back to me, and I had given him no\n'
            '      sign of my occupation.'
        )
        result = segment_text(text, flatten=True, unwrap=True)
        assert len(result) >= 2
        assert "Watson" in result[0]
        assert "Holmes" in result[1]
