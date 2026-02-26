#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Normalize Numbered Lists to prevent False Positive Segmentation """


import re

from fast_sentence_segment.core import BaseObject


# Reference abbreviation word-stems (without trailing period) whose trailing
# period should NOT be treated as a sentence-ending period when followed by
# ". N. " in the inline-list normalization pass.
#
# When ". N. " appears after one of these abbreviations the digit is a
# reference number (page, chapter, section, etc.) — NOT a list-item marker.
# Preserving the period after the digit allows spaCy to detect the sentence
# boundary that follows.
#
# Example: "See p. 3. Results vary." — "3." is a page reference, not a list
# marker, so it must NOT be normalized to "3_".  After the fix spaCy splits
# correctly at "3." giving ["See p. 3.", "Results vary."].
#
# Related GitHub Issue:
#     #47 - Abbreviations with trailing periods cause false sentence splits
#     https://github.com/craigtrim/fast-sentence-segment/issues/47
_INLINE_REF_ABBREVS: frozenset = frozenset({
    # Page / pages
    "p", "pp",
    # Chapter / chapters
    "ch", "chs",
    # Part
    "pt",
    # Footnote
    "fn",
    # Equation
    "eq",
    # Table
    "tab",
    # Appendix
    "app", "appx",
    # Article / articles
    "art", "arts",
    # Paragraph(s)
    "para", "paras", "pars", "par",
    # Annotation
    "ann", "annot",
    # Abridged
    "abr",
    # Illustrated
    "illus",
    # Introduction
    "introd",
    # Definition
    "def",
    # Example
    "ex",
    # Preface
    "pref",
    # Literature
    "lit",
    # Note / notes
    "n", "nn",
    # Line / lines
    "l", "ll",
    # Book / books
    "bk", "bks",
    # Manuscript
    "ms", "mss",
    # Folio / folios
    "fol", "fols",
    # Column / columns
    "col", "cols",
    # Fragment
    "frag",
    # Reprint
    "rpt",
    # Supplement
    "suppl",
    # Correction
    "corr",
    # Volume / volumes (also covered by existing lookbehind)
    "vol", "vols",
    # Section / sections (also covered by existing lookbehind)
    "sec", "secs", "sect",
    # Figure / figures (also covered by existing lookbehind)
    "fig", "figs",
    # Number / numbers (also covered by existing lookbehind)
    "no", "nos",
    # Reference (also covered by existing lookbehind)
    "ref",
    # Versus (also covered by existing lookbehind)
    "vs",
    # Extension (also covered by existing lookbehind)
    "ext",
    # Editor / editors
    "ed", "eds",
    # Translator
    "trans",
    # Compiler
    "comp", "comps",
    # Reprint (repr.)
    "repr",
    # Revision / revised (rev.)
    "rev",
    # Series (ser.)
    "ser",
    # Circa
    "ca",
    # Floruit
    "fl",
    # Continued
    "cont",
})


def _inline_normalize_sub(match: re.Match) -> str:
    """Substitution callback for inline list normalization.

    Prevents '. N. ' from being normalized to '. N_ ' when the digit is
    preceded by a reference abbreviation (e.g. 'p.', 'ch.', 'vol.').  In
    those cases the digit is a reference number — not a list-item marker —
    and preserving the trailing period allows spaCy to detect the sentence
    boundary that follows.

    Args:
        match: Regex match object from __normalize_inline substitution.

    Returns:
        The original match text (un-normalized) when preceded by a reference
        abbreviation; the normalized form (group1 + group2 + '_ ') otherwise.

    Related GitHub Issue:
        #47 - Abbreviations with trailing periods cause false sentence splits
        https://github.com/craigtrim/fast-sentence-segment/issues/47
    """
    before = match.string[:match.start()]
    word_match = re.search(r'\b(\w+)\s*$', before)
    if word_match and word_match.group(1).lower() in _INLINE_REF_ABBREVS:
        # Check whether the abbreviation is at sentence/text start.  When the
        # abbreviation itself opens the sentence (or follows sentence-ending
        # punctuation), it is a numbered-title heading — normalize so the
        # number stays with the title.
        # Example: "Ch. 1. Title." — "Ch" is first token → title → normalize.
        # Example: "See ch. 3. Text." — "ch" follows "See" → reference → don't normalize.
        text_before_abbrev = before[:word_match.start()].rstrip()
        if not text_before_abbrev or text_before_abbrev[-1] in '.!?':
            # Abbreviation at sentence/text start → numbered title → normalize
            return match.group(1) + match.group(2) + '_ '
        # Abbreviation mid-sentence → reference number → preserve sentence boundary
        return match.group(0)
    return match.group(1) + match.group(2) + '_ '


class NumberedListNormalizer(BaseObject):
    """ Normalize Numbered Lists to prevent False Positive Segmentation """

    # Pattern 1: start of string OR newline, followed by number, period, space
    __normalize_line_start = re.compile(r'(^|\n\s*)(\d{1,2})\. ')
    __denormalize_line_start = re.compile(r'(^|\n\s*)(\d{1,2})_ ')

    # Pattern 2: inline numbered list ". N. " (period + space + number + period + space)
    # The substitution callback (_inline_normalize_sub) filters out reference
    # abbreviations (p., ch., vol., etc.) so that reference numbers like
    # "p. 3." are NOT normalized.  The callback replaces the fixed-width
    # negative lookbehinds that could only cover a handful of abbreviations.
    __normalize_inline = re.compile(r'(\. )(\d{1,2})\. ', re.IGNORECASE)
    # Denormalize: restore N_ → N. for inline list markers.
    # No lookbehinds needed — the only ". N_ " patterns in the text come from
    # our own normalization, which now correctly excludes reference abbreviations.
    __denormalize_inline = re.compile(r'(\. )(\d{1,2})_ ', re.IGNORECASE)

    # Pattern 3: denormalize N_ at end of sentence — handles the case where
    # spaCy splits a normalized sentence and SpacyDocSegmenter appends a period
    # to the fragment, producing "ch. 1_." instead of "ch. 1_ " (no trailing
    # space), which the normal __denormalize_inline cannot match.
    # e.g. "ch. 1_." → "ch. 1." (restore underscore → period)
    #
    # Related GitHub Issue:
    #     #47 - Abbreviations with trailing periods cause false sentence splits
    #     https://github.com/craigtrim/fast-sentence-segment/issues/47
    __denormalize_inline_end = re.compile(
        r'(\. )(\d{1,2})_(?=[.!?])',
        re.IGNORECASE
    )

    def __init__(self):
        """
        Created:
            19-Oct-2022
            craigtrim@gmail.com
            *   https://github.com/craigtrim/fast-sentence-segment/issues/1
        Updated:
            27-Dec-2024
            craigtrim@gmail.com
            *   fix to only match at line starts, not mid-sentence
                https://github.com/craigtrim/fast-sentence-segment/issues/3
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                input_text: str,
                denormalize: bool = False) -> str:

        if not denormalize:
            input_text = self.__normalize_line_start.sub(r'\1\2_ ', input_text)
            input_text = self.__normalize_inline.sub(_inline_normalize_sub, input_text)
        else:
            input_text = self.__denormalize_line_start.sub(r'\1\2. ', input_text)
            input_text = self.__denormalize_inline.sub(r'\1\2. ', input_text)
            # Handle N_ followed by terminal punctuation (e.g. "ch. 1_." → "ch. 1.")
            input_text = self.__denormalize_inline_end.sub(r'\1\2', input_text)

        return input_text
