# -*- coding: UTF-8 -*-
"""Tests for quote-aware sentence grouping.

Related GitHub Issue:
    #5 - Normalize quotes and group open-quote sentences in unwrap mode
    https://github.com/craigtrim/fast-sentence-segment/issues/5
"""

import pytest
from fast_sentence_segment.dmo.group_quoted_sentences import (
    group_quoted_sentences,
    format_grouped_sentences,
)


class TestGroupQuotedSentences:
    """Test sentence grouping based on open/close quote tracking."""

    def test_no_quotes(self):
        """Sentences without quotes each form their own group."""
        sentences = ['First.', 'Second.', 'Third.']
        result = group_quoted_sentences(sentences)
        assert result == [['First.'], ['Second.'], ['Third.']]

    def test_open_and_close_in_same_sentence(self):
        """A sentence with balanced quotes forms its own group."""
        sentences = ['"Hello," she said.', 'He nodded.']
        result = group_quoted_sentences(sentences)
        assert result == [['"Hello," she said.'], ['He nodded.']]

    def test_open_quote_spans_two_sentences(self):
        """An unclosed quote groups the next sentence with the opener."""
        sentences = [
            '"The probability lies in that direction.',
            'And if we take this as a working hypothesis."',
            'He paused.',
        ]
        result = group_quoted_sentences(sentences)
        assert result == [
            [
                '"The probability lies in that direction.',
                'And if we take this as a working hypothesis."',
            ],
            ['He paused.'],
        ]

    def test_open_quote_spans_three_sentences(self):
        """A quote spanning three sentences keeps them all grouped."""
        sentences = [
            '"First sentence.',
            'Second sentence.',
            'Third sentence."',
            'Outside.',
        ]
        result = group_quoted_sentences(sentences)
        assert result == [
            ['"First sentence.', 'Second sentence.', 'Third sentence."'],
            ['Outside.'],
        ]

    def test_multiple_quoted_spans(self):
        """Multiple quoted passages each form their own groups."""
        sentences = [
            '"Hello.',
            'World."',
            'Narration.',
            '"Goodbye.',
            'Farewell."',
        ]
        result = group_quoted_sentences(sentences)
        assert result == [
            ['"Hello.', 'World."'],
            ['Narration.'],
            ['"Goodbye.', 'Farewell."'],
        ]

    def test_empty_list(self):
        assert group_quoted_sentences([]) == []

    def test_single_sentence(self):
        assert group_quoted_sentences(['Hello.']) == [['Hello.']]

    def test_unclosed_quote_at_end(self):
        """If the quote is never closed, all remaining sentences group together."""
        sentences = ['"Start.', 'Middle.', 'End.']
        result = group_quoted_sentences(sentences)
        assert result == [['"Start.', 'Middle.', 'End.']]


class TestFormatGroupedSentences:
    """Test the full formatting output."""

    def test_basic_formatting(self):
        sentences = [
            '"The probability lies in that direction.',
            'And if we take this as a working hypothesis."',
            'He paused.',
        ]
        result = format_grouped_sentences(sentences)
        expected = (
            '"The probability lies in that direction.\n'
            'And if we take this as a working hypothesis."\n'
            '\n'
            'He paused.'
        )
        assert result == expected

    def test_no_quotes_formatting(self):
        """Without quotes, every sentence is separated by blank lines."""
        sentences = ['First.', 'Second.', 'Third.']
        result = format_grouped_sentences(sentences)
        assert result == 'First.\n\nSecond.\n\nThird.'

    def test_empty_list_formatting(self):
        assert format_grouped_sentences([]) == ''

    def test_single_sentence_formatting(self):
        assert format_grouped_sentences(['Hello.']) == 'Hello.'
