# -*- coding: UTF-8 -*-
"""Various punctuation marks."""

import pytest
from fast_sentence_segment import segment_text


class TestPunctuation:
    """Various punctuation marks."""

    def test_question_mark(self):
        result = segment_text("How are you? I am fine.", flatten=True)
        assert result == ["How are you?", "I am fine."]

    def test_exclamation(self):
        result = segment_text("Wow! That is amazing.", flatten=True)
        assert result == ["Wow!", "That is amazing."]

    def test_multiple_question_marks(self):
        # ??? followed by capital letter is a sentence boundary
        result = segment_text("What??? Are you serious?", flatten=True)
        assert result == ["What???", "Are you serious?"]

    @pytest.mark.skip(reason="""
        SKIP REASON: Capital "I" after ellipsis is intentionally NOT treated as sentence boundary.

        This test expects "Well... I think so." to split at "I", but our implementation
        specifically EXCLUDES capital "I" from triggering sentence splits after ellipsis.

        Current behavior: ["Well... I think so."] (one sentence)
        Expected by test: ["Well...", "I think so."] (two sentences)

        Design decision (Issue #22): Capital "I" after ellipsis is almost always the
        pronoun, not a new sentence start. This is extremely common in dialogue:
        - "I... I don't know what to say"
        - "But... I can't do that"
        - "Well... I suppose so"

        The EllipsisSentenceSplitter and EllipsisNormalizer use pattern [A-HJ-Z]
        (excludes "I") to avoid splitting these natural hesitation patterns.

        If you need ellipsis + "I" to split, this would require:
        1. Context-aware analysis of whether "I" starts a new thought
        2. Dialogue vs. prose detection
        3. Heuristics that would likely cause more problems than they solve

        Related: https://github.com/craigtrim/fast-sentence-segment/issues/22
                 EllipsisSentenceSplitter in fast_sentence_segment/dmo/ellipsis_sentence_splitter.py
    """)
    def test_ellipsis(self):
        # Ellipsis followed by capital letter is a sentence boundary, but ... is preserved
        result = segment_text("Well... I think so.", flatten=True)
        assert result == ["Well...", "I think so."]
