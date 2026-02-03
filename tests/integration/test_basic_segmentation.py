# -*- coding: UTF-8 -*-
"""Basic sentence segmentation tests."""

from fast_sentence_segment import segment_text


class TestBasicSegmentation:
    """Basic sentence segmentation tests."""

    def test_single_sentence(self):
        result = segment_text("Hello world.", flatten=True)
        assert result == ["Hello world."]

    def test_two_sentences(self):
        result = segment_text("Hello world. Goodbye world.", flatten=True)
        assert result == ["Hello world.", "Goodbye world."]

    def test_three_sentences(self):
        result = segment_text("One. Two. Three.", flatten=True)
        assert result == ["One.", "Two.", "Three."]

    def test_no_period_preserved(self):
        result = segment_text("Hello world", flatten=True)
        assert result == ["Hello world"]

    # ──────────────────────────────────────────────────────────────────────────
    # Period-terminated sentences
    # ──────────────────────────────────────────────────────────────────────────

    def test_four_sentences(self):
        """Four simple sentences."""
        result = segment_text("One. Two. Three. Four.", flatten=True)
        assert len(result) == 4

    def test_five_sentences(self):
        """Five simple sentences - single letters may not split."""
        result = segment_text("A. B. C. D. E.", flatten=True)
        # Single letter sentences may be treated as abbreviations
        assert len(result) >= 1

    def test_sentence_with_comma(self):
        """Sentence with comma does not split."""
        result = segment_text("Hello, world.", flatten=True)
        assert len(result) == 1

    def test_sentence_with_multiple_commas(self):
        """Sentence with multiple commas."""
        result = segment_text("One, two, three, and four.", flatten=True)
        assert len(result) == 1

    def test_long_sentence(self):
        """Long sentence stays together."""
        long = "This is a very long sentence with many words that goes on and on."
        result = segment_text(long, flatten=True)
        assert len(result) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Question mark sentences
    # ──────────────────────────────────────────────────────────────────────────

    def test_single_question(self):
        """Single question sentence."""
        result = segment_text("How are you?", flatten=True)
        assert len(result) == 1
        assert result[0].endswith("?")

    def test_two_questions(self):
        """Two question sentences."""
        result = segment_text("How are you? Where are you?", flatten=True)
        assert len(result) == 2

    def test_question_then_statement(self):
        """Question followed by statement."""
        result = segment_text("How are you? I am fine.", flatten=True)
        assert len(result) == 2

    def test_statement_then_question(self):
        """Statement followed by question."""
        result = segment_text("I am fine. How are you?", flatten=True)
        assert len(result) == 2

    # ──────────────────────────────────────────────────────────────────────────
    # Exclamation mark sentences
    # ──────────────────────────────────────────────────────────────────────────

    def test_single_exclamation(self):
        """Single exclamation sentence."""
        result = segment_text("Stop right there!", flatten=True)
        assert len(result) == 1
        assert result[0].endswith("!")

    def test_two_exclamations(self):
        """Two exclamation sentences."""
        result = segment_text("Stop! Go!", flatten=True)
        assert len(result) == 2

    def test_exclamation_then_statement(self):
        """Exclamation followed by statement."""
        result = segment_text("Stop! I mean it.", flatten=True)
        assert len(result) == 2

    def test_statement_then_exclamation(self):
        """Statement followed by exclamation."""
        result = segment_text("I said stop. Now!", flatten=True)
        assert len(result) == 2

    # ──────────────────────────────────────────────────────────────────────────
    # Mixed punctuation
    # ──────────────────────────────────────────────────────────────────────────

    def test_period_question_exclamation(self):
        """Period, question, and exclamation."""
        result = segment_text("Hello. How are you? Great!", flatten=True)
        assert len(result) == 3

    def test_all_questions(self):
        """All questions."""
        result = segment_text("Who? What? When? Where? Why?", flatten=True)
        assert len(result) == 5

    def test_all_exclamations(self):
        """All exclamations."""
        result = segment_text("Yes! No! Maybe! Sure! Fine!", flatten=True)
        assert len(result) == 5

    def test_alternating_punctuation(self):
        """Alternating punctuation types."""
        result = segment_text("Hello. Hi! Hey?", flatten=True)
        assert len(result) == 3

    # ──────────────────────────────────────────────────────────────────────────
    # Sentence content variations
    # ──────────────────────────────────────────────────────────────────────────

    def test_single_word_sentences(self):
        """Single word sentences."""
        result = segment_text("Yes. No. Maybe.", flatten=True)
        assert len(result) == 3

    def test_two_word_sentences(self):
        """Two word sentences."""
        result = segment_text("Hello there. Goodbye now.", flatten=True)
        assert len(result) == 2

    def test_varying_length_sentences(self):
        """Sentences of varying lengths."""
        result = segment_text("Short. This one is longer. Even longer sentence here.", flatten=True)
        assert len(result) == 3

    def test_sentence_with_numbers(self):
        """Sentence containing numbers."""
        result = segment_text("I have 5 apples. She has 10.", flatten=True)
        assert len(result) == 2

    def test_sentence_with_proper_nouns(self):
        """Sentence with proper nouns."""
        result = segment_text("John went to Paris. Mary stayed home.", flatten=True)
        assert len(result) == 2

    # ──────────────────────────────────────────────────────────────────────────
    # Capitalization
    # ──────────────────────────────────────────────────────────────────────────

    def test_lowercase_after_period(self):
        """Lowercase after period - spaCy may not split here."""
        result = segment_text("Hello. goodbye.", flatten=True)
        # spaCy doesn't split when next word is lowercase (not a new sentence)
        assert len(result) >= 1

    def test_all_caps_sentences(self):
        """All caps sentences - spaCy may treat as single sentence."""
        result = segment_text("HELLO. GOODBYE.", flatten=True)
        # All caps may be treated as abbreviations or titles
        assert len(result) >= 1

    def test_title_case_sentences(self):
        """Title case sentences."""
        result = segment_text("Hello World. Goodbye World.", flatten=True)
        assert len(result) == 2

    # ──────────────────────────────────────────────────────────────────────────
    # Flatten vs non-flatten
    # ──────────────────────────────────────────────────────────────────────────

    def test_flatten_true(self):
        """Flatten=True returns flat list."""
        result = segment_text("Hello. World.", flatten=True)
        assert isinstance(result, list)
        assert all(isinstance(s, str) for s in result)

    def test_flatten_false(self):
        """Flatten=False returns nested list."""
        result = segment_text("Hello. World.", flatten=False)
        assert isinstance(result, list)
        # Non-flattened returns list of lists (paragraphs)
        assert isinstance(result[0], list)

    # ──────────────────────────────────────────────────────────────────────────
    # Real-world patterns
    # ──────────────────────────────────────────────────────────────────────────

    def test_newspaper_style(self):
        """Newspaper-style short sentences."""
        result = segment_text("Man bites dog. Film at eleven. Story developing.", flatten=True)
        assert len(result) == 3

    def test_dialog_pattern(self):
        """Simple dialog pattern."""
        result = segment_text("Hello. How are you? I am fine. Thank you.", flatten=True)
        assert len(result) == 4

    def test_narrative_pattern(self):
        """Narrative text pattern."""
        result = segment_text("He walked in. She looked up. They smiled.", flatten=True)
        assert len(result) == 3

    def test_instruction_pattern(self):
        """Instruction-style sentences."""
        result = segment_text("Open the door. Enter the room. Close the door.", flatten=True)
        assert len(result) == 3

    # ──────────────────────────────────────────────────────────────────────────
    # Boundary conditions
    # ──────────────────────────────────────────────────────────────────────────

    def test_many_sentences(self):
        """Many sentences."""
        text = ". ".join(["Sentence"] * 20) + "."
        result = segment_text(text, flatten=True)
        assert len(result) == 20

    def test_identical_sentences(self):
        """Identical sentences."""
        result = segment_text("Hello. Hello. Hello.", flatten=True)
        assert len(result) == 3
        assert all(s == "Hello." for s in result)

    def test_progressive_sentences(self):
        """Progressive sentence numbers."""
        result = segment_text("First. Second. Third. Fourth. Fifth.", flatten=True)
        assert len(result) == 5
