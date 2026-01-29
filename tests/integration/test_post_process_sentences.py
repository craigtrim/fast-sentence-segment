# -*- coding: UTF-8 -*-
"""Tests for post-process sentence cleanup.

The PostProcessStructure component normalizes punctuation artifacts
left over from earlier pipeline stages. It replaces patterns like
'..' with '. ' and '?.' with '? '.

Note: The replacement map uses literal string substitution, so
'..' -> '. ' can produce double spaces when followed by a space
in the original text. This is the actual behavior of the component.
"""

import pytest
from fast_sentence_segment.dmo.post_process_sentences import PostProcessStructure


@pytest.fixture
def processor():
    return PostProcessStructure()


class TestDoublePeriodCleanup:
    """Replace '..' and '. .' with '. '."""

    def test_double_period_end(self, processor):
        """'..' at end of sentence becomes '. ' (trailing space stripped)."""
        result = processor.process(["Hello world.."])
        assert result == ["Hello world."]

    def test_period_space_period_end(self, processor):
        result = processor.process(["Hello world. ."])
        assert result == ["Hello world."]

    def test_double_period_mid(self, processor):
        """'..' mid-text: literal replacement of '..' with '. '."""
        result = processor.process(["Hello..World"])
        assert result == ["Hello. World"]


class TestCommaCleanup:
    """Replace ',.' and ', .' with ', '."""

    def test_comma_period_end(self, processor):
        result = processor.process(["Hello,."])
        assert result == ["Hello,"]

    def test_comma_period_mid(self, processor):
        result = processor.process(["Hello,.World"])
        assert result == ["Hello, World"]

    def test_comma_space_period_end(self, processor):
        result = processor.process(["Hello, ."])
        assert result == ["Hello,"]


class TestExclamationCleanup:
    """Replace '!.' and '! .' with '! '."""

    def test_exclamation_period_end(self, processor):
        result = processor.process(["Hello!."])
        assert result == ["Hello!"]

    def test_exclamation_period_mid(self, processor):
        result = processor.process(["Hello!.World"])
        assert result == ["Hello! World"]


class TestQuestionCleanup:
    """Replace '?.' and '? .' with '? '."""

    def test_question_period_end(self, processor):
        result = processor.process(["Hello?."])
        assert result == ["Hello?"]

    def test_question_period_mid(self, processor):
        result = processor.process(["Hello?.World"])
        assert result == ["Hello? World"]


class TestColonCleanup:
    """Replace ':.' and ': .' with ': '."""

    def test_colon_period_end(self, processor):
        result = processor.process(["Hello:."])
        assert result == ["Hello:"]

    def test_colon_period_mid(self, processor):
        result = processor.process(["Hello:.World"])
        assert result == ["Hello: World"]


class TestMultipleSentences:
    """Process lists with multiple sentences."""

    def test_multiple_sentences(self, processor):
        result = processor.process(["Hello..end", "Foo?.bar"])
        assert result == ["Hello. end", "Foo? bar"]


class TestNoChange:
    """Sentences that need no cleanup pass through unchanged."""

    def test_clean_sentence(self, processor):
        result = processor.process(["Hello, world."])
        assert result == ["Hello, world."]

    def test_empty_list(self, processor):
        assert processor.process([]) == []
