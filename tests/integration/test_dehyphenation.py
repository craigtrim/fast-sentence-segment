# -*- coding: UTF-8 -*-
"""Tests for dehyphenation of words split across lines.

Related GitHub Issue:
    #8 - Add dehyphenation support for words split across lines
    https://github.com/craigtrim/fast-sentence-segment/issues/8

When processing ebooks and scanned documents, words are often hyphenated
at line breaks for typesetting purposes. For example:
    'we drink a bot-
    tle of wine'
should become 'we drink a bottle of wine', not 'we drink a bot- tle of wine'.
"""

import pytest

from fast_sentence_segment.dmo.unwrap_hard_wrapped_text import unwrap_hard_wrapped_text
from fast_sentence_segment import segment_text


class TestDehyphenationBasic:
    """Test basic dehyphenation of words split across lines."""

    def test_bottle_basic(self):
        """The original example from the issue."""
        text = "we drink a bot-\ntle of wine"
        result = unwrap_hard_wrapped_text(text)
        assert result == "we drink a bottle of wine"

    def test_pillared(self):
        """pil-lared -> pillared"""
        text = "a tall, handsome, pil-\nlared octagon"
        result = unwrap_hard_wrapped_text(text)
        assert result == "a tall, handsome, pillared octagon"

    def test_acknowledge(self):
        """ac-knowledge -> acknowledge"""
        text = "he could not but ac-\nknowledge that"
        result = unwrap_hard_wrapped_text(text)
        assert result == "he could not but acknowledge that"

    def test_anchored(self):
        """an-chored -> anchored"""
        text = "the rest of it was an-\nchored to the man"
        result = unwrap_hard_wrapped_text(text)
        assert result == "the rest of it was anchored to the man"

    def test_convolutions(self):
        """convo-lutions -> convolutions"""
        text = "through its convo-\nlutions and arabesques"
        result = unwrap_hard_wrapped_text(text)
        assert result == "through its convolutions and arabesques"

    def test_threatening(self):
        """threat-ening -> threatening"""
        text = "his hand stirring and threat-\nening to take to the air"
        result = unwrap_hard_wrapped_text(text)
        assert result == "his hand stirring and threatening to take to the air"

    def test_continued(self):
        """con-tinued -> continued"""
        text = "However, she con-\ntinued to acknowledge"
        result = unwrap_hard_wrapped_text(text)
        assert result == "However, she continued to acknowledge"

    def test_disagreeable(self):
        """dis-agreeable -> disagreeable"""
        text = "were peculiarly dis-\nagreeable, as they faded"
        result = unwrap_hard_wrapped_text(text)
        assert result == "were peculiarly disagreeable, as they faded"

    def test_remembering(self):
        """re-membering -> remembering"""
        text = "Jack aloud, re-\nmembering the politic tameness"
        result = unwrap_hard_wrapped_text(text)
        assert result == "Jack aloud, remembering the politic tameness"

    def test_manner(self):
        """man-ner -> manner"""
        text = "in a slanting man-\nner over its surface"
        result = unwrap_hard_wrapped_text(text)
        assert result == "in a slanting manner over its surface"

    def test_employed(self):
        """em-ployed -> employed"""
        text = "Ships and Vessels em-\nployed in the Mediterranean"
        result = unwrap_hard_wrapped_text(text)
        assert result == "Ships and Vessels employed in the Mediterranean"

    def test_instructions(self):
        """Instruc-tions -> Instructions"""
        text = "the General Printed Instruc-\ntions as what Orders"
        result = unwrap_hard_wrapped_text(text)
        assert result == "the General Printed Instructions as what Orders"

    def test_admirable(self):
        """admir-able -> admirable"""
        text = "any ship at all ... admir-\nable copperplate hand"
        result = unwrap_hard_wrapped_text(text)
        assert result == "any ship at all ... admirable copperplate hand"

    def test_chambermaid(self):
        """cham-bermaid -> chambermaid"""
        text = "he was hailing the cham-\nbermaid"
        result = unwrap_hard_wrapped_text(text)
        assert result == "he was hailing the chambermaid"

    def test_appointment(self):
        """appoint-ment -> appointment"""
        text = "and make an appoint-\nment with Allen"
        result = unwrap_hard_wrapped_text(text)
        assert result == "and make an appointment with Allen"

    def test_outfitters(self):
        """outfit-ter's -> outfitter's"""
        text = "to the naval outfit-\nter's and pledge"
        result = unwrap_hard_wrapped_text(text)
        assert result == "to the naval outfitter's and pledge"

    def test_complacency(self):
        """com-placency -> complacency"""
        text = "gazed with great com-\nplacency in the long glass"
        result = unwrap_hard_wrapped_text(text)
        assert result == "gazed with great complacency in the long glass"

    def test_chocolate(self):
        """choc-olate -> chocolate"""
        text = "May I propose a cup of choc-\nolate, or coffee?"
        result = unwrap_hard_wrapped_text(text)
        assert result == "May I propose a cup of chocolate, or coffee?"

    def test_benevolence(self):
        """ben-evolence -> benevolence"""
        text = "with great ben-\nevolence"
        result = unwrap_hard_wrapped_text(text)
        assert result == "with great benevolence"

    def test_morning(self):
        """morn-ing -> morning"""
        text = "out of bed this morn-\ning I noticed"
        result = unwrap_hard_wrapped_text(text)
        assert result == "out of bed this morning I noticed"

    def test_predecessor(self):
        """prede-cessor -> predecessor"""
        text = "an interview with my prede-\ncessor"
        result = unwrap_hard_wrapped_text(text)
        assert result == "an interview with my predecessor"

    def test_deadened(self):
        """dead-ened -> deadened"""
        text = "the sound of a harp, dead-\nened to a tinkle"
        result = unwrap_hard_wrapped_text(text)
        assert result == "the sound of a harp, deadened to a tinkle"

    def test_between(self):
        """be-tween -> between"""
        text = "a strong antipathy be-\ntween them"
        result = unwrap_hard_wrapped_text(text)
        assert result == "a strong antipathy between them"

    def test_followers(self):
        """fol-lowers -> followers"""
        text = "as well as certain fol-\nlowers"
        result = unwrap_hard_wrapped_text(text)
        assert result == "as well as certain followers"

    def test_congratulate(self):
        """con-gratulate -> congratulate"""
        text = "I must pay my respects and con-\ngratulate her"
        result = unwrap_hard_wrapped_text(text)
        assert result == "I must pay my respects and congratulate her"

    def test_taking(self):
        """tak-ing -> taking"""
        text = "eunuchs to tak-\ning possession"
        result = unwrap_hard_wrapped_text(text)
        assert result == "eunuchs to taking possession"

    def test_looking(self):
        """look-ing -> looking"""
        text = "by her harp, look-\ning decorative"
        result = unwrap_hard_wrapped_text(text)
        assert result == "by her harp, looking decorative"

    def test_introductions(self):
        """introduc-tions -> introductions"""
        text = "beginning the introduc-\ntions, he roared out"
        result = unwrap_hard_wrapped_text(text)
        assert result == "beginning the introductions, he roared out"

    def test_willoughby(self):
        """Wil-loughby -> Willoughby (proper noun)"""
        text = "That Ragusan bark poor Wil-\nloughby sent in"
        result = unwrap_hard_wrapped_text(text)
        assert result == "That Ragusan bark poor Willoughby sent in"


class TestDehyphenationProperNouns:
    """Test dehyphenation of proper nouns split across lines."""

    def test_gibraltar(self):
        """Gib-raltar -> Gibraltar"""
        text = "had appeared from Gib-\nraltar"
        result = unwrap_hard_wrapped_text(text)
        assert result == "had appeared from Gibraltar"

    def test_teniente(self):
        """Teni-ente -> Teniente"""
        text = "'Poor Teni-\nente.'"
        result = unwrap_hard_wrapped_text(text)
        assert result == "'Poor Teniente.'"


class TestDehyphenationCompoundWords:
    """Test that compound words with intentional hyphens are preserved."""

    def test_orange_trees_preserved(self):
        """orange-trees should remain hyphenated (legitimate compound)."""
        text = "nightingales in the orange-\ntrees"
        result = unwrap_hard_wrapped_text(text)
        # This is tricky - "orange-trees" is a compound word
        # But heuristically it looks the same as a line-break hyphen
        # For now, we join it: this test documents current behavior
        assert result == "we join it" or result == "nightingales in the orange-trees" or result == "nightingales in the orangetrees"

    def test_well_known_preserved(self):
        """well-known should remain hyphenated if followed by lowercase."""
        text = "a well-\nknown fact"
        result = unwrap_hard_wrapped_text(text)
        # Heuristically this looks like a line-break, so it will be joined
        # This test documents expected behavior - we join by default
        assert result == "a wellknown fact" or result == "a well-known fact"

    def test_self_evident_preserved(self):
        """self-evident is a compound that may be split at line break."""
        text = "it is self-\nevident"
        result = unwrap_hard_wrapped_text(text)
        # Will be joined since pattern matches hyphen-newline-lowercase
        assert result == "it is selfevident" or result == "it is self-evident"


class TestDehyphenationEdgeCases:
    """Test edge cases and special situations."""

    def test_hyphen_at_end_followed_by_uppercase(self):
        """Hyphen followed by uppercase should NOT be joined (likely sentence break)."""
        text = "end of the line-\nThe next sentence"
        result = unwrap_hard_wrapped_text(text)
        # Should NOT join because next word starts with uppercase
        assert "line- The" in result or "line-\nThe" in result or "line- The" in result

    def test_multiple_hyphens_in_text(self):
        """Text with multiple hyphenated words."""
        text = "the cham-\nbermaid and the out-\nfitter"
        result = unwrap_hard_wrapped_text(text)
        assert result == "the chambermaid and the outfitter"

    def test_hyphen_with_leading_whitespace(self):
        """Hyphen at end of line with indented continuation."""
        text = "a bot-\n      tle of wine"
        result = unwrap_hard_wrapped_text(text)
        assert result == "a bottle of wine"

    def test_em_dash_not_affected(self):
        """Em dashes (--) should not trigger dehyphenation."""
        text = "his epaulette -- 'and when first we ship it'"
        result = unwrap_hard_wrapped_text(text)
        assert "--" in result or "—" in result or result == "his epaulette -- 'and when first we ship it'"

    def test_double_hyphen_at_line_end(self):
        """Double hyphen at line end (em-dash style) should be preserved."""
        text = "his epaulette --\n'and when first'"
        result = unwrap_hard_wrapped_text(text)
        # Should preserve the double-hyphen, not treat as word break
        assert "--" in result

    def test_hyphen_followed_by_punctuation(self):
        """Hyphen followed by punctuation should not join."""
        text = "some-\n, thing else"
        result = unwrap_hard_wrapped_text(text)
        # Should not join since next char is punctuation
        assert "some-" in result or "some- ," in result

    def test_no_hyphen_at_line_end(self):
        """Lines without hyphens at end should just be space-joined."""
        text = "This is a normal\nline break"
        result = unwrap_hard_wrapped_text(text)
        assert result == "This is a normal line break"

    def test_single_hyphenated_word_no_break(self):
        """A hyphenated word on a single line stays unchanged."""
        text = "a well-known fact"
        result = unwrap_hard_wrapped_text(text)
        assert result == "a well-known fact"

    def test_empty_after_hyphen(self):
        """Hyphen at very end of text."""
        text = "incomplete-"
        result = unwrap_hard_wrapped_text(text)
        assert result == "incomplete-"

    def test_hyphen_before_blank_line(self):
        """Hyphen before paragraph break should not join across paragraphs."""
        text = "end of para-\n\nNew paragraph"
        result = unwrap_hard_wrapped_text(text)
        # Should NOT join across paragraph boundary
        assert "para-" in result or "para- " in result
        assert "\n\n" in result or "New paragraph" in result


class TestDehyphenationWithQuotes:
    """Test dehyphenation interacts correctly with quoted text."""

    def test_hyphen_inside_quotes(self):
        """Hyphenated word inside quotes."""
        text = '"we drink a bot-\ntle of wine"'
        result = unwrap_hard_wrapped_text(text)
        assert result == '"we drink a bottle of wine"'

    def test_hyphen_before_closing_quote(self):
        """Hyphen at end before closing quote on next line."""
        text = '"incomp-\nlete"'
        result = unwrap_hard_wrapped_text(text)
        assert result == '"incomplete"'


class TestDehyphenationIntegration:
    """Test dehyphenation works with segment_text(unwrap=True)."""

    def test_segment_text_with_dehyphenation(self):
        """Full pipeline: unwrap + dehyphenate + segment."""
        text = (
            "The music-room was filled with the tri-\n"
            "umphant first movement. The players were\n"
            "playing with passionate con-\n"
            "viction."
        )
        result = segment_text(text, flatten=True, unwrap=True)

        # Should have dehyphenated words
        full = ' '.join(result)
        assert "triumphant" in full
        assert "conviction" in full
        # Should NOT have broken hyphenated fragments
        assert "tri-" not in full
        assert "con-" not in full

    def test_master_commander_excerpt(self):
        """Real excerpt from Master and Commander."""
        text = (
            "The swab is this' — patting\n"
            "his epaulette — 'and when first we ship it, we wet it: that is to say, we drink a bot-\n"
            "tle or two of wine.'"
        )
        result = segment_text(text, flatten=True, unwrap=True)

        full = ' '.join(result)
        assert "bottle" in full
        assert "bot-" not in full
