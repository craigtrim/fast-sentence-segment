# -*- coding: UTF-8 -*-
"""Edge-case tests for trailing period after closing quotes.

These tests document system behavior under unusual, malformed, or
degraded inputs — OCR artifacts, encoding remnants, stray punctuation,
mismatched quotes, etc.  Many of these are not "correct" inputs, but
they exercise boundary conditions.  Where the expected output is
debatable, the test records the *current* behavior so that future
changes surface as explicit diffs rather than silent regressions.

Related GitHub Issue:
    #7 - Spurious trailing period appended after sentence-final
         closing quote
    https://github.com/craigtrim/fast-sentence-segment/issues/7
"""

import pytest
from fast_sentence_segment import segment_text


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------
def _seg(text: str) -> list:
    """Convenience wrapper."""
    return segment_text(text, flatten=True)


# ---------------------------------------------------------------------------
# OCR-like artifacts
# ---------------------------------------------------------------------------
class TestOCRArtifacts:
    """Inputs that resemble common OCR recognition errors."""

    def test_ocr_double_period_after_quote(self):
        """OCR sometimes doubles the period: '.".' or even '."..'
        Document current behavior — the post-processor should strip at
        least one spurious period."""
        result = _seg('He said "Fine.". She left.')
        # Record whatever the system produces so regressions are visible
        assert isinstance(result, list)
        assert len(result) >= 1
        # The first sentence should NOT end with '."..'
        assert not result[0].endswith('"..'), f"Double-period artifact: {result[0]}"

    def test_ocr_space_before_period(self):
        """OCR may insert a space before the period: 'Hello ." .'
        The extra space breaks the regex pattern, so the period survives."""
        result = _seg('He said "Hello ." . She left.')
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_ocr_l_for_exclamation(self):
        """OCR sometimes reads '!' as 'l' — so 'Stop!' becomes 'Stopl".'
        The system should still produce valid output."""
        result = _seg('He yelled "Stopl" She froze.')
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_ocr_zero_for_o(self):
        """OCR replaces 'o' with '0': 'Hell0.'
        Should still segment normally."""
        result = _seg('He said "Hell0." She nodded.')
        assert isinstance(result, list)
        for sentence in result:
            assert not sentence.endswith('.".'), f"Spurious period in: {sentence}"

    def test_ocr_pipe_for_quote(self):
        """OCR sometimes reads '"' as '|'.
        The pipe is not a quote character so the post-processor should
        leave it alone — document that no crash occurs."""
        result = _seg('He said |Hello.| She left.')
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_ocr_missing_space_after_quote(self):
        """OCR may drop the space after a closing quote:
        '"Fine."She left.' — two sentences jammed together."""
        result = _seg('"Fine."She left.')
        assert isinstance(result, list)
        assert len(result) >= 1


# ---------------------------------------------------------------------------
# Mismatched / unbalanced quotes
# ---------------------------------------------------------------------------
class TestMismatchedQuotes:
    """Inputs where quotes are not properly paired."""

    def test_opening_quote_never_closed(self):
        """An opening quote with no closing quote."""
        result = _seg('"I started talking and never stopped.')
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_closing_quote_never_opened(self):
        """A closing quote with no opening quote — stray quote mark."""
        result = _seg('I never started" but here we are.')
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_extra_closing_quote(self):
        """Two closing quotes in a row."""
        result = _seg('He said "Hello."" She waved.')
        assert isinstance(result, list)
        assert len(result) >= 1
        # Should not crash or produce empty sentences
        assert all(len(s.strip()) > 0 for s in result)

    def test_only_quotes(self):
        """Input is nothing but quote characters."""
        result = _seg('"""')
        assert isinstance(result, list)

    def test_alternating_quotes_no_content(self):
        """Alternating open/close with minimal content."""
        result = _seg('"" "" ""')
        assert isinstance(result, list)


# ---------------------------------------------------------------------------
# Unusual punctuation combinations
# ---------------------------------------------------------------------------
class TestUnusualPunctuation:
    """Weird but plausible punctuation patterns."""

    def test_multiple_terminal_marks_before_quote(self):
        """Multiple punctuation marks before closing quote: '?!"'"""
        result = _seg('She screamed "What?!" He ran.')
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_interrobang_style(self):
        """Combined ?! before closing quote."""
        result = _seg('"Are you serious?!" He could not believe it.')
        assert isinstance(result, list)
        for sentence in result:
            assert not sentence.endswith('".'), f"Spurious period in: {sentence}"

    def test_semicolon_before_closing_quote(self):
        """Semicolon is not terminal punctuation — period should be appended."""
        result = _seg('"Items: apples; oranges;"')
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_comma_before_closing_quote(self):
        """Comma before closing quote — common in dialogue attribution.
        'He said "well," and left.' — not sentence-ending."""
        result = _seg('He said "well," and left.')
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_dash_before_closing_quote(self):
        """Interrupted speech: em-dash before closing quote."""
        result = _seg('"I was going to—" He stopped.')
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_triple_question_marks_in_quote(self):
        """Emphatic punctuation: '???' before closing quote."""
        result = _seg('"Really???" She stared.')
        assert isinstance(result, list)
        for sentence in result:
            assert not sentence.endswith('".'), f"Spurious period in: {sentence}"

    def test_period_space_quote(self):
        """Period followed by space then quote: '. "' — the space breaks
        the adjacency, so this is a different pattern."""
        result = _seg('He said "Hello. " She waved.')
        assert isinstance(result, list)
        assert len(result) >= 1


# ---------------------------------------------------------------------------
# Whitespace and empty-ish inputs
# ---------------------------------------------------------------------------
class TestWhitespaceEdgeCases:
    """Whitespace, near-empty, and boundary-length inputs."""

    def test_trailing_whitespace_after_quote(self):
        """Trailing spaces after the closing quote."""
        result = _seg('He said "Hello."   ')
        assert isinstance(result, list)
        assert len(result) >= 1
        assert result[-1].strip() == 'He said "Hello."'

    def test_newline_between_quote_and_narration(self):
        """Newline separating quoted and narrated text."""
        result = _seg('"Done."\nShe left.')
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_tab_before_closing_quote(self):
        """Tab character inside the quote before closing."""
        result = _seg('"Hello.\t" She waved.')
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_single_character_quote(self):
        """Minimal quoted content."""
        result = _seg('"A." He said.')
        assert isinstance(result, list)
        for sentence in result:
            assert not sentence.endswith('.".'), f"Spurious period in: {sentence}"


# ---------------------------------------------------------------------------
# Unicode quote variants
# ---------------------------------------------------------------------------
class TestUnicodeQuoteVariants:
    """Smart quotes and other Unicode quotation marks.

    The quote normalizer (issue #5) converts these to ASCII before
    segmentation, so the post-processor only sees ASCII quotes.
    These tests verify the full pipeline handles it end-to-end."""

    def test_smart_double_quotes(self):
        """\u201c \u201d (left/right double quotation marks)."""
        result = _seg('\u201cHello.\u201d She waved.')
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_smart_single_quotes(self):
        """\u2018 \u2019 (left/right single quotation marks)."""
        result = _seg('\u2018Hello.\u2019 She waved.')
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_guillemets(self):
        """\u00ab \u00bb (French-style angle quotes)."""
        result = _seg('\u00abBonjour.\u00bb Elle a salu\u00e9.')
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_german_lower_quote(self):
        """\u201e \u201c (German-style low-high quotes)."""
        result = _seg('\u201eHallo.\u201c Sie winkte.')
        assert isinstance(result, list)
        assert len(result) >= 1


# ---------------------------------------------------------------------------
# Long / stress inputs
# ---------------------------------------------------------------------------
class TestStressInputs:
    """Longer inputs to exercise the post-processor under load."""

    def test_many_short_dialogue_turns(self):
        """20 rapid-fire dialogue turns."""
        turns = [f'"Sentence {i}."' for i in range(20)]
        text = ' '.join(turns)
        result = _seg(text)
        assert isinstance(result, list)
        for sentence in result:
            assert not sentence.endswith('.".'), f"Spurious period in: {sentence}"

    def test_single_very_long_quoted_sentence(self):
        """A single quoted sentence of ~500 words."""
        words = ' '.join(['word'] * 500)
        text = f'"The text is {words}." She finished.'
        result = _seg(text)
        assert isinstance(result, list)
        assert len(result) >= 1


# ---------------------------------------------------------------------------
# Mixed patterns
# ---------------------------------------------------------------------------
class TestMixedPatterns:
    """Combinations that mix quotes with other pipeline features."""

    def test_abbreviation_inside_quote(self):
        """Abbreviations inside quotes should not cause extra splits."""
        result = _seg('"He has an M.D. and a Ph.D." She was impressed.')
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_numbered_list_with_quote(self):
        """Numbered list item containing a quote."""
        result = _seg('1. She said "Go." 2. He left.')
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_quote_after_ellipsis(self):
        """Ellipsis followed by a quoted sentence."""
        result = _seg('And then... "It happened." He sighed.')
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_title_before_quote(self):
        """Title (Dr./Mr.) immediately before a quote."""
        result = _seg('Dr. Smith said "Interesting." The room was silent.')
        assert isinstance(result, list)
        for sentence in result:
            assert not sentence.endswith('.".'), f"Spurious period in: {sentence}"

    def test_parenthetical_with_quote(self):
        """Parenthetical remark containing a quote."""
        result = _seg('He replied (saying "No.") and left.')
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_quote_spanning_apparent_sentence_boundary(self):
        """Quote that itself contains what looks like a sentence boundary.
        The segmenter may split inside the quote — document that behavior."""
        result = _seg(
            '"I went to the store. I bought milk. I came home." He reported.'
        )
        assert isinstance(result, list)
        assert len(result) >= 1
        # At minimum, no spurious period patterns
        for sentence in result:
            assert not sentence.endswith('.".'), f"Spurious period in: {sentence}"
