# -*- coding: UTF-8 -*-
"""Whitespace handling."""

from fast_sentence_segment import segment_text


class TestWhitespace:
    """Whitespace handling."""

    def test_double_space_as_delimiter(self):
        result = segment_text("First sentence.  Second sentence.", flatten=True)
        assert result == ["First sentence.", "Second sentence."]

    def test_leading_trailing_whitespace(self):
        result = segment_text("   Hello world.   ", flatten=True)
        assert result == ["Hello world."]

    def test_multiple_spaces_as_delimiter(self):
        # Multiple spaces are treated as sentence delimiter
        result = segment_text("Hello    world.", flatten=True)
        assert result == ["Hello. world."]

    # ──────────────────────────────────────────────────────────────────────────
    # Tab handling
    # ──────────────────────────────────────────────────────────────────────────

    def test_single_tab(self):
        """Single tab in text."""
        result = segment_text("Hello\tworld.", flatten=True)
        assert len(result) == 1
        assert "Hello" in result[0]
        assert "world" in result[0]

    def test_multiple_tabs(self):
        """Multiple tabs in text."""
        result = segment_text("Hello\t\tworld.", flatten=True)
        assert len(result) == 1

    def test_tab_at_start(self):
        """Tab at start of text."""
        result = segment_text("\tHello world.", flatten=True)
        assert len(result) == 1
        assert "Hello" in result[0]

    def test_tab_at_end(self):
        """Tab at end of text."""
        result = segment_text("Hello world.\t", flatten=True)
        assert len(result) == 1

    def test_mixed_tabs_and_spaces(self):
        """Mix of tabs and spaces."""
        result = segment_text("Hello \t world.", flatten=True)
        assert len(result) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Newline handling
    # ──────────────────────────────────────────────────────────────────────────

    def test_single_newline(self):
        """Single newline in text."""
        result = segment_text("Hello\nworld.", flatten=True)
        assert len(result) >= 1

    def test_multiple_newlines(self):
        """Multiple newlines (paragraph break)."""
        result = segment_text("Hello.\n\nWorld.", flatten=True)
        assert len(result) == 2

    def test_newline_at_start(self):
        """Newline at start."""
        result = segment_text("\nHello world.", flatten=True)
        assert len(result) == 1

    def test_newline_at_end(self):
        """Newline at end."""
        result = segment_text("Hello world.\n", flatten=True)
        assert len(result) == 1

    def test_windows_line_endings(self):
        """Windows-style line endings."""
        result = segment_text("Hello.\r\nWorld.", flatten=True)
        assert len(result) >= 1

    def test_old_mac_line_endings(self):
        """Old Mac-style line endings."""
        result = segment_text("Hello.\rWorld.", flatten=True)
        assert len(result) >= 1

    # ──────────────────────────────────────────────────────────────────────────
    # Leading and trailing whitespace
    # ──────────────────────────────────────────────────────────────────────────

    def test_leading_spaces(self):
        """Leading spaces are stripped."""
        result = segment_text("    Hello world.", flatten=True)
        assert len(result) == 1
        assert result[0].startswith("Hello")

    def test_trailing_spaces(self):
        """Trailing spaces are stripped."""
        result = segment_text("Hello world.    ", flatten=True)
        assert len(result) == 1
        assert result[0].endswith(".")

    def test_leading_and_trailing_spaces(self):
        """Both leading and trailing spaces."""
        result = segment_text("   Hello world.   ", flatten=True)
        assert len(result) == 1

    def test_leading_newlines(self):
        """Leading newlines."""
        result = segment_text("\n\nHello world.", flatten=True)
        assert len(result) == 1

    def test_trailing_newlines(self):
        """Trailing newlines."""
        result = segment_text("Hello world.\n\n", flatten=True)
        assert len(result) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Whitespace between sentences
    # ──────────────────────────────────────────────────────────────────────────

    def test_single_space_between_sentences(self):
        """Single space between sentences."""
        result = segment_text("Hello. World.", flatten=True)
        assert len(result) == 2

    def test_double_space_between_sentences(self):
        """Double space between sentences."""
        result = segment_text("Hello.  World.", flatten=True)
        assert len(result) == 2

    def test_triple_space_between_sentences(self):
        """Triple space between sentences."""
        result = segment_text("Hello.   World.", flatten=True)
        assert len(result) == 2

    def test_newline_between_sentences(self):
        """Newline between sentences."""
        result = segment_text("Hello.\nWorld.", flatten=True)
        assert len(result) == 2

    def test_double_newline_between_sentences(self):
        """Double newline (paragraph break) between sentences."""
        result = segment_text("Hello.\n\nWorld.", flatten=True)
        assert len(result) == 2

    # ──────────────────────────────────────────────────────────────────────────
    # Special whitespace characters
    # ──────────────────────────────────────────────────────────────────────────

    def test_non_breaking_space(self):
        """Non-breaking space."""
        result = segment_text("100\xa0km away.", flatten=True)
        assert len(result) == 1

    def test_vertical_tab(self):
        """Vertical tab character."""
        result = segment_text("Hello\vworld.", flatten=True)
        assert len(result) >= 1

    def test_form_feed(self):
        """Form feed character."""
        result = segment_text("Hello\fworld.", flatten=True)
        assert len(result) >= 1

    # ──────────────────────────────────────────────────────────────────────────
    # Mixed whitespace patterns
    # ──────────────────────────────────────────────────────────────────────────

    def test_space_tab_space(self):
        """Space-tab-space pattern."""
        result = segment_text("Hello \t world.", flatten=True)
        assert len(result) == 1

    def test_tab_newline_tab(self):
        """Tab-newline-tab pattern."""
        result = segment_text("Hello.\t\n\tWorld.", flatten=True)
        assert len(result) >= 1

    def test_all_whitespace_types(self):
        """All whitespace types mixed."""
        result = segment_text("Hello \t\n\r world.", flatten=True)
        assert len(result) >= 1

    # ──────────────────────────────────────────────────────────────────────────
    # Indentation patterns (common in ebooks)
    # ──────────────────────────────────────────────────────────────────────────

    def test_indented_paragraph(self):
        """Indented paragraph."""
        result = segment_text("    This is indented text.", flatten=True)
        assert len(result) == 1

    def test_multiple_indented_lines(self):
        """Multiple indented lines."""
        result = segment_text("    Line one.\n    Line two.", flatten=True)
        assert len(result) >= 1

    def test_hanging_indent(self):
        """Hanging indent pattern."""
        result = segment_text("First line.\n    Continuation.", flatten=True)
        assert len(result) >= 1

    # ──────────────────────────────────────────────────────────────────────────
    # Edge cases
    # ──────────────────────────────────────────────────────────────────────────

    def test_no_space_between_sentences(self):
        """No space between sentences (attached)."""
        result = segment_text("Hello.World.", flatten=True)
        # Behavior may vary - just check it doesn't crash
        assert len(result) >= 1

    def test_many_spaces(self):
        """Very many spaces."""
        result = segment_text("Hello          world.", flatten=True)
        assert len(result) >= 1

    def test_spaces_around_punctuation(self):
        """Spaces around punctuation."""
        result = segment_text("Hello . World .", flatten=True)
        # Unusual but should handle gracefully
        assert len(result) >= 1

    def test_only_whitespace_between_words(self):
        """Only whitespace, no content."""
        try:
            result = segment_text("     ", flatten=True)
            assert result == [] or result == [""]
        except ValueError:
            pass  # Empty raises ValueError

    def test_alternating_whitespace(self):
        """Alternating spaces and tabs."""
        result = segment_text("a b\tc d\te f.", flatten=True)
        assert len(result) == 1
