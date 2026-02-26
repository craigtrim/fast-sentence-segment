# -*- coding: UTF-8 -*-
"""Tests for abbreviation merger.

The AbbreviationMerger merges sentences that spaCy incorrectly splits
at abbreviation boundaries. For example, "ext. 5" split as
["ext.", "5. Ask for help."] should be merged back.

Reference:
    https://github.com/craigtrim/fast-sentence-segment/issues/3
"""

import pytest
from fast_sentence_segment.dmo.abbreviation_merger import AbbreviationMerger


@pytest.fixture
def merger():
    return AbbreviationMerger()


class TestMergeExtension:
    """Merge 'ext.' with following number."""

    def test_ext_lowercase(self, merger):
        sentences = ["Call ext.", "5. Ask for help."]
        result = merger.process(sentences)
        assert result == ["Call ext. 5.", "Ask for help."]

    def test_ext_uppercase(self, merger):
        sentences = ["Call EXT.", "123. Ask for help."]
        result = merger.process(sentences)
        assert result == ["Call EXT. 123.", "Ask for help."]

    def test_ext_mixed_case(self, merger):
        sentences = ["Call Ext.", "42"]
        result = merger.process(sentences)
        assert result == ["Call Ext. 42"]


class TestMergeNumber:
    """Merge 'no.' with following number."""

    def test_no_lowercase(self, merger):
        sentences = ["Item no.", "5 is here."]
        result = merger.process(sentences)
        assert result == ["Item no. 5 is here."]

    def test_no_uppercase(self, merger):
        sentences = ["No.", "42 was selected."]
        result = merger.process(sentences)
        assert result == ["No. 42 was selected."]


class TestMergeVolume:
    """Merge 'vol.' with following number."""

    def test_vol(self, merger):
        sentences = ["See vol.", "3 for details."]
        result = merger.process(sentences)
        assert result == ["See vol. 3 for details."]


class TestMergePart:
    """Merge 'pt.' with following number."""

    def test_pt(self, merger):
        sentences = ["Read pt.", "2 first."]
        result = merger.process(sentences)
        assert result == ["Read pt. 2 first."]


class TestMergeChapter:
    """Merge 'ch.' with following number."""

    def test_ch(self, merger):
        sentences = ["See ch.", "10 for context."]
        result = merger.process(sentences)
        assert result == ["See ch. 10 for context."]


class TestMergeSection:
    """Merge 'sec.' with following number (including dotted)."""

    def test_sec_simple(self, merger):
        sentences = ["Refer to sec.", "3 above."]
        result = merger.process(sentences)
        assert result == ["Refer to sec. 3 above."]

    def test_sec_dotted(self, merger):
        sentences = ["See sec.", "3.2 for details."]
        result = merger.process(sentences)
        assert result == ["See sec. 3.2 for details."]


class TestMergeFigure:
    """Merge 'fig.' with following number (including dotted)."""

    def test_fig_simple(self, merger):
        sentences = ["See fig.", "1 below."]
        result = merger.process(sentences)
        assert result == ["See fig. 1 below."]

    def test_fig_dotted(self, merger):
        sentences = ["As shown in Fig.", "3.2 the data."]
        result = merger.process(sentences)
        assert result == ["As shown in Fig. 3.2 the data."]


class TestMergePage:
    """Merge 'p.' and 'pp.' with following number."""

    def test_p_single(self, merger):
        sentences = ["See p.", "42 for reference."]
        result = merger.process(sentences)
        assert result == ["See p. 42 for reference."]

    def test_pp_range(self, merger):
        sentences = ["See pp.", "42-50 for context."]
        result = merger.process(sentences)
        assert result == ["See pp. 42-50 for context."]


class TestMergeArticle:
    """Merge 'art.' with following number."""

    def test_art(self, merger):
        sentences = ["Under art.", "5 of the treaty."]
        result = merger.process(sentences)
        assert result == ["Under art. 5 of the treaty."]


class TestNoMerge:
    """Cases that should NOT trigger a merge."""

    def test_no_match(self, merger):
        sentences = ["Hello.", "World."]
        result = merger.process(sentences)
        assert result == ["Hello.", "World."]

    def test_empty_list(self, merger):
        assert merger.process([]) == []

    def test_single_sentence(self, merger):
        assert merger.process(["Hello."]) == ["Hello."]

    def test_abbreviation_without_number(self, merger):
        sentences = ["See vol.", "The book is great."]
        result = merger.process(sentences)
        assert result == ["See vol.", "The book is great."]
