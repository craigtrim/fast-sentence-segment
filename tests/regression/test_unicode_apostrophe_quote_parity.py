# -*- coding: UTF-8 -*-
"""Regression tests for Issue #29: Unicode apostrophe quote-parity preservation.

Verifies that the 11 new apostrophe-like Unicode characters do not corrupt
quote-parity tracking after normalization. If normalization misses a variant,
the character passes through to _count_quotes() and gets miscounted as a dialog
quote, breaking paragraph formatting.

These tests exercise the full pipeline:
    normalize_quotes → segment_text → format_dialog

And also directly test _count_quotes() and the unwrap path to ensure both
pre-normalization and post-normalization code paths handle the new characters.

Related GitHub Issues:
    #29 - Augment single-quote normalization with missing apostrophe-like characters
    https://github.com/craigtrim/fast-sentence-segment/issues/29

    #13 - fix: Word-initial elision apostrophes counted as dialog quotes
    https://github.com/craigtrim/fast-sentence-segment/issues/13
"""

import pytest

from fast_sentence_segment.dmo.normalize_quotes import normalize_quotes
from fast_sentence_segment.dmo.dialog_formatter import (
    format_dialog,
    _count_quotes,
    _starts_with_quote,
)
from fast_sentence_segment.dmo.unwrap_hard_wrapped_text import (
    _count_quotes as unwrap_count_quotes,
    unwrap_hard_wrapped_text,
)
from fast_sentence_segment import segment_text


# ==============================================================================
# SECTION 1: _count_quotes() — new chars after normalization
# ==============================================================================


class TestCountQuotesAfterNormalization:
    """After normalize_quotes() converts new chars to ASCII, _count_quotes()
    should correctly identify them as apostrophes, not dialog quotes."""

    # --------------------------------------------------------------------------
    # U+02BC MODIFIER LETTER APOSTROPHE (highest-value character)
    # --------------------------------------------------------------------------

    def test_u02bc_contraction_not_counted(self):
        """U+02BC in contraction should not count after normalization."""
        text = normalize_quotes("don\u02BCt worry")
        assert _count_quotes(text) == 0

    def test_u02bc_possessive_not_counted(self):
        """U+02BC in possessive should not count after normalization."""
        text = normalize_quotes("Jack\u02BCs ship")
        assert _count_quotes(text) == 0

    def test_u02bc_elision_not_counted(self):
        """U+02BC in elision should not count after normalization."""
        text = normalize_quotes("\u02BCtis a fine day")
        assert _count_quotes(text) == 0

    def test_u02bc_em_elision_not_counted(self):
        """U+02BC in 'em elision should not count after normalization."""
        text = normalize_quotes("give \u02BCem the goods")
        assert _count_quotes(text) == 0

    def test_u02bc_cello_elision_not_counted(self):
        """U+02BC in 'cello elision should not count after normalization."""
        text = normalize_quotes("the \u02BCcello played")
        assert _count_quotes(text) == 0

    def test_u02bc_in_dialog_quotes_still_counted(self):
        """Dialog quotes around text with U+02BC apostrophe are still counted."""
        text = normalize_quotes("\"I don\u02BCt know,\" she said.")
        assert _count_quotes(text) == 2  # Only the double quotes

    def test_u02bc_mixed_dialog_and_contraction(self):
        """U+02BC contraction + dialog quotes: only dialog counted."""
        text = normalize_quotes("\"Can\u02BCt you see?\" asked Jack.")
        assert _count_quotes(text) == 2

    # --------------------------------------------------------------------------
    # Parametrized: all 11 new characters in contractions
    # --------------------------------------------------------------------------

    @pytest.mark.parametrize("char,name", [
        ("\u2035", "REVERSED PRIME"),
        ("\u02B9", "MODIFIER LETTER PRIME"),
        ("\u02BC", "MODIFIER LETTER APOSTROPHE"),
        ("\u02C8", "MODIFIER LETTER VERTICAL LINE"),
        ("\u055A", "ARMENIAN APOSTROPHE"),
        ("\u05F3", "HEBREW PUNCTUATION GERESH"),
        ("\u07F4", "NKO HIGH TONE APOSTROPHE"),
        ("\u07F5", "NKO LOW TONE APOSTROPHE"),
        ("\u1FBF", "GREEK PSILI"),
        ("\u1FBD", "GREEK KORONIS"),
        ("\uA78C", "LATIN SMALL LETTER SALTILLO"),
    ])
    def test_contraction_not_counted_after_normalization(self, char, name):
        """don{char}t should not be counted as a quote after normalization."""
        text = normalize_quotes(f"don{char}t worry about it")
        assert _count_quotes(text) == 0, (
            f"U+{ord(char):04X} ({name}) contraction miscounted as quote"
        )

    @pytest.mark.parametrize("char,name", [
        ("\u2035", "REVERSED PRIME"),
        ("\u02B9", "MODIFIER LETTER PRIME"),
        ("\u02BC", "MODIFIER LETTER APOSTROPHE"),
        ("\u02C8", "MODIFIER LETTER VERTICAL LINE"),
        ("\u055A", "ARMENIAN APOSTROPHE"),
        ("\u05F3", "HEBREW PUNCTUATION GERESH"),
        ("\u07F4", "NKO HIGH TONE APOSTROPHE"),
        ("\u07F5", "NKO LOW TONE APOSTROPHE"),
        ("\u1FBF", "GREEK PSILI"),
        ("\u1FBD", "GREEK KORONIS"),
        ("\uA78C", "LATIN SMALL LETTER SALTILLO"),
    ])
    def test_possessive_not_counted_after_normalization(self, char, name):
        """Jack{char}s should not be counted as a quote after normalization."""
        text = normalize_quotes(f"Jack{char}s sword gleamed")
        assert _count_quotes(text) == 0, (
            f"U+{ord(char):04X} ({name}) possessive miscounted as quote"
        )

    @pytest.mark.parametrize("char,name", [
        ("\u2035", "REVERSED PRIME"),
        ("\u02B9", "MODIFIER LETTER PRIME"),
        ("\u02BC", "MODIFIER LETTER APOSTROPHE"),
        ("\u02C8", "MODIFIER LETTER VERTICAL LINE"),
        ("\u055A", "ARMENIAN APOSTROPHE"),
        ("\u05F3", "HEBREW PUNCTUATION GERESH"),
        ("\u07F4", "NKO HIGH TONE APOSTROPHE"),
        ("\u07F5", "NKO LOW TONE APOSTROPHE"),
        ("\u1FBF", "GREEK PSILI"),
        ("\u1FBD", "GREEK KORONIS"),
        ("\uA78C", "LATIN SMALL LETTER SALTILLO"),
    ])
    def test_elision_not_counted_after_normalization(self, char, name):
        """{char}tis should not be counted as a quote after normalization."""
        text = normalize_quotes(f"{char}tis a fine day")
        assert _count_quotes(text) == 0, (
            f"U+{ord(char):04X} ({name}) elision miscounted as quote"
        )


# ==============================================================================
# SECTION 2: _starts_with_quote() — new chars after normalization
# ==============================================================================


class TestStartsWithQuoteAfterNormalization:
    """Verify _starts_with_quote() correctly identifies elisions vs quotes
    after normalization of new Unicode characters."""

    @pytest.mark.parametrize("char,name", [
        ("\u2035", "REVERSED PRIME"),
        ("\u02B9", "MODIFIER LETTER PRIME"),
        ("\u02BC", "MODIFIER LETTER APOSTROPHE"),
        ("\u02C8", "MODIFIER LETTER VERTICAL LINE"),
        ("\u055A", "ARMENIAN APOSTROPHE"),
        ("\u05F3", "HEBREW PUNCTUATION GERESH"),
        ("\u07F4", "NKO HIGH TONE APOSTROPHE"),
        ("\u07F5", "NKO LOW TONE APOSTROPHE"),
        ("\u1FBF", "GREEK PSILI"),
        ("\u1FBD", "GREEK KORONIS"),
        ("\uA78C", "LATIN SMALL LETTER SALTILLO"),
    ])
    def test_elision_not_detected_as_quote_start(self, char, name):
        """{char}tis should not be detected as quote start after normalization."""
        text = normalize_quotes(f"{char}tis a fine day")
        assert not _starts_with_quote(text), (
            f"U+{ord(char):04X} ({name}) elision wrongly detected as quote start"
        )

    @pytest.mark.parametrize("char,name", [
        ("\u2035", "REVERSED PRIME"),
        ("\u02B9", "MODIFIER LETTER PRIME"),
        ("\u02BC", "MODIFIER LETTER APOSTROPHE"),
        ("\u02C8", "MODIFIER LETTER VERTICAL LINE"),
        ("\u055A", "ARMENIAN APOSTROPHE"),
        ("\u05F3", "HEBREW PUNCTUATION GERESH"),
        ("\u07F4", "NKO HIGH TONE APOSTROPHE"),
        ("\u07F5", "NKO LOW TONE APOSTROPHE"),
        ("\u1FBF", "GREEK PSILI"),
        ("\u1FBD", "GREEK KORONIS"),
        ("\uA78C", "LATIN SMALL LETTER SALTILLO"),
    ])
    def test_cello_elision_not_detected_as_quote_start(self, char, name):
        """{char}cello should not be detected as quote start after normalization."""
        text = normalize_quotes(f"The {char}cello played.")
        assert not _starts_with_quote(text), (
            f"U+{ord(char):04X} ({name}) 'cello wrongly detected as quote start"
        )


# ==============================================================================
# SECTION 3: format_dialog() — paragraph breaks preserved with new chars
# ==============================================================================


class TestFormatDialogWithNewChars:
    """Verify format_dialog() produces correct paragraph breaks when sentences
    contain the new Unicode apostrophe characters (after normalization)."""

    def test_u02bc_narrative_paragraph_breaks(self):
        """Narrative with U+02BC contraction should get paragraph breaks."""
        sentences = [
            normalize_quotes("I don\u02BCt believe it."),
            normalize_quotes("Jack\u02BCs ship sailed on."),
            normalize_quotes("The wind was strong."),
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_u02bc_elision_narrative_paragraph_breaks(self):
        """Narrative with U+02BC elision should get paragraph breaks."""
        sentences = [
            normalize_quotes("\u02BCTwas a dark night."),
            normalize_quotes("The stars were hidden."),
            normalize_quotes("Nobody stirred."),
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_u02bc_cello_narrative_paragraph_breaks(self):
        """Narrative with U+02BC 'cello should get paragraph breaks."""
        sentences = [
            normalize_quotes("The \u02BCcello played beautifully."),
            normalize_quotes("Jack closed his eyes."),
            normalize_quotes("The music transported him."),
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_u02bc_inside_dialog_preserves_parity(self):
        """U+02BC contraction inside dialog should not break quote parity."""
        sentences = [
            normalize_quotes("\"I don\u02BCt know,\" she said."),
            normalize_quotes("The room fell silent."),
            normalize_quotes("Nobody spoke."),
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_u02bc_multi_sentence_dialog_stays_grouped(self):
        """Multi-sentence dialog with U+02BC should stay grouped."""
        sentences = [
            normalize_quotes("\"I don\u02BCt think that\u02BCs right."),
            normalize_quotes("It can\u02BCt be."),
            normalize_quotes("We\u02BCll see about that.\""),
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1  # All in one dialog paragraph

    def test_saltillo_in_dialog_preserves_parity(self):
        """U+A78C Latin saltillo in dialog should not break quote parity."""
        sentences = [
            normalize_quotes("\"I can\uA78Ct believe it,\" said Jack."),
            normalize_quotes("Stephen nodded."),
            normalize_quotes("The evidence was clear."),
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_modifier_prime_elision_preserves_formatting(self):
        """U+02B9 modifier letter prime in elision should not break formatting."""
        sentences = [
            normalize_quotes("\u02B9Twas brillig."),
            normalize_quotes("The slithy toves did gyre."),
            normalize_quotes("All mimsy were the borogoves."),
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_mixed_new_chars_complex_dialog(self):
        """Complex dialog with multiple new apostrophe chars."""
        sentences = [
            normalize_quotes("\u02BCTwas a fair wind that morning."),
            normalize_quotes("\"Set the topsails,\" ordered Jack."),
            normalize_quotes("The crew sprang to action."),
            normalize_quotes("\"Give \u02BCem every stitch of canvas,\" he added."),
            normalize_quotes("Speed was of the essence."),
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 5


# ==============================================================================
# SECTION 4: Full pipeline — segment_text() with new chars
# ==============================================================================


class TestFullPipelineWithNewChars:
    """End-to-end tests: segment_text() with normalize=True should handle
    the new Unicode characters transparently."""

    def test_u02bc_contraction_segmentation(self):
        """U+02BC in contraction should segment normally."""
        text = "I don\u02BCt know. She can\u02BCt either."
        result = segment_text(text, flatten=True, normalize=True)
        assert len(result) == 2
        assert result[0] == "I don't know."
        assert result[1] == "She can't either."

    def test_u02bc_possessive_segmentation(self):
        """U+02BC in possessive should segment normally."""
        text = "Jack\u02BCs ship was fast. Stephen\u02BCs was slow."
        result = segment_text(text, flatten=True, normalize=True)
        assert len(result) == 2
        assert result[0] == "Jack's ship was fast."
        assert result[1] == "Stephen's was slow."

    def test_mixed_new_chars_segmentation(self):
        """Multiple new chars in text should segment normally."""
        text = "Don\u02BCt worry. It\u02B9s fine. She\uA78Cs coming."
        result = segment_text(text, flatten=True, normalize=True)
        assert len(result) == 3
        assert result[0] == "Don't worry."
        assert result[1] == "It's fine."
        assert result[2] == "She's coming."

    def test_u02bc_dialog_format(self):
        """U+02BC in dialog with format='dialog' should format correctly."""
        text = (
            "\"I don\u02BCt know,\" said Jack. "
            "\"It\u02BCs a mystery.\" "
            "The room fell silent."
        )
        result = segment_text(text, normalize=True, format="dialog")
        assert isinstance(result, str)
        # Should contain the normalized contractions
        assert "don't" in result
        assert "It's" in result

    def test_u02bc_elision_in_full_pipeline(self):
        """U+02BC elision through full pipeline should work correctly."""
        text = "\u02BCTwas the night before Christmas. All through the house."
        result = segment_text(text, flatten=True, normalize=True)
        assert len(result) == 2
        assert result[0] == "'Twas the night before Christmas."
        assert result[1] == "All through the house."


# ==============================================================================
# SECTION 5: Unwrap path — pre-normalization quote tracking with new chars
# ==============================================================================


class TestUnwrapPreNormalizationQuoteTracking:
    """The unwrap path runs BEFORE normalize_quotes(). When the unwrap module
    encounters new Unicode apostrophe characters, its _count_quotes() must
    recognize them as single-quote variants (included in its expanded
    SINGLE_QUOTES constant) so they can be properly handled.

    These tests verify that unwrap_hard_wrapped_text() correctly handles text
    containing the new characters without corrupting quote-parity tracking.
    """

    def test_u02bc_contraction_in_unwrap(self):
        """U+02BC contraction in unwrapped text should not break unwrap."""
        text = "I don\u02BCt know\nwhat to do."
        result = unwrap_hard_wrapped_text(text)
        assert "don\u02BCt" in result  # char passes through (not normalized here)
        # Lines should be joined
        assert "\n" not in result

    def test_u02bc_in_quoted_dialog_unwrap(self):
        """U+02BC inside quoted dialog should not break quote-aware unwrap."""
        text = '"I don\u02BCt think so.\n\nBut maybe."\nHe paused.'
        result = unwrap_hard_wrapped_text(text)
        # The quote-aware unwrap should join across blank line inside the quote
        assert "I don\u02BCt think so." in result
        assert "But maybe." in result

    def test_u02bc_possessive_in_unwrap(self):
        """U+02BC possessive should not break unwrap quote tracking."""
        text = "Jack\u02BCs ship\nsailed west."
        result = unwrap_hard_wrapped_text(text)
        assert "\n" not in result

    def test_u02bc_elision_in_unwrap_not_counted_as_quote(self):
        """U+02BC elision in unwrap should not be counted as a dialog quote."""
        # If counted as quote, this would be "inside open quote" and join
        # across blank lines incorrectly
        text = "\u02BCTwas a fine day.\n\nThe sun was shining."
        result = unwrap_hard_wrapped_text(text)
        # Should NOT join — the 'Twas is an elision, not a dialog quote.
        # The two lines should remain as separate paragraphs.
        assert "\n\n" in result

    def test_unwrap_count_quotes_u02bc_contraction(self):
        """unwrap _count_quotes should not count U+02BC in contractions."""
        text = "I don\u02BCt know"
        assert unwrap_count_quotes(text) == 0

    def test_unwrap_count_quotes_u02bc_elision(self):
        """unwrap _count_quotes should not count U+02BC in elisions."""
        text = "\u02BCtis a fine day"
        assert unwrap_count_quotes(text) == 0

    @pytest.mark.parametrize("char,name", [
        ("\u2035", "REVERSED PRIME"),
        ("\u02B9", "MODIFIER LETTER PRIME"),
        ("\u02BC", "MODIFIER LETTER APOSTROPHE"),
        ("\u02C8", "MODIFIER LETTER VERTICAL LINE"),
        ("\u055A", "ARMENIAN APOSTROPHE"),
        ("\u05F3", "HEBREW PUNCTUATION GERESH"),
        ("\u07F4", "NKO HIGH TONE APOSTROPHE"),
        ("\u07F5", "NKO LOW TONE APOSTROPHE"),
        ("\u1FBF", "GREEK PSILI"),
        ("\u1FBD", "GREEK KORONIS"),
        ("\uA78C", "LATIN SMALL LETTER SALTILLO"),
    ])
    def test_unwrap_count_quotes_contraction_all_chars(self, char, name):
        """don{char}t should not be counted in unwrap _count_quotes."""
        text = f"I don{char}t know"
        assert unwrap_count_quotes(text) == 0, (
            f"U+{ord(char):04X} ({name}) contraction miscounted in unwrap path"
        )

    @pytest.mark.parametrize("char,name", [
        ("\u2035", "REVERSED PRIME"),
        ("\u02B9", "MODIFIER LETTER PRIME"),
        ("\u02BC", "MODIFIER LETTER APOSTROPHE"),
        ("\u02C8", "MODIFIER LETTER VERTICAL LINE"),
        ("\u055A", "ARMENIAN APOSTROPHE"),
        ("\u05F3", "HEBREW PUNCTUATION GERESH"),
        ("\u07F4", "NKO HIGH TONE APOSTROPHE"),
        ("\u07F5", "NKO LOW TONE APOSTROPHE"),
        ("\u1FBF", "GREEK PSILI"),
        ("\u1FBD", "GREEK KORONIS"),
        ("\uA78C", "LATIN SMALL LETTER SALTILLO"),
    ])
    def test_unwrap_count_quotes_elision_all_chars(self, char, name):
        """{char}tis should not be counted in unwrap _count_quotes."""
        text = f"{char}tis a fine day"
        assert unwrap_count_quotes(text) == 0, (
            f"U+{ord(char):04X} ({name}) elision miscounted in unwrap path"
        )

    @pytest.mark.parametrize("char,name", [
        ("\u2035", "REVERSED PRIME"),
        ("\u02B9", "MODIFIER LETTER PRIME"),
        ("\u02BC", "MODIFIER LETTER APOSTROPHE"),
        ("\u02C8", "MODIFIER LETTER VERTICAL LINE"),
        ("\u055A", "ARMENIAN APOSTROPHE"),
        ("\u05F3", "HEBREW PUNCTUATION GERESH"),
        ("\u07F4", "NKO HIGH TONE APOSTROPHE"),
        ("\u07F5", "NKO LOW TONE APOSTROPHE"),
        ("\u1FBF", "GREEK PSILI"),
        ("\u1FBD", "GREEK KORONIS"),
        ("\uA78C", "LATIN SMALL LETTER SALTILLO"),
    ])
    def test_unwrap_count_quotes_possessive_all_chars(self, char, name):
        """Jack{char}s should not be counted in unwrap _count_quotes."""
        text = f"Jack{char}s ship"
        assert unwrap_count_quotes(text) == 0, (
            f"U+{ord(char):04X} ({name}) possessive miscounted in unwrap path"
        )

    @pytest.mark.parametrize("char,name", [
        ("\u2035", "REVERSED PRIME"),
        ("\u02B9", "MODIFIER LETTER PRIME"),
        ("\u02BC", "MODIFIER LETTER APOSTROPHE"),
        ("\u02C8", "MODIFIER LETTER VERTICAL LINE"),
        ("\u055A", "ARMENIAN APOSTROPHE"),
        ("\u05F3", "HEBREW PUNCTUATION GERESH"),
        ("\u07F4", "NKO HIGH TONE APOSTROPHE"),
        ("\u07F5", "NKO LOW TONE APOSTROPHE"),
        ("\u1FBF", "GREEK PSILI"),
        ("\u1FBD", "GREEK KORONIS"),
        ("\uA78C", "LATIN SMALL LETTER SALTILLO"),
    ])
    def test_unwrap_dialog_quotes_still_counted(self, char, name):
        """Dialog double quotes should still be counted with new char in text."""
        text = f"\"I don{char}t know,\" she said."
        assert unwrap_count_quotes(text) == 2, (
            f"Dialog quotes not counted correctly with U+{ord(char):04X} ({name})"
        )


# ==============================================================================
# SECTION 6: Full unwrap + normalize pipeline
# ==============================================================================


class TestUnwrapThenNormalizePipeline:
    """Test the complete pipeline: unwrap → normalize → segment.

    This is what happens when segment_text(text, unwrap=True, normalize=True)
    is called.
    """

    def test_unwrap_and_normalize_u02bc(self):
        """Unwrap + normalize with U+02BC contractions."""
        text = "I don\u02BCt know\nwhat to do."
        result = segment_text(text, flatten=True, unwrap=True, normalize=True)
        assert len(result) == 1
        assert result[0] == "I don't know what to do."

    def test_unwrap_and_normalize_elision(self):
        """Unwrap + normalize with U+02BC elision."""
        text = "\u02BCTwas a fine day.\nThe sun was shining."
        result = segment_text(text, flatten=True, unwrap=True, normalize=True)
        assert len(result) == 2
        assert result[0] == "'Twas a fine day."
        assert result[1] == "The sun was shining."

    def test_unwrap_and_normalize_mixed(self):
        """Full pipeline with mixed new Unicode chars."""
        text = (
            "Jack\u02BCs ship sailed on.\n"
            "Stephen couldn\u02B9t believe it.\n"
            "\uA78CTwas a miracle."
        )
        result = segment_text(text, flatten=True, unwrap=True, normalize=True)
        assert len(result) == 3
        assert result[0] == "Jack's ship sailed on."
        assert result[1] == "Stephen couldn't believe it."
        assert result[2] == "'Twas a miracle."


# ==============================================================================
# SECTION 7: Regression — original issue #13 scenarios with new chars
# ==============================================================================


class TestOriginalIssue13ScenariosWithNewChars:
    """Reproduce the original issue #13 scenarios but with new Unicode chars.

    The original issue was: 'cello (using ASCII apostrophe) would be miscounted
    as a dialog quote, corrupting paragraph formatting. This verifies the same
    behavior is correct when the apostrophe is a new Unicode variant.
    """

    def test_u02bc_cello_does_not_open_quote_state(self):
        """U+02BC 'cello should not toggle quote state open."""
        sentences = [
            normalize_quotes("First narrative sentence."),
            normalize_quotes("The \u02BCcello played beautifully."),
            normalize_quotes("Second narrative sentence."),
            normalize_quotes("Third narrative sentence."),
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4

    def test_u02bc_em_does_not_open_quote_state(self):
        """U+02BC 'em should not toggle quote state open."""
        sentences = [
            normalize_quotes("The captain gave orders."),
            normalize_quotes("Give \u02BCem no quarter."),
            normalize_quotes("The crew obeyed."),
            normalize_quotes("Battle commenced."),
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4

    def test_u02bc_twas_does_not_open_quote_state(self):
        """U+02BC 'twas should not toggle quote state open."""
        sentences = [
            normalize_quotes("The story began."),
            normalize_quotes("\u02BCTwas a dark and stormy night."),
            normalize_quotes("The wind howled."),
            normalize_quotes("Rain lashed the windows."),
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4

    def test_saltillo_cello_does_not_open_quote_state(self):
        """U+A78C 'cello should not toggle quote state open."""
        sentences = [
            normalize_quotes("First sentence."),
            normalize_quotes("The \uA78Ccello played on."),
            normalize_quotes("Second sentence."),
            normalize_quotes("Third sentence."),
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4

    def test_modifier_prime_twas_does_not_open_quote_state(self):
        """U+02B9 'twas should not toggle quote state open."""
        sentences = [
            normalize_quotes("The evening came."),
            normalize_quotes("\u02B9Twas a cold winter."),
            normalize_quotes("Snow began to fall."),
            normalize_quotes("The fire crackled."),
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4


# ==============================================================================
# SECTION 8: Real-world ebook scenarios with new chars
# ==============================================================================


class TestEbookScenariosWithNewChars:
    """Real-world ebook scenarios using the new Unicode characters."""

    def test_master_and_commander_u02bc(self):
        """Master and Commander style passage with U+02BC throughout."""
        sentences = [
            normalize_quotes("The \u02BCcello\u02BCs voice filled the great cabin."),
            normalize_quotes("Jack\u02BCs bow moved with practiced ease."),
            normalize_quotes("\"Beautifully done,\" said Stephen."),
            normalize_quotes("The last note faded into silence."),
            normalize_quotes("Both men sat in contemplation."),
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 5

    def test_cockney_dialog_u02bc(self):
        """Cockney dialog with U+02BC elisions."""
        sentences = [
            normalize_quotes("\"Give \u02BCem a broadside!\" roared the captain."),
            normalize_quotes("The guns thundered."),
            normalize_quotes("\"Come \u02BCere, you scoundrel!\" shouted the bosun."),
            normalize_quotes("The sailor froze."),
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4

    def test_full_ebook_page_u02bc(self):
        """Full ebook page simulation with U+02BC as apostrophe throughout."""
        sentences = [
            normalize_quotes("\u02BCTwas a fair wind that morning."),
            normalize_quotes("\"Set the topsails,\" ordered Jack."),
            normalize_quotes("The crew sprang to action."),
            normalize_quotes("\"Give \u02BCem every stitch of canvas,\" he added."),
            normalize_quotes("Stephen couldn\u02BCt help but admire the seamanship."),
            normalize_quotes("The ship\u02BCs timbers creaked with the strain."),
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 6
