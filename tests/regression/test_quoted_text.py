# -*- coding: UTF-8 -*-
"""Quoted speech and text."""

from fast_sentence_segment import segment_text


class TestQuotedText:
    """Quoted speech and text."""

    def test_simple_quote(self):
        result = segment_text('He said "Hello there" to me.', flatten=True)
        assert result == ['He said "Hello there" to me.']

    def test_quote_with_period_inside(self):
        # Spurious trailing period after closing quote removed (issue #7)
        result = segment_text('"Hello." He waved.', flatten=True)
        assert result == ['"Hello."', 'He waved.']

    # ──────────────────────────────────────────────────────────────────────────
    # Double quotes - basic patterns
    # ──────────────────────────────────────────────────────────────────────────

    def test_double_quote_at_start(self):
        """Sentence starting with double quote."""
        result = segment_text('"Hello there," she said.', flatten=True)
        assert len(result) == 1
        assert '"Hello there," she said.' in result[0]

    def test_double_quote_at_end(self):
        """Sentence ending with double quote."""
        result = segment_text('He said "goodbye."', flatten=True)
        assert len(result) == 1

    def test_double_quote_mid_sentence(self):
        """Double quote in middle of sentence."""
        result = segment_text('The word "hello" is common.', flatten=True)
        assert len(result) == 1
        assert "hello" in result[0]

    def test_multiple_quoted_words(self):
        """Multiple quoted words in same sentence."""
        result = segment_text('He said "yes" and "no" alternately.', flatten=True)
        assert len(result) == 1

    def test_quoted_phrase_with_comma(self):
        """Quoted phrase followed by comma."""
        result = segment_text('"Indeed," he replied, "it is so."', flatten=True)
        assert len(result) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Single quotes - basic patterns
    # ──────────────────────────────────────────────────────────────────────────

    def test_single_quote_dialog(self):
        """Dialog using single quotes."""
        result = segment_text("'Hello there,' she said.", flatten=True)
        assert len(result) == 1

    def test_single_quote_at_end(self):
        """Sentence ending with single quote."""
        result = segment_text("He said 'goodbye.'", flatten=True)
        assert len(result) == 1

    def test_single_quote_mid_sentence(self):
        """Single quote in middle of sentence."""
        result = segment_text("The word 'hello' is common.", flatten=True)
        assert len(result) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Dialog tags
    # ──────────────────────────────────────────────────────────────────────────

    def test_dialog_tag_he_said(self):
        """Dialog with 'he said' tag."""
        result = segment_text('"I am here," he said.', flatten=True)
        assert len(result) == 1

    def test_dialog_tag_she_replied(self):
        """Dialog with 'she replied' tag."""
        result = segment_text('"Yes," she replied quietly.', flatten=True)
        assert len(result) == 1

    def test_dialog_tag_asked(self):
        """Dialog with question and 'asked' tag."""
        result = segment_text('"Where are you?" he asked.', flatten=True)
        assert len(result) == 1

    def test_dialog_tag_exclaimed(self):
        """Dialog with exclamation and 'exclaimed' tag."""
        result = segment_text('"Fire!" he exclaimed.', flatten=True)
        assert len(result) == 1

    def test_dialog_tag_whispered(self):
        """Dialog with 'whispered' tag."""
        result = segment_text('"Be quiet," she whispered.', flatten=True)
        assert len(result) == 1

    def test_dialog_tag_in_middle(self):
        """Dialog tag in middle of quote."""
        result = segment_text('"I think," said Jack, "we should go."', flatten=True)
        assert len(result) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Quotes with internal punctuation
    # ──────────────────────────────────────────────────────────────────────────

    def test_quote_with_internal_question(self):
        """Quote containing question mark."""
        result = segment_text('He asked "Where is it?" loudly.', flatten=True)
        assert len(result) == 1

    def test_quote_with_internal_exclamation(self):
        """Quote containing exclamation mark."""
        result = segment_text('She shouted "Stop!" at him.', flatten=True)
        assert len(result) == 1

    def test_quote_with_internal_comma(self):
        """Quote containing comma."""
        result = segment_text('He said "Hello, friend" warmly.', flatten=True)
        assert len(result) == 1

    def test_quote_with_internal_semicolon(self):
        """Quote containing semicolon."""
        result = segment_text('She quoted "First; second" from memory.', flatten=True)
        assert len(result) == 1

    def test_quote_with_ellipsis(self):
        """Quote containing ellipsis."""
        result = segment_text('He trailed off "I thought..." quietly.', flatten=True)
        assert len(result) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Multiple sentences with quotes
    # ──────────────────────────────────────────────────────────────────────────

    def test_two_sentences_first_quoted(self):
        """First sentence quoted, second not."""
        result = segment_text('"Hello." He walked away.', flatten=True)
        assert len(result) == 2

    def test_two_sentences_second_quoted(self):
        """First sentence not quoted, second is."""
        result = segment_text('He arrived. "Hello there."', flatten=True)
        assert len(result) == 2

    def test_two_quoted_sentences(self):
        """Two separate quoted sentences."""
        result = segment_text('"Hello." "Goodbye."', flatten=True)
        assert len(result) == 2

    def test_quoted_then_dialog_tag_then_more(self):
        """Quote with tag followed by another sentence."""
        result = segment_text('"Hello," he said. Then he left.', flatten=True)
        assert len(result) == 2

    # ──────────────────────────────────────────────────────────────────────────
    # Nested and complex quotes
    # ──────────────────────────────────────────────────────────────────────────

    def test_quote_within_quote_double_single(self):
        """Single quote inside double quote."""
        result = segment_text("He said \"She told me 'hello' yesterday.\"", flatten=True)
        assert len(result) == 1

    def test_quote_within_quote_single_double(self):
        """Double quote inside single quote."""
        result = segment_text("She said 'He told me \"hello\" yesterday.'", flatten=True)
        assert len(result) == 1

    def test_multiple_levels_of_quotes(self):
        """Multiple nested quotes."""
        result = segment_text("He said \"Jack said 'Mary said hello' to me.\"", flatten=True)
        assert len(result) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Edge cases with quotes
    # ──────────────────────────────────────────────────────────────────────────

    def test_empty_quotes(self):
        """Empty quoted string."""
        result = segment_text('He said "" nothing.', flatten=True)
        assert len(result) == 1

    def test_single_word_quote(self):
        """Single word in quotes."""
        result = segment_text('The answer was "yes" indeed.', flatten=True)
        assert len(result) == 1

    def test_quote_at_sentence_boundary(self):
        """Quote exactly at sentence boundary."""
        result = segment_text('He said "yes." She said "no."', flatten=True)
        assert len(result) == 2

    def test_quote_with_number(self):
        """Quote containing numbers."""
        result = segment_text('She said "I have 3 apples."', flatten=True)
        assert len(result) == 1

    def test_quote_with_abbreviation(self):
        """Quote containing abbreviation."""
        result = segment_text('He said "Dr. Smith is here."', flatten=True)
        assert len(result) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Contractions and possessives (not dialog quotes)
    # ──────────────────────────────────────────────────────────────────────────

    def test_contraction_dont(self):
        """Contraction don't is not a quote."""
        result = segment_text("I don't know what to say.", flatten=True)
        assert len(result) == 1
        assert "don't" in result[0]

    def test_contraction_its(self):
        """Contraction it's is not a quote."""
        result = segment_text("It's a beautiful day.", flatten=True)
        assert len(result) == 1

    def test_possessive_jacks(self):
        """Possessive Jack's is not a quote."""
        result = segment_text("Jack's ship sailed away.", flatten=True)
        assert len(result) == 1

    def test_mixed_contraction_and_dialog(self):
        """Sentence with both contraction and dialog quote."""
        result = segment_text("\"I don't know,\" he said.", flatten=True)
        assert len(result) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Real-world ebook patterns
    # ──────────────────────────────────────────────────────────────────────────

    def test_ebook_dialog_pattern_1(self):
        """Typical ebook dialog pattern."""
        result = segment_text('"Very well," said the captain. "Prepare to sail."', flatten=True)
        assert len(result) == 2

    def test_ebook_dialog_pattern_2(self):
        """Dialog with action in between."""
        result = segment_text('"Wait," he said, holding up his hand. "Listen."', flatten=True)
        assert len(result) == 2

    def test_ebook_narrative_with_quote(self):
        """Narrative containing quoted word."""
        result = segment_text('The word "honor" meant everything to him.', flatten=True)
        assert len(result) == 1

    def test_ebook_chapter_opening(self):
        """Chapter opening with quote."""
        result = segment_text('"Call me Ishmael." So begins the famous novel.', flatten=True)
        assert len(result) == 2
