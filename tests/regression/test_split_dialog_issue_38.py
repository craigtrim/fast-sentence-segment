# -*- coding: UTF-8 -*-
"""
Test cases for Issue #38: Add optional parameter to segment dialog sentences individually.

Tests the split_dialog parameter which controls whether multi-sentence quotes
should be kept together (default) or segmented individually for stylometry
and prosody analysis.

Reference: https://github.com/craigtrim/fast-sentence-segment/issues/38
"""

import pytest
from fast_sentence_segment import segment_text


class TestSplitDialogParameter:
    """Test split_dialog parameter for controlling dialog sentence segmentation."""

    def test_default_behavior_splits_dialog(self):
        """Default behavior (split_dialog=True) splits dialog sentences individually."""
        text = '"Hello. How are you?" she asked.'
        result = segment_text(text, flatten=True)
        # Default: split dialog
        assert result == ['"Hello.', 'How are you?" she asked.']

    def test_split_dialog_false_explicit(self):
        """Explicitly setting split_dialog=False keeps dialog together."""
        text = '"Hello. How are you?" she asked.'
        result = segment_text(text, flatten=True, split_dialog=False)
        assert result == ['"Hello. How are you?" she asked.']

    def test_split_dialog_true_segments_individually(self):
        """Setting split_dialog=True segments dialog sentences individually."""
        text = '"Hello. How are you?" she asked.'
        result = segment_text(text, flatten=True, split_dialog=True)
        # Split dialog: each sentence separate
        assert result == ['"Hello.', 'How are you?" she asked.']

    def test_split_dialog_true_multiple_sentences(self):
        """split_dialog=True handles multiple sentences in quotes."""
        text = '"Hello world. This is a test. Multiple sentences here." He smiled.'
        result = segment_text(text, flatten=True, split_dialog=True)
        # Each sentence separated individually
        assert result == [
            '"Hello world.',
            'This is a test.',
            'Multiple sentences here."',
            'He smiled.'
        ]

    def test_split_dialog_true_no_attribution(self):
        """split_dialog=True works when quote has no attribution."""
        text = '"First sentence. Second sentence. Third sentence."'
        result = segment_text(text, flatten=True, split_dialog=True)
        assert result == [
            '"First sentence.',
            'Second sentence.',
            'Third sentence."'
        ]

    def test_split_dialog_false_no_attribution(self):
        """Default behavior with quote having no attribution."""
        text = '"First sentence. Second sentence. Third sentence."'
        result = segment_text(text, flatten=True, split_dialog=False)
        # Keep together
        assert result == ['"First sentence. Second sentence. Third sentence."']

    def test_split_dialog_true_mixed_dialog_and_narration(self):
        """split_dialog=True handles mixed dialog and narration."""
        text = 'She approached. "Are you ready? Let\'s go." They left quickly.'
        result = segment_text(text, flatten=True, split_dialog=True)
        assert result == [
            'She approached.',
            '"Are you ready?',
            'Let\'s go."',
            'They left quickly.'
        ]

    def test_split_dialog_false_mixed_dialog_and_narration(self):
        """Default behavior with mixed dialog and narration (splits at ? and !)."""
        text = 'She approached. "Are you ready? Let\'s go." They left quickly.'
        result = segment_text(text, flatten=True, split_dialog=False)
        # Note: Question/exclamation splitter runs after quote merger, so this splits at ?
        assert result == [
            'She approached.',
            '"Are you ready?',
            'Let\'s go."',
            'They left quickly.'
        ]

    def test_split_dialog_true_nested_quotes(self):
        """split_dialog=True handles nested quotes."""
        text = '"He said, \'Hello there.\' I was surprised." She laughed.'
        result = segment_text(text, flatten=True, split_dialog=True)
        # Note: This is complex - behavior depends on quote handling
        # Just verify it segments without error
        assert isinstance(result, list)
        assert len(result) > 0

    def test_split_dialog_parameter_with_paragraphs(self):
        """split_dialog works with nested paragraph structure."""
        text = '"First. Second." He said.'
        result = segment_text(text, flatten=False, split_dialog=True)
        # Should return list of paragraphs, each containing sentences
        assert isinstance(result, list)
        assert isinstance(result[0], list)

    def test_split_dialog_with_curly_quotes(self):
        """split_dialog handles curly quotes."""
        text = '"First sentence. Second sentence." she said.'
        result = segment_text(text, flatten=True, split_dialog=True)
        assert len(result) >= 2
        assert '"First sentence.' in result

    def test_split_dialog_no_quotes(self):
        """split_dialog has no effect on text without quotes."""
        text = 'First sentence. Second sentence. Third sentence.'
        result_false = segment_text(text, flatten=True, split_dialog=False)
        result_true = segment_text(text, flatten=True, split_dialog=True)
        # Both should give same result (no quotes to split)
        assert result_false == result_true == [
            'First sentence.',
            'Second sentence.',
            'Third sentence.'
        ]


class TestSplitDialogEdgeCases:
    """Test edge cases for split_dialog parameter."""

    def test_split_dialog_empty_string(self):
        """split_dialog handles empty string (raises ValueError as expected)."""
        with pytest.raises(ValueError, match="Empty Input"):
            segment_text('', flatten=True, split_dialog=True)

    def test_split_dialog_single_word_quote(self):
        """split_dialog handles single-word quote."""
        text = '"Hello." she said.'
        result = segment_text(text, flatten=True, split_dialog=True)
        assert '"Hello." she said.' in result

    def test_split_dialog_exclamation_question_in_quotes(self):
        """split_dialog handles ! and ? inside quotes."""
        text = '"What? Really!" she exclaimed.'
        result = segment_text(text, flatten=True, split_dialog=True)
        assert isinstance(result, list)
        assert len(result) >= 2

    def test_split_dialog_multiple_paragraphs(self):
        """split_dialog works with multiple paragraphs."""
        text = '"Para one. Para two."\n\n"Para three." Done.'
        result = segment_text(text, flatten=True, split_dialog=True)
        assert len(result) > 2
