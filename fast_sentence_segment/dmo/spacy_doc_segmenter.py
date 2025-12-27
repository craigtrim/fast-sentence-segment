#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Run Sentence Segmentation using spaCy """


from spacy.lang.en import English


from fast_sentence_segment.core import BaseObject


class SpacyDocSegmenter(BaseObject):
    """ Run Sentence Segmentation using spaCy """

    def __init__(self,
                 nlp: English):
        """
        Created:
            30-Sept-2021
        """
        BaseObject.__init__(self, __name__)
        self._nlp = nlp

    @staticmethod
    def _append_period(a_sentence: str) -> str:
        """
        Purpose:
            if the sentence is not terminated with a period, then add one
        :return:
            a sentence terminated by a period
        """
        __blacklist = [':', '?', '!']
        if not a_sentence.strip().endswith('.'):
            for ch in __blacklist:
                if not a_sentence.endswith(ch):
                    return f"{a_sentence}."
        return a_sentence

    @staticmethod
    def _is_valid_sentence(a_sentence: str) -> bool:
        """
        Purpose:
            enable filtering of invalid sentences
        :return:
            True        if the sentence is a valid one
        """
        if not a_sentence:
            return False
        if not len(a_sentence):
            return False
        if a_sentence.strip() == '.':
            return False
        return True

    @staticmethod
    def _cleanse(sentences: list) -> str:
        sentences = [sent for sent in sentences
                     if sent != '..']

        normalized = []

        for s in sentences:
            s = s.replace('\n', ' ')

            if s.startswith('.. '):
                s = s[3:]

            if s.endswith('.  ..'):
                s = s[:len(s) - 3].strip()

            normalized.append(s)

        return normalized

    def process(self,
                input_text: str) -> list:
        """
        Purpose:
            Perform Sentence Segmentation
        :param input_text:
            any input text
        :return:
            a list of 0-or-More sentences
        """

        doc = self._nlp(input_text)

        sentences = [str(sent) for sent in doc.sents]

        sentences = [sent for sent in sentences if
                     sent and len(sent) and sent != 'None']

        sentences = [self._append_period(sent)
                     for sent in sentences]

        sentences = [sent.strip() for sent in sentences
                     if self._is_valid_sentence(sent)]

        sentences = self._cleanse(sentences)

        return sentences
