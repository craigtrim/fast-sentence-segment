#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Convert New Lines into Periods """


import re

from fast_sentence_segment.core import BaseObject


# Matches a clause-terminal punctuation character (semicolon or colon)
# optionally followed by horizontal whitespace, then a newline.
# These characters are NOT sentence-terminal on their own, so spaCy will
# not split there. We insert a phantom `. ` so the segmenter sees a hard
# sentence boundary.  The phantom period is cleaned up later in
# PostProcessStructure (which already strips `: .` and will strip `; .`).
#
# Related GitHub Issue:
#     #39 - Semicolon + newline incorrectly merges verse lines into single sentence
#     https://github.com/craigtrim/fast-sentence-segment/issues/39
_CLAUSE_TERMINAL_NEWLINE = re.compile(r'([;:])[ \t]*\n')


class NewlinesToPeriods(BaseObject):
    """ Convert New Lines into Periods """

    def __init__(self):
        """
        Created:
            30-Sept-2021
        """
        BaseObject.__init__(self, __name__)

    @staticmethod
    def process(input_text: str):
        """Convert newlines to spaces, inserting sentence boundaries where needed.

        When a newline is immediately preceded by clause-terminal punctuation
        (`;` or `:`), it is treated as a sentence boundary by inserting a
        phantom period (`. `).  The phantom period is cleaned up downstream by
        PostProcessStructure, which strips `; .` → `; ` and `; .` → `; `.

        For all other newlines the original behaviour is preserved: the
        newline is replaced with a plain space so hard-wrapped prose is
        rejoined into a single sentence.

        Args:
            input_text (str): Raw input text, possibly containing newlines.

        Returns:
            str: Text with newlines normalised for downstream segmentation.

        Related GitHub Issue:
            #39 - Semicolon + newline incorrectly merges verse lines
            https://github.com/craigtrim/fast-sentence-segment/issues/39
        """

        # Step 1: When `;` or `:` immediately precedes a newline, insert a
        # phantom period so spaCy recognises the sentence boundary.
        # `; \n` → `; . `   and   `: \n` → `: . `
        result = _CLAUSE_TERMINAL_NEWLINE.sub(r'\1. ', input_text)

        # Step 2: Replace all remaining newlines with a plain space so that
        # hard-wrapped prose is rejoined into a single sentence (original
        # behaviour, preserved from 20230309).
        result = result.replace('\n', ' ')

        return result
