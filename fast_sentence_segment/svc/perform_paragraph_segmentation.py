#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Paragraph Segmentation """


from fast_sentence_segment.core import BaseObject


class PerformParagraphSegmentation(BaseObject):
    """ Paragraph Segmentation """

    def __init__(self):
        """
        Created:
            1-Oct-2021
        """
        BaseObject.__init__(self, __name__)

    def _process(self,
                 input_text: str) -> list:
        paragraphs = input_text.split('\n\n')

        paragraphs = [x.strip() for x in paragraphs if x]
        paragraphs = [x for x in paragraphs if len(x)]

        return paragraphs

    def process(self,
                input_text: str) -> list:
        """Perform Paragraph Segmentation

        Args:
            input_text (str): An input string of any length or type

        Raises:
            ValueError: input must be a string

        Returns:
            list:   a list of 1..* paragraphs
                    each list item is an input string of any length, but is a paragraph
                    A paragraph is a structural concept rather than a semantic one
        """
        if input_text is None or not len(input_text):
            raise ValueError("Empty Input")

        if not isinstance(input_text, str):
            self.logger.warning(f"Invalid Input Text: {input_text}")
            return []

        return self._process(input_text)
