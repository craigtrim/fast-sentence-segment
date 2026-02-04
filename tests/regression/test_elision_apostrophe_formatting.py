# -*- coding: UTF-8 -*-
"""Tests for Issue #13: Word-initial elision apostrophes in dialog formatting.

Word-initial elision apostrophes ('cello, 'tis, 'em, etc.) should NOT be counted
as dialog quotes because they don't indicate dialog boundaries. They are followed
by lowercase letters, unlike dialog openings which use capitals ('Hello!).

These tests verify that the --format flag (dialog_formatter.py) handles elisions
correctly without throwing off quote parity tracking.

Related GitHub Issue:
    #13 - fix: Word-initial elision apostrophes ('cello, 'tis) counted as dialog quotes
    https://github.com/craigtrim/fast-sentence-segment/issues/13
"""

import pytest

from fast_sentence_segment.dmo.dialog_formatter import (
    format_dialog,
    _count_quotes,
    _starts_with_quote,
    _is_complete_quote,
)


# ==============================================================================
# SECTION 1: _count_quotes() function tests for elision detection
# ==============================================================================


class TestCountQuotesElisionDetection:
    """Tests for _count_quotes() properly excluding elision apostrophes."""

    # --------------------------------------------------------------------------
    # Musical elisions
    # --------------------------------------------------------------------------

    def test_cello_not_counted(self):
        """'cello (violoncello) apostrophe should not be counted."""
        text = "the 'cello came in"
        assert _count_quotes(text) == 0

    def test_copter_not_counted(self):
        """'copter (helicopter) apostrophe should not be counted."""
        text = "the 'copter landed"
        assert _count_quotes(text) == 0

    # --------------------------------------------------------------------------
    # Archaic "it" elisions
    # --------------------------------------------------------------------------

    def test_tis_not_counted(self):
        """'tis (it is) apostrophe should not be counted."""
        text = "'tis a fine day"
        assert _count_quotes(text) == 0

    def test_twas_not_counted(self):
        """'twas (it was) apostrophe should not be counted."""
        text = "'twas the night before"
        assert _count_quotes(text) == 0

    def test_twere_not_counted(self):
        """'twere (it were) apostrophe should not be counted."""
        text = "'twere better to wait"
        assert _count_quotes(text) == 0

    def test_twill_not_counted(self):
        """'twill (it will) apostrophe should not be counted."""
        text = "'twill be done soon"
        assert _count_quotes(text) == 0

    def test_twould_not_counted(self):
        """'twould (it would) apostrophe should not be counted."""
        text = "'twould seem so"
        assert _count_quotes(text) == 0

    # --------------------------------------------------------------------------
    # Common elisions (a- prefix)
    # --------------------------------------------------------------------------

    def test_bout_not_counted(self):
        """'bout (about) apostrophe should not be counted."""
        text = "what's it all 'bout"
        assert _count_quotes(text) == 0

    def test_cross_not_counted(self):
        """'cross (across) apostrophe should not be counted."""
        text = "walked 'cross the field"
        assert _count_quotes(text) == 0

    def test_gainst_not_counted(self):
        """'gainst (against) apostrophe should not be counted."""
        text = "fought 'gainst the enemy"
        assert _count_quotes(text) == 0

    def test_midst_not_counted(self):
        """'midst (amidst) apostrophe should not be counted."""
        text = "stood 'midst the crowd"
        assert _count_quotes(text) == 0

    def test_round_not_counted(self):
        """'round (around) apostrophe should not be counted."""
        text = "looked 'round the corner"
        assert _count_quotes(text) == 0

    def test_tween_not_counted(self):
        """'tween (between) apostrophe should not be counted."""
        text = "'tween you and me"
        assert _count_quotes(text) == 0

    def test_twixt_not_counted(self):
        """'twixt (betwixt) apostrophe should not be counted."""
        text = "'twixt heaven and earth"
        assert _count_quotes(text) == 0

    # --------------------------------------------------------------------------
    # Cockney/dialect h-dropping
    # --------------------------------------------------------------------------

    def test_em_not_counted(self):
        """'em (them) apostrophe should not be counted."""
        text = "give 'em to me"
        assert _count_quotes(text) == 0

    def test_im_not_counted(self):
        """'im (him) apostrophe should not be counted."""
        text = "tell 'im the news"
        assert _count_quotes(text) == 0

    def test_er_not_counted(self):
        """'er (her) apostrophe should not be counted."""
        text = "give 'er the book"
        assert _count_quotes(text) == 0

    def test_ere_not_counted(self):
        """'ere (here) apostrophe should not be counted."""
        text = "come 'ere now"
        assert _count_quotes(text) == 0

    def test_ave_not_counted(self):
        """'ave (have) apostrophe should not be counted."""
        text = "I 'ave the goods"
        assert _count_quotes(text) == 0

    def test_ead_not_counted(self):
        """'ead (head) apostrophe should not be counted."""
        text = "use your 'ead"
        assert _count_quotes(text) == 0

    def test_elp_not_counted(self):
        """'elp (help) apostrophe should not be counted."""
        text = "can't 'elp it"
        assert _count_quotes(text) == 0

    def test_ouse_not_counted(self):
        """'ouse (house) apostrophe should not be counted."""
        text = "in the big 'ouse"
        assert _count_quotes(text) == 0

    # --------------------------------------------------------------------------
    # Year/decade abbreviations
    # --------------------------------------------------------------------------

    def test_year_99_not_counted(self):
        """'99 (year) apostrophe should not be counted."""
        text = "back in '99"
        assert _count_quotes(text) == 0

    def test_decade_20s_not_counted(self):
        """'20s (decade) apostrophe should not be counted."""
        text = "the roaring '20s"
        assert _count_quotes(text) == 0

    # --------------------------------------------------------------------------
    # Dialog quotes SHOULD still be counted
    # --------------------------------------------------------------------------

    def test_dialog_opening_capital_counted(self):
        """Dialog opening with capital letter should be counted."""
        text = "'Hello!' she said"
        assert _count_quotes(text) == 2  # Opening and closing quote

    def test_double_quote_dialog_counted(self):
        """Double quote dialog should be counted."""
        text = '"Hello there," he said.'
        assert _count_quotes(text) == 2

    def test_mixed_elision_and_dialog(self):
        """Elision inside dialog - only dialog quotes counted."""
        text = "\"Give 'em the goods,\" he said."
        assert _count_quotes(text) == 2  # Only the double quotes

    def test_elision_plus_dialog_quotes(self):
        """Sentence with elision and separate dialog quotes."""
        text = "The 'cello played. \"Beautiful,\" she said."
        # 'cello = 0, dialog quotes = 2
        assert _count_quotes(text) == 2


# ==============================================================================
# SECTION 2: Elisions in Narrative Text (should NOT affect paragraph breaks)
# ==============================================================================


class TestElisionsInNarrativeText:
    """Elisions in narrative text should not throw off paragraph breaks."""

    # --------------------------------------------------------------------------
    # Musical instruments
    # --------------------------------------------------------------------------

    def test_cello_narrative_paragraph_breaks(self):
        """Narrative with 'cello should still get paragraph breaks."""
        sentences = [
            "The music swelled as the 'cello came in.",
            "Jack listened intently.",
            "The performance was magnificent.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_cello_mid_sentence_narrative(self):
        """'cello in middle of sentence, narrative continues correctly."""
        sentences = [
            "So as the 'cello came in with its predictable contribution.",
            "The audience applauded.",
            "Stephen smiled at the music.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_copter_narrative(self):
        """Narrative with 'copter should get paragraph breaks."""
        sentences = [
            "The 'copter landed on the pad.",
            "Soldiers rushed out.",
            "The mission had begun.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    # --------------------------------------------------------------------------
    # Archaic literary elisions
    # --------------------------------------------------------------------------

    def test_tis_narrative_paragraph_breaks(self):
        """Narrative starting with 'tis should get proper breaks."""
        sentences = [
            "'Tis a far better thing I do.",
            "The crowd watched in silence.",
            "History would remember this day.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_twas_narrative_paragraph_breaks(self):
        """Narrative with 'twas should get proper breaks."""
        sentences = [
            "'Twas the night before Christmas.",
            "All through the house.",
            "Not a creature was stirring.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_twere_narrative(self):
        """Narrative with 'twere should get proper breaks."""
        sentences = [
            "'Twere better to have loved and lost.",
            "The philosopher pondered this truth.",
            "Time passed slowly.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_twixt_narrative(self):
        """Narrative with 'twixt should get proper breaks."""
        sentences = [
            "The valley lay 'twixt the mountains.",
            "A river flowed through it.",
            "The view was breathtaking.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_gainst_narrative(self):
        """Narrative with 'gainst should get proper breaks."""
        sentences = [
            "They fought 'gainst impossible odds.",
            "The battle raged for hours.",
            "Victory seemed distant.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    # --------------------------------------------------------------------------
    # Dialect elisions in narrative
    # --------------------------------------------------------------------------

    def test_em_narrative_paragraph_breaks(self):
        """Narrative with 'em should get proper breaks."""
        sentences = [
            "He told 'em to wait outside.",
            "The men obeyed without question.",
            "Discipline was strict on this ship.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_ere_narrative(self):
        """Narrative with 'ere should get proper breaks."""
        sentences = [
            "Come 'ere and see this.",
            "The discovery was remarkable.",
            "Everyone gathered around.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_ouse_narrative(self):
        """Narrative with 'ouse should get proper breaks."""
        sentences = [
            "The big 'ouse stood on the hill.",
            "Its windows gleamed in the sun.",
            "The garden was overgrown.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    # --------------------------------------------------------------------------
    # Year abbreviations in narrative
    # --------------------------------------------------------------------------

    def test_year_narrative(self):
        """Narrative with year abbreviation should get proper breaks."""
        sentences = [
            "Back in '99, things were different.",
            "The world was changing rapidly.",
            "Nobody could have predicted what came next.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_decade_narrative(self):
        """Narrative with decade abbreviation should get proper breaks."""
        sentences = [
            "The roaring '20s were a time of excess.",
            "Jazz filled the speakeasies.",
            "Prohibition was widely ignored.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3


# ==============================================================================
# SECTION 3: Elisions Inside Dialog (quote parity should remain correct)
# ==============================================================================


class TestElisionsInsideDialog:
    """Elisions inside dialog should not break quote parity tracking."""

    # --------------------------------------------------------------------------
    # Single elision inside dialog
    # --------------------------------------------------------------------------

    def test_em_inside_dialog(self):
        """'em inside dialog should not break quote parity."""
        sentences = [
            '"Give \'em the goods," said Jack.',
            "The crew obeyed.",
            "The cargo was transferred.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_tis_inside_dialog(self):
        """'tis inside dialog should not break quote parity."""
        sentences = [
            "\"'Tis a fine morning,\" observed Stephen.",
            "Jack nodded in agreement.",
            "The sun was indeed bright.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_cello_inside_dialog(self):
        """'cello inside dialog should not break quote parity."""
        sentences = [
            '"The \'cello is out of tune," he complained.',
            "The musician adjusted the strings.",
            "The rehearsal continued.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_twas_inside_dialog(self):
        """'twas inside dialog should not break quote parity."""
        sentences = [
            "\"'Twas a dark and stormy night,\" he began.",
            "The children leaned forward eagerly.",
            "The story had begun.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_ere_inside_dialog(self):
        """'ere inside dialect dialog should not break quote parity."""
        sentences = [
            '"Come \'ere, you scoundrel!" shouted the bosun.',
            "The sailor froze.",
            "Trouble was brewing.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    # --------------------------------------------------------------------------
    # Multiple elisions inside dialog
    # --------------------------------------------------------------------------

    def test_multiple_elisions_inside_dialog(self):
        """Multiple elisions in one dialog should not break parity."""
        sentences = [
            '"Give \'em to \'im," ordered the captain.',
            "The order was carried out.",
            "Efficiency was paramount.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_elision_and_contraction_inside_dialog(self):
        """Elision plus contraction in dialog should work correctly."""
        sentences = [
            '"I can\'t give \'em any more," he protested.',
            "The supplies were running low.",
            "Rationing would begin tomorrow.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    # --------------------------------------------------------------------------
    # Single quote dialog with elisions
    # --------------------------------------------------------------------------

    def test_em_inside_single_quote_dialog(self):
        """'em inside single-quoted dialog should work correctly."""
        sentences = [
            "'Give 'em what they want,' said the merchant.",
            "The deal was struck.",
            "Both parties departed satisfied.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_tis_inside_single_quote_dialog(self):
        """'tis inside single-quoted dialog."""
        sentences = [
            "''Tis but a scratch,' he declared bravely.",
            "Blood dripped from the wound.",
            "The surgeon prepared his instruments.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3


# ==============================================================================
# SECTION 4: Dialog Opening with Elision (Edge Cases)
# ==============================================================================


class TestDialogOpeningWithElision:
    """Edge cases where dialog opens with an elision-like pattern.

    Note: 'Twas can be either:
    1. Narrative elision: 'Twas a dark night. (not dialog)
    2. Dialog opening: "'Twas the night before," he read aloud.

    The key distinction is context - is there a closing quote?
    """

    # --------------------------------------------------------------------------
    # Elision as narrative opener (no quotes around it)
    # --------------------------------------------------------------------------

    def test_twas_narrative_opener(self):
        """'Twas as narrative opener (not dialog)."""
        sentences = [
            "'Twas brillig and the slithy toves.",
            "Did gyre and gimble in the wabe.",
            "All mimsy were the borogoves.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        # Each should be separate paragraph (narrative)
        assert len(paragraphs) == 3

    def test_tis_narrative_opener(self):
        """'Tis as narrative opener (not dialog)."""
        sentences = [
            "'Tis the season to be jolly.",
            "Decorations adorned every surface.",
            "The holiday spirit was palpable.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    # --------------------------------------------------------------------------
    # Elision inside quoted dialog that spans multiple sentences
    # --------------------------------------------------------------------------

    def test_twas_starts_multi_sentence_dialog(self):
        """Dialog that starts with 'Twas and continues."""
        sentences = [
            "\"'Twas a fine day for sailing.",
            "The wind was perfect.",
            'We made excellent time."',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        # All three should be one paragraph (continuing dialog)
        assert len(paragraphs) == 1

    def test_tis_starts_multi_sentence_dialog(self):
        """Dialog that starts with 'tis and continues."""
        sentences = [
            "\"'Tis true what they say.",
            "Fortune favors the bold.",
            'I have seen it myself."',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    def test_em_in_dialog_continuation(self):
        """Multi-sentence dialog with 'em."""
        sentences = [
            '"Give \'em hell, boys.',
            "We've trained for this.",
            'Victory will be ours."',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 1

    # --------------------------------------------------------------------------
    # Single quote elision-like dialog openers
    # --------------------------------------------------------------------------

    def test_single_quote_twas_dialog(self):
        """Single-quoted dialog starting with 'Twas."""
        sentences = [
            "''Twas the best of times.",
            "It was the worst of times.",
            "It was the age of wisdom.'",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        # This is a multi-sentence quote, should stay together
        assert len(paragraphs) == 1


# ==============================================================================
# SECTION 5: Narrative Following Elision-containing Sentences
# ==============================================================================


class TestNarrativeAfterElisions:
    """Narrative after elision-containing sentences should still format correctly."""

    def test_narrative_after_cello_sentence(self):
        """Narrative after 'cello sentence gets proper breaks."""
        sentences = [
            "The 'cello's tone was rich and deep.",
            "Jack closed his eyes.",
            "The music transported him.",
            "He thought of home.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4

    def test_narrative_after_em_sentence(self):
        """Narrative after 'em sentence gets proper breaks."""
        sentences = [
            "Tell 'em we're coming.",
            "The messenger rode off.",
            "Dust clouds followed.",
            "Time was running short.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4

    def test_narrative_after_twas_sentence(self):
        """Narrative after 'twas sentence gets proper breaks."""
        sentences = [
            "'Twas ever thus.",
            "The old man shook his head.",
            "Wisdom comes with age.",
            "But so does regret.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4

    def test_dialog_after_elision_narrative(self):
        """Dialog after elision-containing narrative works correctly."""
        sentences = [
            "The 'cello played on.",
            '"Beautiful," whispered Stephen.',
            "The audience remained silent.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_alternating_elision_and_dialog(self):
        """Alternating elision sentences and dialog."""
        sentences = [
            "The 'cello sang its melody.",
            '"Magnificent," said Jack.',
            "'Twas a performance to remember.",
            '"Indeed," agreed Stephen.',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4


# ==============================================================================
# SECTION 6: Multiple Elisions in Same Text
# ==============================================================================


class TestMultipleElisions:
    """Tests for text containing multiple elisions."""

    def test_two_elisions_same_sentence(self):
        """Two elisions in one sentence."""
        sentences = [
            "The 'cello and 'copter both arrived.",
            "An unusual combination.",
            "The crowd was puzzled.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_three_elisions_same_sentence(self):
        """Three elisions in one sentence."""
        sentences = [
            "Give 'em to 'im over 'ere.",
            "The order was confusing.",
            "Nobody moved.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_consecutive_elision_sentences(self):
        """Consecutive sentences each with elisions."""
        sentences = [
            "'Twas a dark night.",
            "The 'cello played mournfully.",
            "Give 'em no quarter.",
            "The battle began.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4

    def test_elisions_across_paragraph(self):
        """Elisions in both narrative and dialog."""
        sentences = [
            "The 'cello's sound filled the room.",
            '"\'Tis beautiful," said Stephen.',
            "Jack nodded in agreement.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3


# ==============================================================================
# SECTION 7: Elisions Mixed with Contractions and Possessives
# ==============================================================================


class TestElisionsMixedWithContractions:
    """Elisions combined with contractions and possessives."""

    def test_elision_and_contraction_same_sentence(self):
        """Elision and contraction in same sentence."""
        sentences = [
            "I don't like the 'cello's tone.",
            "It sounds too harsh.",
            "The musician disagreed.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_elision_and_possessive_same_sentence(self):
        """Elision and possessive in same sentence."""
        sentences = [
            "Jack's 'cello was Italian-made.",
            "Stephen admired it greatly.",
            "Music was their shared passion.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_elision_contraction_possessive_same_sentence(self):
        """All three in same sentence."""
        sentences = [
            "Jack's 'cello wouldn't stay in tune.",
            "The humidity was to blame.",
            "Repairs were needed.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_multiple_possessives_with_elision(self):
        """Multiple possessives with elision."""
        sentences = [
            "Joselito's coffee-house had Stephen's favorite 'cello music.",
            "The ambiance was perfect.",
            "They met there often.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_em_with_contractions(self):
        """'em with contractions."""
        sentences = [
            "I can't give 'em what they're asking.",
            "The demands were unreasonable.",
            "Negotiations stalled.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3


# ==============================================================================
# SECTION 8: Different Quote Styles with Elisions
# ==============================================================================


class TestQuoteStylesWithElisions:
    """Different quote styles interacting with elisions."""

    def test_double_quotes_with_elision(self):
        """Double-quoted dialog with elision."""
        sentences = [
            '"The \'cello is ready," announced the conductor.',
            "The orchestra prepared.",
            "The concert was about to begin.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_single_quotes_with_elision(self):
        """Single-quoted dialog with elision."""
        sentences = [
            "'Give 'em time,' advised Stephen.",
            "Jack's patience was thin.",
            "The waiting continued.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_nested_quotes_with_elision(self):
        """Nested quotes with elision."""
        sentences = [
            "\"He said 'give 'em nothing' to me,\" Jack reported.",
            "Stephen frowned.",
            "The situation was complicated.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_curly_quotes_with_elision(self):
        """Curly quotes with elision."""
        sentences = [
            "\u201cThe 'cello sounds divine,\u201d she remarked.",
            "The audience murmured agreement.",
            "The performance continued.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3


# ==============================================================================
# SECTION 9: Real-world Ebook Patterns (Master and Commander Style)
# ==============================================================================


class TestMasterAndCommanderPatterns:
    """Realistic ebook patterns from nautical fiction."""

    def test_mandc_cello_passage(self):
        """Original Master and Commander 'cello passage."""
        sentences = [
            "The high note came, the pause, the resolution.",
            "So as the 'cello came in with its predictable contribution.",
            "Jack beat time with his heel.",
            "Stephen's eyes were closed.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4

    def test_mandc_naval_dialect(self):
        """Naval dialect with elisions."""
        sentences = [
            "\"Give 'em a broadside!\" roared the captain.",
            "The guns thundered in response.",
            "Smoke obscured the enemy vessel.",
            "The battle was joined.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4

    def test_mandc_mess_deck_dialog(self):
        """Mess deck dialog with dialect."""
        sentences = [
            "\"I 'eard tell the captain's taking us 'round the 'orn,\" said Davies.",
            "The men groaned.",
            "Cape Horn was notorious.",
            "Many ships had foundered there.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4

    def test_mandc_mixed_dialog_narrative(self):
        """Mixed dialog and narrative with elisions."""
        sentences = [
            "'Twas a fair wind that morning.",
            '"Set the topsails," ordered Jack.',
            "The crew sprang to action.",
            "\"Give 'em every stitch of canvas,\" he added.",
            "Speed was of the essence.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 5

    def test_mandc_musical_evening(self):
        """Musical evening scene with 'cello."""
        sentences = [
            "The 'cello's voice filled the great cabin.",
            "Jack's bow moved with practiced ease.",
            '"Beautifully done," said Stephen.',
            "The last note faded into silence.",
            "Both men sat in contemplation.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 5

    def test_mandc_joselitos_scene(self):
        """Joselito's coffee-house scene."""
        sentences = [
            "At Joselito's, Stephen found his usual corner.",
            "The 'cello music drifted from upstairs.",
            '"A pot of chocolate," he ordered.',
            "The waiter nodded and disappeared.",
            "'Twas a pleasant establishment.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 5


# ==============================================================================
# SECTION 10: Cockney and Working Class Dialect
# ==============================================================================


class TestCockneyDialect:
    """Cockney and working-class dialect elisions."""

    def test_cockney_h_dropping_narrative(self):
        """Cockney h-dropping in narrative."""
        sentences = [
            "'E came 'ere yesterday.",
            "The constable took note.",
            "Witnesses were few.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_cockney_full_sentence(self):
        """Full Cockney dialect sentence."""
        sentences = [
            "'Ere, what's all this then?",
            "The crowd parted.",
            "Authority had arrived.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_cockney_ave_narrative(self):
        """'ave in narrative."""
        sentences = [
            "I 'ave me doubts about this.",
            "The plan seemed risky.",
            "Success was uncertain.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_cockney_dialog_with_multiple_elisions(self):
        """Cockney dialog with multiple elisions."""
        sentences = [
            "\"'E said 'e'd 'elp us,\" reported Bill.",
            "The gang considered this.",
            "Trust was hard to come by.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_ow_elision(self):
        """'ow (how) elision."""
        sentences = [
            "'Ow did you manage that?",
            "The trick seemed impossible.",
            "The audience applauded.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_igh_elision(self):
        """'igh (high) elision."""
        sentences = [
            "The 'igh street was crowded.",
            "Market day brought everyone out.",
            "Business was brisk.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3


# ==============================================================================
# SECTION 11: Shakespearean and Archaic Patterns
# ==============================================================================


class TestShakespeareanPatterns:
    """Shakespearean and archaic elision patterns."""

    def test_sblood_oath(self):
        """'sblood oath."""
        sentences = [
            "'Sblood, what villainy is this?",
            "The knight drew his sword.",
            "Honor demanded satisfaction.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_zounds_oath(self):
        """'zounds oath."""
        sentences = [
            "'Zounds, I am betrayed!",
            "The conspiracy was revealed.",
            "Heads would roll.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_tother_archaic(self):
        """'tother (the other) archaic."""
        sentences = [
            "'Tother day I met a stranger.",
            "He bore strange tidings.",
            "War was coming.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_neath_poetic(self):
        """'neath (beneath) poetic."""
        sentences = [
            "The treasure lay 'neath the old oak.",
            "Generations had searched for it.",
            "Now at last it was found.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_midst_poetic(self):
        """'midst (amidst) poetic."""
        sentences = [
            "He stood 'midst the flames.",
            "His courage never wavered.",
            "The crowd watched in awe.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3


# ==============================================================================
# SECTION 12: Modern Colloquial Elisions
# ==============================================================================


class TestModernColloquialElisions:
    """Modern colloquial elision patterns."""

    def test_bout_colloquial(self):
        """'bout (about) colloquial."""
        sentences = [
            "What's it all 'bout anyway?",
            "Nobody could explain.",
            "The mystery deepened.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_cause_colloquial(self):
        """'cause (because) colloquial."""
        sentences = [
            "He left early 'cause he was tired.",
            "Nobody blamed him.",
            "It had been a long day.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_til_colloquial(self):
        """'til (until) colloquial."""
        sentences = [
            "Wait 'til you see this.",
            "The surprise was ready.",
            "Excitement built.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_kay_colloquial(self):
        """'kay (okay) colloquial."""
        sentences = [
            "'Kay, let's do this.",
            "Everyone prepared.",
            "The plan was set.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_cuz_colloquial(self):
        """'cuz (because) colloquial."""
        sentences = [
            "I did it 'cuz I wanted to.",
            "No other reason.",
            "Simple as that.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3


# ==============================================================================
# SECTION 13: Edge Cases - Sentence Position
# ==============================================================================


class TestElisionPosition:
    """Elisions at different positions in sentences."""

    def test_elision_at_sentence_start(self):
        """Elision at start of sentence."""
        sentences = [
            "'Twas brillig.",
            "The sun was setting.",
            "Evening approached.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_elision_at_sentence_middle(self):
        """Elision in middle of sentence."""
        sentences = [
            "The lovely 'cello played sweetly.",
            "Music filled the air.",
            "Spirits lifted.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_elision_at_sentence_end(self):
        """Elision near end of sentence."""
        sentences = [
            "Listen to the 'cello.",
            "Its tone is remarkable.",
            "True craftsmanship.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_elision_after_comma(self):
        """Elision after comma."""
        sentences = [
            "Well, 'tis time to go.",
            "The hour was late.",
            "All retired.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_elision_before_comma(self):
        """Elision before comma."""
        sentences = [
            "The 'cello, beautifully crafted, sang.",
            "Its voice echoed.",
            "The audience was spellbound.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3


# ==============================================================================
# SECTION 14: Complex Multi-turn Dialog with Elisions
# ==============================================================================


class TestComplexDialogWithElisions:
    """Complex multi-turn dialog scenes with elisions."""

    def test_two_speakers_with_elisions(self):
        """Two speakers, both using elisions."""
        sentences = [
            "\"'Twas a dark night,\" said Jack.",
            "\"Give 'em no quarter,\" replied Stephen.",
            "The conversation turned serious.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_dialog_elision_dialog_pattern(self):
        """Dialog-elision narrative-dialog pattern."""
        sentences = [
            '"I see," said Jack.',
            "The 'cello's notes hung in the air.",
            '"Beautiful," agreed Stephen.',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_multi_sentence_dialog_with_elision(self):
        """Multi-sentence dialog containing elision."""
        sentences = [
            '"Listen to me carefully.',
            "Give 'em nothing until I return.",
            'Is that clear?"',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        # Should stay together as one dialog block
        assert len(paragraphs) == 1

    def test_interrupted_dialog_with_elision(self):
        """Interrupted dialog with elision in narrative."""
        sentences = [
            '"I was saying—"',
            "The 'cello's note interrupted him.",
            '"Never mind," he finished.',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3


# ==============================================================================
# SECTION 15: Stress Tests - Many Elisions
# ==============================================================================


class TestStressTestElisions:
    """Stress tests with many elisions."""

    def test_five_elisions_in_paragraph(self):
        """Five elisions across multiple sentences."""
        sentences = [
            "'Twas a fine day.",
            "The 'cello played.",
            "Give 'em the goods.",
            "Come 'ere quickly.",
            "'Tis nearly over.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 5

    def test_elision_every_sentence(self):
        """Elision in every sentence."""
        sentences = [
            "'Twas midnight.",
            "The 'copter landed.",
            "Give 'em time.",
            "Look 'ere now.",
            "'Tis done.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 5

    def test_alternating_elision_types(self):
        """Different elision types alternating."""
        sentences = [
            "'Twas the beginning.",
            "The 'cello sang.",
            "'Ere, watch this.",
            "Give 'em all.",
            "'Tis the end.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 5


# ==============================================================================
# SECTION 16: Boundary Conditions
# ==============================================================================


class TestElisionBoundaryConditions:
    """Boundary conditions for elision handling."""

    def test_elision_only_sentence(self):
        """Sentence that is just an elision word."""
        sentences = [
            "'Twas.",
            "Indeed.",
            "Quite so.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_elision_with_single_word_sentences(self):
        """Elision mixed with single word sentences."""
        sentences = [
            "'Twas.",
            "Yes.",
            "'Tis.",
            "No.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4

    def test_elision_at_paragraph_boundary(self):
        """Elision at what would be a paragraph boundary."""
        sentences = [
            "The night was dark.",
            "'Twas the calm before the storm.",
            "Thunder rumbled in the distance.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_back_to_back_elision_sentences(self):
        """Two elision sentences back to back."""
        sentences = [
            "'Twas a cold morning.",
            "'Tis colder now.",
            "Winter had arrived.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3


# ==============================================================================
# SECTION 17: Regression Prevention
# ==============================================================================


class TestElisionRegression:
    """Regression tests to prevent reintroduction of bugs."""

    def test_original_issue_13_scenario(self):
        """Original Issue #13 scenario: 'cello breaks formatting."""
        sentences = [
            "The music swelled.",
            "So as the 'cello came in with its predictable contribution.",
            "Jack nodded approvingly.",
            "Stephen's eyes remained closed.",
            "The performance continued.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        # Each narrative sentence should be its own paragraph
        # The 'cello should NOT throw off the quote parity
        assert len(paragraphs) == 5

    def test_cello_does_not_open_quote_state(self):
        """'cello should not toggle quote state open."""
        sentences = [
            "First narrative sentence.",
            "The 'cello played beautifully.",
            "Second narrative sentence.",
            "Third narrative sentence.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        # If 'cello wrongly opened quote state, sentences 2-4 would be grouped
        assert len(paragraphs) == 4

    def test_em_does_not_open_quote_state(self):
        """'em should not toggle quote state open."""
        sentences = [
            "The captain gave orders.",
            "Give 'em no quarter.",
            "The crew obeyed.",
            "Battle commenced.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4

    def test_twas_does_not_open_quote_state(self):
        """'twas should not toggle quote state open."""
        sentences = [
            "The story began.",
            "'Twas a dark and stormy night.",
            "The wind howled.",
            "Rain lashed the windows.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4


# ==============================================================================
# SECTION 18: Integration with Other Features
# ==============================================================================


class TestElisionIntegration:
    """Integration tests with other dialog formatter features."""

    def test_elision_with_dialog_tag(self):
        """Elision in sentence with dialog tag."""
        sentences = [
            '"The \'cello sounds fine," said Jack, tuning his violin.',
            "Stephen agreed.",
            "The concert would proceed.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_elision_after_complete_quote(self):
        """Elision sentence after a complete quote."""
        sentences = [
            '"I am ready," announced Stephen.',
            "'Twas time to begin.",
            "The audience settled.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_elision_before_incomplete_quote(self):
        """Elision sentence before an incomplete (multi-sentence) quote."""
        sentences = [
            "The 'cello was tuned.",
            '"We shall begin with Bach.',
            "Then move to Mozart.",
            'And finish with Beethoven."',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        # First sentence: narrative (1 para)
        # Next three: one multi-sentence dialog (1 para)
        assert len(paragraphs) == 2

    def test_elision_preserves_dialog_grouping(self):
        """Elision in dialog should not break multi-sentence grouping."""
        sentences = [
            '"First sentence.',
            "The 'cello is ready.",
            'Final sentence."',
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        # All three should be one paragraph (same dialog)
        assert len(paragraphs) == 1


# ==============================================================================
# SECTION 19: Unicode Variants
# ==============================================================================


class TestElisionUnicodeVariants:
    """Unicode apostrophe variants with elisions."""

    def test_curly_apostrophe_elision(self):
        """Curly apostrophe in elision."""
        sentences = [
            "The 'cello played on.",  # Using curly apostrophe
            "Jack listened intently.",
            "The music was beautiful.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_backtick_style(self):
        """Backtick style opening quote vs elision."""
        sentences = [
            "`Twas the night before.",  # Backtick
            "The children slept.",
            "Santa approached.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3


# ==============================================================================
# SECTION 20: Special Cases
# ==============================================================================


class TestElisionSpecialCases:
    """Special edge cases for elision handling."""

    def test_elision_with_hyphenated_word(self):
        """Elision near hyphenated word."""
        sentences = [
            "The well-tuned 'cello sang.",
            "Its tone was pure.",
            "The audience sighed.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_elision_with_number(self):
        """Elision with number."""
        sentences = [
            "Back in '99, the 'cello was new.",
            "Now it shows its age.",
            "Time passes.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_elision_at_line_start_looks_like_quote(self):
        """Elision at line start that could be mistaken for quote."""
        sentences = [
            "'Twas brillig.",
            "'Tis done.",
            "'Ere long.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        # Each should be separate (narrative), not grouped as dialog
        assert len(paragraphs) == 3

    def test_elision_vs_actual_opening_quote(self):
        """Distinguish elision from actual opening quote."""
        sentences = [
            "'Twas a fine day.",  # Elision (lowercase after ')
            "'Hello there!'",    # Actual quote (capital after ')
            "She waved back.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_real_quote_capital_vs_elision_lowercase(self):
        """Real quote (capital) vs elision (lowercase) distinction."""
        sentences = [
            "'Stop right there!'",  # Real dialog (capital S)
            "'twas too late.",      # Elision (lowercase t)
            "The chase was over.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3


# ==============================================================================
# SECTION 21: Additional Dialect Elisions
# ==============================================================================


class TestAdditionalDialectElisions:
    """Additional dialect elisions for comprehensive coverage."""

    def test_ard_dialect(self):
        """'ard (hard) dialect."""
        sentences = [
            "It was 'ard work.",
            "The men were exhausted.",
            "Rest was earned.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_alf_dialect(self):
        """'alf (half) dialect."""
        sentences = [
            "Give me 'alf of that.",
            "The portion was divided.",
            "Fair is fair.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_and_dialect(self):
        """'and (hand) dialect."""
        sentences = [
            "Give us a 'and here.",
            "The task required teamwork.",
            "Together they lifted it.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_eart_dialect(self):
        """'eart (heart) dialect."""
        sentences = [
            "Put your 'eart into it.",
            "Effort was required.",
            "Success would follow.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_eaven_dialect(self):
        """'eaven (heaven) dialect."""
        sentences = [
            "Good 'eavens above!",
            "The surprise was complete.",
            "Nobody expected this.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_ome_dialect(self):
        """'ome (home) dialect."""
        sentences = [
            "Let's go 'ome now.",
            "The journey was long.",
            "Home awaited.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_orrible_dialect(self):
        """'orrible (horrible) dialect."""
        sentences = [
            "It was 'orrible to see.",
            "The sight was disturbing.",
            "They looked away.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_ungry_dialect(self):
        """'ungry (hungry) dialect."""
        sentences = [
            "I'm 'ungry as a wolf.",
            "Food was scarce.",
            "Patience wore thin.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3


# ==============================================================================
# SECTION 22: Elisions in Literary Contexts
# ==============================================================================


class TestLiteraryElisions:
    """Elisions in various literary contexts."""

    def test_poetry_elision(self):
        """Elision in poetic context."""
        sentences = [
            "'Twas brillig and the slithy toves.",
            "Did gyre and gimble in the wabe.",
            "All mimsy were the borogoves.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_fairy_tale_elision(self):
        """Elision in fairy tale context."""
        sentences = [
            "'Twas once upon a time.",
            "A princess lived in a tower.",
            "Her hair was golden.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_christmas_carol_elision(self):
        """Elision in Christmas carol context."""
        sentences = [
            "'Twas the night before Christmas.",
            "All through the house.",
            "Not a creature was stirring.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_biblical_archaic_elision(self):
        """Elision in biblical/archaic context."""
        sentences = [
            "'Tis written in the scriptures.",
            "The prophecy was clear.",
            "All would be fulfilled.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_gothic_novel_elision(self):
        """Elision in gothic novel context."""
        sentences = [
            "'Twas a dark and stormy night.",
            "The castle loomed ahead.",
            "Lightning split the sky.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_sea_shanty_elision(self):
        """Elision in sea shanty context."""
        sentences = [
            "'Twas on the good ship Venus.",
            "By Christ you should have seen us.",
            "The figurehead was a whore in bed.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3


# ==============================================================================
# SECTION 23: Elisions with Punctuation Variations
# ==============================================================================


class TestElisionPunctuationVariations:
    """Elisions with various punctuation patterns."""

    def test_elision_with_exclamation(self):
        """Elision in exclamatory sentence."""
        sentences = [
            "'Twas magnificent!",
            "The crowd roared.",
            "Victory was theirs.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_elision_with_question(self):
        """Elision in question."""
        sentences = [
            "'Twas it not so?",
            "The lawyer pressed.",
            "The witness hesitated.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_elision_with_ellipsis(self):
        """Elision with ellipsis."""
        sentences = [
            "'Twas a long time ago...",
            "Memory fades.",
            "Some things remain.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_elision_with_dash(self):
        """Elision with em-dash."""
        sentences = [
            "'Twas—how shall I say it—unusual.",
            "Words failed her.",
            "Silence spoke volumes.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_elision_with_semicolon(self):
        """Elision with semicolon in sentence."""
        sentences = [
            "'Twas a strange affair; most peculiar.",
            "Nobody understood.",
            "Mystery remained.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3

    def test_elision_with_colon(self):
        """Elision followed by colon."""
        sentences = [
            "'Twas clear: war was coming.",
            "Preparations began.",
            "Time was short.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 3


# ==============================================================================
# SECTION 24: More Count Quotes Tests
# ==============================================================================


class TestCountQuotesMoreElisions:
    """Additional _count_quotes() tests for elision coverage."""

    def test_neath_not_counted(self):
        """'neath (beneath) apostrophe should not be counted."""
        text = "the treasure 'neath the oak"
        assert _count_quotes(text) == 0

    def test_fore_not_counted(self):
        """'fore (before) apostrophe should not be counted."""
        text = "'fore you go"
        assert _count_quotes(text) == 0

    def test_mongst_not_counted(self):
        """'mongst (amongst) apostrophe should not be counted."""
        text = "'mongst the crowd"
        assert _count_quotes(text) == 0

    def test_prentice_not_counted(self):
        """'prentice (apprentice) apostrophe should not be counted."""
        text = "a mere 'prentice"
        assert _count_quotes(text) == 0

    def test_pon_not_counted(self):
        """'pon (upon) apostrophe should not be counted."""
        text = "'pon my word"
        assert _count_quotes(text) == 0

    def test_scuse_not_counted(self):
        """'scuse (excuse) apostrophe should not be counted."""
        text = "'scuse me"
        assert _count_quotes(text) == 0

    def test_spose_not_counted(self):
        """'spose (suppose) apostrophe should not be counted."""
        text = "I 'spose so"
        assert _count_quotes(text) == 0

    def test_member_not_counted(self):
        """'member (remember) apostrophe should not be counted."""
        text = "I 'member that day"
        assert _count_quotes(text) == 0


# ==============================================================================
# SECTION 25: Complex Scenarios
# ==============================================================================


class TestComplexElisionScenarios:
    """Complex real-world scenarios with multiple elements."""

    def test_naval_action_with_elisions(self):
        """Naval action scene with dialect."""
        sentences = [
            "\"Give 'em a broadside!\" roared the captain.",
            "The guns thundered.",
            "\"'Ard to port!\" came the next order.",
            "The ship heeled sharply.",
            "Battle was joined.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 5

    def test_cockney_conversation(self):
        """Full Cockney conversation."""
        sentences = [
            "\"'Ere, 'ave you 'eard the news?\" asked Bill.",
            "\"What news?\" replied Tom.",
            "\"The guv'nor's been 'ere looking for you.\"",
            "Tom went pale.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 4

    def test_musical_evening_with_elisions(self):
        """Musical evening with 'cello and dialog."""
        sentences = [
            "The 'cello's mournful voice filled the cabin.",
            '"Beautiful," whispered Stephen.',
            "Jack smiled and played on.",
            "\"'Twas my mother's favorite,\" he said.",
            "The music continued into the night.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 5

    def test_historical_narrative_with_elisions(self):
        """Historical narrative with archaic elisions."""
        sentences = [
            "'Twas the year of our Lord 1805.",
            "England stood alone 'gainst Napoleon.",
            "The fleet was ready.",
            "'Ere long, battle would be joined.",
            "History awaited.",
        ]
        result = format_dialog(sentences)
        paragraphs = result.split("\n\n")
        assert len(paragraphs) == 5
