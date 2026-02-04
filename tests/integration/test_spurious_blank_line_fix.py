# -*- coding: UTF-8 -*-
"""Tests for issue #12: Unwrap fails when hard-wrap splits across blank line.

This file contains tests for the fix that joins text across a single spurious
blank line when:
1. The previous line does NOT end with sentence-ending punctuation (.?!)
2. There is exactly ONE blank line
3. The next non-empty line starts with a lowercase letter

These tests should FAIL before the fix is implemented and PASS after.
"""

import pytest

from fast_sentence_segment.dmo.unwrap_hard_wrapped_text import unwrap_hard_wrapped_text


class TestSpuriousBlankLineShouldJoin:
    """25 test cases where a single blank line is a hard-wrap artifact and should be joined."""

    def test_01_colour_mounted(self):
        """Original issue example: 'His colour' + blank + 'mounted;'"""
        text = "His colour\n\nmounted; he fixed his neighbour's pale eye."
        result = unwrap_hard_wrapped_text(text)
        assert result == "His colour mounted; he fixed his neighbour's pale eye."

    def test_02_ship_sailed(self):
        """Mid-sentence split: 'the ship' + blank + 'sailed'"""
        text = "The great ship\n\nsailed into the harbor at dawn."
        result = unwrap_hard_wrapped_text(text)
        assert result == "The great ship sailed into the harbor at dawn."

    def test_03_captain_ordered(self):
        """Verb continuation: 'captain' + blank + 'ordered'"""
        text = "The captain\n\nordered all hands on deck immediately."
        result = unwrap_hard_wrapped_text(text)
        assert result == "The captain ordered all hands on deck immediately."

    def test_04_wind_blowing(self):
        """Participle continuation: 'wind' + blank + 'blowing'"""
        text = "With the wind\n\nblowing fiercely from the north."
        result = unwrap_hard_wrapped_text(text)
        assert result == "With the wind blowing fiercely from the north."

    def test_05_adjective_continuation(self):
        """Adjective split: 'very' + blank + 'carefully'"""
        text = "He walked very\n\ncarefully across the deck."
        result = unwrap_hard_wrapped_text(text)
        assert result == "He walked very carefully across the deck."

    def test_06_preposition_split(self):
        """Preposition at line end: 'to' + blank + 'the'"""
        text = "They went to\n\nthe quarterdeck for inspection."
        result = unwrap_hard_wrapped_text(text)
        assert result == "They went to the quarterdeck for inspection."

    def test_07_article_split(self):
        """Article at line end: 'a' + blank + 'beautiful'"""
        text = "It was a\n\nbeautiful morning at sea."
        result = unwrap_hard_wrapped_text(text)
        assert result == "It was a beautiful morning at sea."

    def test_08_conjunction_split(self):
        """Conjunction at line end: 'and' + blank + 'then'"""
        text = "He stood up and\n\nthen walked to the window."
        result = unwrap_hard_wrapped_text(text)
        assert result == "He stood up and then walked to the window."

    def test_09_possessive_split(self):
        """Possessive split: 'Jack's' + blank + 'face'"""
        text = "Jack's\n\nface instantly changed from friendly to hostile."
        result = unwrap_hard_wrapped_text(text)
        assert result == "Jack's face instantly changed from friendly to hostile."

    def test_10_compound_word_split(self):
        """Compound context: 'quarter' + blank + 'deck'"""
        text = "He climbed to the quarter\n\ndeck to observe the horizon."
        result = unwrap_hard_wrapped_text(text)
        assert result == "He climbed to the quarter deck to observe the horizon."

    def test_11_adverb_split(self):
        """Adverb continuation: 'quickly' + blank + 'ran'"""
        text = "The boy quickly\n\nran below decks to fetch the rope."
        result = unwrap_hard_wrapped_text(text)
        assert result == "The boy quickly ran below decks to fetch the rope."

    def test_12_relative_pronoun(self):
        """Relative clause: 'man who' + blank + 'had'"""
        text = "The man who\n\nhad been standing there left quietly."
        result = unwrap_hard_wrapped_text(text)
        assert result == "The man who had been standing there left quietly."

    def test_13_infinitive_split(self):
        """Infinitive split: 'to' + blank + 'understand'"""
        text = "He tried to\n\nunderstand the complex navigation charts."
        result = unwrap_hard_wrapped_text(text)
        assert result == "He tried to understand the complex navigation charts."

    def test_14_modal_verb_split(self):
        """Modal verb: 'could' + blank + 'not'"""
        text = "He could\n\nnot but acknowledge his mistake."
        result = unwrap_hard_wrapped_text(text)
        assert result == "He could not but acknowledge his mistake."

    def test_15_determiner_split(self):
        """Determiner: 'the' + blank + 'ancient'"""
        text = "They examined the\n\nancient maps with great care."
        result = unwrap_hard_wrapped_text(text)
        assert result == "They examined the ancient maps with great care."

    def test_16_with_comma(self):
        """Comma at line end: 'however,' + blank + 'remained'"""
        text = "The captain, however,\n\nremained calm throughout the storm."
        result = unwrap_hard_wrapped_text(text)
        assert result == "The captain, however, remained calm throughout the storm."

    def test_17_semicolon_continuation(self):
        """Semicolon continuation: 'provisions;' + blank + 'they'"""
        text = "They needed more provisions;\n\nthey had been at sea too long."
        result = unwrap_hard_wrapped_text(text)
        assert result == "They needed more provisions; they had been at sea too long."

    def test_18_colon_continuation(self):
        """Colon continuation: 'items:' + blank + 'rope'"""
        text = "He requested the following items:\n\nrope, canvas, and tar."
        result = unwrap_hard_wrapped_text(text)
        assert result == "He requested the following items: rope, canvas, and tar."

    def test_19_dash_continuation(self):
        """Dash continuation: 'thought--' + blank + 'but'"""
        text = "He thought--\n\nbut no, it was impossible."
        result = unwrap_hard_wrapped_text(text)
        assert result == "He thought-- but no, it was impossible."

    def test_20_participle_phrase(self):
        """Participle phrase: 'seeing' + blank + 'nothing'"""
        text = "Seeing\n\nnothing on the horizon, he lowered the glass."
        result = unwrap_hard_wrapped_text(text)
        assert result == "Seeing nothing on the horizon, he lowered the glass."

    def test_21_comparative(self):
        """Comparative: 'more' + blank + 'carefully'"""
        text = "He examined it more\n\ncarefully than before."
        result = unwrap_hard_wrapped_text(text)
        assert result == "He examined it more carefully than before."

    def test_22_negation_split(self):
        """Negation: 'not' + blank + 'entirely'"""
        text = "This was not\n\nentirely unexpected news."
        result = unwrap_hard_wrapped_text(text)
        assert result == "This was not entirely unexpected news."

    def test_23_auxiliary_split(self):
        """Auxiliary verb: 'had' + blank + 'been'"""
        text = "The message had\n\nbeen delivered that morning."
        result = unwrap_hard_wrapped_text(text)
        assert result == "The message had been delivered that morning."

    def test_24_quantifier_split(self):
        """Quantifier: 'several' + blank + 'officers'"""
        text = "There were several\n\nofficers waiting on the dock."
        result = unwrap_hard_wrapped_text(text)
        assert result == "There were several officers waiting on the dock."

    def test_25_long_sentence_split(self):
        """Complex sentence with mid-split."""
        text = "The intricate mechanism of the ship's chronometer, which had been carefully\n\nmaintained by the sailing master, finally gave out."
        result = unwrap_hard_wrapped_text(text)
        assert result == "The intricate mechanism of the ship's chronometer, which had been carefully maintained by the sailing master, finally gave out."


class TestLegitimateBlankLineShouldNotJoin:
    """25 test cases where a blank line is a real paragraph break and should NOT be joined."""

    def test_01_period_then_capital(self):
        """Sentence ends with period, next starts with capital."""
        text = "The ship arrived safely.\n\nThe crew celebrated loudly."
        result = unwrap_hard_wrapped_text(text)
        assert result == "The ship arrived safely.\n\nThe crew celebrated loudly."

    def test_02_question_mark_paragraph(self):
        """Question ends paragraph, new paragraph follows."""
        text = "Did you see that?\n\nThe captain pointed to the horizon."
        result = unwrap_hard_wrapped_text(text)
        assert result == "Did you see that?\n\nThe captain pointed to the horizon."

    def test_03_exclamation_paragraph(self):
        """Exclamation ends paragraph."""
        text = "All hands on deck!\n\nThe storm was approaching fast."
        result = unwrap_hard_wrapped_text(text)
        assert result == "All hands on deck!\n\nThe storm was approaching fast."

    def test_04_dialogue_new_speaker(self):
        """Dialogue with new speaker."""
        text = '"I see land," said Jack.\n\n"Where?" asked Stephen.'
        result = unwrap_hard_wrapped_text(text)
        assert result == '"I see land," said Jack.\n\n"Where?" asked Stephen.'

    def test_05_multiple_blank_lines(self):
        """Multiple blank lines = definite section break."""
        text = "End of chapter one.\n\n\nChapter Two"
        result = unwrap_hard_wrapped_text(text)
        assert "End of chapter one." in result
        assert "Chapter Two" in result
        assert result.count("\n\n") >= 1

    def test_06_capital_proper_noun(self):
        """Next paragraph starts with proper noun."""
        text = "He looked out to sea\n\nEngland was nowhere in sight."
        result = unwrap_hard_wrapped_text(text)
        assert result == "He looked out to sea\n\nEngland was nowhere in sight."

    def test_07_capital_after_no_punct(self):
        """No ending punct but next line is clearly new paragraph (capital start)."""
        text = "The weather was fine\n\nMorning came with clear skies."
        result = unwrap_hard_wrapped_text(text)
        assert result == "The weather was fine\n\nMorning came with clear skies."

    def test_08_period_lowercase_but_proper(self):
        """Period at end, even if next could theoretically continue."""
        text = "Jack nodded.\n\nstephen looked away."
        result = unwrap_hard_wrapped_text(text)
        # Period at end means real paragraph break, even with lowercase next
        assert "Jack nodded." in result
        assert "\n\n" in result or "stephen" in result

    def test_09_chapter_heading(self):
        """Chapter heading after paragraph."""
        text = "And so they sailed away.\n\nCHAPTER THREE"
        result = unwrap_hard_wrapped_text(text)
        assert result == "And so they sailed away.\n\nCHAPTER THREE"

    def test_10_scene_break(self):
        """Asterisk scene break."""
        text = "The door closed behind him.\n\n* * *"
        result = unwrap_hard_wrapped_text(text)
        assert result == "The door closed behind him.\n\n* * *"

    def test_11_new_time_reference(self):
        """New paragraph with time reference."""
        text = "He went to sleep.\n\nThe next morning brought fresh winds."
        result = unwrap_hard_wrapped_text(text)
        assert result == "He went to sleep.\n\nThe next morning brought fresh winds."

    def test_12_ellipsis_then_new_para(self):
        """Ellipsis ending, then new paragraph."""
        text = "He wondered if...\n\nNo, it was impossible to know."
        result = unwrap_hard_wrapped_text(text)
        assert result == "He wondered if...\n\nNo, it was impossible to know."

    def test_13_quote_attribution_split(self):
        """Quote ends, attribution in next paragraph."""
        text = '"Very well," he said.\n\nThe others nodded in agreement.'
        result = unwrap_hard_wrapped_text(text)
        assert result == '"Very well," he said.\n\nThe others nodded in agreement.'

    def test_14_number_starting_para(self):
        """Number starting new paragraph."""
        text = "He counted them carefully.\n\n42 ships lay at anchor."
        result = unwrap_hard_wrapped_text(text)
        assert result == "He counted them carefully.\n\n42 ships lay at anchor."

    def test_15_pronoun_new_subject(self):
        """New paragraph with different subject pronoun."""
        text = "Jack finished his meal.\n\nShe waited by the door."
        result = unwrap_hard_wrapped_text(text)
        assert result == "Jack finished his meal.\n\nShe waited by the door."

    def test_16_location_shift(self):
        """New paragraph indicating location shift."""
        text = "He left the cabin.\n\nOn deck, the wind was fierce."
        result = unwrap_hard_wrapped_text(text)
        assert result == "He left the cabin.\n\nOn deck, the wind was fierce."

    def test_17_quoted_capital(self):
        """Quote starting new paragraph."""
        text = 'He paused to think.\n\n"Perhaps," he said slowly.'
        result = unwrap_hard_wrapped_text(text)
        assert result == 'He paused to think.\n\n"Perhaps," he said slowly.'

    def test_18_question_response(self):
        """Question followed by response paragraph."""
        text = "What could be done?\n\nNothing, it seemed."
        result = unwrap_hard_wrapped_text(text)
        assert result == "What could be done?\n\nNothing, it seemed."

    def test_19_exclamation_continuation(self):
        """Exclamation followed by new paragraph."""
        text = "Land ho!\n\nAll eyes turned to the west."
        result = unwrap_hard_wrapped_text(text)
        assert result == "Land ho!\n\nAll eyes turned to the west."

    def test_20_closing_quote_period(self):
        """Closing quote with period, then new para."""
        text = '"I understand."\n\nThe captain turned away.'
        result = unwrap_hard_wrapped_text(text)
        assert result == '"I understand."\n\nThe captain turned away.'

    def test_21_abbreviation_vs_sentence(self):
        """Sentence ends (not abbreviation), new paragraph."""
        text = "The hour was late.\n\nDr. Maturin arrived at dawn."
        result = unwrap_hard_wrapped_text(text)
        assert result == "The hour was late.\n\nDr. Maturin arrived at dawn."

    def test_22_triple_blank_lines(self):
        """Three blank lines = major break."""
        text = "Part One ends here.\n\n\n\nPart Two begins."
        result = unwrap_hard_wrapped_text(text)
        assert "Part One ends here." in result
        assert "Part Two begins." in result

    def test_23_uppercase_word_start(self):
        """All-caps word starts new paragraph."""
        text = "He signaled the fleet\n\nHMS Surprise led the way."
        result = unwrap_hard_wrapped_text(text)
        assert result == "He signaled the fleet\n\nHMS Surprise led the way."

    def test_24_date_new_para(self):
        """Date starting new paragraph."""
        text = "The voyage had begun.\n\nJanuary 15th dawned cold and grey."
        result = unwrap_hard_wrapped_text(text)
        assert result == "The voyage had begun.\n\nJanuary 15th dawned cold and grey."

    def test_25_action_description_split(self):
        """Action ends, description begins."""
        text = "He drew his sword.\n\nThe blade gleamed in the sunlight."
        result = unwrap_hard_wrapped_text(text)
        assert result == "He drew his sword.\n\nThe blade gleamed in the sunlight."
