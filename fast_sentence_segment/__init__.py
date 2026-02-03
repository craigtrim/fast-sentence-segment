from typing import List, Optional, Union

from .bp import *
from .svc import *
from .dmo import *

from .bp.segmenter import Segmenter
from .dmo.unwrap_hard_wrapped_text import unwrap_hard_wrapped_text
from .dmo.normalize_quotes import normalize_quotes
from .dmo.dialog_formatter import format_dialog

segment = Segmenter().input_text


def segment_text(
    input_text: str,
    flatten: bool = False,
    unwrap: bool = False,
    normalize: bool = True,
    format: Optional[str] = None,
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

    Returns:
        If format is None: List of sentences (if flatten=True) or list
        of paragraph groups, each containing a list of sentences.
        If format="dialog": Formatted string with paragraph breaks.

    Related GitHub Issues:
        #6 - Review findings from Issue #5
        https://github.com/craigtrim/fast-sentence-segment/issues/6

        #10 - feat: Add --format flag for dialog-aware paragraph formatting
        https://github.com/craigtrim/fast-sentence-segment/issues/10
    """
    if unwrap:
        input_text = unwrap_hard_wrapped_text(input_text)

    if normalize:
        input_text = normalize_quotes(input_text)

    results = segment(input_text)

    # Flatten to list of sentences
    flat = []
    [[flat.append(y) for y in x] for x in results]

    # Apply formatting if requested
    if format == "dialog":
        return format_dialog(flat)

    if flatten:
        return flat

    return results
