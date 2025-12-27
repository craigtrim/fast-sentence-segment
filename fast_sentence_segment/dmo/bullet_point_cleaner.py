#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Prevent Bullet Points from Triggering False Positive Segmentation """


from fast_sentence_segment.core import BaseObject


class BulletPointCleaner(BaseObject):
    """ Prevent Bullet Points from Triggering False Positive Segmentation """

    def __init__(self):
        """ Change Log

        Created:
            30-Sept-2021
            craigtrim@gmail.com
        Updated:
            19-Oct-2022
            craigtrim@gmail.com
            *   clean up for segment_text_3_test.py
        """
        BaseObject.__init__(self, __name__)

    @staticmethod
    def process(input_text: str) -> str:
        """
        Purpose:
            prevent numbered bullet points from triggering sentence detection
        :param input_text:
            any input text
        :return:
            preprocessed input text
        """
        if input_text.startswith("-"):
            input_text = input_text[1:]  # segment_text_3_test.py

        if "  " in input_text:
            input_text = input_text.replace("  ", " ")

        # the replacement routine above leaves double '..' in the text
        # this replacement will solve that
        while ".." in input_text:
            input_text = input_text.replace("..", ".")

        while ". -" in input_text:  # segment_text_3_test.py
            input_text = input_text.replace(". -", ". ")

        while ". . " in input_text:
            input_text = input_text.replace(". . ", ".")

        while '  ' in input_text:
            input_text = input_text.replace('  ', ' ')

        return input_text
