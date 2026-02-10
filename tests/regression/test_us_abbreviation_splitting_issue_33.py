#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Comprehensive test suite for issue #33: U.S. abbreviation splitting.

Tests that capital letter abbreviations (U.S., U.K., U.N., E.U., etc.)
are never split across lines or sentences, with "U" on one line and "S."
on another.

Reference: https://github.com/craigtrim/fast-sentence-segment/issues/33
"""

import re
import pytest
from typing import List

from fast_sentence_segment import segment_text


# Test data constants
ABBREVIATIONS = ["U.S.", "U.K.", "U.N.", "E.U.", "U.S.A."]

FOLLOWING_LOWERCASE_WORDS = [
    "is", "are", "was", "were", "has", "have", "had",
    "does", "did", "can", "could", "should", "would",
    "will", "might", "may", "must", "shall",
    "economy", "government", "people", "citizens", "residents",
    "and", "or", "but", "because", "since", "when", "while",
    "to", "for", "of", "in", "on", "at", "by", "with"
]

FOLLOWING_CAPITAL_WORDS = [
    # From COUNTRY_ABBREV_PROPER_NOUNS list
    "Senate", "Congress", "Government", "Constitution", "Supreme",
    "President", "Army", "Navy", "Air", "Marines", "Coast",
    "State", "Defense", "Treasury", "Justice", "Interior",
    "Agriculture", "Commerce", "Labor", "Health", "Housing",
    "Transportation", "Energy", "Education", "Veterans", "Homeland",
    "Embassy", "Consulate", "Ambassador", "Secretary", "Attorney",
    "House", "Representatives", "Capitol", "White", "Pentagon"
]

PUNCTUATION_BEFORE = ["", '"', "(", "[", "—", "'"]
PUNCTUATION_AFTER = ["", ",", ";", ":", ")", "]", "?", "!"]

SENTENCE_STARTERS = ["She", "He", "They", "It", "We", "The", "This", "That"]

YEARS = ["1", "50", "2024", "1776"]


# Validation helpers
def validate_no_split_abbreviation(result: List[str], abbrev: str):
    """
    Ensure abbreviation is never split within itself.

    Args:
        result: List of segmented sentences
        abbrev: The abbreviation to check (e.g., "U.S.")
    """
    # Join all results
    full_result = " ".join(result)

    # Check abbreviation appears intact
    assert abbrev in full_result, f"{abbrev} not found in result"

    # Check for actual splitting patterns:
    # 1. First letter followed by space/newline (not period)
    first_letter = abbrev[0]
    # Look for patterns like " U " or " U\n" that indicate actual splitting
    split_pattern = rf'\s{first_letter}\s'
    assert not re.search(split_pattern, full_result), \
        f"Found standalone '{first_letter}' with spaces - abbreviation may be split"

    # 2. Check no sentence starts with just the first letter followed by newline/nothing
    for sentence in result:
        stripped = sentence.strip()
        # Check if sentence is ONLY the first letter (indicates split)
        if stripped == first_letter:
            raise AssertionError(f"Found sentence with only '{first_letter}' - abbreviation split")

    # 3. Check no sentence starts with second part (e.g., "S.")
    second_part = abbrev[2:]  # "S." from "U.S."
    for sentence in result:
        if sentence.strip().startswith(second_part):
            raise AssertionError(f"Sentence starts with '{second_part}' - abbreviation split")


class TestUSFollowedByLowercaseWords:
    """U.S. + every possible lowercase word (30+ tests)"""

    @pytest.mark.parametrize("word", FOLLOWING_LOWERCASE_WORDS)
    def test_us_followed_by_lowercase_word(self, word):
        """Test U.S. followed by common lowercase words"""
        text = f"The U.S. {word} something important."
        result = segment_text(text, flatten=True)

        assert len(result) == 1
        assert "U.S." in result[0]
        validate_no_split_abbreviation(result, "U.S.")


class TestUSFollowedByProperNouns:
    """U.S. + every proper noun from COUNTRY_ABBREV_PROPER_NOUNS (35+ tests)"""

    @pytest.mark.parametrize("word", FOLLOWING_CAPITAL_WORDS)
    def test_us_followed_by_proper_noun(self, word):
        """Test U.S. followed by government/institutional proper nouns"""
        text = f"The U.S. {word} made a decision."
        result = segment_text(text, flatten=True)

        assert len(result) == 1
        assert "U.S." in result[0]
        assert f"U.S. {word}" in result[0]
        validate_no_split_abbreviation(result, "U.S.")


class TestAllAbbreviationsWithLowercase:
    """Every abbreviation × top lowercase words (50+ tests)"""

    @pytest.mark.parametrize("abbrev", ABBREVIATIONS)
    @pytest.mark.parametrize("word", FOLLOWING_LOWERCASE_WORDS[:10])
    def test_all_abbreviations_with_lowercase(self, abbrev, word):
        """Test all country abbreviations with common lowercase words"""
        text = f"The {abbrev} {word} important."
        result = segment_text(text, flatten=True)

        assert len(result) == 1
        assert abbrev in result[0]
        validate_no_split_abbreviation(result, abbrev)


class TestSentencePositions:
    """Abbreviations in different sentence positions (50+ tests)"""

    @pytest.mark.parametrize("abbrev", ABBREVIATIONS)
    def test_abbreviation_at_sentence_start(self, abbrev):
        """Test each abbreviation at sentence start"""
        text = f"{abbrev} is important to us."
        result = segment_text(text, flatten=True)

        assert len(result) == 1
        assert abbrev in result[0]
        validate_no_split_abbreviation(result, abbrev)

    @pytest.mark.parametrize("abbrev", ABBREVIATIONS)
    def test_abbreviation_in_middle(self, abbrev):
        """Test each abbreviation in sentence middle"""
        text = f"Living in the {abbrev} is wonderful."
        result = segment_text(text, flatten=True)

        assert len(result) == 1
        assert abbrev in result[0]
        validate_no_split_abbreviation(result, abbrev)

    @pytest.mark.parametrize("abbrev", ABBREVIATIONS)
    def test_abbreviation_at_end(self, abbrev):
        """Test each abbreviation at sentence end"""
        text = f"She moved to the {abbrev}"
        result = segment_text(text, flatten=True)

        assert len(result) == 1
        assert abbrev in result[0]
        validate_no_split_abbreviation(result, abbrev)

    @pytest.mark.parametrize("abbrev", ABBREVIATIONS)
    @pytest.mark.parametrize("next_word", SENTENCE_STARTERS)
    def test_abbreviation_sentence_boundary(self, abbrev, next_word):
        """Test abbreviation ending one sentence, capital starting next"""
        text = f"I live in the {abbrev}. {next_word} lives elsewhere."
        result = segment_text(text, flatten=True)

        assert len(result) == 2
        assert abbrev in result[0]
        assert next_word in result[1]
        validate_no_split_abbreviation(result, abbrev)


class TestPunctuationContexts:
    """Abbreviations with various punctuation (50+ tests)"""

    @pytest.mark.parametrize("abbrev", ABBREVIATIONS)
    @pytest.mark.parametrize("punct", PUNCTUATION_BEFORE)
    def test_abbreviation_after_punctuation(self, abbrev, punct):
        """Test each abbreviation after various punctuation marks"""
        if punct == "(":
            text = f"The country (the {abbrev}) is large."
        elif punct == "[":
            text = f"The country [the {abbrev}] is powerful."
        elif punct in ['"', "'"]:
            text = f"The phrase {punct}the {abbrev}{punct} appeared."
        elif punct == "—":
            text = f"The country—the {abbrev}—is mighty."
        else:
            text = f"The {abbrev} is large."

        result = segment_text(text, flatten=True)
        assert abbrev in result[0]
        validate_no_split_abbreviation(result, abbrev)

    @pytest.mark.parametrize("abbrev", ABBREVIATIONS)
    @pytest.mark.parametrize("punct", PUNCTUATION_AFTER)
    def test_abbreviation_before_punctuation(self, abbrev, punct):
        """Test each abbreviation before various punctuation marks"""
        text = f"Living in the {abbrev}{punct} is great."
        result = segment_text(text, flatten=True)

        assert abbrev in result[0]
        validate_no_split_abbreviation(result, abbrev)


class TestMultipleAbbreviations:
    """Multiple abbreviations in same/different sentences (20+ tests)"""

    @pytest.mark.parametrize("abbrev1,abbrev2", [
        ("U.S.", "U.K."), ("U.S.", "U.N."), ("U.S.", "E.U."),
        ("U.K.", "U.N."), ("U.K.", "E.U."), ("U.N.", "E.U.")
    ])
    def test_two_abbreviations_same_sentence(self, abbrev1, abbrev2):
        """Test two different abbreviations in same sentence"""
        text = f"The {abbrev1} and {abbrev2} agreed."
        result = segment_text(text, flatten=True)

        assert len(result) == 1
        assert abbrev1 in result[0]
        assert abbrev2 in result[0]
        validate_no_split_abbreviation(result, abbrev1)
        validate_no_split_abbreviation(result, abbrev2)

    @pytest.mark.parametrize("abbrev1,abbrev2", [
        ("U.S.", "U.K."), ("U.S.", "U.N."), ("U.K.", "E.U.")
    ])
    def test_two_abbreviations_different_sentences(self, abbrev1, abbrev2):
        """Test two abbreviations in separate sentences"""
        text = f"The {abbrev1} is powerful. The {abbrev2} is influential."
        result = segment_text(text, flatten=True)

        assert len(result) == 2
        assert abbrev1 in result[0]
        assert abbrev2 in result[1]
        validate_no_split_abbreviation(result, abbrev1)
        validate_no_split_abbreviation(result, abbrev2)

    def test_three_abbreviations_same_sentence(self):
        """Test three abbreviations together"""
        text = "The U.S., U.K., and U.N. cooperated."
        result = segment_text(text, flatten=True)

        assert len(result) == 1
        for abbr in ["U.S.", "U.K.", "U.N."]:
            assert abbr in result[0]
            validate_no_split_abbreviation(result, abbr)

    def test_abbreviation_repeated(self):
        """Test same abbreviation multiple times"""
        text = "The U.S. government and U.S. citizens and U.S. military acted."
        result = segment_text(text, flatten=True)

        assert len(result) == 1
        assert result[0].count("U.S.") == 3
        validate_no_split_abbreviation(result, "U.S.")

    @pytest.mark.parametrize("abbrev", ABBREVIATIONS)
    def test_abbreviation_repeated_twice(self, abbrev):
        """Test each abbreviation repeated in same sentence"""
        text = f"The {abbrev} government and {abbrev} people worked together."
        result = segment_text(text, flatten=True)

        assert len(result) == 1
        assert result[0].count(abbrev) == 2
        validate_no_split_abbreviation(result, abbrev)


class TestQuotations:
    """Abbreviations with quotation marks (15+ tests)"""

    @pytest.mark.parametrize("abbrev", ABBREVIATIONS)
    def test_abbreviation_in_double_quotes(self, abbrev):
        """Test each abbreviation inside double quotes"""
        text = f'"The {abbrev} is great," she said.'
        result = segment_text(text, flatten=True)

        assert abbrev in result[0]
        validate_no_split_abbreviation(result, abbrev)

    @pytest.mark.parametrize("abbrev", ABBREVIATIONS)
    def test_abbreviation_in_single_quotes(self, abbrev):
        """Test each abbreviation inside single quotes"""
        text = f"'The {abbrev} is powerful,' he noted."
        result = segment_text(text, flatten=True)

        assert abbrev in result[0]
        validate_no_split_abbreviation(result, abbrev)

    @pytest.mark.parametrize("abbrev", ABBREVIATIONS)
    def test_abbreviation_quote_starts_after(self, abbrev):
        """Test quote starting after abbreviation"""
        text = f'The {abbrev}. "She agreed."'
        result = segment_text(text, flatten=True)

        assert abbrev in result[0]
        validate_no_split_abbreviation(result, abbrev)


class TestComplexPunctuation:
    """Abbreviations with complex punctuation (20+ tests)"""

    @pytest.mark.parametrize("abbrev", ABBREVIATIONS)
    def test_abbreviation_in_parentheses(self, abbrev):
        """Test each abbreviation in parentheses"""
        text = f"The country (the {abbrev}) is large."
        result = segment_text(text, flatten=True)

        assert abbrev in result[0]
        validate_no_split_abbreviation(result, abbrev)

    @pytest.mark.parametrize("abbrev", ABBREVIATIONS)
    def test_abbreviation_in_brackets(self, abbrev):
        """Test each abbreviation in brackets"""
        text = f"The country [the {abbrev}] is powerful."
        result = segment_text(text, flatten=True)

        assert abbrev in result[0]
        validate_no_split_abbreviation(result, abbrev)

    @pytest.mark.parametrize("abbrev", ABBREVIATIONS)
    def test_abbreviation_with_em_dash(self, abbrev):
        """Test each abbreviation with em dash"""
        text = f"The country—the {abbrev}—is mighty."
        result = segment_text(text, flatten=True)

        assert abbrev in result[0]
        validate_no_split_abbreviation(result, abbrev)

    @pytest.mark.parametrize("abbrev", ABBREVIATIONS)
    def test_abbreviation_with_ellipsis(self, abbrev):
        """Test each abbreviation near ellipsis"""
        text = f"The {abbrev}... is something."
        result = segment_text(text, flatten=True)

        assert abbrev in result[0]
        validate_no_split_abbreviation(result, abbrev)


class TestQuestionsAndExclamations:
    """Abbreviations in questions and exclamations (10+ tests)"""

    @pytest.mark.parametrize("abbrev", ABBREVIATIONS)
    def test_abbreviation_in_question(self, abbrev):
        """Test each abbreviation in question"""
        text = f"Where is the {abbrev} located?"
        result = segment_text(text, flatten=True)

        assert len(result) == 1
        assert abbrev in result[0]
        validate_no_split_abbreviation(result, abbrev)

    @pytest.mark.parametrize("abbrev", ABBREVIATIONS)
    def test_abbreviation_in_exclamation(self, abbrev):
        """Test each abbreviation in exclamation"""
        text = f"The {abbrev} is amazing!"
        result = segment_text(text, flatten=True)

        assert len(result) == 1
        assert abbrev in result[0]
        validate_no_split_abbreviation(result, abbrev)


class TestNumericalContexts:
    """Abbreviations with numbers and years (20+ tests)"""

    @pytest.mark.parametrize("abbrev", ABBREVIATIONS)
    @pytest.mark.parametrize("number", YEARS)
    def test_abbreviation_with_year(self, abbrev, number):
        """Test abbreviation with year/number"""
        text = f"In {number}, the {abbrev} did something."
        result = segment_text(text, flatten=True)

        assert abbrev in result[0]
        validate_no_split_abbreviation(result, abbrev)


class TestIssueSpecificRegressions:
    """Exact examples from issue #33 (4 tests)"""

    def test_gannon_pillai_example(self):
        """Test exact example from issue #33"""
        text = 'According to Gannon and Pillai, "football in the U.S. is not only a sport but also an assortment of common beliefs and ideals; indeed, football has steadily become an integral component of the community."'
        result = segment_text(text, flatten=True)

        assert len(result) == 1
        assert "U.S." in result[0]
        assert "U.S. is" in result[0]
        validate_no_split_abbreviation(result, "U.S.")

    def test_where_is_us_ranked(self):
        """Test 'Where is U.S.' example from issue"""
        text = "Where is U.S. ranked in terms of individualism and community?"
        result = segment_text(text, flatten=True)

        assert len(result) == 1
        assert "U.S." in result[0]
        validate_no_split_abbreviation(result, "U.S.")

    def test_are_us_managers(self):
        """Test 'Are U.S. managers' example from issue"""
        text = "Are U.S. managers open to change?"
        result = segment_text(text, flatten=True)

        assert len(result) == 1
        assert "U.S." in result[0]
        validate_no_split_abbreviation(result, "U.S.")

    def test_difficult_for_us_living(self):
        """Test 'difficult for us living in the U.S.' example from issue"""
        text = "This may be difficult for us living in the U.S. to grasp and understand."
        result = segment_text(text, flatten=True)

        assert len(result) == 1
        assert "U.S." in result[0]
        validate_no_split_abbreviation(result, "U.S.")


class TestEdgeCases:
    """Edge case scenarios (15+ tests)"""

    def test_abbreviation_only(self):
        """Test just the abbreviation alone"""
        text = "U.S."
        result = segment_text(text, flatten=True)

        assert len(result) == 1
        assert "U.S." in result[0]
        validate_no_split_abbreviation(result, "U.S.")

    def test_abbreviation_with_no_trailing_text(self):
        """Test abbreviation with no text after"""
        text = "The U.S."
        result = segment_text(text, flatten=True)

        assert "U.S." in result[0]
        validate_no_split_abbreviation(result, "U.S.")

    def test_multiple_spaces_after_abbreviation(self):
        """Test multiple spaces after abbreviation"""
        text = "The U.S.  is large."
        result = segment_text(text, flatten=True)

        assert "U.S." in result[0]
        validate_no_split_abbreviation(result, "U.S.")

    def test_abbreviation_repeated_back_to_back(self):
        """Test abbreviation repeated immediately"""
        text = "The U.S. U.S. is written twice."
        result = segment_text(text, flatten=True)

        assert result[0].count("U.S.") == 2
        validate_no_split_abbreviation(result, "U.S.")

    def test_lowercase_after_abbreviation_mid_sentence(self):
        """Test lowercase word after abbreviation in middle of sentence"""
        text = "The people in the U.S. are diverse and the culture varies."
        result = segment_text(text, flatten=True)

        assert "U.S." in result[0]
        validate_no_split_abbreviation(result, "U.S.")

    def test_conjunction_after_abbreviation(self):
        """Test conjunction directly after abbreviation"""
        text = "The U.S. and Canada border each other."
        result = segment_text(text, flatten=True)

        assert "U.S." in result[0]
        validate_no_split_abbreviation(result, "U.S.")

    def test_preposition_after_abbreviation(self):
        """Test preposition after abbreviation"""
        text = "The U.S. of America is large."
        result = segment_text(text, flatten=True)

        assert "U.S." in result[0]
        validate_no_split_abbreviation(result, "U.S.")

    @pytest.mark.parametrize("abbrev", ABBREVIATIONS)
    def test_abbreviation_with_comma_and_continuation(self, abbrev):
        """Test abbreviation with comma and sentence continues"""
        text = f"In the {abbrev}, people live well."
        result = segment_text(text, flatten=True)

        assert abbrev in result[0]
        validate_no_split_abbreviation(result, abbrev)

    @pytest.mark.parametrize("abbrev", ABBREVIATIONS)
    def test_abbreviation_with_semicolon(self, abbrev):
        """Test abbreviation followed by semicolon"""
        text = f"The {abbrev}; it is powerful."
        result = segment_text(text, flatten=True)

        assert abbrev in result[0]
        validate_no_split_abbreviation(result, abbrev)

    @pytest.mark.parametrize("abbrev", ABBREVIATIONS)
    def test_abbreviation_with_colon(self, abbrev):
        """Test abbreviation followed by colon"""
        text = f"The {abbrev}: a powerful nation."
        result = segment_text(text, flatten=True)

        assert abbrev in result[0]
        validate_no_split_abbreviation(result, abbrev)

    def test_abbreviation_with_apostrophe(self):
        """Test abbreviation with possessive apostrophe"""
        text = "The U.S.'s economy is strong."
        result = segment_text(text, flatten=True)

        assert "U.S." in result[0]
        # Note: This checks for "U.S." not "U.S.'s" split
        validate_no_split_abbreviation(result, "U.S.")

    def test_abbreviation_all_caps_sentence(self):
        """Test abbreviation in context with other capitals"""
        text = "NATO and the U.S. and EU cooperated."
        result = segment_text(text, flatten=True)

        assert "U.S." in result[0]
        validate_no_split_abbreviation(result, "U.S.")

    def test_abbreviation_after_number(self):
        """Test abbreviation immediately after number"""
        text = "The top 10 U.S. companies are successful."
        result = segment_text(text, flatten=True)

        assert "U.S." in result[0]
        validate_no_split_abbreviation(result, "U.S.")

    def test_abbreviation_before_number(self):
        """Test abbreviation immediately before number"""
        text = "The U.S. 50 states are diverse."
        result = segment_text(text, flatten=True)

        assert "U.S." in result[0]
        validate_no_split_abbreviation(result, "U.S.")

    def test_multiple_abbreviations_with_punctuation(self):
        """Test multiple abbreviations with various punctuation"""
        text = "The U.S., U.K., and U.N. (three powers) cooperated."
        result = segment_text(text, flatten=True)

        for abbr in ["U.S.", "U.K.", "U.N."]:
            assert abbr in result[0]
            validate_no_split_abbreviation(result, abbr)
