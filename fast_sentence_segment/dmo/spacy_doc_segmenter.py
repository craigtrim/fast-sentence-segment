#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Run Sentence Segmentation using spaCy """


from spacy.lang.en import English


from fast_sentence_segment.core import BaseObject


class SpacyDocSegmenter(BaseObject):
    """ Run Sentence Segmentation using spaCy """

    def __init__(self,
                 nlp: English):
        """
        Created:
            30-Sept-2021
        """
        BaseObject.__init__(self, __name__)
        self._nlp = nlp

    @staticmethod
    def _append_period(a_sentence: str) -> str:
        """Append a period if the sentence lacks terminal punctuation.

        Checks for terminal punctuation (. ? ! :) after stripping any
        trailing quote characters (" '). This prevents a spurious period
        from being appended to sentences like:
            'He said "Hello."'  ->  unchanged (not 'He said "Hello.".')

        Also recognizes ANY ellipsis placeholder (not just at the end) as
        terminal punctuation to avoid appending a period. This handles cases
        like 'I was thinking... maybe not' where the ellipsis is mid-sentence.

        Also recognizes URL placeholders to avoid appending a period. URLs at
        the end of sentences should not have periods appended (Issue #32).

        Also recognizes numbered title patterns (Part 2., Chapter 5., etc.) that
        end with closing delimiters like ) or ] - these are complete sentences
        and should not have periods appended (Issue #30).

        Related GitHub Issues:
            #7 - Spurious trailing period appended after sentence-final
                 closing quote
            https://github.com/craigtrim/fast-sentence-segment/issues/7

            #23 - Trailing period added to sentences containing ellipsis
            https://github.com/craigtrim/fast-sentence-segment/issues/23

            #30 - Incorrect sentence break on numbered titles
            https://github.com/craigtrim/fast-sentence-segment/issues/30

            #32 - URLs incorrectly get periods appended at end
            https://github.com/craigtrim/fast-sentence-segment/issues/32

        Args:
            a_sentence: A sentence that may or may not have terminal
                punctuation.

        Returns:
            The sentence with a period appended if it lacked terminal
            punctuation, otherwise unchanged.
        """
        # Strip trailing quotes to inspect the actual punctuation
        stripped = a_sentence.strip().rstrip('"\'')
        if stripped and stripped[-1] in '.?!:':
            return a_sentence
        # Don't append period if sentence contains any ellipsis placeholder
        # (xellipsisthreex, xellipsisfourx, xellipsisthreespacedx, etc.)
        # These indicate the user's original text had ellipsis, which serves as
        # terminal punctuation or indicates trailing thought (Issue #23)
        # Reference: https://github.com/craigtrim/fast-sentence-segment/issues/23
        if 'xellipsis' in a_sentence:
            return a_sentence
        # Don't append period if sentence ends with URL placeholder
        # (xurl1x, xurl2x, etc.)
        # URLs at sentence boundaries should not have periods appended (Issue #32)
        # Reference: https://github.com/craigtrim/fast-sentence-segment/issues/32
        import re
        if re.search(r'xurl\d+x\s*$', stripped):
            return a_sentence
        # Don't append period if sentence contains numbered title pattern and ends with ) or ]
        # Examples: "Part 2. (May 6, 2008)", "Chapter 5. [Video File]"
        # These are complete sentences that just happen to end with metadata (Issue #30)
        # Reference: https://github.com/craigtrim/fast-sentence-segment/issues/30
        if stripped and stripped[-1] in ')]}>':
            # Check if sentence contains a numbered title pattern
            # Pattern: (Part|Chapter|Module|Section|Week|Step|Phase|Unit|Level|Stage) N.
            numbered_title_pattern = r'\b(Part|Chapter|Module|Section|Week|Step|Phase|Unit|Level|Stage)\s+(\d+|[IVXLCDMivxlcdm]+|[A-Za-z])\.'
            if re.search(numbered_title_pattern, a_sentence, re.IGNORECASE):
                return a_sentence
        # Don't append period if sentence starts with metadata delimiter
        # Examples: "[Video File]", "(May 6, 2008)", "<tag>", "{data}"
        # These are often metadata fragments that will be merged with numbered titles
        # Reference: https://github.com/craigtrim/fast-sentence-segment/issues/30
        if stripped and stripped[0] in '([{<':
            return a_sentence
        return f"{a_sentence}."

    @staticmethod
    def _is_valid_sentence(a_sentence: str) -> bool:
        """
        Purpose:
            enable filtering of invalid sentences
        :return:
            True        if the sentence is a valid one
        """
        if not a_sentence:
            return False
        if not len(a_sentence):
            return False
        if a_sentence.strip() == '.':
            return False
        return True

    @staticmethod
    def _merge_orphaned_quotes(sentences: list) -> list:
        """Merge orphaned opening quotes with the following sentence.

        spaCy sometimes splits on opening quotes, producing sentences like:
            ["'", "Oh, the funeral..."]
        This merges them into:
            ["'Oh, the funeral..."]

        Also handles trailing orphaned quotes that should belong to next sentence:
            ["He said. '", "Hello!'"]
        Becomes:
            ["He said.", "'Hello!'"]
        """
        if not sentences:
            return sentences

        result = []
        i = 0
        while i < len(sentences):
            sent = sentences[i]
            # Check if this sentence is just an opening quote
            if sent.strip() in ("'", '"', "'.", '".'):
                # Merge with the next sentence if available
                if i + 1 < len(sentences):
                    quote_char = sent.strip().rstrip('.')
                    result.append(quote_char + sentences[i + 1])
                    i += 2
                    continue
            result.append(sent)
            i += 1

        # Second pass: handle trailing orphaned quotes
        # Pattern: sentence ends with `. '` or `. "` - move quote to next sentence
        fixed = []
        for i, sent in enumerate(result):
            # Check for trailing orphaned quote (`. '` or `? '` or `! '`)
            if len(sent) >= 3 and sent[-2:] in (" '", ' "') and sent[-3] in '.?!':
                # Strip the trailing quote
                trailing_quote = sent[-1]
                sent = sent[:-2]
                # Prepend to next sentence if available
                if i + 1 < len(result) and not result[i + 1].startswith(('"', "'")):
                    result[i + 1] = trailing_quote + result[i + 1]
            fixed.append(sent)

        return fixed

    @staticmethod
    def _cleanse(sentences: list) -> str:
        sentences = [sent for sent in sentences
                     if sent != '..']

        normalized = []

        for s in sentences:
            s = s.replace('\n', ' ')

            if s.startswith('.. '):
                s = s[3:]

            if s.endswith('.  ..'):
                s = s[:len(s) - 3].strip()

            normalized.append(s)

        return normalized

    def process(self,
                input_text: str) -> list:
        """
        Purpose:
            Perform Sentence Segmentation
        :param input_text:
            any input text
        :return:
            a list of 0-or-More sentences
        """

        doc = self._nlp(input_text)

        sentences = [str(sent) for sent in doc.sents]

        sentences = [sent for sent in sentences if
                     sent and len(sent) and sent != 'None']

        # Merge orphaned opening quotes with following sentence
        sentences = self._merge_orphaned_quotes(sentences)

        sentences = [self._append_period(sent)
                     for sent in sentences]

        sentences = [sent.strip() for sent in sentences
                     if self._is_valid_sentence(sent)]

        sentences = self._cleanse(sentences)

        return sentences
