# -*- coding: UTF-8 -*-
"""Time-related abbreviations."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestTimeAbbreviations:
    """Time-related abbreviations."""

    @pytest.mark.parametrize("text,expected", [
        # a.m. and p.m.
        ("The meeting is at 9 a.m.", ["The meeting is at 9 a.m."]),
        ("We close at 5 p.m.", ["We close at 5 p.m."]),
        ("I woke up at 6 a.m. It was still dark.",
         ["I woke up at 6 a.m.", "It was still dark."]),
        ("The show starts at 8 p.m. Don't be late.",
         ["The show starts at 8 p.m.", "Don't be late."]),
        ("The store opens at 9 a.m. and closes at 9 p.m.",
         ["The store opens at 9 a.m. and closes at 9 p.m."]),

        # Alternate forms
        ("Meet me at 3 P.M.", ["Meet me at 3 P.M."]),
        ("Wake up at 7 A.M. tomorrow.",
         ["Wake up at 7 A.M. tomorrow."]),
    ])
    def test_time_abbreviations(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
