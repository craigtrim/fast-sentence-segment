#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Normalize Numbered Lists to prevent False Positive Segmentation """


from fast_sentence_segment.core import BaseObject


class NumberedListNormalizer(BaseObject):
    """ Normalize Numbered Lists to prevent False Positive Segmentation """

    __d_candidate_list_elements = {
        "1. ": "1_ ",
        "2. ": "2_ ",
        "3. ": "3_ ",
        "4. ": "4_ ",
        "5. ": "5_ ",
        "6. ": "6_ ",
        "7. ": "7_ ",
        "8. ": "8_ ",
        "9. ": "9_ ",
        "10. ": "10_ ",
    }

    def __init__(self):
        """
        Created:
            19-Oct-2022
            craigtrim@gmail.com
            *   https://github.com/craigtrim/fast-sentence-segment/issues/1
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                input_text: str,
                denormalize: bool = False) -> str:

        if not denormalize:
            for candidate in self.__d_candidate_list_elements:
                if candidate in input_text:
                    input_text = input_text.replace(
                        candidate, self.__d_candidate_list_elements[candidate])

        else:  # reverse the process
            d_rev = {self.__d_candidate_list_elements[k]: k
                     for k in self.__d_candidate_list_elements}

            for candidate in d_rev:
                if candidate in input_text:
                    input_text = input_text.replace(
                        candidate, d_rev[candidate])

        return input_text
