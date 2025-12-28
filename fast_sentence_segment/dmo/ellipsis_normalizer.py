#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Normalize Ellipses to prevent them being stripped by cleanup routines """


import re

from fast_sentence_segment.core import BaseObject


PLACEHOLDER = "〈ELLIPSIS〉"

# Pattern: ... followed by space and capital letter
BOUNDARY_PATTERN = re.compile(r'\.\.\.(\s+)([A-Z])')


class EllipsisNormalizer(BaseObject):
    """ Normalize Ellipses to prevent them being stripped by cleanup routines """

    def __init__(self):
        """
        Created:
            27-Dec-2024
            craigtrim@gmail.com
            *   preserve ellipses through the pipeline
                https://github.com/craigtrim/fast-sentence-segment/issues/3
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                input_text: str,
                denormalize: bool = False) -> str:

        if not denormalize:
            # "... [Capital]" → "〈ELLIPSIS〉. [Capital]" (adds period for spaCy to split)
            input_text = BOUNDARY_PATTERN.sub(PLACEHOLDER + r'.\1\2', input_text)
            # Remaining ellipses (mid-sentence): "..." → "〈ELLIPSIS〉"
            input_text = input_text.replace("...", PLACEHOLDER)
        else:
            # "〈ELLIPSIS〉." → "..." (remove extra period added for boundary)
            input_text = input_text.replace(PLACEHOLDER + ".", "...")
            # Remaining placeholders: "〈ELLIPSIS〉" → "..."
            input_text = input_text.replace(PLACEHOLDER, "...")

        return input_text
