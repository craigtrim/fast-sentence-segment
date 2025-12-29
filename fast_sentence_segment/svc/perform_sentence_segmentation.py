#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Sentence Segmentation """


import spacy

from fast_sentence_segment.core import BaseObject

from fast_sentence_segment.dmo import AbbreviationMerger
from fast_sentence_segment.dmo import AbbreviationSplitter
from fast_sentence_segment.dmo import TitleNameMerger
from fast_sentence_segment.dmo import EllipsisNormalizer
from fast_sentence_segment.dmo import NewlinesToPeriods
from fast_sentence_segment.dmo import BulletPointCleaner
from fast_sentence_segment.dmo import NumberedListNormalizer
from fast_sentence_segment.dmo import QuestionExclamationSplitter
from fast_sentence_segment.dmo import SpacyDocSegmenter
from fast_sentence_segment.dmo import PostProcessStructure


class PerformSentenceSegmentation(BaseObject):
    """ Sentence Segmentation """

    __nlp = None

    def __init__(self):
        """ Change Log

        Created:
            30-Sept-2021
            craigtrim@gmail.com
        Updated:
            19-Oct-2022
            craigtrim@gmail.com
            *   add numbered-list normalization
                https://github.com/craigtrim/fast-sentence-segment/issues/1
        Updated:
            27-Dec-2024
            craigtrim@gmail.com
            *   add abbreviation-aware sentence splitting
                https://github.com/craigtrim/fast-sentence-segment/issues/3
        """
        BaseObject.__init__(self, __name__)
        if not self.__nlp:
            self.__nlp = spacy.load("en_core_web_sm")

        self._newlines_to_periods = NewlinesToPeriods.process
        self._normalize_numbered_lists = NumberedListNormalizer().process
        self._normalize_ellipses = EllipsisNormalizer().process
        self._clean_bullet_points = BulletPointCleaner.process
        self._spacy_segmenter = SpacyDocSegmenter(self.__nlp).process
        self._abbreviation_merger = AbbreviationMerger().process
        self._abbreviation_splitter = AbbreviationSplitter().process
        self._question_exclamation_splitter = QuestionExclamationSplitter().process
        self._title_name_merger = TitleNameMerger().process
        self._post_process = PostProcessStructure().process

    def _denormalize(self, text: str) -> str:
        """ Restore normalized placeholders to original form """
        text = self._normalize_numbered_lists(text, denormalize=True)
        text = self._normalize_ellipses(text, denormalize=True)
        return text

    @staticmethod
    def _has_sentence_punct(text: str) -> bool:
        """ Check if text has sentence-ending punctuation """
        return "." in text or "?" in text or "!" in text

    @staticmethod
    def _clean_punctuation(input_text: str) -> str:
        """ Purpose:
            Clean punctuation oddities; this is likely highly overfitted (for now)
        """
        if ", Inc" in input_text:
            input_text = input_text.replace(", Inc", " Inc")

        return input_text

    @staticmethod
    def _clean_spacing(a_sentence: str) -> str:

        # eliminate triple-space
        a_sentence = a_sentence.replace('   ', '  ')

        # treat double-space as delimiter
        a_sentence = a_sentence.replace('  ', '. ')

        return a_sentence

    def _process(self,
                 input_text: str) -> list:

        # Normalize tabs to spaces
        input_text = input_text.replace('\t', ' ')

        input_text = self._normalize_numbered_lists(input_text)
        input_text = self._normalize_ellipses(input_text)

        input_text = self._newlines_to_periods(input_text)

        input_text = self._clean_spacing(input_text)
        if not self._has_sentence_punct(input_text):
            return [self._denormalize(input_text)]

        input_text = self._clean_bullet_points(input_text)
        if not self._has_sentence_punct(input_text):
            return [self._denormalize(input_text)]

        input_text = self._clean_punctuation(input_text)
        if not self._has_sentence_punct(input_text):
            return [self._denormalize(input_text)]

        sentences = self._spacy_segmenter(input_text)
        if not self._has_sentence_punct(input_text):
            return [self._denormalize(input_text)]

        # Merge sentences incorrectly split at abbreviations (issue #3)
        sentences = self._abbreviation_merger(sentences)

        # Merge title + single-word name splits (e.g., "Dr." + "Who?" -> "Dr. Who?")
        sentences = self._title_name_merger(sentences)

        # Split sentences at abbreviation boundaries (issue #3)
        sentences = self._abbreviation_splitter(sentences)

        # Split sentences at ? and ! boundaries (issue #3)
        sentences = self._question_exclamation_splitter(sentences)

        sentences = self._post_process(sentences)

        sentences = [
            self._normalize_numbered_lists(x, denormalize=True)
            for x in sentences
        ]
        sentences = [
            self._normalize_ellipses(x, denormalize=True)
            for x in sentences
        ]

        return sentences

    def process(self,
                input_text: str) -> list:
        """Perform Sentence Segmentation

        Args:
            input_text (str): An input string of any length or type

        Raises:
            ValueError: input must be a string

        Returns:
            list:   a list of sentences
                    each list item is an input string of any length, but is a semantic sentence
        """

        if input_text is None or not len(input_text):
            raise ValueError("Empty Input")

        if not isinstance(input_text, str):
            self.logger.warning(f"Invalid Input Text: {input_text}")
            return []

        return self._process(input_text)
