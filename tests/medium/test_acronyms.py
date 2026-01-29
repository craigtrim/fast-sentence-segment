# -*- coding: UTF-8 -*-
"""Sentences containing common acronyms with periods."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestAcronyms:
    """Sentences containing common acronyms with periods."""

    @pytest.mark.parametrize("text,expected", [
        # U.S.
        ("The U.S. economy is growing.", ["The U.S. economy is growing."]),
        ("She moved to the U.S. last year.",
         ["She moved to the U.S. last year."]),
        ("The U.S.A. is a large country.",
         ["The U.S.A. is a large country."]),

        # U.K.
        ("The U.K. voted for Brexit.", ["The U.K. voted for Brexit."]),
        ("He's from the U.K. originally.",
         ["He's from the U.K. originally."]),

        # U.N.
        ("The U.N. held a meeting today.", ["The U.N. held a meeting today."]),

        # D.C.
        ("Washington D.C. is the capital.",
         ["Washington D.C. is the capital."]),
        ("I visited D.C. last summer. It was hot.",
         ["I visited D.C. last summer.", "It was hot."]),

        # Multiple acronyms
        ("The U.S. and U.K. signed a treaty.",
         ["The U.S. and U.K. signed a treaty."]),
    ])
    def test_acronyms(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
