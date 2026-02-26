#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Post Process Sentences """


import re

from fast_sentence_segment.core import BaseObject

# Matches exactly two consecutive periods that are NOT part of a longer
# ellipsis sequence (three or more periods).  Uses negative lookbehind and
# lookahead to exclude "..." and "....".
#
# Examples that match (and get cleaned):  "Hello.."  "Main St.."  "Hello..World"
# Examples that do NOT match:             "Hello..."  "...."
_DOUBLE_PERIOD_RE = re.compile(r'(?<!\.)\.\.(?!\.)')


class PostProcessStructure(BaseObject):
    """ Post Process Sentences """

    __replace = {
        # Normalize ".." followed by a space (mid-sentence artifact).
        '.. ': '. ',
        '. .': '. ',

        ',.': ', ',
        ', .': ', ',

        '!.': '! ',
        '! .': '! ',

        '?.': '? ',
        '? .': '? ',

        ':.': ': ',
        ': .': ': ',

        # Strip phantom periods inserted by NewlinesToPeriods for semicolons.
        # When `;\n` is converted to `; . ` so spaCy detects the sentence
        # boundary, the first split sentence ends with `; .` which must be
        # cleaned back to `; ` (then stripped to `;`).
        # Related: https://github.com/craigtrim/fast-sentence-segment/issues/39
        ';.': '; ',
        '; .': '; ',
    }

    def __init__(self):
        """
        Created:
            1-Oct-2021
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                sentences: list) -> list:
        normalized = []

        for sentence in sentences:

            for k in self.__replace:
                if k in sentence:
                    sentence = sentence.replace(k, self.__replace[k]).strip()

            # Clean up isolated double-period (not part of an ellipsis).
            # "Hello world.." → "Hello world."
            # "Hello..World"  → "Hello. World"
            if '..' in sentence:
                sentence = _DOUBLE_PERIOD_RE.sub('. ', sentence).strip()

            normalized.append(sentence)

        return normalized
