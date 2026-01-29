# -*- coding: UTF-8 -*-
"""Tests for question/exclamation splitter.

The QuestionExclamationSplitter splits sentences at ? and ! boundaries
when followed by a space and capital letter, since spaCy doesn't always
detect these boundaries.

Reference:
    https://github.com/craigtrim/fast-sentence-segment/issues/3
"""

import pytest
from fast_sentence_segment.dmo.question_exclamation_splitter import (
    QuestionExclamationSplitter,
)


@pytest.fixture
def splitter():
    return QuestionExclamationSplitter()


class TestSplitAtQuestionMark:
    """Split at ? followed by capital letter."""

    def test_question_then_statement(self, splitter):
        sentences = ["Is it raining? The sky looks clear."]
        result = splitter.process(sentences)
        assert result == ["Is it raining?", "The sky looks clear."]

    def test_question_then_question(self, splitter):
        sentences = ["Where are you? What happened?"]
        result = splitter.process(sentences)
        assert result == ["Where are you?", "What happened?"]

    def test_question_lowercase_no_split(self, splitter):
        """? followed by lowercase should not split."""
        sentences = ["Is it the one? he asked."]
        result = splitter.process(sentences)
        assert result == ["Is it the one? he asked."]


class TestSplitAtExclamation:
    """Split at ! followed by capital letter."""

    def test_exclamation_then_statement(self, splitter):
        sentences = ["Stop! The bridge is out."]
        result = splitter.process(sentences)
        assert result == ["Stop!", "The bridge is out."]

    def test_exclamation_then_exclamation(self, splitter):
        sentences = ["Run! Hide! They are coming."]
        result = splitter.process(sentences)
        assert result == ["Run!", "Hide!", "They are coming."]

    def test_exclamation_lowercase_no_split(self, splitter):
        """! followed by lowercase should not split."""
        sentences = ["Oh! she exclaimed softly."]
        result = splitter.process(sentences)
        assert result == ["Oh! she exclaimed softly."]


class TestNoSplit:
    """Cases that should NOT be split."""

    def test_no_punctuation(self, splitter):
        sentences = ["This is a normal sentence."]
        result = splitter.process(sentences)
        assert result == ["This is a normal sentence."]

    def test_empty_list(self, splitter):
        assert splitter.process([]) == []

    def test_period_not_split(self, splitter):
        """Periods should not trigger splitting here."""
        sentences = ["Hello. World."]
        result = splitter.process(sentences)
        assert result == ["Hello. World."]


class TestMixed:
    """Mixed question and exclamation marks."""

    def test_question_and_exclamation(self, splitter):
        sentences = ["What? No! That is impossible."]
        result = splitter.process(sentences)
        assert result == ["What?", "No!", "That is impossible."]
