#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Normalize Numbered Lists to prevent False Positive Segmentation """


import re

from fast_sentence_segment.core import BaseObject


class NumberedListNormalizer(BaseObject):
    """ Normalize Numbered Lists to prevent False Positive Segmentation """

    # Pattern 1: start of string OR newline, followed by number, period, space
    __normalize_line_start = re.compile(r'(^|\n\s*)(\d{1,2})\. ')
    __denormalize_line_start = re.compile(r'(^|\n\s*)(\d{1,2})_ ')

    # Pattern 2: inline numbered list ". N. " (period + space + number + period + space)
    __normalize_inline = re.compile(r'(\. )(\d{1,2})\. ')
    __denormalize_inline = re.compile(r'(\. )(\d{1,2})_ ')

    def __init__(self):
        """
        Created:
            19-Oct-2022
            craigtrim@gmail.com
            *   https://github.com/craigtrim/fast-sentence-segment/issues/1
        Updated:
            27-Dec-2024
            craigtrim@gmail.com
            *   fix to only match at line starts, not mid-sentence
                https://github.com/craigtrim/fast-sentence-segment/issues/3
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                input_text: str,
                denormalize: bool = False) -> str:

        if not denormalize:
            input_text = self.__normalize_line_start.sub(r'\1\2_ ', input_text)
            input_text = self.__normalize_inline.sub(r'\1\2_ ', input_text)
        else:
            input_text = self.__denormalize_line_start.sub(r'\1\2. ', input_text)
            input_text = self.__denormalize_inline.sub(r'\1\2. ', input_text)

        return input_text
