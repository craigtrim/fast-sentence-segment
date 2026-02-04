# -*- coding: UTF-8 -*-
"""Fix common OCR/text extraction artifacts.

Ebook text files often contain artifacts where common word pairs
are incorrectly joined. This module fixes known patterns.

Related GitHub Issues:
    #9 - Fix common OCR/cleaning artifacts (Iam, witha)
    https://github.com/craigtrim/fast-sentence-segment/issues/9
    #28 - Fix lowercase iam OCR artifact not being corrected
    https://github.com/craigtrim/fast-sentence-segment/issues/28
"""

from fast_sentence_segment.core import BaseObject

# Known OCR artifact patterns: (pattern, replacement)
# All patterns include surrounding spaces to ensure exact word boundaries
_OCR_ARTIFACTS = [
    (" Iam ", " I am "),
    (" iam ", " I am "),
    (" Ihave ", " I have "),
    (" ihave ", " I have "),
    (" Ithink ", " I think "),
    (" ithink ", " I think "),
    (" anda ", " and a "),
    (" witha ", " with a "),
    (" sucha ", " such a "),
    (" aliquid ", " a liquid "),
]


class OcrArtifactFixer(BaseObject):
    """Fix common OCR/text extraction artifacts.

    Detects and corrects known patterns where words are incorrectly
    joined during OCR or text extraction processes.

    Related GitHub Issue:
        #9 - Fix common OCR/cleaning artifacts (Iam, witha)
        https://github.com/craigtrim/fast-sentence-segment/issues/9
    """

    def __init__(self):
        """Change Log

        Created:
            3-Feb-2026
            craigtrim@gmail.com
            *   fix common OCR/cleaning artifacts
                https://github.com/craigtrim/fast-sentence-segment/issues/9
        Updated:
            4-Feb-2026
            craigtrim@gmail.com
            *   add lowercase 'iam' variant
                https://github.com/craigtrim/fast-sentence-segment/issues/28
        """
        BaseObject.__init__(self, __name__)

    @staticmethod
    def process(input_text: str) -> str:
        """Fix known OCR artifact patterns.

        Args:
            input_text: Text that may contain OCR artifacts.

        Returns:
            Text with known OCR artifacts corrected.

        Examples:
            >>> OcrArtifactFixer.process("Jack, Iam so happy")
            'Jack, I am so happy'
            >>> OcrArtifactFixer.process("horizon witha hint")
            'horizon with a hint'
        """
        for pattern, replacement in _OCR_ARTIFACTS:
            if pattern in input_text:
                input_text = input_text.replace(pattern, replacement)
        return input_text
