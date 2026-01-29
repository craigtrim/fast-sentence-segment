# -*- coding: UTF-8 -*-
"""Tests for ellipsis normalizer.

The EllipsisNormalizer replaces ellipses (...) with a placeholder during
preprocessing to prevent spaCy from misinterpreting them as sentence
boundaries, then restores them during denormalization.

Reference:
    https://github.com/craigtrim/fast-sentence-segment/issues/3
"""

import pytest
from fast_sentence_segment.dmo.ellipsis_normalizer import (
    EllipsisNormalizer,
    PLACEHOLDER,
)


@pytest.fixture
def normalizer():
    return EllipsisNormalizer()


class TestNormalize:
    """Test forward normalization (ellipsis -> placeholder)."""

    def test_ellipsis_before_capital(self, normalizer):
        """'... Capital' should become placeholder + period for splitting."""
        text = "Wait... The answer is here."
        result = normalizer.process(text)
        assert PLACEHOLDER in result
        assert "..." not in result

    def test_mid_sentence_ellipsis(self, normalizer):
        """Mid-sentence ellipsis replaced with placeholder."""
        text = "I was thinking... about it."
        result = normalizer.process(text)
        assert result == f"I was thinking{PLACEHOLDER} about it."

    def test_no_ellipsis(self, normalizer):
        text = "No ellipsis here."
        result = normalizer.process(text)
        assert result == text

    def test_multiple_ellipses(self, normalizer):
        text = "First... second... third."
        result = normalizer.process(text)
        assert "..." not in result
        assert result.count(PLACEHOLDER) == 2


class TestDenormalize:
    """Test reverse denormalization (placeholder -> ellipsis)."""

    def test_denormalize_placeholder(self, normalizer):
        text = f"I was thinking{PLACEHOLDER} about it."
        result = normalizer.process(text, denormalize=True)
        assert result == "I was thinking... about it."

    def test_denormalize_placeholder_with_period(self, normalizer):
        """Placeholder followed by period should become just ellipsis."""
        text = f"Wait{PLACEHOLDER}. The answer."
        result = normalizer.process(text, denormalize=True)
        assert result == "Wait... The answer."

    def test_denormalize_no_placeholder(self, normalizer):
        text = "No placeholder here."
        result = normalizer.process(text, denormalize=True)
        assert result == text


class TestRoundTrip:
    """Normalize then denormalize should preserve ellipses."""

    def test_round_trip_mid_sentence(self, normalizer):
        original = "I was thinking... about it."
        normalized = normalizer.process(original)
        restored = normalizer.process(normalized, denormalize=True)
        assert restored == original

    def test_round_trip_boundary(self, normalizer):
        """Ellipsis at sentence boundary round-trips correctly."""
        original = "Wait... The answer is here."
        normalized = normalizer.process(original)
        restored = normalizer.process(normalized, denormalize=True)
        assert restored == original
