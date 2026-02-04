#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Tests for country abbreviation + proper noun handling.

Reference: https://github.com/craigtrim/fast-sentence-segment/issues/15
"""

import pytest
from fast_sentence_segment import segment_text


class TestUSProperNouns:
    """Test that U.S. followed by proper nouns does NOT split."""

    def test_us_senate(self):
        text = "The U.S. Senate voted today. It was close."
        result = segment_text(text, flatten=True)
        assert result == [
            "The U.S. Senate voted today.",
            "It was close."
        ]

    def test_us_congress(self):
        text = "The U.S. Congress passed the bill. The president signed it."
        result = segment_text(text, flatten=True)
        assert result == [
            "The U.S. Congress passed the bill.",
            "The president signed it."
        ]

    def test_us_army(self):
        text = "The U.S. Army deployed troops. They arrived yesterday."
        result = segment_text(text, flatten=True)
        assert result == [
            "The U.S. Army deployed troops.",
            "They arrived yesterday."
        ]

    def test_us_supreme_court(self):
        text = "The U.S. Supreme Court ruled. The decision was unanimous."
        result = segment_text(text, flatten=True)
        assert result == [
            "The U.S. Supreme Court ruled.",
            "The decision was unanimous."
        ]

    def test_us_department(self):
        text = "The U.S. Department of Justice investigated. They found evidence."
        result = segment_text(text, flatten=True)
        assert result == [
            "The U.S. Department of Justice investigated.",
            "They found evidence."
        ]

    def test_us_government(self):
        text = "The U.S. Government issued a statement. It was brief."
        result = segment_text(text, flatten=True)
        assert result == [
            "The U.S. Government issued a statement.",
            "It was brief."
        ]


class TestUKProperNouns:
    """Test that U.K. followed by proper nouns does NOT split."""

    def test_uk_parliament(self):
        text = "The U.K. Parliament debated the issue. It was contentious."
        result = segment_text(text, flatten=True)
        assert result == [
            "The U.K. Parliament debated the issue.",
            "It was contentious."
        ]

    def test_uk_prime_minister(self):
        text = "The U.K. Prime Minister spoke. The speech was long."
        result = segment_text(text, flatten=True)
        assert result == [
            "The U.K. Prime Minister spoke.",
            "The speech was long."
        ]


class TestUNProperNouns:
    """Test that U.N. followed by proper nouns does NOT split."""

    def test_un_security_council(self):
        text = "The U.N. Security Council met. They discussed sanctions."
        result = segment_text(text, flatten=True)
        assert result == [
            "The U.N. Security Council met.",
            "They discussed sanctions."
        ]


class TestEUProperNouns:
    """Test that E.U. followed by proper nouns does NOT split."""

    def test_eu_commission(self):
        text = "The E.U. Commission proposed new rules. They were strict."
        result = segment_text(text, flatten=True)
        assert result == [
            "The E.U. Commission proposed new rules.",
            "They were strict."
        ]


class TestCountryAbbrevStillSplitsWhenAppropriate:
    """Test that country abbreviations still split when NOT followed by proper nouns."""

    def test_us_then_lowercase(self):
        """U.S. followed by lowercase should still be handled by spaCy."""
        text = "I visited the U.S. last year. It was fun."
        result = segment_text(text, flatten=True)
        # This should still work because spaCy handles the lowercase case
        assert len(result) == 2

    def test_us_at_end_of_sentence(self):
        """U.S. at end of sentence followed by new sentence."""
        text = "I live in the U.S. The weather is nice."
        result = segment_text(text, flatten=True)
        assert len(result) == 2
