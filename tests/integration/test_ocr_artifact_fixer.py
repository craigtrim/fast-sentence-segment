# -*- coding: UTF-8 -*-
"""Tests for OCR artifact fixer.

Related GitHub Issue:
    #9 - Fix common OCR/cleaning artifacts (Iam, witha)
    https://github.com/craigtrim/fast-sentence-segment/issues/9
"""

import pytest

from fast_sentence_segment.dmo import OcrArtifactFixer


class TestOcrArtifactFixer:
    """Test OCR artifact correction."""

    @pytest.fixture
    def fixer(self):
        return OcrArtifactFixer()

    # ──────────────────────────────────────────────────────────────────────────
    # "Iam" -> "I am"
    # ──────────────────────────────────────────────────────────────────────────

    def test_iam_basic(self, fixer):
        """Basic Iam correction."""
        assert fixer.process("Jack, Iam so happy") == "Jack, I am so happy"

    def test_iam_mid_sentence(self, fixer):
        """Iam in middle of sentence."""
        result = fixer.process("You have caught the Sophie in her shift, Iam afraid.")
        assert result == "You have caught the Sophie in her shift, I am afraid."

    def test_iam_start_of_clause(self, fixer):
        """Iam at start of clause."""
        result = fixer.process("Here's good news. Iam to have a capital fellow")
        assert result == "Here's good news. I am to have a capital fellow"

    def test_iam_preserved_when_not_artifact(self, fixer):
        """Words containing 'Iam' but not the artifact are preserved."""
        # "William" contains "iam" but lowercase
        assert fixer.process("William is here") == "William is here"

    # ──────────────────────────────────────────────────────────────────────────
    # "iam" -> "I am" (lowercase variant, Issue #28)
    # ──────────────────────────────────────────────────────────────────────────

    def test_iam_lowercase_basic(self, fixer):
        """Lowercase iam correction.

        Related GitHub Issue:
            #28 - Fix lowercase iam OCR artifact not being corrected
            https://github.com/craigtrim/fast-sentence-segment/issues/28
        """
        assert fixer.process("so iam going to the store") == "so I am going to the store"

    def test_iam_lowercase_mid_sentence(self, fixer):
        """Lowercase iam in middle of sentence.

        Related GitHub Issue:
            #28 - Fix lowercase iam OCR artifact not being corrected
            https://github.com/craigtrim/fast-sentence-segment/issues/28
        """
        result = fixer.process("he said iam not sure about that")
        assert result == "he said I am not sure about that"

    def test_iam_lowercase_after_punctuation(self, fixer):
        """Lowercase iam after comma.

        Related GitHub Issue:
            #28 - Fix lowercase iam OCR artifact not being corrected
            https://github.com/craigtrim/fast-sentence-segment/issues/28
        """
        result = fixer.process("well, iam afraid it is so")
        assert result == "well, I am afraid it is so"

    # ──────────────────────────────────────────────────────────────────────────
    # "witha" -> "with a"
    # ──────────────────────────────────────────────────────────────────────────

    def test_witha_basic(self, fixer):
        """Basic witha correction."""
        assert fixer.process("horizon witha hint") == "horizon with a hint"

    def test_witha_mid_sentence(self, fixer):
        """witha in middle of sentence."""
        result = fixer.process("flash on the horizon witha hint of darkness")
        assert result == "flash on the horizon with a hint of darkness"

    # ──────────────────────────────────────────────────────────────────────────
    # "sucha" -> "such a"
    # ──────────────────────────────────────────────────────────────────────────

    def test_sucha_basic(self, fixer):
        """Basic sucha correction."""
        assert fixer.process("It was sucha fine day") == "It was such a fine day"

    # ──────────────────────────────────────────────────────────────────────────
    # "ihave" -> "I have"
    # ──────────────────────────────────────────────────────────────────────────

    def test_ihave_basic(self, fixer):
        """Basic ihave correction."""
        assert fixer.process("Well, ihave seen it") == "Well, I have seen it"

    # ──────────────────────────────────────────────────────────────────────────
    # "ithink" -> "I think"
    # ──────────────────────────────────────────────────────────────────────────

    def test_ithink_basic(self, fixer):
        """Basic ithink correction."""
        assert fixer.process("Well, ithink so") == "Well, I think so"

    # ──────────────────────────────────────────────────────────────────────────
    # "aliquid" -> "a liquid"
    # ──────────────────────────────────────────────────────────────────────────

    def test_aliquid_basic(self, fixer):
        """Basic aliquid correction."""
        assert fixer.process("poured aliquid into") == "poured a liquid into"

    # ──────────────────────────────────────────────────────────────────────────
    # Multiple artifacts
    # ──────────────────────────────────────────────────────────────────────────

    def test_multiple_artifacts(self, fixer):
        """Multiple artifacts in same text."""
        text = "Jack, Iam happy witha new ship"
        result = fixer.process(text)
        assert result == "Jack, I am happy with a new ship"

    # ──────────────────────────────────────────────────────────────────────────
    # Real examples from Master and Commander ebook
    # ──────────────────────────────────────────────────────────────────────────

    def test_mandc_iam_forgive(self, fixer):
        """Real example: 'Iam sure' from Master and Commander."""
        text = "hungry and peevish by then that you will forgive me, Iam sure."
        expected = "hungry and peevish by then that you will forgive me, I am sure."
        assert fixer.process(text) == expected

    def test_mandc_iam_happy(self, fixer):
        """Real example: 'Iam so happy' from Master and Commander."""
        text = "Jack, Iam so happy you have a ship at last."
        expected = "Jack, I am so happy you have a ship at last."
        assert fixer.process(text) == expected

    def test_mandc_iam_athwart(self, fixer):
        """Real example: 'Iam athwart' from Master and Commander."""
        text = "tricks with me, Iam athwart your hawse and I can rake you from stem to stern."
        expected = "tricks with me, I am athwart your hawse and I can rake you from stem to stern."
        assert fixer.process(text) == expected

    def test_mandc_iam_very_much(self, fixer):
        """Real example: 'Iam very much' from Master and Commander."""
        text = "tion, and which I reciprocate most heartily, Iam very much at a stand"
        expected = "tion, and which I reciprocate most heartily, I am very much at a stand"
        assert fixer.process(text) == expected

    def test_mandc_iam_sure_of(self, fixer):
        """Real example: 'Iam sure of' from Master and Commander."""
        text = "A warrant from the Navy Office you must have, that Iam sure of"
        expected = "A warrant from the Navy Office you must have, that I am sure of"
        assert fixer.process(text) == expected

    def test_mandc_iam_upset(self, fixer):
        """Real example: 'Iam upset' from Master and Commander."""
        text = "How wonderfully strange, he thought, to be upset by this trifle; yet Iam upset."
        expected = "How wonderfully strange, he thought, to be upset by this trifle; yet I am upset."
        assert fixer.process(text) == expected

    def test_mandc_ihave_sprung(self, fixer):
        """Real example: 'Ihave sprung' from Master and Commander."""
        text = "service, if you will. Ihave sprung my mainyard hopelessly, Iam concerned to tell"
        expected = "service, if you will. I have sprung my mainyard hopelessly, I am concerned to tell"
        assert fixer.process(text) == expected

    def test_mandc_ithink_may_answer(self, fixer):
        """Real example: 'Ithink they may' from Master and Commander."""
        text = "Oh, Ithink they may answer well enough, said Mr Marshall"
        expected = "Oh, I think they may answer well enough, said Mr Marshall"
        assert fixer.process(text) == expected

    def test_mandc_anda_friend(self, fixer):
        """Real example: 'anda friend' from Master and Commander."""
        text = "nephew anda friend's son and the other Americans"
        expected = "nephew and a friend's son and the other Americans"
        assert fixer.process(text) == expected

    def test_mandc_anda_cross_sea(self, fixer):
        """Real example: 'anda cross sea' from Master and Commander."""
        text = "waste, anda cross sea: after frustrating days of calm"
        expected = "waste, and a cross sea: after frustrating days of calm"
        assert fixer.process(text) == expected

    def test_mandc_witha_added(self, fixer):
        """Real example: 'he added witha' from Master and Commander."""
        text = "You will see the gunner's brain, my dear sir, he added witha smile"
        expected = "You will see the gunner's brain, my dear sir, he added with a smile"
        assert fixer.process(text) == expected

    def test_mandc_horizon_witha(self, fixer):
        """Real example: 'horizon witha' from Master and Commander."""
        text = "a far-off triple flash on the horizon witha hint of something"
        expected = "a far-off triple flash on the horizon with a hint of something"
        assert fixer.process(text) == expected

    # ──────────────────────────────────────────────────────────────────────────
    # No change when no artifacts
    # ──────────────────────────────────────────────────────────────────────────

    def test_no_change_clean_text(self, fixer):
        """Clean text is unchanged."""
        text = "This is a perfectly normal sentence."
        assert fixer.process(text) == text
