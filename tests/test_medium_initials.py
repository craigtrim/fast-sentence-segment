# -*- coding: UTF-8 -*-
"""Names with initials."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestInitials:
    """Names with initials."""

    @pytest.mark.parametrize("text,expected", [
        # Single initial
        ("J. Smith is here.", ["J. Smith is here."]),
        ("Meet R. Jones at noon.", ["Meet R. Jones at noon."]),

        # Two initials
        ("J.R. Smith signed the contract.", ["J.R. Smith signed the contract."]),
        ("Contact A.B. Wilson for help.",
         ["Contact A.B. Wilson for help."]),

        # Three initials
        ("J.F.K. was president.", ["J.F.K. was president."]),
        ("She admired F.D.R. greatly.", ["She admired F.D.R. greatly."]),

        # Initials with full name
        ("John F. Kennedy was president.",
         ["John F. Kennedy was president."]),
        ("Franklin D. Roosevelt led during the war.",
         ["Franklin D. Roosevelt led during the war."]),

        # Multiple people with initials
        ("J.R. Smith and A.B. Jones arrived.",
         ["J.R. Smith and A.B. Jones arrived."]),
        ("J.F.K. met with L.B.J. that day.",
         ["J.F.K. met with L.B.J. that day."]),

        # Initials at end of sentence
        ("The author is R.J. I love his work.",
         ["The author is R.J.", "I love his work."]),
    ])
    def test_initials(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
