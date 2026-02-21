# -*- coding: UTF-8 -*-
"""Pathological xfail tests for hard-wrap corruption (issue #42).

These tests document known edge cases and limitations that the fix to
NewlinesToPeriods is NOT expected to fully resolve. Each test is marked
xfail with a reason explaining why the case is hard or out of scope.

Categories:
  A. Unicode whitespace characters (not stripped by basic str.strip())
  B. Blank continuation lines (empty after stripping)
  C. Wrap inside a URL, path, or code token
  D. Wrap inside a quoted string with structural whitespace
  E. Compound wrap patterns that interact with other pipeline components
  F. Wrap after clause-terminal punctuation (; :) — handled by a different path
  G. Wraps that happen to create false sentence boundaries
  H. Mixed-direction text and unusual character classes
  I. Extremely long runs of whitespace (hundreds of spaces)
  J. Content that is intentionally formatted with periods (e.g. numbered lists)

Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
"""

import pytest

from fast_sentence_segment.dmo.newlines_to_periods import NewlinesToPeriods
from fast_sentence_segment import segment_text


class TestXfailPathological:
    """Known hard cases and acknowledged limitations for issue #42."""

    # ================================================================ A. Unicode whitespace

    @pytest.mark.xfail(reason="U+00A0 non-breaking space is not stripped by str.strip()")
    def test_unicode_nbsp_indent_01(self):
        # \u00a0 is non-breaking space — str.strip() does not remove it
        assert NewlinesToPeriods.process("assist in the business\n\u00a0\u00a0\u00a0\u00a0department.") == "assist in the business department."

    @pytest.mark.xfail(reason="U+00A0 non-breaking space is not stripped by str.strip()")
    def test_unicode_nbsp_indent_02(self):
        assert NewlinesToPeriods.process("the advertising\n\u00a0\u00a0department.") == "the advertising department."

    @pytest.mark.xfail(reason="U+2002 en-space is not stripped by str.strip() in some Python builds")
    def test_unicode_enspace_indent_01(self):
        assert NewlinesToPeriods.process("assist in the business\n\u2002\u2002department.") == "assist in the business department."

    @pytest.mark.xfail(reason="U+2003 em-space is not stripped by str.strip() in some Python builds")
    def test_unicode_emspace_indent_01(self):
        assert NewlinesToPeriods.process("the fire\n\u2003station.") == "the fire station."

    @pytest.mark.xfail(reason="U+3000 ideographic space is not stripped by ASCII str.strip()")
    def test_unicode_ideographic_space_01(self):
        assert NewlinesToPeriods.process("the post\n\u3000office.") == "the post office."

    @pytest.mark.xfail(reason="U+205F medium mathematical space not stripped")
    def test_unicode_math_space_01(self):
        assert NewlinesToPeriods.process("the town\n\u205f\u205fcouncil.") == "the town council."

    @pytest.mark.xfail(reason="U+2009 thin space not stripped by basic str.strip()")
    def test_unicode_thin_space_01(self):
        assert NewlinesToPeriods.process("the health\n\u2009\u2009department.") == "the health department."

    @pytest.mark.xfail(reason="U+00A0 NBSP trailing + 4-space indent compounds the gap")
    def test_unicode_nbsp_trailing_01(self):
        assert NewlinesToPeriods.process("business\u00a0\n    department.") == "business department."

    @pytest.mark.xfail(reason="Mixed unicode and ASCII whitespace in indent")
    def test_unicode_mixed_indent_01(self):
        assert NewlinesToPeriods.process("the foreign\n  \u00a0 office.") == "the foreign office."

    @pytest.mark.xfail(reason="U+FEFF byte-order mark used as indent — not stripped")
    def test_unicode_bom_indent_01(self):
        assert NewlinesToPeriods.process("the night\n\ufeffwatchman.") == "the night watchman."

    # ================================================================ B. Blank continuation lines

    @pytest.mark.xfail(reason="Blank continuation line (only spaces) collapses to empty token, join skips it")
    def test_blank_continuation_01(self):
        # Line 2 is only spaces — after strip it becomes empty, join ignores it
        # Expected: words on line 1 and line 3 joined directly
        assert NewlinesToPeriods.process("business\n    \ndepartment.") == "business department."

    @pytest.mark.xfail(reason="All-whitespace middle line causes word-jump without space")
    def test_blank_continuation_02(self):
        assert NewlinesToPeriods.process("the advertising\n  \n  department.") == "the advertising department."

    @pytest.mark.xfail(reason="Double blank continuation lines (paragraph-style) should be paragraph boundary, not join")
    def test_double_blank_continuation_01(self):
        # \n\n is a paragraph separator — joining makes no sense here
        # This should probably produce two separate items, not a join
        assert NewlinesToPeriods.process("End of paragraph.\n\nStart of next.") == "End of paragraph. Start of next."

    # ================================================================ C. Wrap inside URL / path / code

    @pytest.mark.xfail(reason="URL split across lines cannot be safely rejoined without context — fix is upstream (UrlNormalizer)")
    def test_url_split_01(self):
        # A URL that wraps across lines in Gutenberg errata or README
        assert NewlinesToPeriods.process("See https://example.com/very/long/\npath/to/resource.html") == "See https://example.com/very/long/path/to/resource.html"

    @pytest.mark.xfail(reason="File path split across lines — pipeline is not path-aware")
    def test_filepath_split_01(self):
        assert NewlinesToPeriods.process("The file is at /usr/local/share/\ndoc/readme.txt.") == "The file is at /usr/local/share/doc/readme.txt."

    @pytest.mark.xfail(reason="Code token split across lines — pipeline is not code-aware")
    def test_code_split_01(self):
        assert NewlinesToPeriods.process("Call the function\nsegment_text(text).") == "Call the function segment_text(text)."

    @pytest.mark.xfail(reason="Email address split at wrap point — pipeline is not email-aware")
    def test_email_split_01(self):
        assert NewlinesToPeriods.process("Send to user\n@example.com.") == "Send to user@example.com."

    # ================================================================ D. Structural whitespace in quoted strings

    @pytest.mark.xfail(reason="Quoted string with intentional leading spaces — strip destroys alignment")
    def test_quoted_aligned_01(self):
        # The spaces inside the quote are semantically meaningful
        assert NewlinesToPeriods.process('He read aloud:\n    "    indented verse line."') == 'He read aloud: "    indented verse line."'

    @pytest.mark.xfail(reason="Preformatted block — indentation is content, not formatting")
    def test_preformatted_block_01(self):
        # In a preformatted/code block, the 4-space indent IS the content
        assert NewlinesToPeriods.process("Output:\n    Hello world") == "Output: Hello world"

    @pytest.mark.xfail(reason="Dialogue indent is meaningful in some formats")
    def test_dialogue_stage_direction_01(self):
        assert NewlinesToPeriods.process("HAMLET.\n    To be or not to be.") == "HAMLET. To be or not to be."

    # ================================================================ E. Compound patterns with other pipeline components

    @pytest.mark.xfail(reason="4-space indent + trailing space creates 6-space gap — even after fix, _clean_spacing may still fire")
    def test_compound_trailing_plus_large_indent_01(self):
        result = segment_text(
            "assist in the business  \n      department during the holidays.",
            flatten=True
        )
        full_text = " ".join(result)
        assert "business.department" not in full_text
        assert "business department" in full_text

    @pytest.mark.xfail(reason="8-space indent with 3 trailing spaces — very large gap may still corrupt")
    def test_compound_large_gap_01(self):
        result = segment_text(
            "assist in the business   \n        department.",
            flatten=True
        )
        full_text = " ".join(result)
        assert "business.department" not in full_text

    @pytest.mark.xfail(reason="Wrapping inside a list item marker confuses ListMarkerNormalizer")
    def test_list_marker_wrap_01(self):
        result = segment_text(
            "1. Assist in the business\n    department.\n2. Apply to manager.",
            flatten=True
        )
        full_text = " ".join(result)
        assert "business.department" not in full_text

    @pytest.mark.xfail(reason="Numbered list wrap interacts with NumberedListNormalizer")
    def test_numbered_list_wrap_01(self):
        result = segment_text(
            "1. Bright young men to assist\n    in the business department.\n2. Promotion possible.",
            flatten=True
        )
        full_text = " ".join(result)
        assert "business.department" not in full_text

    @pytest.mark.xfail(reason="Block quote wrap with bullet prefix confuses BulletPointCleaner")
    def test_bullet_block_wrap_01(self):
        result = segment_text(
            "• Assist in the business\n    department.\n• Promotion possible.",
            flatten=True
        )
        full_text = " ".join(result)
        assert "business.department" not in full_text

    @pytest.mark.xfail(reason="Deeply nested quoted dialogue with wraps confuses QuoteAttributionMerger")
    def test_deep_quoted_wrap_01(self):
        result = segment_text(
            '"She said "I must go to the\n    business department." He nodded."',
            flatten=True
        )
        full_text = " ".join(result)
        assert "business.department" not in full_text

    @pytest.mark.xfail(reason="Ellipsis at wrap point confuses EllipsisNormalizer")
    def test_ellipsis_at_wrap_01(self):
        result = segment_text(
            "She wondered...\n    what would happen next.",
            flatten=True
        )
        full_text = " ".join(result)
        assert "wondered.what" not in full_text

    # ================================================================ F. Clause-terminal wraps (;:) — different pipeline path

    @pytest.mark.xfail(reason="Semicolon-terminated wrap inserts phantom period via NewlinesToPeriods — different path, not the 4-space bug")
    def test_semicolon_wrap_4space_01(self):
        # `;\n    ` triggers the clause-terminal path, not the plain-wrap path
        result = NewlinesToPeriods.process("He refused;\n    she insisted.")
        assert result == "He refused; she insisted."

    @pytest.mark.xfail(reason="Colon-terminated wrap with 4-space indent — phantom period inserted, cleanup may leave artifact")
    def test_colon_wrap_4space_01(self):
        result = NewlinesToPeriods.process("The items are as follows:\n    first item, second item.")
        assert result == "The items are as follows: first item, second item."

    @pytest.mark.xfail(reason="Semicolon wrap with trailing space + 4-space indent — compounded gap after phantom period")
    def test_semicolon_trailing_4space_01(self):
        result = NewlinesToPeriods.process("He refused; \n    she insisted.")
        assert result == "He refused; she insisted."

    # ================================================================ G. Wraps that create false sentence boundaries

    @pytest.mark.xfail(reason="Wrap before capitalised word looks like sentence boundary to spaCy")
    def test_false_boundary_capital_01(self):
        # 'business\n    New' — after fix: 'business New' — spaCy may still split here
        result = segment_text(
            "He joined the business\n    New employees received training.",
            flatten=True
        )
        # Should be one sentence but spaCy may split at 'business New'
        assert len(result) == 1

    @pytest.mark.xfail(reason="Wrap after sentence-terminal character creates extra sentence boundary")
    def test_false_boundary_after_period_01(self):
        result = segment_text(
            "The first sentence ended.\n    But this is a continuation.",
            flatten=True
        )
        assert len(result) == 2

    @pytest.mark.xfail(reason="Abbreviation at wrap point confuses AbbreviationMerger")
    def test_abbreviation_at_wrap_01(self):
        result = segment_text(
            "She works at Co.\n    Ltd. in the city.",
            flatten=True
        )
        full_text = " ".join(result)
        assert "Co.Ltd" not in full_text

    @pytest.mark.xfail(reason="Title abbreviation at wrap point causes false split")
    def test_title_abbrev_at_wrap_01(self):
        result = segment_text(
            "He was appointed by Dr.\n    Smith to the committee.",
            flatten=True
        )
        assert len(result) == 1

    @pytest.mark.xfail(reason="Initials at wrap point cause false split")
    def test_initials_at_wrap_01(self):
        result = segment_text(
            "The letter was from A.\n    B. Williams.",
            flatten=True
        )
        full_text = " ".join(result)
        assert "A. B. Williams" in full_text

    # ================================================================ H. Unusual character classes and mixed content

    @pytest.mark.xfail(reason="Arabic text with RTL wrap — pipeline is not RTL-aware")
    def test_rtl_wrap_01(self):
        # Arabic text with a forced line break
        assert NewlinesToPeriods.process("مرحبا\n    بالعالم.") == "مرحبا بالعالم."

    @pytest.mark.xfail(reason="Chinese text wrap — no space expected between CJK characters")
    def test_cjk_wrap_01(self):
        # Chinese text: wrapping should not insert a space
        assert NewlinesToPeriods.process("你好\n世界。") == "你好世界。"

    @pytest.mark.xfail(reason="Mixed ASCII and CJK wrap — space handling unclear")
    def test_mixed_cjk_ascii_wrap_01(self):
        assert NewlinesToPeriods.process("He said 你好\n    世界.") == "He said 你好 世界."

    @pytest.mark.xfail(reason="Cyrillic text wrap — valid case but pipeline not tested against it")
    def test_cyrillic_wrap_01(self):
        assert NewlinesToPeriods.process("Привет\n    мир.") == "Привет мир."

    @pytest.mark.xfail(reason="Greek text wrap — valid case but untested")
    def test_greek_wrap_01(self):
        assert NewlinesToPeriods.process("Γεια σου\n    κόσμε.") == "Γεια σου κόσμε."

    @pytest.mark.xfail(reason="Diacritics in word at wrap boundary — encoding edge case")
    def test_diacritics_wrap_01(self):
        assert NewlinesToPeriods.process("résumé\n    department.") == "résumé department."

    @pytest.mark.xfail(reason="Zero-width non-joiner in indent — not visible but affects strip")
    def test_zwj_indent_01(self):
        assert NewlinesToPeriods.process("the fire\n\u200c\u200cstation.") == "the fire station."

    @pytest.mark.xfail(reason="Soft hyphen in word at wrap — U+00AD should not split word")
    def test_soft_hyphen_word_01(self):
        assert NewlinesToPeriods.process("busi\u00adness\n    department.") == "business department."

    # ================================================================ I. Extremely large whitespace runs

    @pytest.mark.xfail(reason="50-space indent — clean_spacing loop may not converge correctly")
    def test_huge_indent_50spaces_01(self):
        indent = " " * 50
        result = NewlinesToPeriods.process(f"assist in the business\n{indent}department.")
        assert "business.department" not in result
        assert result == "assist in the business department."

    @pytest.mark.xfail(reason="100-space indent — edge case for normalization loops")
    def test_huge_indent_100spaces_01(self):
        indent = " " * 100
        result = NewlinesToPeriods.process(f"assist in the business\n{indent}department.")
        assert "business.department" not in result
        assert result == "assist in the business department."

    @pytest.mark.xfail(reason="200-space indent — stress test")
    def test_huge_indent_200spaces_01(self):
        indent = " " * 200
        result = NewlinesToPeriods.process(f"assist in the business\n{indent}department.")
        assert "business.department" not in result
        assert result == "assist in the business department."

    @pytest.mark.xfail(reason="32-space indent — very deep nesting")
    def test_huge_indent_32spaces_01(self):
        indent = " " * 32
        result = NewlinesToPeriods.process(f"assist in the business\n{indent}department.")
        assert "business.department" not in result
        assert result == "assist in the business department."

    @pytest.mark.xfail(reason="16-space indent — double the Gutenberg standard")
    def test_huge_indent_16spaces_01(self):
        indent = " " * 16
        result = NewlinesToPeriods.process(f"assist in the business\n{indent}department.")
        assert "business.department" not in result
        assert result == "assist in the business department."

    @pytest.mark.xfail(reason="12-space indent — triple the 4-space standard")
    def test_huge_indent_12spaces_01(self):
        indent = " " * 12
        result = NewlinesToPeriods.process(f"assist in the business\n{indent}department.")
        assert "business.department" not in result
        assert result == "assist in the business department."

    @pytest.mark.xfail(reason="50 trailing spaces before newline — extreme trailing whitespace")
    def test_huge_trailing_50spaces_01(self):
        trailing = " " * 50
        result = NewlinesToPeriods.process(f"assist in the business{trailing}\ndepartment.")
        assert "business.department" not in result
        assert result == "assist in the business department."

    @pytest.mark.xfail(reason="50 trailing + 50 indent — maximum compound gap")
    def test_huge_combined_50_50(self):
        trailing = " " * 50
        indent = " " * 50
        result = NewlinesToPeriods.process(f"assist in the business{trailing}\n{indent}department.")
        assert "business.department" not in result
        assert result == "assist in the business department."

    # ================================================================ J. Content with intentional periods

    @pytest.mark.xfail(reason="Numbered list with period at wrap — 1. may interact with NumberedListNormalizer")
    def test_numbered_list_period_01(self):
        assert NewlinesToPeriods.process("1. Assist in the business\n    department.") == "1. Assist in the business department."

    @pytest.mark.xfail(reason="Lettered list at wrap — a. may confuse list normalizer")
    def test_lettered_list_period_01(self):
        assert NewlinesToPeriods.process("a. Assist in the business\n    department.") == "a. Assist in the business department."

    @pytest.mark.xfail(reason="Roman numeral list at wrap")
    def test_roman_numeral_list_01(self):
        assert NewlinesToPeriods.process("ii. Assist in the business\n    department.") == "ii. Assist in the business department."

    @pytest.mark.xfail(reason="Decimal number at wrap point — 3.14 at start of continuation")
    def test_decimal_at_wrap_01(self):
        assert NewlinesToPeriods.process("The value is\n    3.14 radians.") == "The value is 3.14 radians."

    @pytest.mark.xfail(reason="Version number at wrap — 2.0 may look like list marker")
    def test_version_number_at_wrap_01(self):
        assert NewlinesToPeriods.process("Requires version\n    2.0 or higher.") == "Requires version 2.0 or higher."

    @pytest.mark.xfail(reason="Initialism with periods at wrap boundary")
    def test_initialism_at_wrap_01(self):
        assert NewlinesToPeriods.process("Contact the U.S.\n    Embassy directly.") == "Contact the U.S. Embassy directly."

    @pytest.mark.xfail(reason="Ordinal abbreviation at wrap — 3rd. or 4th. at end of line")
    def test_ordinal_abbrev_at_wrap_01(self):
        assert NewlinesToPeriods.process("She lives at No.\n    42 Elm Street.") == "She lives at No. 42 Elm Street."

    # ================================================================ K. Multi-line with blank internal lines (pathological)

    @pytest.mark.xfail(reason="Three lines with blank line in middle — ambiguous paragraph vs. continuation")
    def test_blank_middle_line_01(self):
        result = NewlinesToPeriods.process("line one\n\nline three.")
        assert result == "line one line three."

    @pytest.mark.xfail(reason="Five lines alternating indented/non-indented — complex strip pattern")
    def test_alternating_indent_five_lines_01(self):
        inp = "line one\n    line two\nline three\n    line four\nline five."
        assert NewlinesToPeriods.process(inp) == "line one line two line three line four line five."

    @pytest.mark.xfail(reason="Wrap at very short line (1 char) then 4-space indent")
    def test_single_char_line_wrap_01(self):
        assert NewlinesToPeriods.process("I\n    went.") == "I went."

    @pytest.mark.xfail(reason="Wrap at single letter word followed by large indent")
    def test_single_word_large_indent_01(self):
        assert NewlinesToPeriods.process("a\n        department.") == "a department."

    # ================================================================ L. OCR / scan artifacts with wraps

    @pytest.mark.xfail(reason="OCR artifact (l→1 substitution) at wrap point confuses word boundary detection")
    def test_ocr_artifact_wrap_01(self):
        result = segment_text(
            "He ieft the business\n    department.",
            flatten=True
        )
        full_text = " ".join(result)
        assert "business.department" not in full_text

    @pytest.mark.xfail(reason="OCR double-space artifact IN the word at wrap")
    def test_ocr_double_space_in_word_01(self):
        result = segment_text(
            "assist in the  business\n    department.",
            flatten=True
        )
        full_text = " ".join(result)
        assert "business.department" not in full_text

    @pytest.mark.xfail(reason="Broken word across line with no hyphen (OCR failure mode)")
    def test_ocr_broken_word_wrap_01(self):
        # 'busi' on line 1, 'ness' on line 2 — not hyphenated, not split by dehyphenator
        result = NewlinesToPeriods.process("assist in the busi\n    ness department.")
        # Desired: rejoin busi + ness, but that's outside scope of NewlinesToPeriods
        assert "busi ness" in result or "business" in result

    # ================================================================ M. Stress tests — many consecutive wraps

    @pytest.mark.xfail(reason="10 consecutive 4-space-indented lines — stress test for normalizer loops")
    def test_ten_consecutive_4space_wraps(self):
        lines = [f"word{i}" for i in range(10)]
        inp = lines[0] + "".join(f"\n    {w}" for w in lines[1:])
        expected = " ".join(lines)
        assert NewlinesToPeriods.process(inp) == expected

    @pytest.mark.xfail(reason="20 consecutive 4-space-indented lines — extreme stress test")
    def test_twenty_consecutive_4space_wraps(self):
        lines = [f"word{i}" for i in range(20)]
        inp = lines[0] + "".join(f"\n    {w}" for w in lines[1:])
        expected = " ".join(lines)
        assert NewlinesToPeriods.process(inp) == expected

    @pytest.mark.xfail(reason="50 consecutive 4-space-indented lines — beyond practical Gutenberg wrapping")
    def test_fifty_consecutive_4space_wraps(self):
        lines = [f"word{i}" for i in range(50)]
        inp = lines[0] + "".join(f"\n    {w}" for w in lines[1:])
        expected = " ".join(lines)
        assert NewlinesToPeriods.process(inp) == expected

    # ================================================================ N. Edge cases in the dreiser family

    @pytest.mark.xfail(reason="Dreiser passage with internal period in advertisement text confuses spaCy")
    def test_dreiser_advertisement_full_pipeline_clean_output(self):
        passage = (
            "Wanted: A number of bright young men to assist in the business\n"
            "    department during the Christmas holidays. Promotion possible.\n"
            "    Apply to Business Manager between 9 and 10 a.m."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        # After fix: business.department must not appear
        assert "business.department" not in full_text
        # After fix: 'business department' should appear
        assert "business department" in full_text

    @pytest.mark.xfail(reason="Dreiser passage: 'Promotion possible' split as separate sentence is correct but 'possible.Apply' must not appear")
    def test_dreiser_possible_apply_no_corruption(self):
        passage = (
            "Promotion possible.\n"
            "    Apply to Business Manager between 9 and 10 a.m."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "possible.Apply" not in full_text
        assert "possible.apply" not in full_text

    @pytest.mark.xfail(reason="Dreiser passage wrap before 'Promotion' — wrap before capital creates false boundary")
    def test_dreiser_wrap_before_promotion(self):
        passage = "during the Christmas holidays.\n    Promotion possible."
        result = segment_text(passage, flatten=True)
        # 'Promotion' starts with capital — spaCy correctly splits here
        # both sentences should be present and clean
        assert "holidays.Promotion" not in " ".join(result)

    # ================================================================ O. Pipeline-level xfails (full segment_text)

    @pytest.mark.xfail(reason="4-space indent + sentence ending on prior line causes double-period in post-processing")
    def test_pipeline_double_period_01(self):
        passage = "He was right.\n    She was wrong."
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert ".." not in full_text

    @pytest.mark.xfail(reason="Very long single line followed by 4-space wrap confuses spaCy tokenizer")
    def test_pipeline_very_long_line_01(self):
        long_line = "a " * 200 + "business"
        passage = f"{long_line}\n    department."
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "business.department" not in full_text

    @pytest.mark.xfail(reason="All-caps word at wrap creates false sentence boundary in spaCy")
    def test_pipeline_allcaps_at_wrap_01(self):
        passage = "The BUSINESS\n    department issued a notice."
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "BUSINESS.department" not in full_text

    @pytest.mark.xfail(reason="Wrap after exclamation brand name (e.g. Yahoo!) confuses ExclamationBrandNormalizer")
    def test_pipeline_exclamation_brand_at_wrap_01(self):
        passage = "He worked at Yahoo!\n    as a software engineer."
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "Yahoo!.as" not in full_text

    @pytest.mark.xfail(reason="Wrap after bracket citation confuses BracketContentNormalizer")
    def test_pipeline_bracket_citation_at_wrap_01(self):
        passage = "As noted [Smith, 2020]\n    the effect was significant."
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "[Smith, 2020].the" not in full_text

    @pytest.mark.xfail(reason="Wrap after URL placeholder — URL normalizer may not restore correctly")
    def test_pipeline_url_at_wrap_01(self):
        passage = "See https://example.com\n    for more details."
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "example.com.for" not in full_text

    @pytest.mark.xfail(reason="Wrap after middle initial — MiddleInitialNormalizer may not protect across wrap")
    def test_pipeline_middle_initial_at_wrap_01(self):
        passage = "Albert I.\n    Jones joined the firm."
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert len(result) == 1

    @pytest.mark.xfail(reason="Deeply nested parenthetical at wrap — ParentheticalMerger may fail")
    def test_pipeline_nested_paren_at_wrap_01(self):
        passage = "He teaches (formerly worked\n    as engineer) at university."
        result = segment_text(passage, flatten=True)
        assert len(result) == 1

    @pytest.mark.xfail(reason="Leading ellipsis on continuation line — LeadingEllipsisMerger may produce artifact")
    def test_pipeline_leading_ellipsis_continuation_01(self):
        passage = "He paused...\n    then continued speaking."
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "....then" not in full_text

    @pytest.mark.xfail(reason="Wrap splits an APA citation across lines — CitationNormalizer may not protect")
    def test_pipeline_citation_at_wrap_01(self):
        passage = "Research confirms this (Smith,\n    2020, p. 42)."
        result = segment_text(passage, flatten=True)
        assert len(result) == 1

    @pytest.mark.xfail(reason="Wrap immediately after opening quote — QuoteAttributionMerger confusion")
    def test_pipeline_open_quote_at_wrap_01(self):
        passage = '"She said\n    "I will not go."'
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "said.she" not in full_text.lower()

    @pytest.mark.xfail(reason="Gutenberg chapter header wrap — ALL CAPS + wrap + 4-space triggers false boundary")
    def test_pipeline_chapter_header_wrap_01(self):
        passage = "CHAPTER I\n\n    It was a dark and stormy night."
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "I.It" not in full_text

    @pytest.mark.xfail(reason="Wrap at en-dash — not handled by dehyphenator")
    def test_pipeline_endash_at_wrap_01(self):
        passage = "He walked — slowly —\n    towards the door."
        result = segment_text(passage, flatten=True)
        assert len(result) == 1

    @pytest.mark.xfail(reason="Wrap before quoted capital letter — looks like sentence boundary")
    def test_pipeline_capital_after_wrap_and_quote_01(self):
        passage = 'She said "The\n    Business department is closed."'
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "The.Business" not in full_text

    @pytest.mark.xfail(reason="Three-line wrap with 4-space indent then period then capital — multiple interactions")
    def test_pipeline_three_line_capital_wrap_01(self):
        passage = (
            "He graduated from the business\n"
            "    school in 1920.\n"
            "    After that he found work."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "business.school" not in full_text

    @pytest.mark.xfail(reason="Roman numeral chapter heading followed by 4-space indent body text")
    def test_pipeline_roman_numeral_chapter_01(self):
        passage = "IV.\n\n    The next morning brought rain."
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "IV.The" not in full_text
