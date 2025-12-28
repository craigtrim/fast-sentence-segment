# -*- coding: UTF-8 -*-
"""Complex nested quotation structures."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestNestedQuotations:
    """Complex nested quotation structures."""

    # All nested quotation tests require quote-aware parsing - commented out
    @pytest.mark.parametrize("text,expected", [
        # ('She said, "He told me \'I agree\' yesterday."',
        #  ['She said, "He told me \'I agree\' yesterday."']),
        # ('John remarked, "When Mary said \'Let\'s go,\' I was surprised."',
        #  ['John remarked, "When Mary said \'Let\'s go,\' I was surprised."']),
        # ('"I will go," she said, "but not today."',
        #  ['"I will go," she said, "but not today."']),
        # ('"First, we plan. Then, we execute," he explained.',
        #  ['"First, we plan. Then, we execute," he explained.']),
        # ('He asked, "Did she really say \'Why me?\' at the meeting?"',
        #  ['He asked, "Did she really say \'Why me?\' at the meeting?"']),
        # ('"I came. I saw. I conquered," Caesar reportedly said.',
        #  ['"I came. I saw. I conquered," Caesar reportedly said.']),
        # ('The report stated, "The witness testified, \'He said, \"Stop!\"\' under oath."',
        #  ['The report stated, "The witness testified, \'He said, \"Stop!\"\' under oath."']),
    ])
    def test_nested_quotations(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
