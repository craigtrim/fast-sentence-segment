# -*- coding: UTF-8 -*-
"""Tests for issue #14: Quote-aware unwrap to join text across blank lines inside open quotes.

When a blank line appears inside a multi-sentence quote, the unwrap function
should recognize that we're inside an open quote and join the text, rather
than treating it as a paragraph break.

Related GitHub Issue:
    #14 - feat: Make unwrap quote-aware to join text across blank lines inside open quotes
    https://github.com/craigtrim/fast-sentence-segment/issues/14

These tests should FAIL before the fix is implemented and PASS after.
"""

import pytest

from fast_sentence_segment.dmo.unwrap_hard_wrapped_text import unwrap_hard_wrapped_text


# ==============================================================================
# SECTION 1: Basic Multi-Sentence Dialog with Blank Line
# ==============================================================================


class TestBasicMultiSentenceDialogWithBlankLine:
    """Basic cases where blank line appears inside a multi-sentence quote."""

    def test_01_maturin_introduction(self):
        """Original issue: Maturin's introduction from Master and Commander."""
        text = "'Mine, sir, is Maturin.\nI am to be found any morning at Joselito's coffee-house.\n\nMay I beg you to stand aside?'"
        result = unwrap_hard_wrapped_text(text)
        # All three sentences should be joined (no paragraph break)
        assert "\n\n" not in result
        assert "Joselito's coffee-house. May I beg" in result

    def test_02_two_sentences_blank_line_single_quotes(self):
        """Two sentences with blank line, single quotes."""
        text = "'First sentence here.\n\nSecond sentence here.'"
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result
        assert "here. Second" in result

    def test_03_two_sentences_blank_line_double_quotes(self):
        """Two sentences with blank line, double quotes."""
        text = '"First sentence here.\n\nSecond sentence here."'
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result
        assert "here. Second" in result

    def test_04_three_sentences_one_blank_line(self):
        """Three sentences with one blank line in middle."""
        text = '"One sentence.\nTwo sentence.\n\nThree sentence."'
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_05_three_sentences_two_blank_lines(self):
        """Three sentences with blank lines between each."""
        text = '"One sentence.\n\nTwo sentence.\n\nThree sentence."'
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_06_four_sentences_scattered_blank_lines(self):
        """Four sentences with scattered blank lines."""
        text = '"One.\n\nTwo.\nThree.\n\nFour."'
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result


# ==============================================================================
# SECTION 2: Complete Quotes (Should Still Split)
# ==============================================================================


class TestCompleteQuotesShouldSplit:
    """Complete quotes followed by new content should still split properly."""

    def test_07_complete_quote_then_narrative(self):
        """Complete quote followed by narrative should split."""
        text = '"Hello there."\n\nHe walked away.'
        result = unwrap_hard_wrapped_text(text)
        # Should have paragraph break - quote is complete
        assert "\n\n" in result

    def test_08_complete_quote_then_new_quote(self):
        """Complete quote followed by new quote should split."""
        text = '"First speaker."\n\n"Second speaker."'
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" in result

    def test_09_narrative_then_complete_quote(self):
        """Narrative followed by complete quote should split."""
        text = 'He arrived.\n\n"Hello there."'
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" in result

    def test_10_two_complete_quotes_same_speaker(self):
        """Two complete quotes should split."""
        text = '"Yes."\n\n"No."'
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" in result


# ==============================================================================
# SECTION 3: Dialog with Possessives
# ==============================================================================


class TestDialogWithPossessives:
    """Possessives like Joselito's should not affect quote tracking."""

    def test_11_possessive_in_first_sentence(self):
        """Possessive in first sentence of open quote."""
        text = "\"Jack's ship sailed.\n\nThe crew cheered.\""
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_12_possessive_in_middle_sentence(self):
        """Possessive in middle sentence of open quote."""
        text = '"First sentence.\nThe captain\'s orders were clear.\n\nThird sentence."'
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_13_possessive_in_last_sentence(self):
        """Possessive in last sentence of open quote."""
        text = '"First sentence.\n\nThat was Stephen\'s opinion."'
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_14_multiple_possessives(self):
        """Multiple possessives in open quote."""
        text = "\"Jack's ship met Stephen's expectations.\n\nThe Admiral's orders were followed.\""
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_15_long_possessive_name(self):
        """Long name possessive like Joselito's."""
        text = "'Meet me at Joselito's.\n\nI'll be waiting.'"
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result


# ==============================================================================
# SECTION 4: Dialog with Contractions
# ==============================================================================


class TestDialogWithContractions:
    """Contractions like don't, can't should not affect quote tracking."""

    def test_16_contraction_dont(self):
        """Contraction don't in open quote."""
        text = "\"I don't understand.\n\nPlease explain.\""
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_17_contraction_cant(self):
        """Contraction can't in open quote."""
        text = "\"I can't do it.\n\nIt's impossible.\""
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_18_contraction_wont(self):
        """Contraction won't in open quote."""
        text = "\"I won't agree.\n\nNever.\""
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_19_contraction_its(self):
        """Contraction it's in open quote."""
        text = "\"It's a beautiful day.\n\nThe sun is shining.\""
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_20_multiple_contractions(self):
        """Multiple contractions in open quote."""
        text = "\"I don't think he's coming.\n\nWe shouldn't wait.\""
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result


# ==============================================================================
# SECTION 5: Dialog with Elisions
# ==============================================================================


class TestDialogWithElisions:
    """Elisions like 'tis, 'twas should not affect quote tracking."""

    def test_21_elision_tis(self):
        """Elision 'tis in open quote."""
        text = "\"'Tis a fine day.\n\nThe weather is perfect.\""
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_22_elision_twas(self):
        """Elision 'twas in open quote."""
        text = "\"'Twas the night before.\n\nAll was quiet.\""
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_23_elision_em(self):
        """Elision 'em in open quote."""
        text = "\"Give 'em nothing!\n\nFire!\""
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_24_elision_cello(self):
        """Elision 'cello in open quote."""
        text = "\"The 'cello sounds beautiful.\n\nPlay on.\""
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_25_elision_ere(self):
        """Elision 'ere in open quote."""
        text = "\"Come 'ere quickly.\n\nI need help.\""
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result


# ==============================================================================
# SECTION 6: Mixed Dialog and Narrative
# ==============================================================================


class TestMixedDialogAndNarrative:
    """Mixed dialog and narrative with proper splitting."""

    def test_26_narrative_open_quote_narrative(self):
        """Narrative, then open quote, then narrative."""
        text = 'He spoke.\n\n"First sentence.\n\nSecond sentence."\n\nShe listened.'
        result = unwrap_hard_wrapped_text(text)
        # Should have breaks before/after the dialog, but not inside
        parts = result.split("\n\n")
        assert len(parts) == 3
        assert "First sentence. Second sentence." in parts[1]

    def test_27_dialog_with_tag_blank_continuation(self):
        """Dialog with tag, blank line, then continuation."""
        text = '"Hello," he said.\n\n"How are you?"'
        result = unwrap_hard_wrapped_text(text)
        # These are separate complete quotes - should split
        assert "\n\n" in result

    def test_28_narrative_breaks_around_dialog(self):
        """Narrative before and after multi-sentence dialog."""
        text = 'The captain spoke.\n\n"We sail at dawn.\n\nPrepare the ship."\n\nThe crew scrambled.'
        result = unwrap_hard_wrapped_text(text)
        parts = result.split("\n\n")
        assert len(parts) == 3


# ==============================================================================
# SECTION 7: Question and Exclamation Marks
# ==============================================================================


class TestQuestionAndExclamationMarks:
    """Question and exclamation marks inside open quotes."""

    def test_29_question_blank_statement(self):
        """Question followed by blank then statement in quote."""
        text = '"Where are you?\n\nI need to know."'
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_30_exclamation_blank_statement(self):
        """Exclamation followed by blank then statement in quote."""
        text = '"Fire!\n\nAll hands on deck!"'
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_31_statement_blank_question(self):
        """Statement followed by blank then question in quote."""
        text = '"I have a question.\n\nDo you understand?"'
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_32_statement_blank_exclamation(self):
        """Statement followed by blank then exclamation in quote."""
        text = '"This is it.\n\nCharge!"'
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result


# ==============================================================================
# SECTION 8: Curly Quotes
# ==============================================================================


class TestCurlyQuotes:
    """Curly/smart quotes should work the same as straight quotes."""

    def test_33_curly_double_quotes(self):
        """Curly double quotes with blank line."""
        text = "\u201cFirst sentence.\n\nSecond sentence.\u201d"
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_34_curly_single_quotes(self):
        """Curly single quotes with blank line."""
        text = "\u2018First sentence.\n\nSecond sentence.\u2019"
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_35_mixed_curly_straight(self):
        """Mixed curly and straight quotes."""
        text = "\u201cHe said 'hello'.\n\nShe nodded.\u201d"
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result


# ==============================================================================
# SECTION 9: Long Multi-Sentence Dialog
# ==============================================================================


class TestLongMultiSentenceDialog:
    """Long dialog passages with multiple blank lines."""

    def test_36_five_sentences_two_blanks(self):
        """Five sentences with two blank lines."""
        text = '"One.\nTwo.\n\nThree.\nFour.\n\nFive."'
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_37_speech_with_many_sentences(self):
        """Long speech with scattered blank lines."""
        text = '''"My dear sir.
I must confess.
The situation is most grave.

We find ourselves in a predicament.
I cannot see a way forward.

What would you advise?"'''
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_38_naval_orders(self):
        """Naval orders style dialog."""
        text = '''"Mr Pullings, set the topsails.

We sail with the morning tide.

The Admiral expects us at Gibraltar."'''
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result


# ==============================================================================
# SECTION 10: Edge Cases
# ==============================================================================


class TestEdgeCases:
    """Edge cases and unusual patterns."""

    def test_39_quote_at_very_start(self):
        """Quote starts at very beginning of text."""
        text = '"First.\n\nSecond."'
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_40_quote_at_very_end(self):
        """Text ends mid-quote (unclosed)."""
        text = 'He said, "First.\n\nSecond.'
        result = unwrap_hard_wrapped_text(text)
        # Unclosed quote - should still join
        assert "\n\n" not in result

    def test_41_single_char_sentences(self):
        """Single character sentences in quote."""
        text = '"A.\n\nB."'
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_42_ellipsis_blank_continuation(self):
        """Ellipsis followed by blank then continuation."""
        text = '"I thought...\n\nNever mind."'
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_43_multiple_blank_lines_inside_quote(self):
        """Multiple consecutive blank lines inside quote."""
        text = '"First.\n\n\nSecond."'
        result = unwrap_hard_wrapped_text(text)
        # Multiple blanks = definite break, even in quote? Or join?
        # For safety, join inside quotes
        assert "First." in result and "Second." in result

    def test_44_nested_quotes_with_blank(self):
        """Nested quotes with blank line."""
        text = "\"He said 'hello'.\n\nShe said 'goodbye'.\""
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result


# ==============================================================================
# SECTION 11: Real-World Ebook Patterns
# ==============================================================================


class TestRealWorldEbookPatterns:
    """Patterns commonly found in real ebooks."""

    def test_45_gutenberg_dialog_block(self):
        """Project Gutenberg style dialog block."""
        text = '''      "I am bound to say that in
      all the accounts which you have been so good as to give.

      May I beg you to continue?"'''
        result = unwrap_hard_wrapped_text(text)
        # After unwrapping indentation, should join across blank
        assert "give. May I beg" in result or "give.\n\nMay" not in result

    def test_46_mandc_style_dialog(self):
        """Master and Commander style dialog."""
        text = "'Mine, sir, is Maturin.\nI am to be found any morning at Joselito's coffee-house.\n\nMay I beg you to stand aside?'"
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_47_sherlock_holmes_dialog(self):
        """Sherlock Holmes style dialog."""
        text = '''"Well, Watson, what do you make of it?

I confess that I am at a loss.

This is a most singular case."'''
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_48_jane_austen_dialog(self):
        """Jane Austen style dialog with social commentary."""
        text = '''"It is a truth universally acknowledged.

A single man in possession of a good fortune.

Must be in want of a wife."'''
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result


# ==============================================================================
# SECTION 12: Boundary Between Speakers
# ==============================================================================


class TestBoundaryBetweenSpeakers:
    """Proper boundaries between different speakers."""

    def test_49_two_speakers_proper_split(self):
        """Two different speakers should split."""
        text = '"Hello," said Jack.\n\n"Goodbye," said Stephen.'
        result = unwrap_hard_wrapped_text(text)
        # These are complete, attributed quotes - should split
        assert "\n\n" in result

    def test_50_alternating_speakers(self):
        """Alternating speakers should split."""
        text = '"Yes."\n\n"No."\n\n"Perhaps."'
        result = unwrap_hard_wrapped_text(text)
        # Each is complete - should split
        parts = result.split("\n\n")
        assert len(parts) == 3

    def test_51_speaker_tag_then_continuation(self):
        """Speaker tag between quote parts."""
        text = '"Hello," he said.\n\n"How are you today?"'
        result = unwrap_hard_wrapped_text(text)
        # First quote is complete with tag, second is new - split
        assert "\n\n" in result


# ==============================================================================
# SECTION 13: Punctuation Variations
# ==============================================================================


class TestPunctuationVariations:
    """Various punctuation patterns inside quotes."""

    def test_52_semicolon_blank_continuation(self):
        """Semicolon followed by blank in quote."""
        text = '"First clause;\n\nSecond clause."'
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_53_colon_blank_continuation(self):
        """Colon followed by blank in quote."""
        text = '"Here is the list:\n\nFirst item."'
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_54_dash_blank_continuation(self):
        """Dash followed by blank in quote."""
        text = '"I thought--\n\nNo, never mind."'
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_55_comma_blank_continuation(self):
        """Comma followed by blank in quote (unusual but possible)."""
        text = '"Well,\n\nI suppose so."'
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result


# ==============================================================================
# SECTION 14: Quote Parity Edge Cases
# ==============================================================================


class TestQuoteParityEdgeCases:
    """Edge cases involving quote parity tracking."""

    def test_56_unbalanced_quote_start(self):
        """Text starts mid-quote (odd parity from start)."""
        text = 'continued speaking.\n\nAnd then he stopped."'
        result = unwrap_hard_wrapped_text(text)
        # Hard to determine - preserve paragraph for safety
        # This is ambiguous without more context

    def test_57_triple_quote_nesting(self):
        """Triple level quote nesting."""
        text = "\"He said 'She said \\\"hello\\\" to me'.\n\nIt was confusing.\""
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_58_quote_spans_many_lines(self):
        """Quote that spans many lines with multiple blanks."""
        text = '''"Line one.
Line two.

Line three.
Line four.

Line five."'''
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_59_single_quote_vs_apostrophe(self):
        """Distinguish single quote from apostrophe."""
        text = "'Jack's ship sailed.\n\nThe crew's morale was high.'"
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result

    def test_60_year_elision_in_quote(self):
        """Year elision like '99 inside quote."""
        text = "\"Back in '99 it happened.\n\nNo one expected it.\""
        result = unwrap_hard_wrapped_text(text)
        assert "\n\n" not in result
