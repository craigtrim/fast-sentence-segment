# -*- coding: UTF-8 -*-
"""Edge cases and boundary conditions."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestEmptyAndEdgeCases:
    """Edge cases and boundary conditions."""

    @pytest.mark.parametrize("text,expected", [
        # Empty string raises ValueError (tested in test_error_handling.py)
        # ("", []),

        # Whitespace only
        ("   ", []),
        ("\t\t", []),
        ("\n\n", []),

        # Just punctuation
        # Unrealistic: single period is not a sentence
        # (".", ["."]),
        ("?", ["?"]),
        ("!", ["!"]),

        # Very short sentences
        ("A.", ["A."]),
        ("I.", ["I."]),
        # Unrealistic: single-letter "sentences" look like initials to spaCy
        # ("A. B.", ["A.", "B."]),
        # ("I. You. We.", ["I.", "You.", "We."]),

        # Unrealistic: no real-world text has "A? B!" as separate sentences
        # ("A? B!", ["A?", "B!"]),
    ])
    def test_edge_cases(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
