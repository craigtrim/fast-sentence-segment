# -*- coding: UTF-8 -*-
"""Sentences containing dates in various formats."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestDates:
    """Sentences containing dates in various formats."""

    @pytest.mark.parametrize("text,expected", [
        # Month abbreviations
        ("The meeting is on Jan. 15th.", ["The meeting is on Jan. 15th."]),
        ("We met on Feb. 3rd. It was cold.",
         ["We met on Feb. 3rd.", "It was cold."]),
        ("Her birthday is Mar. 21st.", ["Her birthday is Mar. 21st."]),
        ("We launch in Apr. 2025.", ["We launch in Apr. 2025."]),

        # Multiple dates
        ("The event runs from Aug. 1st to Sept. 5th.",
         ["The event runs from Aug. 1st to Sept. 5th."]),
        ("From Dec. 24th to Jan. 2nd, we're closed.",
         ["From Dec. 24th to Jan. 2nd, we're closed."]),

        # Full month names (no periods)
        ("The party is on December 25th. Please come.",
         ["The party is on December 25th.", "Please come."]),

        # Date followed by sentence
        ("Born on Oct. 15, 1985. Raised in Boston.",
         ["Born on Oct. 15, 1985.", "Raised in Boston."]),
    ])
    def test_dates(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
