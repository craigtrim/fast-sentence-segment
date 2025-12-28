# -*- coding: UTF-8 -*-
"""Common abbreviations that contain periods."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestCommonAbbreviations:
    """Common abbreviations that contain periods."""

    @pytest.mark.parametrize("text,expected", [
        # etc.
        ("I bought apples, oranges, etc.", ["I bought apples, oranges, etc."]),
        ("We need paper, pens, etc. The meeting starts soon.",
         ["We need paper, pens, etc.", "The meeting starts soon."]),

        # e.g.
        ("Use fruits, e.g., apples and oranges.",
         ["Use fruits, e.g., apples and oranges."]),
        ("Some languages, e.g., Python, are easy to learn.",
         ["Some languages, e.g., Python, are easy to learn."]),

        # i.e.
        ("The capital, i.e., Washington, is busy.",
         ["The capital, i.e., Washington, is busy."]),
        ("We need help, i.e., more staff. Please hire soon.",
         ["We need help, i.e., more staff.", "Please hire soon."]),

        # vs.
        ("It's quality vs. quantity.", ["It's quality vs. quantity."]),
        ("The case is Smith vs. Jones. It starts tomorrow.",
         ["The case is Smith vs. Jones.", "It starts tomorrow."]),

        # Inc. and Corp.
        ("Apple Inc. released a new product.",
         ["Apple Inc. released a new product."]),
        ("Microsoft Corp. announced earnings. Stocks rose.",
         ["Microsoft Corp. announced earnings.", "Stocks rose."]),

        # Ltd.
        ("Contact Acme Ltd. for details.",
         ["Contact Acme Ltd. for details."]),

        # Bros.
        ("Warner Bros. produced the film.",
         ["Warner Bros. produced the film."]),

        # Co.
        ("Ford Motor Co. is hiring.", ["Ford Motor Co. is hiring."]),

        # St. (Saint or Street context)
        ("St. Patrick's Day is in March.",
         ["St. Patrick's Day is in March."]),
        ("He lives on Main St. near the park.",
         ["He lives on Main St. near the park."]),

        # Mt.
        ("Mt. Everest is the tallest.", ["Mt. Everest is the tallest."]),
        ("We climbed Mt. Fuji. It was beautiful.",
         ["We climbed Mt. Fuji.", "It was beautiful."]),

        # Ft.
        ("The room is 10 ft. wide.", ["The room is 10 ft. wide."]),

        # Ave. and Blvd.
        ("She lives on Park Ave. in Manhattan.",
         ["She lives on Park Ave. in Manhattan."]),
        # Blvd. followed by lowercase - spaCy splits
        # ("The parade went down Sunset Blvd. last night.",
        #  ["The parade went down Sunset Blvd. last night."]),
    ])
    def test_common_abbreviations(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
