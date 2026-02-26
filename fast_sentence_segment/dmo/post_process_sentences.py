#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Post Process Sentences """


from fast_sentence_segment.core import BaseObject


class PostProcessStructure(BaseObject):
    """ Post Process Sentences """

    __replace = {
        # Only normalize double-period when followed by a space (mid-sentence
        # artifact from _clean_spacing).  A trailing ".." at sentence end
        # (e.g. "Main St..") is preserved so tests that supply it get it back.
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

            normalized.append(sentence)

        return normalized
