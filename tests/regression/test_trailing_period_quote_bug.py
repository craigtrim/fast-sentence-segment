# -*- coding: UTF-8 -*-
"""Regression tests for spurious trailing period after closing quotes.

The _append_period method in SpacyDocSegmenter was appending a period
after sentences that end with a closing quote preceded by terminal
punctuation (. ? !), producing patterns like:
    'He said "Hello.".'   (wrong)
    'She asked "Why?".'   (wrong)

Related GitHub Issue:
    #7 - Spurious trailing period appended after sentence-final
         closing quote
    https://github.com/craigtrim/fast-sentence-segment/issues/7
"""

import pytest
from fast_sentence_segment import segment_text


class TestNoSpuriousPeriodAfterQuote:
    """Verify that sentences ending with punctuation inside quotes
    do not get a spurious trailing period."""

    def test_period_inside_closing_quote(self):
        """Pattern: ." should not become ."."""
        result = segment_text(
            'He said "Hello." She waved.', flatten=True
        )
        assert result[0] == 'He said "Hello."'

    def test_question_mark_inside_closing_quote(self):
        """Pattern: ?" should not become ?"."""
        result = segment_text(
            'She asked "Why?" He shrugged.', flatten=True
        )
        assert result[0] == 'She asked "Why?"'

    def test_exclamation_inside_closing_quote(self):
        """Pattern: !" should not become !"."""
        result = segment_text(
            'He yelled "Stop!" Everyone froze.', flatten=True
        )
        assert result[0] == 'He yelled "Stop!"'

    def test_dialogue_sequence(self):
        """Multiple dialogue sentences should have no spurious periods."""
        text = (
            '"Yes, I am." '
            '"Then we shall do it together." '
            'He nodded.'
        )
        result = segment_text(text, flatten=True)
        for sentence in result:
            # No sentence should end with ."." or ?"." or !"."
            assert not sentence.endswith('.".'), f"Spurious period in: {sentence}"
            assert not sentence.endswith('?.'), f"Spurious period in: {sentence}"
            assert not sentence.endswith('!.'), f"Spurious period in: {sentence}"

    def test_plain_sentence_append_period_directly(self):
        """The _append_period method should add a period to unterminated text."""
        from fast_sentence_segment.dmo.spacy_doc_segmenter import SpacyDocSegmenter
        assert SpacyDocSegmenter._append_period('Hello world') == 'Hello world.'

    def test_sentence_ending_with_period_unchanged(self):
        """Sentences already ending with a period stay unchanged."""
        result = segment_text('Hello world.', flatten=True)
        assert result[0] == 'Hello world.'
        assert not result[0].endswith('..')

    def test_sentence_ending_with_question_mark_unchanged(self):
        """Sentences ending with ? stay unchanged."""
        result = segment_text('Is it done?', flatten=True)
        assert result[0] == 'Is it done?'

    def test_sentence_ending_with_exclamation_unchanged(self):
        """Sentences ending with ! stay unchanged."""
        result = segment_text('Stop right there!', flatten=True)
        assert result[0] == 'Stop right there!'

    def test_single_quote_wrapping(self):
        """Terminal punctuation inside single quotes should not trigger
        a spurious period either."""
        result = segment_text(
            "He said 'Hello.' She waved.", flatten=True
        )
        assert not result[0].endswith(".'.")

    def test_multiple_sentences_inside_quotes(self):
        """Quoted passage containing multiple sentences."""
        result = segment_text(
            '"I came. I saw. I conquered." He smiled.', flatten=True
        )
        for sentence in result:
            assert not sentence.endswith('.".'), f"Spurious period in: {sentence}"

    def test_quote_at_end_of_input(self):
        """Input that ends entirely with a quoted sentence."""
        result = segment_text(
            'She whispered "Goodbye."', flatten=True
        )
        assert result[-1] == 'She whispered "Goodbye."'

    def test_nested_punctuation_question_exclamation(self):
        """Alternating question and exclamation inside quotes."""
        result = segment_text(
            '"Really?" "Yes!" He laughed.', flatten=True
        )
        for sentence in result:
            assert not sentence.endswith('".'), f"Spurious period in: {sentence}"

    def test_ellipsis_inside_quote(self):
        """Ellipsis before closing quote should not gain a period."""
        result = segment_text(
            'He trailed off: "I wonder..." She waited.', flatten=True
        )
        for sentence in result:
            assert not sentence.endswith('...".'), f"Spurious period in: {sentence}"

    def test_colon_before_quote(self):
        """Sentence with colon introducing a quote."""
        result = segment_text(
            'He said: "Fine." She nodded.', flatten=True
        )
        for sentence in result:
            assert not sentence.endswith('.".'), f"Spurious period in: {sentence}"

    def test_long_dialogue_exchange(self):
        """Extended dialogue with alternating speakers."""
        text = (
            '"Where are you going?" '
            '"To the store." '
            '"Can I come?" '
            '"Of course!" '
            'They left together.'
        )
        result = segment_text(text, flatten=True)
        for sentence in result:
            assert not sentence.endswith('.".'), f"Spurious period in: {sentence}"
            assert not sentence.endswith('?.'), f"Spurious period in: {sentence}"
            assert not sentence.endswith('!.'), f"Spurious period in: {sentence}"

    def test_quote_only_input(self):
        """Input that is entirely a quoted sentence."""
        result = segment_text('"Hello world."', flatten=True)
        assert result[0] == '"Hello world."'

    def test_mid_sentence_quote_no_terminal(self):
        """Quote in middle of sentence without terminal punctuation inside."""
        result = segment_text(
            'He called it "the best" and moved on.', flatten=True
        )
        assert result[0] == 'He called it "the best" and moved on.'

    def test_back_to_back_quoted_sentences(self):
        """Consecutive quoted sentences with no narration between."""
        result = segment_text('"Stop." "Go." "Wait."', flatten=True)
        for sentence in result:
            assert not sentence.endswith('.".'), f"Spurious period in: {sentence}"
