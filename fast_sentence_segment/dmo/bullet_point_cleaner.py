#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Prevent Bullet Points from Triggering False Positive Segmentation """


from baseblock import BaseObject


class BulletPointCleaner(BaseObject):
    """ Prevent Bullet Points from Triggering False Positive Segmentation """

    def __init__(self):
        """
        Created:
            30-Sept-2021
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
        if "  " in input_text:
            input_text = input_text.replace("  ", " ")

        # the replacement routine above leaves double '..' in the text
        # this replacement will solve that
        while ".." in input_text:
            input_text = input_text.replace("..", ".")

        while ". . " in input_text:
            input_text = input_text.replace(". . ", ".")

        return input_text
