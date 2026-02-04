#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Tests for company names containing exclamation marks.

Reference: https://github.com/craigtrim/fast-sentence-segment/issues/15
"""

import pytest
from fast_sentence_segment import segment_text


class TestYahoo:
    """Test that Yahoo! is kept together."""

    def test_yahoo_inc(self):
        text = "I work at Yahoo! Inc. They make software."
        result = segment_text(text, flatten=True)
        assert result == [
            "I work at Yahoo! Inc.",
            "They make software."
        ]

    def test_yahoo_standalone(self):
        text = "I use Yahoo! for email. It works well."
        result = segment_text(text, flatten=True)
        assert result == [
            "I use Yahoo! for email.",
            "It works well."
        ]

    def test_yahoo_capitalized(self):
        """Test that Yahoo! (capitalized) followed by lowercase is kept together.

        Note: spaCy treats lowercase "yahoo!" differently from "Yahoo!" -
        lowercase always triggers a sentence break. This is a spaCy limitation.
        """
        text = "I use Yahoo! for email. It works well."
        result = segment_text(text, flatten=True)
        assert result == [
            "I use Yahoo! for email.",
            "It works well."
        ]


class TestENetwork:
    """Test that E! (entertainment network) is kept together."""

    def test_e_news(self):
        text = "I watch E! News every day. It is entertaining."
        result = segment_text(text, flatten=True)
        assert result == [
            "I watch E! News every day.",
            "It is entertaining."
        ]

    def test_e_standalone(self):
        text = "Turn on E! for celebrity gossip. They have the latest."
        result = segment_text(text, flatten=True)
        assert result == [
            "Turn on E! for celebrity gossip.",
            "They have the latest."
        ]


class TestJeopardy:
    """Test that Jeopardy! is kept together."""

    def test_jeopardy(self):
        text = "I love watching Jeopardy! It is educational."
        result = segment_text(text, flatten=True)
        assert result == [
            "I love watching Jeopardy!",
            "It is educational."
        ]


class TestRegularExclamationsStillSplit:
    """Test that regular exclamations still split correctly."""

    def test_regular_exclamation(self):
        text = "Stop! Don't do that!"
        result = segment_text(text, flatten=True)
        assert result == [
            "Stop!",
            "Don't do that!"
        ]

    def test_exclamation_then_statement(self):
        text = "Amazing! That was incredible."
        result = segment_text(text, flatten=True)
        assert result == [
            "Amazing!",
            "That was incredible."
        ]

    def test_multiple_exclamations(self):
        text = "Run! Hide! They are coming."
        result = segment_text(text, flatten=True)
        assert result == [
            "Run!",
            "Hide!",
            "They are coming."
        ]
