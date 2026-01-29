# -*- coding: UTF-8 -*-
"""Tests for abbreviation splitter.

The AbbreviationSplitter splits sentences where spaCy fails to detect
a boundary after a sentence-ending abbreviation followed by a capital
letter (e.g., "I woke at 6 a.m. It was dark.").

Reference:
    https://github.com/craigtrim/fast-sentence-segment/issues/3
"""

import pytest
from fast_sentence_segment.dmo.abbreviation_splitter import AbbreviationSplitter


@pytest.fixture
def splitter():
    return AbbreviationSplitter()


class TestSplitAtAbbreviationBoundary:
    """Split sentences at known abbreviation + capital letter boundaries."""

    def test_split_at_am(self, splitter):
        sentences = ["I woke at 6 a.m. It was dark."]
        result = splitter.process(sentences)
        assert result == ["I woke at 6 a.m.", "It was dark."]

    def test_split_at_pm(self, splitter):
        sentences = ["The meeting ends at 5 p.m. Please be on time."]
        result = splitter.process(sentences)
        assert result == ["The meeting ends at 5 p.m.", "Please be on time."]

    def test_split_at_etc(self, splitter):
        sentences = ["Bring food, drinks, etc. The party starts soon."]
        result = splitter.process(sentences)
        assert result == ["Bring food, drinks, etc.", "The party starts soon."]

    def test_split_at_inc(self, splitter):
        sentences = ["He works at Acme Inc. She works elsewhere."]
        result = splitter.process(sentences)
        assert result == ["He works at Acme Inc.", "She works elsewhere."]


class TestNoSplit:
    """Cases that should NOT be split."""

    def test_no_abbreviation(self, splitter):
        sentences = ["This is a normal sentence."]
        result = splitter.process(sentences)
        assert result == ["This is a normal sentence."]

    def test_abbreviation_without_capital(self, splitter):
        """Abbreviation followed by lowercase should not split."""
        sentences = ["I arrived at 6 a.m. and left early."]
        result = splitter.process(sentences)
        assert result == ["I arrived at 6 a.m. and left early."]

    def test_empty_list(self, splitter):
        assert splitter.process([]) == []

    def test_vs_not_split(self, splitter):
        """'vs.' is a title abbreviation -- never a sentence ender."""
        sentences = ["It was Smith vs. Jones in the final."]
        result = splitter.process(sentences)
        assert result == ["It was Smith vs. Jones in the final."]

    def test_multiple_sentences_no_split(self, splitter):
        sentences = ["Hello.", "World."]
        result = splitter.process(sentences)
        assert result == ["Hello.", "World."]


class TestMultipleSplits:
    """Sentences with multiple abbreviation boundaries."""

    def test_two_abbreviation_splits(self, splitter):
        sentences = ["I woke at 6 a.m. It was dark. I left at 7 p.m. The sun had set."]
        result = splitter.process(sentences)
        assert len(result) >= 3
        assert result[0] == "I woke at 6 a.m."
