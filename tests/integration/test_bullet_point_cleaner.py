# -*- coding: UTF-8 -*-
"""Tests for bullet point cleaner.

The BulletPointCleaner prevents bullet points and list markers from
triggering false positive sentence detection. It strips leading dashes,
collapses double spaces, and cleans up double-period artifacts.
"""

import pytest
from fast_sentence_segment.dmo.bullet_point_cleaner import BulletPointCleaner


@pytest.fixture
def cleaner():
    return BulletPointCleaner()


class TestLeadingDash:
    """Strip leading dash from bullet point lines."""

    def test_leading_dash_removed(self, cleaner):
        assert cleaner.process("-Item one") == "Item one"

    def test_leading_dash_with_space(self, cleaner):
        assert cleaner.process("- Item one") == " Item one"

    def test_no_leading_dash(self, cleaner):
        assert cleaner.process("Item one") == "Item one"


class TestDoubleSpaces:
    """Collapse double spaces to single."""

    def test_double_space(self, cleaner):
        assert "  " not in cleaner.process("Hello  world")

    def test_triple_space(self, cleaner):
        assert "  " not in cleaner.process("Hello   world")


class TestDoublePeriods:
    """Clean up double period artifacts (..)."""

    def test_double_period_collapsed(self, cleaner):
        result = cleaner.process("Hello.. World")
        assert ".." not in result

    def test_triple_period_collapsed(self, cleaner):
        """Triple dots become single period (not ellipsis preservation)."""
        result = cleaner.process("Hello... World")
        assert ".." not in result


class TestDashPeriodCleanup:
    """Clean '. -' patterns from bullet-point artifacts."""

    def test_period_dash_cleaned(self, cleaner):
        result = cleaner.process("Item one. - Item two.")
        assert ". -" not in result

    def test_period_space_period_cleaned(self, cleaner):
        result = cleaner.process("Hello. . World")
        assert ". . " not in result


class TestEdgeCases:
    """Edge cases."""

    def test_empty_string(self, cleaner):
        assert cleaner.process("") == ""

    def test_only_dash(self, cleaner):
        assert cleaner.process("-") == ""

    def test_no_cleaning_needed(self, cleaner):
        text = "This is a normal sentence."
        assert cleaner.process(text) == text
