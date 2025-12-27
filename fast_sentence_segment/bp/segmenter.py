#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Orchestrate Sentence Segmentation """


from functools import lru_cache

from fast_sentence_segment.core import BaseObject, Stopwatch
from fast_sentence_segment.svc import PerformParagraphSegmentation
from fast_sentence_segment.svc import PerformSentenceSegmentation


class Segmenter(BaseObject):
    """ Orchestrate Sentence Segmentation """

    def __init__(self):
        """ Change Log

        Created:
            30-Sept-2021
        """
        BaseObject.__init__(self, __name__)
        self._segment_paragraphs = PerformParagraphSegmentation().process
        self._segment_sentences = PerformSentenceSegmentation().process

    def _input_text(self,
                    input_text: str) -> list:
        paragraphs = []

        for paragraph in self._segment_paragraphs(input_text):
            paragraphs.append(self._segment_sentences(paragraph))

        return paragraphs

    @lru_cache(maxsize=1024, typed=True)
    def input_text(self,
                   input_text: str) -> list:
        """Segment Input Text into Paragraphs and Sentences

        Args:
            input_text (str): An input string of any length or type

        Raises:
            ValueError: input must be a string

        Returns:
            list:   returns a list of lists.
                    Each outer list is a paragraph.
                    Each inner list contains 1..* sentences
        """

        if self.isEnabledForDebug and not isinstance(input_text, str):
            raise ValueError(f"Expected str, got {type(input_text)}")

        sw = Stopwatch()

        paragraphs = self._input_text(input_text)

        if self.isEnabledForInfo:
            self.logger.info('\n'.join([
                "Segmentation of Input Text Complete",
                f"\tTotal Paragraphs: {len(paragraphs)}",
                f"\tTotal Time: {str(sw)}"]))

        return paragraphs
