# -*- coding: UTF-8 -*-
"""Regression tests for ebook formatting issues.

Tests for:
1. Spurious sentence breaks from double spaces/OCR artifacts
2. Paragraph formatting with --format flag
3. Real-world ebook text patterns from Master and Commander

These tests cover scenarios similar to the reported defects:
- "His colour." appearing as separate sentence
- Missing paragraph breaks in --format output
"""

import pytest

from fast_sentence_segment import segment_text
from fast_sentence_segment.dmo.dialog_formatter import format_dialog
from fast_sentence_segment.dmo.unwrap_hard_wrapped_text import unwrap_hard_wrapped_text


class TestSpuriousSentenceBreaks:
    """Tests for spurious sentence breaks from double spaces/OCR artifacts.

    When text has double spaces (from OCR or formatting), they should NOT
    cause spurious sentence breaks like "His colour. mounted".
    """

    # ──────────────────────────────────────────────────────────────────────────
    # Basic double-space scenarios
    # ──────────────────────────────────────────────────────────────────────────

    def test_double_space_mid_sentence(self):
        """Double space mid-sentence should not create break."""
        text = "His colour  mounted quickly."
        result = segment_text(text, flatten=True, unwrap=True)
        assert len(result) == 1
        assert "colour" in result[0] and "mounted" in result[0]

    def test_double_space_before_verb(self):
        """Double space before verb should not create break."""
        text = "The ship  sailed into port."
        result = segment_text(text, flatten=True, unwrap=True)
        assert len(result) == 1
        assert "ship" in result[0] and "sailed" in result[0]

    def test_double_space_after_noun(self):
        """Double space after noun should not create break."""
        text = "Jack  turned to his companion."
        result = segment_text(text, flatten=True, unwrap=True)
        assert len(result) == 1
        assert "Jack" in result[0] and "turned" in result[0]

    def test_double_space_between_adjective_noun(self):
        """Double space between adjective and noun should not create break."""
        text = "The cold  wind blew from the east."
        result = segment_text(text, flatten=True, unwrap=True)
        assert len(result) == 1
        assert "cold" in result[0] and "wind" in result[0]

    def test_triple_space_mid_sentence(self):
        """Triple space mid-sentence should not create break."""
        text = "He stood   watching the horizon."
        result = segment_text(text, flatten=True, unwrap=True)
        assert len(result) == 1
        assert "stood" in result[0] and "watching" in result[0]

    # ──────────────────────────────────────────────────────────────────────────
    # Real Master and Commander patterns
    # ──────────────────────────────────────────────────────────────────────────

    def test_mandc_colour_mounted(self):
        """The original 'His colour mounted' pattern that caused the defect."""
        text = "Jack Aubrey's face changed. His colour  mounted; he fixed his eye."
        result = segment_text(text, flatten=True, unwrap=True)
        # "His colour mounted" should be one sentence, not split
        full_text = " ".join(result)
        assert "colour" in full_text and "mounted" in full_text
        # Should not have "colour." as end of sentence
        for sent in result:
            assert not sent.strip().endswith("colour.")

    def test_mandc_hostility_pattern(self):
        """Baffled hostility pattern should not be split."""
        text = "expression of somewhat  baffled hostility"
        result = segment_text(text, flatten=True, unwrap=True)
        assert len(result) == 1
        assert "baffled hostility" in result[0]

    def test_mandc_acknowledging_pattern(self):
        """He could not but acknowledge pattern."""
        text = "he could not  but acknowledge that he had been beating the time"
        result = segment_text(text, flatten=True, unwrap=True)
        assert len(result) == 1
        assert "could not" in result[0] and "acknowledge" in result[0]

    def test_mandc_perfect_accuracy(self):
        """Perfect accuracy pattern should stay together."""
        text = "he had certainly done so with  perfect accuracy"
        result = segment_text(text, flatten=True, unwrap=True)
        assert len(result) == 1
        assert "perfect accuracy" in result[0]

    def test_mandc_thing_was_wrong(self):
        """'In itself the thing was wrong' should stay together."""
        text = "although accurate, in itself  the thing was wrong"
        result = segment_text(text, flatten=True, unwrap=True)
        assert len(result) == 1
        assert "the thing was wrong" in result[0]

    # ──────────────────────────────────────────────────────────────────────────
    # Multiple double spaces in text
    # ──────────────────────────────────────────────────────────────────────────

    def test_multiple_double_spaces(self):
        """Multiple double spaces should all be normalized."""
        text = "Jack  Aubrey's  face  instantly changed."
        result = segment_text(text, flatten=True, unwrap=True)
        assert len(result) == 1
        assert "Jack" in result[0] and "changed" in result[0]

    def test_double_space_near_punctuation(self):
        """Double space near punctuation should be handled correctly."""
        text = "He said,  'Hello there.'"
        result = segment_text(text, flatten=True, unwrap=True)
        assert len(result) == 1

    def test_double_space_after_semicolon(self):
        """Double space after semicolon should stay in same sentence if appropriate."""
        text = "He paused;  his thoughts drifted."
        result = segment_text(text, flatten=True, unwrap=True)
        # This could be one or two sentences depending on segmenter, but no spurious splits
        full = " ".join(result)
        assert "paused" in full and "thoughts" in full


class TestNarrativeParagraphFormatting:
    """Tests for --format flag narrative paragraph formatting.

    Each narrative sentence should be its own paragraph with blank lines between.
    """

    # ──────────────────────────────────────────────────────────────────────────
    # Basic narrative paragraph tests
    # ──────────────────────────────────────────────────────────────────────────

    def test_two_narrative_sentences(self):
        """Two narrative sentences should each be their own paragraph."""
        sentences = [
            "The listener was a man between twenty and thirty.",
            "He was wearing his best uniform.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 2

    def test_three_narrative_sentences(self):
        """Three narrative sentences should each be their own paragraph."""
        sentences = [
            "The sun was setting.",
            "The wind had died down.",
            "All was calm.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_five_narrative_sentences(self):
        """Five narrative sentences should each be their own paragraph."""
        sentences = [
            "First sentence here.",
            "Second sentence here.",
            "Third sentence here.",
            "Fourth sentence here.",
            "Fifth sentence here.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 5

    # ──────────────────────────────────────────────────────────────────────────
    # Real ebook narrative patterns
    # ──────────────────────────────────────────────────────────────────────────

    def test_mandc_opening_passage(self):
        """Master and Commander opening passage style."""
        sentences = [
            "And on the little gilt chairs at least some of the audience were following the rise with an equal intensity.",
            "There were two in the third row, on the left-hand side.",
            "They happened to be sitting next to one another.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3
        assert "gilt chairs" in paragraphs[0]
        assert "third row" in paragraphs[1]
        assert "sitting next" in paragraphs[2]

    def test_mandc_character_description(self):
        """Character description passage."""
        sentences = [
            "The listener farther to the left was a man of between twenty and thirty whose big form overflowed his seat.",
            "He was wearing his best uniform.",
            "His bright blue eyes gazed fixedly at the bow of the first violin.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_mandc_action_sequence(self):
        """Action sequence passage."""
        sentences = [
            "The high note came, the pause, the resolution.",
            "With the resolution the fist swept firmly down upon his knee.",
            "He leant back in his chair.",
            "He sighed happily and turned towards his neighbour with a smile.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4

    def test_mandc_emotional_passage(self):
        """Emotional description passage."""
        sentences = [
            "Jack Aubrey faced him with hostility.",
            "He could not but acknowledge that he had been beating the time.",
            "His colour mounted.",
            "He fixed his eye upon the man for a moment.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4

    # ──────────────────────────────────────────────────────────────────────────
    # Mixed dialog and narrative
    # ──────────────────────────────────────────────────────────────────────────

    def test_narrative_before_dialog(self):
        """Narrative sentences before dialog should each be paragraphs."""
        sentences = [
            "The room was silent.",
            "Everyone waited.",
            '"At last," he said.',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_narrative_after_dialog(self):
        """Narrative sentences after dialog should each be paragraphs."""
        sentences = [
            '"Very well," she replied.',
            "The door closed behind her.",
            "He stood alone in the darkness.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_narrative_between_dialog(self):
        """Narrative sentences between dialog should each be paragraphs."""
        sentences = [
            '"Hello," said Jack.',
            "There was a long pause.",
            "The clock ticked steadily.",
            '"Goodbye," said Mary.',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4


class TestMultiSentenceDialogStaysTogether:
    """Tests for multi-sentence dialog staying on one line.

    When dialog is enclosed in quotes and spans multiple sentences,
    those sentences should stay together, not split across paragraphs.
    """

    # ──────────────────────────────────────────────────────────────────────────
    # Basic multi-sentence dialog tests
    # ──────────────────────────────────────────────────────────────────────────

    def test_single_speaker_three_sentences(self):
        """Three sentences in one quote should stay together."""
        sentences = [
            "'Mine, sir, is Maturin.",
            "I am to be found any morning at Joselito's coffee-house.",
            "May I beg you to stand aside?'",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    def test_single_speaker_two_sentences(self):
        """Two sentences in one quote should stay together."""
        sentences = [
            '"I am delighted to meet you.',
            'Pray, come this way."',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    def test_single_speaker_four_sentences(self):
        """Four sentences in one quote should stay together."""
        sentences = [
            '"First sentence here.',
            "Second sentence here.",
            "Third sentence here.",
            'Fourth and final."',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    def test_single_speaker_five_sentences(self):
        """Five sentences in one quote should stay together."""
        sentences = [
            '"One.',
            "Two.",
            "Three.",
            "Four.",
            'Five."',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Possessives and contractions
    # ──────────────────────────────────────────────────────────────────────────

    def test_dialog_with_possessives(self):
        """Dialog containing possessives should stay together."""
        sentences = [
            "'The captain's orders were clear.",
            "We must follow the ship's course.",
            "That is the Admiral's decision.'",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    def test_dialog_with_contractions(self):
        """Dialog containing contractions should stay together."""
        sentences = [
            '"I don\'t know what you mean.',
            "It wasn't my intention.",
            'I can\'t explain it."',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    def test_dialog_with_mixed_apostrophes(self):
        """Dialog with both possessives and contractions stays together."""
        sentences = [
            "'Jack's ship won't arrive until tomorrow.",
            "The captain's orders can't be ignored.",
            "That's the Admiral's way.'",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    def test_dialog_with_names_possessive(self):
        """Dialog with name possessives like Joselito's should stay together."""
        sentences = [
            "'Meet me at Joselito's.",
            "We'll discuss Stephen's plan.",
            "And Jack's objections.'",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    def test_dialog_multiple_contractions_per_sentence(self):
        """Dialog with multiple contractions per sentence stays together."""
        sentences = [
            '"I won\'t say I didn\'t try.',
            "It's not that I couldn't do it.",
            'I just wouldn\'t."',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    def test_dialog_its_vs_apostrophe_s(self):
        """Dialog with its (possessive) vs it's (contraction) stays together."""
        sentences = [
            '"It\'s clear the ship lost its way.',
            "Its crew wasn't prepared.",
            'It\'s a tragedy."',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Multiple speakers (should separate)
    # ──────────────────────────────────────────────────────────────────────────

    def test_two_speakers_separate_paragraphs(self):
        """Two complete dialog turns should be separate paragraphs."""
        sentences = [
            "'Hello there, my friend.'",
            "'Goodbye, and fare thee well.'",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 2

    def test_three_speakers_separate_paragraphs(self):
        """Three complete dialog turns should be three paragraphs."""
        sentences = [
            '"First speaker here."',
            '"Second speaker responds."',
            '"Third speaker adds."',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_alternating_dialog(self):
        """Alternating speakers should create separate paragraphs."""
        sentences = [
            '"Yes."',
            '"No."',
            '"Perhaps."',
            '"Definitely."',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4

    # ──────────────────────────────────────────────────────────────────────────
    # Long dialog passages
    # ──────────────────────────────────────────────────────────────────────────

    def test_long_dialog_passage(self):
        """Long dialog passage should stay as one paragraph."""
        sentences = [
            '"My dear sir, I must confess.',
            "The situation is most grave.",
            "We find ourselves in a predicament.",
            "I cannot see a way forward.",
            'What would you advise?"',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    def test_very_long_dialog_six_sentences(self):
        """Six sentences in dialog should stay together."""
        sentences = [
            '"I have much to tell you.',
            "The news arrived yesterday.",
            "It concerns the war.",
            "The enemy has advanced.",
            "Our forces are retreating.",
            'We must act now."',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    def test_dialog_with_questions_and_statements(self):
        """Mix of questions and statements in dialog stays together."""
        sentences = [
            '"What do you mean?',
            "I thought you understood.",
            "Is this not clear?",
            'Let me explain again."',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    def test_dialog_with_exclamations(self):
        """Dialog with exclamations stays together."""
        sentences = [
            '"Fire!',
            "All hands on deck!",
            "The enemy approaches!",
            'To arms!"',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Master and Commander examples
    # ──────────────────────────────────────────────────────────────────────────

    def test_mandc_maturin_introduction(self):
        """Real example: Maturin's introduction from Master and Commander."""
        sentences = [
            "'Mine, sir, is Maturin.",
            "I am to be found any morning at Joselito's coffee-house.",
            "May I beg you to stand aside?'",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    def test_mandc_naval_orders(self):
        """Naval orders style dialog stays together."""
        sentences = [
            '"Mr Pullings, set the topsails.',
            "We sail with the morning tide.",
            'The Admiral expects us at Gibraltar."',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    def test_mandc_doctor_patient(self):
        """Doctor-patient dialog stays together."""
        sentences = [
            '"Your fever has broken.',
            "The wound is healing well.",
            "You'll be on your feet within a week.",
            'Take this tincture twice daily."',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    def test_mandc_mess_conversation(self):
        """Mess deck conversation with contractions."""
        sentences = [
            "\"There's been talk below decks.",
            "The men aren't happy.",
            "They've heard we're heading to the Indies.",
            "That's a year's voyage at least.",
            "I don't like the mood.\"",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Edge cases
    # ──────────────────────────────────────────────────────────────────────────

    def test_dialog_ending_with_question(self):
        """Dialog ending with question mark stays together."""
        sentences = [
            '"I have been thinking.',
            "What if we tried a different approach?'",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    def test_dialog_with_ellipsis_in_middle(self):
        """Dialog with sentence ending in ellipsis stays together."""
        sentences = [
            '"I was thinking...',
            "Perhaps we should wait.",
            'Yes, that would be best."',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    def test_single_word_sentences_in_dialog(self):
        """Single word sentences in dialog stay together."""
        sentences = [
            '"Indeed.',
            "Yes.",
            "Absolutely.",
            'Agreed."',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    def test_dialog_with_numbers(self):
        """Dialog containing numbers stays together."""
        sentences = [
            '"We need 50 men.',
            "The voyage takes 3 months.",
            'Provisions for 100 days."',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    def test_dialog_with_double_quotes(self):
        """Dialog using double quotes stays together."""
        sentences = [
            '"First sentence.',
            "Middle sentence.",
            'Final sentence."',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    def test_dialog_with_single_quotes(self):
        """Dialog using single quotes stays together."""
        sentences = [
            "'First sentence.",
            "Middle sentence.",
            "Final sentence.'",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1


class TestEndToEndEbookFormatting:
    """End-to-end tests for ebook processing with segment_text and format."""

    def test_unwrapped_narrative_with_format(self):
        """Full pipeline: unwrap + segment + format for narrative text."""
        # Simulated hard-wrapped ebook text
        text = (
            "The listener farther to the left was a man\n"
            "of between twenty and thirty. He was wearing\n"
            "his best uniform."
        )
        result = segment_text(text, flatten=True, unwrap=True, format="dialog")
        # Should have paragraph breaks between sentences
        assert "\n\n" in result
        # Check sentences are present
        assert "listener" in result
        assert "uniform" in result

    def test_no_spurious_periods_in_formatted_output(self):
        """Formatted output should not have spurious periods from double spaces."""
        text = "His colour  mounted; he fixed his eye."
        result = segment_text(text, flatten=True, unwrap=True, format="dialog")
        # Should not have "colour." as a separate sentence
        assert "colour." not in result.replace("colour. mounted", "VALID")

    def test_long_narrative_passage_formatting(self):
        """Long narrative passage should format with paragraph breaks."""
        sentences = [
            "At least some of the audience were following the rise with equal intensity.",
            "There were two in the third row, on the left-hand side.",
            "They happened to be sitting next to one another.",
            "The listener farther to the left was a man between twenty and thirty.",
            "His big form overflowed his seat.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        # Each sentence should be its own paragraph
        assert len(paragraphs) == 5

    def test_format_dialog_preserves_sentence_content(self):
        """format_dialog should not alter sentence content, only add breaks."""
        sentences = [
            "First sentence.",
            "Second sentence.",
            "Third sentence.",
        ]
        result = format_dialog(sentences)
        assert "First sentence." in result
        assert "Second sentence." in result
        assert "Third sentence." in result


class TestUnwrapDoubleSpaceEdgeCases:
    """Edge cases for double-space handling in unwrap."""

    def test_space_at_line_join(self):
        """When lines are joined, result should have single space."""
        text = "end of line\nstart of next"
        result = unwrap_hard_wrapped_text(text)
        assert "line start" in result
        # No double space
        assert "  " not in result

    def test_trailing_space_before_newline(self):
        """Trailing space before newline should not create double space."""
        text = "end of line \nstart of next"
        result = unwrap_hard_wrapped_text(text)
        # Should be single space between words
        assert "  " not in result

    def test_leading_space_after_newline(self):
        """Leading space after newline (indentation) should be handled."""
        text = "end of line\n  start of next"
        result = unwrap_hard_wrapped_text(text)
        # Should be single space between words
        assert "  " not in result

    def test_both_trailing_and_leading_space(self):
        """Both trailing and leading spaces should result in single space."""
        text = "end of line \n  start of next"
        result = unwrap_hard_wrapped_text(text)
        assert "  " not in result
        assert "line start" in result
