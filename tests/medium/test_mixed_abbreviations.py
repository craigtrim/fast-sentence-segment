# -*- coding: UTF-8 -*-
"""Sentences with multiple types of abbreviations."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestMixedAbbreviations:
    """Sentences with multiple types of abbreviations."""

    @pytest.mark.parametrize("text,expected", [
        # Honorific + time
        ("Dr. Smith arrives at 9 a.m. every day.",
         ["Dr. Smith arrives at 9 a.m. every day."]),

        # Honorific + acronym
        ("Dr. Lee works at the U.N. headquarters.",
         ["Dr. Lee works at the U.N. headquarters."]),

        # Multiple abbreviations
        ("Dr. J.R. Smith of Acme Inc. spoke at 3 p.m.",
         ["Dr. J.R. Smith of Acme Inc. spoke at 3 p.m."]),

        # Abbreviations with numbers
        ("Prof. Williams teaches at Room 101, Bldg. A.",
         ["Prof. Williams teaches at Room 101, Bldg. A."]),

        # Complex mix
        ("Mr. A.B. Chen, CEO of Tech Corp., arrived at 2 p.m. via St. James Ave.",
         ["Mr. A.B. Chen, CEO of Tech Corp., arrived at 2 p.m. via St. James Ave."]),
    ])
    def test_mixed_abbreviations(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
