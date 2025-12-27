#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Post Process Sentences """


from fast_sentence_segment.core import BaseObject


class PostProcessStructure(BaseObject):
    """ Post Process Sentences """

    __replace = {
        '..': '. ',
        '. .': '. ',

        ',.': ', ',
        ', .': ', ',

        '!.': '! ',
        '! .': '! ',

        '?.': '? ',
        '? .': '? ',

        ':.': ': ',
        ': .': ': ',
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
