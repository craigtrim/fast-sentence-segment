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

    def test_double_spaces_normalized(self):
        """Double spaces in original text are normalized to single spaces.

        This prevents _clean_spacing from treating them as sentence boundaries
        and creating spurious periods like "His colour. mounted" from "His colour  mounted".
        """
        text = "His colour  mounted; he fixed his neighbour's pale eye."
        result = unwrap_hard_wrapped_text(text)
        assert result == "His colour mounted; he fixed his neighbour's pale eye."

    def test_triple_spaces_normalized(self):
        """Triple or more spaces are normalized to single space."""
        text = "The ship   sailed   into the harbor."
        result = unwrap_hard_wrapped_text(text)
        assert result == "The ship sailed into the harbor."

    def test_multiple_double_spaces(self):
        """Multiple double-space occurrences are all normalized."""
        text = "Jack  Aubrey's  face  changed."
        result = unwrap_hard_wrapped_text(text)
        assert result == "Jack Aubrey's face changed."

    def test_mixed_spacing_normalization(self):
        """Various spacing issues from OCR are normalized."""
        text = "He could not  but acknowledge  that he had been   beating the time."
        result = unwrap_hard_wrapped_text(text)
        assert result == "He could not but acknowledge that he had been beating the time."


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

    def test_unwrap_honorific_at_line_end(self):
        """Honorifics like Mr. at end of line should stay with the following name.

        In hard-wrapped text, "Mr." may appear at the end of a line with the
        name continuing on the next line. After unwrapping, "Mr. William"
        should be on the same line, not split.
        """
        text = "To Mr.\nWilliam Marshall, then, Master of His Majesty's sloop the Sophie."
        result = segment_text(text, flatten=True, unwrap=True)
        # Should be a single sentence with "Mr. William" together
        assert len(result) == 1
        assert "Mr. William" in result[0]
        assert "To Mr." in result[0]

    def test_unwrap_mid_sentence_line_break(self):
        """Hard-wrapped lines mid-sentence should be joined.

        When text is hard-wrapped in the middle of a sentence (e.g., after
        "no pleasure"), unwrapping should join the lines into one sentence.
        """
        text = "straightforward winding-up that he had foreseen, but he could take no pleasure\nin it."
        result = segment_text(text, flatten=True, unwrap=True)
        assert len(result) == 1
        assert "no pleasure in it" in result[0]
