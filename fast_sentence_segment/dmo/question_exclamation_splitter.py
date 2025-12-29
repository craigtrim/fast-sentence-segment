#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Split sentences at ? and ! followed by capital letter """


import re
from typing import List

from fast_sentence_segment.core import BaseObject


# Pattern: ? or ! followed by space and capital letter
BOUNDARY_PATTERN = re.compile(r'([?!])(\s+)([A-Z])')


class QuestionExclamationSplitter(BaseObject):
    """ Split sentences at ? and ! followed by capital letter """

    def __init__(self):
        """
        Created:
            27-Dec-2024
            craigtrim@gmail.com
            *   spaCy doesn't always split on ? and ! boundaries
                https://github.com/craigtrim/fast-sentence-segment/issues/3
        """
        BaseObject.__init__(self, __name__)

    def process(self, sentences: List[str]) -> List[str]:
        """Split sentences that contain ? or ! followed by capital letter.

        Args:
            sentences: List of sentences from earlier processing

        Returns:
            List of sentences with ? and ! boundaries split
        """
        result = []
        for sent in sentences:
            # Split on pattern, keeping the punctuation with the first part
            parts = BOUNDARY_PATTERN.split(sent)
            if len(parts) == 1:
                result.append(sent)
            else:
                # Reassemble: parts = [before, punct, space, capital, after, ...]
                i = 0
                while i < len(parts):
                    if i + 3 < len(parts):
                        # before + punct
                        result.append(parts[i] + parts[i + 1])
                        # capital + rest will be handled in next iteration
                        parts[i + 4] = parts[i + 3] + parts[i + 4] if i + 4 < len(parts) else parts[i + 3]
                        i += 4
                    else:
                        if parts[i].strip():
                            result.append(parts[i])
                        i += 1

        return [s.strip() for s in result if s.strip()]
