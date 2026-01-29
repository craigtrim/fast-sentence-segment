# -*- coding: UTF-8 -*-
"""Tests for newlines-to-periods converter.

The NewlinesToPeriods component replaces newline characters with spaces
in text before sentence segmentation. (Originally converted to periods,
but changed in 2023 to avoid inserting spurious periods.)
"""

import pytest
from fast_sentence_segment.dmo.newlines_to_periods import NewlinesToPeriods


@pytest.fixture
def converter():
    return NewlinesToPeriods()


class TestNewlineReplacement:
    """Newlines are replaced with spaces."""

    def test_single_newline(self, converter):
        assert converter.process("Hello\nWorld") == "Hello World"

    def test_multiple_newlines(self, converter):
        result = converter.process("Line1\nLine2\nLine3")
        assert result == "Line1 Line2 Line3"

    def test_newline_at_start(self, converter):
        assert converter.process("\nHello") == " Hello"

    def test_newline_at_end(self, converter):
        assert converter.process("Hello\n") == "Hello "


class TestNoNewlines:
    """Text without newlines passes through unchanged."""

    def test_plain_text(self, converter):
        text = "No newlines here."
        assert converter.process(text) == text

    def test_empty_string(self, converter):
        assert converter.process("") == ""


class TestCarriageReturn:
    """Carriage returns are not handled (only \\n)."""

    def test_carriage_return_preserved(self, converter):
        """\\r is not replaced -- only \\n is."""
        text = "Hello\rWorld"
        result = converter.process(text)
        assert "\r" in result
