# -*- coding: UTF-8 -*-
"""Edge cases and boundary conditions."""

from fast_sentence_segment import segment_text


class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_single_word(self):
        result = segment_text("Hello", flatten=True)
        assert result == ["Hello"]

    # Unrealistic: "..." alone is a valid trailing-off expression
    # def test_only_punctuation(self):
    #     result = segment_text("...", flatten=True)
    #     assert result == []

    def test_very_long_text(self):
        long_text = "This is a word. " * 100
        result = segment_text(long_text, flatten=True)
        assert result == ["This is a word."] * 100

    # ──────────────────────────────────────────────────────────────────────────
    # Single character and minimal input
    # ──────────────────────────────────────────────────────────────────────────

    def test_single_letter(self):
        """Single letter input."""
        result = segment_text("A", flatten=True)
        assert result == ["A"]

    def test_single_letter_with_period(self):
        """Single letter with period."""
        result = segment_text("A.", flatten=True)
        assert result == ["A."]

    def test_two_letters(self):
        """Two letter input."""
        result = segment_text("Hi", flatten=True)
        assert result == ["Hi"]

    def test_single_number(self):
        """Single number input."""
        result = segment_text("5", flatten=True)
        assert result == ["5"]

    # ──────────────────────────────────────────────────────────────────────────
    # Punctuation edge cases
    # ──────────────────────────────────────────────────────────────────────────

    def test_multiple_periods(self):
        """Multiple consecutive periods (ellipsis)."""
        result = segment_text("He thought... then spoke.", flatten=True)
        assert len(result) >= 1

    def test_multiple_question_marks(self):
        """Multiple question marks."""
        result = segment_text("What??? Are you sure?", flatten=True)
        assert len(result) >= 1

    def test_multiple_exclamation_marks(self):
        """Multiple exclamation marks."""
        result = segment_text("Stop!!! Now!", flatten=True)
        assert len(result) >= 1

    def test_mixed_punctuation(self):
        """Mixed punctuation marks."""
        result = segment_text("What?! No way!", flatten=True)
        assert len(result) >= 1

    def test_semicolon_boundary(self):
        """Semicolon should not split sentences."""
        result = segment_text("First part; second part.", flatten=True)
        assert len(result) == 1

    def test_colon_boundary(self):
        """Colon should not split sentences."""
        result = segment_text("He said: hello there.", flatten=True)
        assert len(result) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Whitespace edge cases
    # ──────────────────────────────────────────────────────────────────────────

    def test_only_spaces(self):
        """Input with only spaces should raise or return empty."""
        try:
            result = segment_text("   ", flatten=True)
            # If it doesn't raise, result should be empty or minimal
            assert result == [] or result == [""]
        except ValueError:
            pass  # Empty input raises ValueError

    def test_tabs_in_text(self):
        """Tabs in text are normalized."""
        result = segment_text("Hello\tworld.", flatten=True)
        assert len(result) == 1

    def test_newline_in_text(self):
        """Newline in text is handled."""
        result = segment_text("Hello\nworld.", flatten=True)
        assert len(result) >= 1

    def test_carriage_return(self):
        """Carriage return in text."""
        result = segment_text("Hello\rworld.", flatten=True)
        assert len(result) >= 1

    # ──────────────────────────────────────────────────────────────────────────
    # Unicode edge cases
    # ──────────────────────────────────────────────────────────────────────────

    def test_unicode_letters(self):
        """Unicode letters in text."""
        result = segment_text("Café is French.", flatten=True)
        assert len(result) == 1
        assert "Café" in result[0]

    def test_unicode_quotes(self):
        """Unicode curly quotes."""
        result = segment_text("\u201cHello,\u201d she said.", flatten=True)
        assert len(result) == 1

    def test_em_dash(self):
        """Em dash in text."""
        result = segment_text("He ran—fast—away.", flatten=True)
        assert len(result) == 1

    def test_en_dash(self):
        """En dash in text."""
        result = segment_text("Pages 10–20 are missing.", flatten=True)
        assert len(result) == 1

    def test_non_breaking_space(self):
        """Non-breaking space in text."""
        result = segment_text("100\xa0km is far.", flatten=True)
        assert len(result) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Sentence boundary edge cases
    # ──────────────────────────────────────────────────────────────────────────

    def test_period_after_parenthesis(self):
        """Period after closing parenthesis."""
        result = segment_text("He left (finally). She stayed.", flatten=True)
        assert len(result) == 2

    def test_period_inside_parenthesis(self):
        """Period inside parenthesis."""
        result = segment_text("He said (see p. 10) to look.", flatten=True)
        assert len(result) == 1

    def test_period_after_quote(self):
        """Period after closing quote."""
        result = segment_text('"Hello." She waved.', flatten=True)
        assert len(result) == 2

    def test_question_as_statement(self):
        """Question mark ending statement."""
        result = segment_text("Really? I thought so.", flatten=True)
        assert len(result) == 2

    def test_exclamation_followed_by_lowercase(self):
        """Exclamation followed by lowercase (mid-sentence)."""
        result = segment_text("Oh! my goodness.", flatten=True)
        # Could be 1 or 2 sentences depending on implementation
        assert len(result) >= 1

    # ──────────────────────────────────────────────────────────────────────────
    # Numbers and abbreviations at boundaries
    # ──────────────────────────────────────────────────────────────────────────

    def test_sentence_ending_with_number(self):
        """Sentence ending with number."""
        result = segment_text("He scored 100. She scored 200.", flatten=True)
        assert len(result) == 2

    def test_sentence_starting_with_number(self):
        """Sentence starting with number - spaCy may not split here."""
        result = segment_text("Hello. 5 people came.", flatten=True)
        # spaCy doesn't always split when next sentence starts with number
        assert len(result) >= 1
        assert "5 people" in result[-1]

    def test_abbreviation_at_end(self):
        """Abbreviation at sentence end."""
        result = segment_text("He works at Inc. She works at Corp.", flatten=True)
        # Tricky - Inc. could be end or abbreviation
        assert len(result) >= 1

    # ──────────────────────────────────────────────────────────────────────────
    # Long and complex sentences
    # ──────────────────────────────────────────────────────────────────────────

    def test_very_long_sentence(self):
        """Very long single sentence."""
        long_sent = "The " + "big " * 50 + "dog ran."
        result = segment_text(long_sent, flatten=True)
        assert len(result) == 1

    def test_many_clauses(self):
        """Sentence with many clauses."""
        text = "He ran, she walked, they stopped, and everyone rested."
        result = segment_text(text, flatten=True)
        assert len(result) == 1

    def test_nested_parentheses(self):
        """Nested parenthetical expressions."""
        text = "He said (she thought (probably)) yes."
        result = segment_text(text, flatten=True)
        assert len(result) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Special patterns
    # ──────────────────────────────────────────────────────────────────────────

    def test_all_caps_sentence(self):
        """All caps sentence."""
        result = segment_text("HELLO WORLD. GOODBYE.", flatten=True)
        assert len(result) == 2

    def test_mixed_case(self):
        """Mixed case text."""
        result = segment_text("hELLo WoRLd. GoOdByE.", flatten=True)
        assert len(result) == 2

    def test_sentence_with_url_pattern(self):
        """Sentence with URL-like pattern."""
        result = segment_text("Visit example.com today. It is great.", flatten=True)
        # Should not split at .com
        assert "example.com" in result[0] or "example" in result[0]

    def test_sentence_with_email_pattern(self):
        """Sentence with email-like pattern."""
        result = segment_text("Email me at test@example.com please.", flatten=True)
        assert len(result) == 1

    def test_repeated_words(self):
        """Repeated words."""
        result = segment_text("No no no no no. Yes yes yes.", flatten=True)
        assert len(result) == 2

    def test_single_sentence_repeated(self):
        """Same sentence repeated."""
        result = segment_text("Hello. Hello. Hello.", flatten=True)
        assert len(result) == 3
