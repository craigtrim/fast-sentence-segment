# -*- coding: utf-8 -*-
"""
Ellipsis Chaos Test Suite

Edge cases that test the limits of ellipsis handling.
These represent real-world messy text patterns.

Reference: GitHub Issue #19
"""
import pytest
from fast_sentence_segment import segment_text


class TestEmotionalEllipsis:
    """Ellipsis as emotional expression."""

    def test_passive_aggressive_fine(self):
        """Ellipsis as emotional hostage-taking."""
        text = "Fine..."
        expected = ["Fine..."]
        assert segment_text(text, flatten=True) == expected

    def test_veiled_threat(self):
        """Ellipsis as threat-without-content."""
        text = "Just wait..."
        expected = ["Just wait..."]
        assert segment_text(text, flatten=True) == expected

    def test_passive_aggressive_double(self):
        """Ellipsis as passive-aggressive period."""
        text = "Sure... whatever..."
        expected = ["Sure... whatever..."]
        assert segment_text(text, flatten=True) == expected

    def test_fake_suspense(self):
        """Ellipsis as fake suspense."""
        text = "And then he opened the door..."
        expected = ["And then he opened the door..."]
        assert segment_text(text, flatten=True) == expected

    def test_unfinished_threat(self):
        """Ellipsis as 'I refuse to finish this thought'."""
        text = "If you do that again..."
        expected = ["If you do that again..."]
        assert segment_text(text, flatten=True) == expected

    def test_sarcastic_delay(self):
        """Ellipsis as sarcastic delay."""
        text = "Oh... brilliant idea."
        expected = ["Oh... brilliant idea."]
        assert segment_text(text, flatten=True) == expected

    def test_trailing_into_silence(self):
        """Ellipsis as speech trailing into silence."""
        text = "I thought you loved me..."
        expected = ["I thought you loved me..."]
        assert segment_text(text, flatten=True) == expected


class TestEllipsisDashCollision:
    """Ellipsis combined with em-dashes and other punctuation."""

    def test_abrupt_cutoff(self):
        """Ellipsis plus abrupt dash cutoff."""
        text = "I swear to— ..."
        expected = ["I swear to— ..."]
        assert segment_text(text, flatten=True) == expected

    def test_dash_collision(self):
        """Ellipsis with dash collision."""
        text = "Well... —no, forget it"
        expected = ["Well... —no, forget it"]
        assert segment_text(text, flatten=True) == expected

    def test_dash_then_ellipsis(self):
        text = "I thought—... never mind."
        expected = ["I thought—... never mind."]
        assert segment_text(text, flatten=True) == expected


class TestEllipsisMaskingContent:
    """Ellipsis used to mask or redact content."""

    def test_masking_redaction(self):
        """Ellipsis masking redaction."""
        text = "He was a real... gentleman."
        expected = ["He was a real... gentleman."]
        assert segment_text(text, flatten=True) == expected

    def test_censored_word(self):
        text = "What the... heck?"
        expected = ["What the... heck?"]
        assert segment_text(text, flatten=True) == expected

    def test_implied_profanity(self):
        text = "Son of a..."
        expected = ["Son of a..."]
        assert segment_text(text, flatten=True) == expected


class TestBrokenDialogue:
    """Ellipsis in stuttering/broken dialogue."""

    def test_stuttering_dialogue(self):
        """Ellipsis inside broken dialogue."""
        text = '"I… I can\'t…"'
        expected = ['"I… I can\'t…"']
        assert segment_text(text, flatten=True) == expected

    def test_hesitant_speech(self):
        text = '"I... I don\'t... know..."'
        expected = ['"I... I don\'t... know..."']
        assert segment_text(text, flatten=True) == expected

    def test_trailing_off_in_quotes(self):
        text = '"And then I..." He stopped.'
        expected = ['"And then I..."', "He stopped."]
        assert segment_text(text, flatten=True) == expected


class TestEllipsisSpam:
    """Excessive/spammed ellipsis usage."""

    def test_indecision_spam(self):
        """Ellipsis spam as indecision."""
        text = "uh... um... maybe..."
        expected = ["uh... um... maybe..."]
        assert segment_text(text, flatten=True) == expected

    def test_repeated_ellipsis(self):
        """Ellipsis after ellipsis."""
        text = "... ... ..."
        expected = ["... ... ..."]
        assert segment_text(text, flatten=True) == expected

    def test_ellipsis_only_sentence(self):
        """Ellipsis used as a whole sentence."""
        text = "..."
        expected = ["..."]
        assert segment_text(text, flatten=True) == expected

    def test_multiple_trailing(self):
        text = "okay... fine... whatever... done."
        expected = ["okay... fine... whatever... done."]
        assert segment_text(text, flatten=True) == expected


class TestRhetoricalEllipsis:
    """Ellipsis in rhetorical/question contexts."""

    def test_rhetorical_void(self):
        """Ellipsis as rhetorical void."""
        text = "And you expect me to... what?"
        expected = ["And you expect me to... what?"]
        assert segment_text(text, flatten=True) == expected

    def test_before_scream_punctuation(self):
        """Ellipsis before scream punctuation."""
        text = "Don't you dare...!"
        expected = ["Don't you dare...!"]
        assert segment_text(text, flatten=True) == expected

    def test_leading_question(self):
        text = "So you're saying...?"
        expected = ["So you're saying...?"]
        assert segment_text(text, flatten=True) == expected


class TestEllipsisWithEmoji:
    """Ellipsis near emoji (modern text patterns)."""

    def test_emoji_contamination(self):
        """Ellipsis + emoji contamination."""
        text = "Sure... 🙂"
        expected = ["Sure... 🙂"]
        assert segment_text(text, flatten=True) == expected

    def test_emoji_before_ellipsis(self):
        text = "🤔..."
        expected = ["🤔..."]
        assert segment_text(text, flatten=True) == expected

    def test_emoji_sandwich(self):
        text = "😅... 😬"
        expected = ["😅... 😬"]
        assert segment_text(text, flatten=True) == expected


class TestFragmentedSpeech:
    """Ellipsis in fragmented/incomplete structures."""

    def test_missing_subject(self):
        """Ellipsis hiding missing subject."""
        text = "Went to the store..."
        expected = ["Went to the store..."]
        assert segment_text(text, flatten=True) == expected

    def test_between_fragments(self):
        """Ellipsis between fragments."""
        text = "So... yeah. That happened."
        expected = ["So... yeah.", "That happened."]
        assert segment_text(text, flatten=True) == expected

    def test_fragment_chain(self):
        text = "You know... the thing... with the stuff..."
        expected = ["You know... the thing... with the stuff..."]
        assert segment_text(text, flatten=True) == expected


class TestCorruptedEllipsis:
    """Ellipsis in OCR-corrupted or malformed text."""

    def test_ocr_corrupted_spaced(self):
        """Ellipsis in OCR-corrupted text."""
        text = "W e l l . . ."
        # This might get mangled - just ensure no crash
        result = segment_text(text, flatten=True)
        assert len(result) >= 1

    def test_extra_spaces(self):
        text = "Well  ...  okay"
        result = segment_text(text, flatten=True)
        assert len(result) >= 1

    def test_mixed_dots_spaces(self):
        text = "So. . ... maybe"
        result = segment_text(text, flatten=True)
        assert len(result) >= 1


class TestMultilingualEllipsis:
    """Ellipsis in multilingual contexts."""

    def test_multilingual_mix(self):
        """Ellipsis in multilingual punctuation mix."""
        text = "Bueno… okay..."
        expected = ["Bueno… okay..."]
        assert segment_text(text, flatten=True) == expected

    def test_unicode_and_ascii_mix(self):
        text = "First… then... finally."
        expected = ["First… then... finally."]
        assert segment_text(text, flatten=True) == expected


class TestNestedQuoteEllipsis:
    """Ellipsis within nested quote structures."""

    def test_nested_single_in_double(self):
        """Ellipsis with nested quotes."""
        text = "\"He said 'I don't know...' and left.\""
        expected = ["\"He said 'I don't know...' and left.\""]
        assert segment_text(text, flatten=True) == expected

    def test_nested_double_in_single(self):
        text = "'She replied \"Whatever...\" coldly.'"
        expected = ["'She replied \"Whatever...\" coldly.'"]
        assert segment_text(text, flatten=True) == expected


class TestEllipsisInTechnicalContext:
    """Ellipsis near URLs, paths, and code."""

    def test_url_path_ellipsis(self):
        """Ellipsis near URLs/paths."""
        text = "See example.com/.../index for details."
        # The /.../ in URL should be preserved
        result = segment_text(text, flatten=True)
        assert "..." in result[0] or "/.../" in result[0]

    def test_code_comment_ellipsis(self):
        """Ellipsis in code/comments."""
        text = "// TODO... maybe fix later"
        expected = ["// TODO... maybe fix later"]
        assert segment_text(text, flatten=True) == expected

    def test_path_like(self):
        text = "Check /home/.../config file."
        result = segment_text(text, flatten=True)
        assert len(result) >= 1


class TestEllipsisTokenizerStress:
    """Edge cases that stress tokenization."""

    def test_no_spaces_unicode(self):
        """Ellipsis where tokenizer might struggle."""
        text = "Wait…what…now?"
        expected = ["Wait…what…now?"]
        assert segment_text(text, flatten=True) == expected

    def test_no_spaces_ascii(self):
        text = "Wait...what...now?"
        expected = ["Wait...what...now?"]
        assert segment_text(text, flatten=True) == expected

    def test_run_together(self):
        text = "one...two...three"
        expected = ["one...two...three"]
        assert segment_text(text, flatten=True) == expected

    def test_ellipsis_number_ellipsis(self):
        text = "...42..."
        expected = ["...42..."]
        assert segment_text(text, flatten=True) == expected


class TestEllipsisExtremeEdges:
    """Truly extreme edge cases."""

    def test_just_periods(self):
        """Many periods in a row."""
        text = "................"
        result = segment_text(text, flatten=True)
        assert len(result) >= 1

    def test_alternating_space_period(self):
        text = ". . . . . . . . ."
        result = segment_text(text, flatten=True)
        assert len(result) >= 1

    def test_ellipsis_at_every_word(self):
        text = "I... am... so... tired..."
        expected = ["I... am... so... tired..."]
        assert segment_text(text, flatten=True) == expected

    def test_empty_quotes_with_ellipsis(self):
        text = '"..." she said.'
        expected = ['"..." she said.']
        assert segment_text(text, flatten=True) == expected
