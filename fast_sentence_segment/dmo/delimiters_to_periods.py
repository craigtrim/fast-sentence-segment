#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Convert Delimiters into Periods """


from fast_sentence_segment.core import BaseObject


class DelimitersToPeriods(BaseObject):
    """ Convert Delimiters into Periods """

    def __init__(self):
        """
        Created:
            30-Sept-2021
        """
        BaseObject.__init__(self, __name__)

    @staticmethod
    def process(input_text: str,
                delimiter: str):
        """
        Purpose:
            Take a CSV list and transform to sentences
        :param input_text:
        :return:
        """
        total_len = len(input_text)
        total_delims = input_text.count(delimiter)

        if total_delims == 0:
            return input_text

        if total_delims / total_len > 0.04:
            return input_text.replace(delimiter, '.')

        return input_text
