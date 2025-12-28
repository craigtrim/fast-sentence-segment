# -*- coding: UTF-8 -*-
"""Abbreviations should NOT trigger sentence splits."""

from fast_sentence_segment import segment_text


class TestAbbreviations:
    """Abbreviations should NOT trigger sentence splits."""

    def test_dr(self):
        result = segment_text("Dr. Smith is here.", flatten=True)
        assert result == ["Dr. Smith is here."]

    def test_mr_mrs_ms(self):
        result = segment_text("Mr. and Mrs. Jones met Ms. Davis.", flatten=True)
        assert result == ["Mr. and Mrs. Jones met Ms. Davis."]

    def test_academic_titles(self):
        result = segment_text("She has a Ph.D. and an M.D. degree.", flatten=True)
        assert result == ["She has a Ph.D. and an M.D. degree."]

    def test_us_uk(self):
        result = segment_text("The U.S. and U.K. are allies.", flatten=True)
        assert result == ["The U.S. and U.K. are allies."]

    def test_etc(self):
        result = segment_text("Apples, oranges, etc. are fruits.", flatten=True)
        assert result == ["Apples, oranges, etc. are fruits."]

    def test_st_street(self):
        result = segment_text("He lives on Main St. in town.", flatten=True)
        assert result == ["He lives on Main St. in town."]
