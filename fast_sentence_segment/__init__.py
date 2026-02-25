from typing import List, Optional, Union

from .bp import *
from .svc import *
from .dmo import *

from .bp.segmenter import Segmenter
from .dmo.unwrap_hard_wrapped_text import unwrap_hard_wrapped_text
from .dmo.normalize_quotes import normalize_quotes
from .dmo.dialog_formatter import format_dialog

segment = Segmenter().input_text


def segment_paragraphs(sentences: List[List[str]]) -> List[str]:
    """Join sentences within each paragraph into a single string.

    Takes the nested list output of segment_text(flatten=False) and collapses
    each paragraph's sentence list into one space-joined string.

    Args:
        sentences: A list of paragraphs, each paragraph being a list of sentences.

    Returns:
        A flat list of paragraph strings, one string per paragraph.

    Related GitHub Issue:
        #72 - segment_paragraphs not exported from package
        https://github.com/craigtrim/fast-sentence-segment/issues/72
    """
    return [" ".join(paragraph) for paragraph in sentences]


def segment_text(
    input_text: str,
    flatten: bool = False,
    unwrap: bool = False,
    normalize: bool = True,
    format: Optional[str] = None,
    split_dialog: bool = True,
) -> Union[List, str]:
    """Segment text into sentences.

    Args:
        input_text: The text to segment.
        flatten: If True, return a flat list of sentences instead of
            nested paragraphs.
        unwrap: If True, unwrap hard-wrapped lines (e.g., Project
            Gutenberg e-texts) before segmenting.
        normalize: If True (default), normalize unicode quote variants
            to ASCII equivalents before segmenting. Ensures consistent
            quote characters for downstream processing.
        format: Optional output format. Supported values:
            - None (default): Return list of sentences/paragraphs
            - "dialog": Return formatted string with dialog-aware
              paragraph grouping (keeps multi-sentence quotes together,
              adds paragraph breaks between speakers)
        split_dialog: If True (default), segment dialog sentences individually.
            Set to False to keep multi-sentence quotes together for narrative
            flow. Default is True, which is useful for stylometry and prosody
            analysis that requires examining each sentence separately.

    Returns:
        If format is None: List of sentences (if flatten=True) or list
        of paragraph groups, each containing a list of sentences.
        If format="dialog": Formatted string with paragraph breaks.

    Related GitHub Issues:
        #6 - Review findings from Issue #5
        https://github.com/craigtrim/fast-sentence-segment/issues/6

        #10 - feat: Add --format flag for dialog-aware paragraph formatting
        https://github.com/craigtrim/fast-sentence-segment/issues/10

        #38 - feat: Add optional parameter to segment dialog sentences individually
        https://github.com/craigtrim/fast-sentence-segment/issues/38
    """
    if unwrap:
        input_text = unwrap_hard_wrapped_text(input_text)

    if normalize:
        input_text = normalize_quotes(input_text)

    results = segment(input_text, split_dialog=split_dialog)

    # Flatten to list of sentences
    flat = []
    [[flat.append(y) for y in x] for x in results]

    # Apply formatting if requested
    if format == "dialog":
        return format_dialog(flat)

    if flatten:
        return flat

    return results
