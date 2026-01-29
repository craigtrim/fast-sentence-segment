# -*- coding: UTF-8 -*-
"""Strip spurious trailing periods appended after sentence-final closing quotes.

The spaCy segmenter's _append_period method can produce sentences like:
    'He said "Hello.".'   (spurious trailing period)
    'She asked "Why?".'   (spurious trailing period)
    'He yelled "Stop!".'  (spurious trailing period)

This post-processor removes the trailing period when the sentence ends
with a closing double quote preceded by terminal punctuation.

Related GitHub Issue:
    #7 - Spurious trailing period appended after sentence-final
         closing quote
    https://github.com/craigtrim/fast-sentence-segment/issues/7
"""

import re

from fast_sentence_segment.core import BaseObject

# Matches a sentence that ends with terminal punctuation (. ? !)
# followed by a closing double quote, followed by a spurious period.
# The fix strips the final period.
_SPURIOUS_PERIOD_PATTERN = re.compile(r'([.?!]")\.$')


class StripTrailingPeriodAfterQuote(BaseObject):
    """Strip spurious trailing periods after sentence-final closing quotes.

    Detects sentences ending with patterns like:
        ."."  ->  ."
        ?"."  ->  ?"
        !"."  ->  !"

    Applied as a post-processing step in the sentence segmentation
    pipeline, after spaCy segmentation and after the existing
    PostProcessStructure step.

    Related GitHub Issue:
        #7 - Spurious trailing period appended after sentence-final
             closing quote
        https://github.com/craigtrim/fast-sentence-segment/issues/7
    """

    def __init__(self):
        """
        Created:
            29-Jan-2026
        """
        BaseObject.__init__(self, __name__)

    def process(self, sentences: list) -> list:
        """Remove spurious trailing periods after closing quotes.

        Args:
            sentences: List of segmented sentences.

        Returns:
            List of sentences with spurious trailing periods removed.

        Example:
            >>> proc = StripTrailingPeriodAfterQuote()
            >>> proc.process(['He said "Hello.".', 'She waved.'])
            ['He said "Hello."', 'She waved.']
        """
        return [
            _SPURIOUS_PERIOD_PATTERN.sub(r'\1', sentence)
            for sentence in sentences
        ]
