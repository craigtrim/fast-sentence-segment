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
from fast_sentence_segment.dmo import NumberedTitleMerger  # noqa: E402
from fast_sentence_segment.dmo import EllipsisNormalizer  # noqa: E402
from fast_sentence_segment.dmo import NewlinesToPeriods  # noqa: E402
from fast_sentence_segment.dmo import BulletPointCleaner  # noqa: E402
from fast_sentence_segment.dmo import NumberedListNormalizer  # noqa: E402
from fast_sentence_segment.dmo import QuestionExclamationSplitter  # noqa: E402
from fast_sentence_segment.dmo import SpacyDocSegmenter  # noqa: E402
from fast_sentence_segment.dmo import PostProcessStructure  # noqa: E402
from fast_sentence_segment.dmo import StripTrailingPeriodAfterQuote  # noqa: E402
from fast_sentence_segment.dmo import Dehyphenator  # noqa: E402
from fast_sentence_segment.dmo import OcrArtifactFixer  # noqa: E402
from fast_sentence_segment.dmo import ListItemSplitter  # noqa: E402
from fast_sentence_segment.dmo import ListMarkerNormalizer  # noqa: E402
from fast_sentence_segment.dmo import ExclamationBrandNormalizer  # noqa: E402
from fast_sentence_segment.dmo import MiddleInitialNormalizer  # noqa: E402
from fast_sentence_segment.dmo import UnicodeTokenNormalizer  # noqa: E402
from fast_sentence_segment.dmo import ParentheticalMerger  # noqa: E402
from fast_sentence_segment.dmo import LeadingEllipsisMerger  # noqa: E402
from fast_sentence_segment.dmo import CitationNormalizer  # noqa: E402
from fast_sentence_segment.dmo import UrlNormalizer  # noqa: E402
from fast_sentence_segment.dmo import BracketContentNormalizer  # noqa: E402


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
        Updated:
            10-Feb-2026
            craigtrim@gmail.com
            *   add citation pattern detection for APA/MLA/informal citations
                prevents false sentence splits at citation boundaries
                https://github.com/craigtrim/fast-sentence-segment/issues/31
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
        self._numbered_title_merger = NumberedTitleMerger().process
        self._post_process = PostProcessStructure().process
        self._strip_trailing_period = StripTrailingPeriodAfterQuote().process
        self._list_item_splitter = ListItemSplitter().process
        self._normalize_list_markers = ListMarkerNormalizer().process
        # New normalizers for Golden Rules compliance (issues #25, #26, #27)
        self._normalize_exclamation_brands = ExclamationBrandNormalizer().process
        self._normalize_middle_initials = MiddleInitialNormalizer().process
        self._normalize_unicode_tokens = UnicodeTokenNormalizer().process
        # Parenthetical merger for Golden Rule 21
        self._parenthetical_merger = ParentheticalMerger().process
        # Leading ellipsis merger for Golden Rule 48
        self._leading_ellipsis_merger = LeadingEllipsisMerger().process
        # Citation normalizer for Issue #31 (APA/MLA citation handling)
        self._normalize_citations = CitationNormalizer().process
        # URL normalizer for issue #32
        self._normalize_urls = UrlNormalizer().process
        # Bracket content normalizer for Issue #37 (never split inside [...])
        self._normalize_brackets = BracketContentNormalizer().process

    def _denormalize(self, text: str) -> str:
        """ Restore normalized placeholders to original form """
        text = self._normalize_numbered_lists(text, denormalize=True)
        text = self._normalize_ellipses(text, denormalize=True)
        text = self._normalize_list_markers(text, denormalize=True)
        # Restore Golden Rules normalizers (issues #25, #26, #27)
        text = self._normalize_exclamation_brands(text, denormalize=True)
        text = self._normalize_middle_initials(text, denormalize=True)
        text = self._normalize_unicode_tokens(text, denormalize=True)
        # Restore brackets first (issue #37) - must happen before URLs/citations
        # because they may contain URL or citation placeholders
        text = self._normalize_brackets(text, denormalize=True)
        # Restore citations (issue #31)
        text = self._normalize_citations(text, denormalize=True)
        # Restore URLs (issue #32)
        text = self._normalize_urls(text, denormalize=True)
        return text

    @staticmethod
    def _has_sentence_punct(text: str) -> bool:
        """ Check if text has sentence-ending punctuation or ellipsis placeholder """
        return "." in text or "?" in text or "!" in text or "xellipsisthreex" in text

    @staticmethod
    def _has_unicode_bullet_list(text: str) -> bool:
        """Check if text contains a Unicode bullet list (2+ bullets).

        When text has 2+ Unicode bullets, it should be split directly at
        bullet positions rather than going through spaCy (which may mangle it).

        Related: https://github.com/craigtrim/fast-sentence-segment/issues/26
        Golden Rules 37, 38

        Args:
            text: Input text

        Returns:
            True if text has 2+ Unicode bullets (indicates inline list)
        """
        import re
        # Unicode bullets that indicate list items
        # NOTE: This must match UNICODE_BULLET_PATTERN in list_item_splitter.py
        unicode_bullet_pattern = r'[•⁃◦▪▸▹●○◆◇★☆✓✔✗✘➢➤›»]'
        bullets = re.findall(unicode_bullet_pattern, text)
        return len(bullets) >= 2

    @staticmethod
    def _split_unicode_bullet_list(text: str) -> list:
        """Split text directly at Unicode bullet positions.

        Used when text has 2+ Unicode bullets to bypass spaCy and split
        correctly at bullet boundaries.

        Related: https://github.com/craigtrim/fast-sentence-segment/issues/26

        Args:
            text: Input text with Unicode bullets

        Returns:
            List of items split at bullet positions
        """
        import re
        unicode_bullet_pattern = r'[•⁃◦▪▸▹●○◆◇★☆✓✔✗✘➢➤›»]'
        items = re.split(rf'(?={unicode_bullet_pattern})', text)
        items = [item.strip() for item in items if item.strip()]
        return items

    @staticmethod
    def _has_list_markers(text: str) -> bool:
        """Check if text contains inline list markers that should be split.

        Returns True if there are 2+ list markers, indicating an inline list.
        Also checks for list marker placeholders (xlm...x).
        """
        import re
        # Check for list marker placeholders (from ListMarkerNormalizer)
        # Format: xlm{encoded}x where encoded can contain letters and digits
        placeholder_count = len(re.findall(r'xlm[a-z0-9]+x', text))
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
                 input_text: str,
                 split_dialog: bool = True) -> list:

        # Normalize tabs to spaces
        input_text = input_text.replace('\t', ' ')

        # Dehyphenate words split across lines (issue #8)
        # Must happen before newlines are converted to periods
        input_text = self._dehyphenate(input_text)

        # Fix common OCR artifacts (issue #9)
        input_text = self._fix_ocr_artifacts(input_text)

        # Protect URLs BEFORE spaCy (issue #32)
        # URLs at sentence boundaries were getting periods appended
        # Replace URLs with placeholders to protect them during segmentation
        input_text = self._normalize_urls(input_text)

        # Protect bracketed content BEFORE spaCy (issue #37)
        # Brackets [...] are for references/citations and should never be split
        # regardless of internal punctuation like [Fig. 1.] or [p. 42.]
        input_text = self._normalize_brackets(input_text)

        # Protect Golden Rules patterns BEFORE spaCy (issues #25, #26, #27)
        # Must happen before spaCy to prevent false splits at:
        # - Middle initials (Albert I. Jones)
        # - Brand names with ! (Yahoo!)
        # - Unicode bullets and N°. abbreviation
        input_text = self._normalize_exclamation_brands(input_text)
        input_text = self._normalize_middle_initials(input_text)
        input_text = self._normalize_unicode_tokens(input_text)

        # Protect citation patterns BEFORE spaCy (issue #31)
        # Must happen before spaCy to prevent false splits at:
        # - APA citations (Author. (Year). Title)
        # - MLA citations (Author, Name. Title. Publisher, Year.)
        # - Informal citations (By Author, Date)
        input_text = self._normalize_citations(input_text)

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

        # Early handling of Unicode bullet lists (issue #26, Golden Rules 37, 38)
        # When text has 2+ Unicode bullets, split directly at bullet positions
        # instead of going through spaCy (which may mangle the text).
        # Related: https://github.com/craigtrim/fast-sentence-segment/issues/26
        if self._has_unicode_bullet_list(input_text):
            sentences = self._split_unicode_bullet_list(input_text)
            # Denormalize and return - these are already properly split
            return [self._denormalize(s) for s in sentences]

        sentences = self._spacy_segmenter(input_text)

        # Merge sentences incorrectly split at ellipsis + lowercase
        # e.g., ['She saidxellipsisthreex', 'but she didn\\'t.'] -> ['She saidxellipsisthreex but she didn\\'t.']
        sentences = self._ellipsis_sentence_merger(sentences)

        # Merge sentences incorrectly split inside quotes (issue #20)
        # e.g., ['"First thing.', 'Second thing," she said.'] -> ['"First thing. Second thing," she said.']
        # Skip this merge if split_dialog=True for stylometry/prosody analysis (issue #38)
        if not split_dialog:
            sentences = self._unclosed_quote_merger(sentences)

        # Merge sentences incorrectly split at abbreviations (issue #3)
        sentences = self._abbreviation_merger(sentences)

        # Merge sentences incorrectly split at quote attribution (issue #20)
        # e.g., ['"Are you sure?"', 'she asked.'] -> ['"Are you sure?" she asked.']
        sentences = self._quote_attribution_merger(sentences)

        # Merge title + single-word name splits (e.g., "Dr." + "Who?" -> "Dr. Who?")
        sentences = self._title_name_merger(sentences)

        # Merge numbered titles incorrectly split (e.g., "Part" + "2." -> "Part 2.")
        # Reference: https://github.com/craigtrim/fast-sentence-segment/issues/30
        sentences = self._numbered_title_merger(sentences)

        # Merge sentences incorrectly split at parenthetical boundaries (Golden Rule 21)
        # e.g., ['He teaches (worked as engineer.)', 'at university.'] -> single sentence
        # Related: https://github.com/craigtrim/fast-sentence-segment/issues/26
        sentences = self._parenthetical_merger(sentences)

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

        # Merge standalone ellipsis with following sentence (Golden Rule 48)
        # Must happen AFTER ellipsis denormalization so we can see actual ". . ."
        # Related: https://github.com/craigtrim/fast-sentence-segment/issues/26
        sentences = self._leading_ellipsis_merger(sentences)

        # Restore Golden Rules normalizers (issues #25, #26, #27)
        sentences = [
            self._normalize_exclamation_brands(x, denormalize=True)
            for x in sentences
        ]
        sentences = [
            self._normalize_middle_initials(x, denormalize=True)
            for x in sentences
        ]
        sentences = [
            self._normalize_unicode_tokens(x, denormalize=True)
            for x in sentences
        ]

        # Restore brackets first (issue #37) - must happen before URLs/citations
        # because they may contain URL or citation placeholders
        sentences = [
            self._normalize_brackets(x, denormalize=True)
            for x in sentences
        ]

        # Restore citations (issue #31)
        sentences = [
            self._normalize_citations(x, denormalize=True)
            for x in sentences
        ]

        # Restore URLs (issue #32)
        sentences = [
            self._normalize_urls(x, denormalize=True)
            for x in sentences
        ]

        return sentences

    def process(self,
                input_text: str,
                split_dialog: bool = True) -> list:
        """Perform Sentence Segmentation

        Args:
            input_text (str): An input string of any length or type
            split_dialog (bool): If True (default), segment dialog sentences individually.
                Set to False to keep multi-sentence quotes together.

        Raises:
            ValueError: input must be a string

        Returns:
            list:   a list of sentences
                    each list item is an input string of any length, but is a semantic sentence

        Related GitHub Issue:
            #38 - feat: Add optional parameter to segment dialog sentences individually
            https://github.com/craigtrim/fast-sentence-segment/issues/38
        """

        if input_text is None or not len(input_text):
            raise ValueError("Empty Input")

        if not isinstance(input_text, str):
            self.logger.warning(f"Invalid Input Text: {input_text}")
            return []

        return self._process(input_text, split_dialog=split_dialog)
