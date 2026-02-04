#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Sentence Segmentation """


import subprocess
import sys

import spacy

from fast_sentence_segment.core import BaseObject


def _load_spacy_model(model_name: str = "en_core_web_sm"):
    """Load spaCy model, auto-downloading if not found."""
    # ANSI color codes
    bold = "\033[1m"
    cyan = "\033[36m"
    green = "\033[32m"
    yellow = "\033[33m"
    reset = "\033[0m"

    try:
        return spacy.load(model_name)
    except OSError:
        print(f"\n{bold}{cyan}fast-sentence-segment{reset}", file=sys.stderr)
        print(f"{'─' * 40}", file=sys.stderr)
        print(
            f"  {yellow}⚠{reset}  spaCy model '{model_name}' not found.",
            file=sys.stderr,
        )
        print(f"  {yellow}⏳{reset} Downloading model (one-time setup)...", file=sys.stderr)
        print(file=sys.stderr)

        subprocess.check_call(
            [sys.executable, "-m", "spacy", "download", model_name],
        )

        print(file=sys.stderr)
        print(f"  {green}✓{reset}  Model '{model_name}' installed successfully.", file=sys.stderr)
        print(f"  {green}✓{reset}  You won't see this message again.", file=sys.stderr)
        print(file=sys.stderr)

        return spacy.load(model_name)

# Imports after lazy spacy loading function (intentional)
from fast_sentence_segment.dmo import AbbreviationMerger  # noqa: E402
from fast_sentence_segment.dmo import AbbreviationSplitter  # noqa: E402
from fast_sentence_segment.dmo import QuoteAttributionMerger  # noqa: E402
from fast_sentence_segment.dmo import QuoteClosingSplitter  # noqa: E402
from fast_sentence_segment.dmo import UnclosedQuoteMerger  # noqa: E402
from fast_sentence_segment.dmo import EllipsisSentenceSplitter  # noqa: E402
from fast_sentence_segment.dmo import EllipsisSentenceMerger  # noqa: E402
from fast_sentence_segment.dmo import TitleNameMerger  # noqa: E402
from fast_sentence_segment.dmo import EllipsisNormalizer  # noqa: E402
from fast_sentence_segment.dmo import NewlinesToPeriods  # noqa: E402
from fast_sentence_segment.dmo import BulletPointCleaner  # noqa: E402
from fast_sentence_segment.dmo import NumberedListNormalizer  # noqa: E402
from fast_sentence_segment.dmo import QuestionExclamationSplitter  # noqa: E402
from fast_sentence_segment.dmo import SpacyDocSegmenter  # noqa: E402
from fast_sentence_segment.dmo import PostProcessStructure  # noqa: E402
from fast_sentence_segment.dmo import StripTrailingPeriodAfterQuote  # noqa: E402
from fast_sentence_segment.dmo import Dehyphenator  # noqa: E402
from fast_sentence_segment.dmo import OcrArtifactFixer
from fast_sentence_segment.dmo import ListItemSplitter  # noqa: E402
from fast_sentence_segment.dmo import ListMarkerNormalizer  # noqa: E402


class PerformSentenceSegmentation(BaseObject):
    """ Sentence Segmentation """

    __nlp = None

    def __init__(self):
        """ Change Log

        Created:
            30-Sept-2021
            craigtrim@gmail.com
        Updated:
            19-Oct-2022
            craigtrim@gmail.com
            *   add numbered-list normalization
                https://github.com/craigtrim/fast-sentence-segment/issues/1
        Updated:
            27-Dec-2024
            craigtrim@gmail.com
            *   add abbreviation-aware sentence splitting
                https://github.com/craigtrim/fast-sentence-segment/issues/3
        """
        BaseObject.__init__(self, __name__)
        if not self.__nlp:
            self.__nlp = _load_spacy_model("en_core_web_sm")

        self._dehyphenate = Dehyphenator.process
        self._fix_ocr_artifacts = OcrArtifactFixer.process
        self._newlines_to_periods = NewlinesToPeriods.process
        self._normalize_numbered_lists = NumberedListNormalizer().process
        self._normalize_ellipses = EllipsisNormalizer().process
        self._clean_bullet_points = BulletPointCleaner.process
        self._spacy_segmenter = SpacyDocSegmenter(self.__nlp).process
        self._abbreviation_merger = AbbreviationMerger().process
        self._quote_attribution_merger = QuoteAttributionMerger().process
        self._quote_closing_splitter = QuoteClosingSplitter().process
        self._unclosed_quote_merger = UnclosedQuoteMerger().process
        self._ellipsis_sentence_splitter = EllipsisSentenceSplitter().process
        self._ellipsis_sentence_merger = EllipsisSentenceMerger().process
        self._abbreviation_splitter = AbbreviationSplitter().process
        self._question_exclamation_splitter = QuestionExclamationSplitter().process
        self._title_name_merger = TitleNameMerger().process
        self._post_process = PostProcessStructure().process
        self._strip_trailing_period = StripTrailingPeriodAfterQuote().process
        self._list_item_splitter = ListItemSplitter().process
        self._normalize_list_markers = ListMarkerNormalizer().process

    def _denormalize(self, text: str) -> str:
        """ Restore normalized placeholders to original form """
        text = self._normalize_numbered_lists(text, denormalize=True)
        text = self._normalize_ellipses(text, denormalize=True)
        text = self._normalize_list_markers(text, denormalize=True)
        return text

    @staticmethod
    def _has_sentence_punct(text: str) -> bool:
        """ Check if text has sentence-ending punctuation or ellipsis placeholder """
        return "." in text or "?" in text or "!" in text or "xellipsisthreex" in text

    @staticmethod
    def _has_list_markers(text: str) -> bool:
        """Check if text contains inline list markers that should be split.

        Returns True if there are 2+ list markers, indicating an inline list.
        Also checks for list marker placeholders (listmarker...end).
        """
        import re
        # Check for list marker placeholders (from ListMarkerNormalizer)
        placeholder_count = len(re.findall(r'listmarker[a-z]+end', text))
        if placeholder_count >= 2:
            return True

        # Simple patterns for list markers
        # Note: Hyphen (-) is NOT included as it conflicts with phone numbers
        patterns = [
            r'\d{1,3}\.\)',      # 1.)
            r'\d{1,3}\)',        # 1)
            r'(?:^|\s)\d{1,3}\.(?=\s)',  # 1.
            r'(?:^|\s)[a-zA-Z]\.(?=\s)',  # a. or A.
            r'(?:^|\s)[a-zA-Z]\)(?=\s)',  # a) or A)
            r'[•⁃\*‣→☐☑]',    # bullets (no hyphen)
        ]
        count = 0
        for pat in patterns:
            count += len(re.findall(pat, text))
            if count >= 2:
                return True
        return False

    @staticmethod
    def _clean_punctuation(input_text: str) -> str:
        """ Purpose:
            Clean punctuation oddities; this is likely highly overfitted (for now)
        """
        if ", Inc" in input_text:
            input_text = input_text.replace(", Inc", " Inc")

        return input_text

    @staticmethod
    def _clean_spacing(a_sentence: str) -> str:

        # eliminate triple-space
        a_sentence = a_sentence.replace('   ', '  ')

        # treat double-space as delimiter
        a_sentence = a_sentence.replace('  ', '. ')

        return a_sentence

    def _process(self,
                 input_text: str) -> list:

        # Normalize tabs to spaces
        input_text = input_text.replace('\t', ' ')

        # Dehyphenate words split across lines (issue #8)
        # Must happen before newlines are converted to periods
        input_text = self._dehyphenate(input_text)

        # Fix common OCR artifacts (issue #9)
        input_text = self._fix_ocr_artifacts(input_text)

        # Protect inline list markers BEFORE other normalizers run (issue #18)
        # Must happen before NumberedListNormalizer which would partially normalize them
        input_text = self._normalize_list_markers(input_text)

        input_text = self._normalize_numbered_lists(input_text)
        input_text = self._normalize_ellipses(input_text)

        input_text = self._newlines_to_periods(input_text)

        input_text = self._clean_spacing(input_text)
        # Check if we need further processing (sentence punct or list markers)
        needs_processing = self._has_sentence_punct(input_text) or self._has_list_markers(input_text)
        if not needs_processing:
            return [self._denormalize(input_text)]

        input_text = self._clean_bullet_points(input_text)
        needs_processing = self._has_sentence_punct(input_text) or self._has_list_markers(input_text)
        if not needs_processing:
            return [self._denormalize(input_text)]

        input_text = self._clean_punctuation(input_text)
        needs_processing = self._has_sentence_punct(input_text) or self._has_list_markers(input_text)
        if not needs_processing:
            return [self._denormalize(input_text)]

        sentences = self._spacy_segmenter(input_text)

        # Merge sentences incorrectly split at ellipsis + lowercase
        # e.g., ['She saidxellipsisthreex', 'but she didn\\'t.'] -> ['She saidxellipsisthreex but she didn\\'t.']
        sentences = self._ellipsis_sentence_merger(sentences)

        # Merge sentences incorrectly split inside quotes (issue #20)
        # e.g., ['"First thing.', 'Second thing," she said.'] -> ['"First thing. Second thing," she said.']
        sentences = self._unclosed_quote_merger(sentences)

        # Merge sentences incorrectly split at abbreviations (issue #3)
        sentences = self._abbreviation_merger(sentences)

        # Merge sentences incorrectly split at quote attribution (issue #20)
        # e.g., ['"Are you sure?"', 'she asked.'] -> ['"Are you sure?" she asked.']
        sentences = self._quote_attribution_merger(sentences)

        # Merge title + single-word name splits (e.g., "Dr." + "Who?" -> "Dr. Who?")
        sentences = self._title_name_merger(sentences)

        # Split sentences at abbreviation boundaries (issue #3)
        sentences = self._abbreviation_splitter(sentences)

        # Split sentences at ? and ! boundaries (issue #3)
        sentences = self._question_exclamation_splitter(sentences)

        # Split sentences at quote closing + capital boundaries (issue #20)
        # e.g., ['"We should go." Dr. Smith suggested.'] -> ['"We should go."', 'Dr. Smith suggested.']
        sentences = self._quote_closing_splitter(sentences)

        # Split sentences at ellipsis + capital letter boundaries
        # e.g., ['I thoughtxellipsisthreex Never mind.'] -> ['I thoughtxellipsisthreex', 'Never mind.']
        sentences = self._ellipsis_sentence_splitter(sentences)

        # Restore list markers before splitting (issue #18)
        sentences = [
            self._normalize_list_markers(x, denormalize=True)
            for x in sentences
        ]

        # Split inline lists into individual items (issue #18)
        sentences = self._list_item_splitter(sentences)

        sentences = self._post_process(sentences)

        # Strip spurious trailing periods after closing quotes (issue #7)
        sentences = self._strip_trailing_period(sentences)

        sentences = [
            self._normalize_numbered_lists(x, denormalize=True)
            for x in sentences
        ]
        sentences = [
            self._normalize_ellipses(x, denormalize=True)
            for x in sentences
        ]

        return sentences

    def process(self,
                input_text: str) -> list:
        """Perform Sentence Segmentation

        Args:
            input_text (str): An input string of any length or type

        Raises:
            ValueError: input must be a string

        Returns:
            list:   a list of sentences
                    each list item is an input string of any length, but is a semantic sentence
        """

        if input_text is None or not len(input_text):
            raise ValueError("Empty Input")

        if not isinstance(input_text, str):
            self.logger.warning(f"Invalid Input Text: {input_text}")
            return []

        return self._process(input_text)
