#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Prevent Bullet Points from Triggering False Positive Segmentation """

import re

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

        # Strip double-period artifacts.  _clean_spacing() converts double-
        # spaces to ". " which can create ".." sequences in the output
        # (e.g., "abbrev.  next" → "abbrev.. next").  Strip ".." ONLY when
        # it is followed by at least one more character — this preserves a
        # deliberate trailing ".." at the very end of the string (e.g.,
        # "Main St..") which appears in scholarly and abbreviation contexts.
        while re.search(r'\.\.(?=.)', input_text):
            input_text = re.sub(r'\.\.(?=.)', '.', input_text)

        while ". -" in input_text:  # segment_text_3_test.py
            input_text = input_text.replace(". -", ". ")

        while ". . " in input_text:
            input_text = input_text.replace(". . ", ".")

        while '  ' in input_text:
            input_text = input_text.replace('  ', ' ')

        return input_text
