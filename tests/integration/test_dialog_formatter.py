# -*- coding: UTF-8 -*-
"""Tests for DialogFormatter - dialog-aware paragraph formatting.

Related GitHub Issue:
    #10 - feat: Add --format flag for dialog-aware paragraph formatting
    https://github.com/craigtrim/fast-sentence-segment/issues/10
"""

import pytest

from fast_sentence_segment.dmo.dialog_formatter import (
    DialogFormatter,
    format_dialog,
)


class TestDialogFormatterBasic:
    """Basic tests for dialog formatting."""

    def test_empty_input(self):
        """Empty input returns empty string."""
        assert format_dialog([]) == ""

    def test_single_sentence_no_quotes(self):
        """Single sentence without quotes formats as-is."""
        result = format_dialog(["He walked down the street."])
        assert result == "He walked down the street."

    def test_single_quoted_sentence(self):
        """Single complete quoted sentence formats as-is."""
        result = format_dialog(['"Hello there," she said.'])
        assert result == '"Hello there," she said.'

    def test_multiple_unquoted_sentences(self):
        """Multiple narrative sentences are kept together."""
        sentences = [
            "The sun was setting.",
            "Birds flew across the sky.",
            "It was peaceful.",
        ]
        result = format_dialog(sentences)
        # Narrative sentences should be grouped together
        assert "The sun was setting.\nBirds flew across the sky." in result


class TestDialogFormatterQuotedSpeech:
    """Tests for keeping quoted speech together."""

    def test_multi_sentence_quote_stays_together(self):
        """Multiple sentences within one quote stay grouped."""
        sentences = [
            '"My dear sir, cried the man in the black coat.',
            'You had every reason to be carried away.',
            'I have never heard a better quartetto in my life."',
        ]
        result = format_dialog(sentences)
        # All three sentences should be in the same paragraph (no double newlines between them)
        lines = result.split("\n\n")
        # Should be one group
        assert len(lines) == 1

    def test_separate_speakers_get_paragraph_breaks(self):
        """Different speakers/quotes get paragraph breaks between them."""
        sentences = [
            '"You are very good, sir."',
            '"I should like it of all things."',
        ]
        result = format_dialog(sentences)
        # Each complete quoted sentence is its own paragraph
        assert "\n\n" in result

    def test_narrative_after_dialog_gets_break(self):
        """Narrative text after dialog gets a paragraph break."""
        sentences = [
            '"Hello there," said Jack.',
            "The room fell silent.",
            "Everyone looked at him.",
        ]
        result = format_dialog(sentences)
        # Dialog and narrative should be separated
        assert "\n\n" in result

    def test_dialog_tag_keeps_quote_together(self):
        """A quote with dialog tag stays together."""
        sentences = [
            '"I have just been promoted," he added, with an off-hand laugh.',
        ]
        result = format_dialog(sentences)
        assert result == '"I have just been promoted," he added, with an off-hand laugh.'


class TestDialogFormatterComplexScenarios:
    """Tests for complex dialog scenarios from the issue example."""

    def test_extended_dialog_passage(self):
        """Test extended dialog passage with clear speaker turns."""
        # Using cleaner quote patterns for reliable parsing
        sentences = [
            '"My dear sir," cried the man, "you had every reason to be carried away.',
            'I have never heard a better quartetto in my life.',
            'May I propose a cup of chocolate?"',
            '"You are very good, sir.',
            'I should like it of all things.',
            'I have just been promoted," he added.',
            '"Have you indeed?',
            'I wish you joy of it.',
            'Pray walk in."',
        ]
        result = format_dialog(sentences)

        # First speaker (sentences 1-3), second speaker (4-6), first speaker response (7-9)
        paragraphs = result.split("\n\n")

        # Should have 3 paragraphs (3 turns of dialog)
        assert len(paragraphs) == 3
        # First paragraph should contain "My dear sir"
        assert "My dear sir" in paragraphs[0]
        # Second paragraph should start the second speaker
        assert "You are very good" in paragraphs[1]
        # Third paragraph should be the response
        assert "Have you indeed" in paragraphs[2]

    def test_mixed_dialog_and_narrative(self):
        """Test mixing dialog with narrative description."""
        sentences = [
            "At the sight of Mr Maturin the waiter waved his forefinger.",
            "Maturin shrugged, said to Jack, 'The posts are wonderfully slow these days.'",
            "'Bring us a pot of chocolate, Jep, furiously whipped, and some cream.'",
        ]
        result = format_dialog(sentences)

        # Should have paragraph breaks between different types
        paragraphs = result.split("\n\n")
        assert len(paragraphs) >= 2

    def test_question_and_response_pattern(self):
        """Questions and responses are properly separated."""
        sentences = [
            "'Have you indeed?'",
            "'I wish you joy of it with all my heart, sure.'",
        ]
        result = format_dialog(sentences)
        # Two complete quotes should be separate paragraphs
        assert "\n\n" in result


class TestDialogFormatterEdgeCases:
    """Edge cases and special handling."""

    def test_handles_single_quotes(self):
        """Handles single quotes (apostrophes) for dialog."""
        sentences = [
            "'Hello,' he said.",
            "'Goodbye,' she replied.",
        ]
        result = format_dialog(sentences)
        # Two complete quoted sentences should be separate
        assert "\n\n" in result

    def test_handles_mixed_quote_styles(self):
        """Handles mixed double and single quotes."""
        sentences = [
            '"Hello," he said.',
            "'Goodbye,' she replied.",
        ]
        result = format_dialog(sentences)
        assert "\n\n" in result

    def test_long_narrative_passage(self):
        """Long narrative passage stays as one paragraph."""
        sentences = [
            "He laughed so heartily at the recollection.",
            "The waiter with the chocolate laughed too.",
            "He said, 'Fine day, Captain, sir, fine day!'",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        # All narrative (including embedded speech) stays together
        # Note: "He said, '...'" starts with narrative, not a quote
        assert len(paragraphs) == 1

    def test_narrative_then_direct_dialog(self):
        """Narrative followed by direct dialog gets paragraph break."""
        sentences = [
            "He laughed so heartily at the recollection.",
            "The waiter laughed too.",
            "'Fine day, Captain, sir!'",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        # Narrative grouped, then direct dialog is new paragraph
        assert len(paragraphs) == 2
        assert "laughed" in paragraphs[0]
        assert "Fine day" in paragraphs[1]

    def test_incomplete_quote_handling(self):
        """Incomplete quotes (no closing) are handled gracefully."""
        sentences = [
            '"The probability lies in that direction.',
            "And if we take this as a working hypothesis.",
            "He paused.",
        ]
        result = format_dialog(sentences)
        # Should still produce valid output
        assert result
        assert "The probability lies in that direction." in result


class TestDialogFormatterClass:
    """Tests for the DialogFormatter class interface."""

    def test_class_instantiation(self):
        """DialogFormatter can be instantiated."""
        formatter = DialogFormatter()
        assert formatter is not None

    def test_class_process_method(self):
        """DialogFormatter.process() works correctly."""
        formatter = DialogFormatter()
        sentences = ['"Hello," he said.', "The door opened."]
        result = formatter.process(sentences)
        assert isinstance(result, str)
        assert "Hello" in result

    def test_static_format_method(self):
        """Static format_dialog() function works."""
        result = format_dialog(["Test sentence."])
        assert result == "Test sentence."
