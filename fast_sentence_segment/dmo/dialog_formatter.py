# -*- coding: UTF-8 -*-
"""Dialog-aware paragraph formatter for segmented text.

Formats segmented sentences into readable paragraphs with intelligent
grouping of dialog and narrative text. Keeps multi-sentence quoted speech
together and adds paragraph breaks between different speakers.

Related GitHub Issue:
    #10 - feat: Add --format flag for dialog-aware paragraph formatting
    https://github.com/craigtrim/fast-sentence-segment/issues/10

Example:
    >>> from fast_sentence_segment.dmo.dialog_formatter import format_dialog
    >>> sentences = [
    ...     '"Hello," said Jack.',
    ...     '"How are you today?',
    ...     'I hope you are well."',
    ...     '"I am fine," replied Mary.',
    ... ]
    >>> print(format_dialog(sentences))
    "Hello," said Jack.

    "How are you today?
    I hope you are well."

    "I am fine," replied Mary.
"""

import re
from typing import List

from fast_sentence_segment.core import BaseObject
from fast_sentence_segment.dmo.quote_utils import (
    KNOWN_ELISION_WORDS,
    is_elision as _is_elision_impl,
    count_quotes as _count_quotes_impl,
)


# Quote characters to track for dialog detection.
# dialog_formatter runs AFTER normalize_quotes(), so only ASCII quotes
# and their curly variants (for defensive handling) are needed.
DOUBLE_QUOTES = '""\""'
SINGLE_QUOTES = "'''"
ALL_QUOTES = DOUBLE_QUOTES + SINGLE_QUOTES


def _is_elision(text: str, pos: int) -> bool:
    """Check if apostrophe at position is a word-initial elision.

    Delegates to shared implementation in quote_utils.

    Args:
        text: The full text.
        pos: Position of the apostrophe character.

    Returns:
        True if this appears to be an elision, not a dialog quote.
    """
    return _is_elision_impl(text, pos)


def _count_quotes(text: str) -> int:
    """Count actual quote characters in text, excluding apostrophes.

    Delegates to shared implementation in quote_utils.
    Uses this module's ALL_QUOTES and SINGLE_QUOTES constants.
    """
    return _count_quotes_impl(text, ALL_QUOTES, SINGLE_QUOTES)


def _starts_with_quote(text: str) -> bool:
    """Check if text starts with a dialog quote (not an elision).

    Returns True only for actual dialog openings, not for elisions
    like 'tis, 'twas, 'cello, etc.
    """
    text = text.lstrip()
    if not text or text[0] not in ALL_QUOTES:
        return False

    # Check if this is an elision rather than a dialog quote
    if text[0] in SINGLE_QUOTES and _is_elision(text, 0):
        return False

    return True


def _ends_with_closing_quote(text: str) -> bool:
    """Check if text ends with a closing quote (possibly followed by punctuation)."""
    text = text.rstrip()
    if not text:
        return False
    # Check last few characters for closing quote pattern
    # e.g., '" or "' or .' or ."
    for i in range(min(3, len(text)), 0, -1):
        if text[-i] in ALL_QUOTES:
            return True
    return False


def _is_complete_quote(text: str) -> bool:
    """Check if text contains a complete (balanced) quote.

    A complete quote has an even number of quote characters,
    meaning all opened quotes are closed.
    """
    quote_count = _count_quotes(text)
    return quote_count > 0 and quote_count % 2 == 0


def _sentence_is_dialog_continuation(sentence: str, in_quote: bool) -> bool:
    """Determine if sentence continues an open quote.

    Args:
        sentence: The sentence to check.
        in_quote: Whether we're currently inside an unclosed quote.

    Returns:
        True if this sentence is a continuation of open dialog.
    """
    if in_quote:
        return True
    return False


def _get_quote_delta(sentence: str) -> int:
    """Get the net change in quote depth for a sentence.

    Returns:
        Positive if more quotes opened than closed,
        negative if more closed than opened,
        zero if balanced.
    """
    return _count_quotes(sentence) % 2


class DialogFormatter(BaseObject):
    """Formats segmented sentences with dialog-aware paragraph grouping.

    This formatter analyzes sentence structure to intelligently group
    text into paragraphs:

    - Multi-sentence quoted speech stays together (same speaker)
    - Paragraph breaks added between different speakers
    - Narrative text grouped appropriately
    - Handles both single and double quote styles

    Example:
        >>> formatter = DialogFormatter()
        >>> sentences = ['"Hello," he said.', 'The door opened.']
        >>> print(formatter.process(sentences))
        "Hello," he said.

        The door opened.
    """

    def __init__(self):
        """Initialize the DialogFormatter."""
        BaseObject.__init__(self, __name__)

    def process(self, sentences: List[str]) -> str:
        """Format sentences into dialog-aware paragraphs.

        Args:
            sentences: List of segmented sentences.

        Returns:
            Formatted string with appropriate paragraph breaks.
        """
        return format_dialog(sentences)


def _is_narrative(sentence: str) -> bool:
    """Check if a sentence is narrative (no quotes at start)."""
    return not _starts_with_quote(sentence)


def _ends_dialog_turn(sentence: str) -> bool:
    """Check if a sentence ends a dialog turn.

    A dialog turn ends when the sentence ends with a closing quote
    followed by optional punctuation or dialog tag ending.
    """
    sentence = sentence.rstrip()
    if not sentence:
        return False

    # Pattern: ends with quote + optional punctuation
    # e.g., ." or .' or "' or '" or ," he said. etc.
    # Check if there's a closing quote near the end
    last_chars = sentence[-10:] if len(sentence) >= 10 else sentence

    # Count quotes in last part - if odd from end, likely closes
    for i, c in enumerate(reversed(last_chars)):
        if c in ALL_QUOTES:
            # Found a quote - check if it's likely a closer
            # A closer is typically followed by punctuation or end
            remaining = last_chars[len(last_chars) - i:]
            if not remaining or all(ch in '.,!?;: ' for ch in remaining):
                return True
            # Also handle dialog tags: ,' he said.
            if remaining and remaining[0] in '.,!?' and 'said' not in sentence.lower()[-20:]:
                return True
            break

    return False


def format_dialog(sentences: List[str]) -> str:
    """Format sentences into dialog-aware paragraphs.

    Groups sentences intelligently based on dialog structure:
    - Sentences within an unclosed quote stay grouped
    - Complete quoted sentences become their own paragraphs
    - Narrative text is grouped together
    - Paragraph breaks separate different speakers/turns

    Args:
        sentences: List of segmented sentences.

    Returns:
        Formatted string with paragraph breaks (double newlines)
        between logical groups and single newlines within groups.

    Example:
        >>> sentences = [
        ...     '"My dear sir," cried the man.',
        ...     '"You had every reason to be carried away."',
        ... ]
        >>> print(format_dialog(sentences))
        "My dear sir," cried the man.

        "You had every reason to be carried away."
    """
    if not sentences:
        return ""

    paragraphs: List[List[str]] = []
    current_para: List[str] = []
    in_quote = False  # Track if we're inside an unclosed quote

    for i, sentence in enumerate(sentences):
        sentence = sentence.strip()
        if not sentence:
            continue

        quote_count = _count_quotes(sentence)
        starts_quote = _starts_with_quote(sentence)
        is_narrative = _is_narrative(sentence)

        # Get info about previous sentence
        prev_sentence = current_para[-1] if current_para else ""
        prev_was_narrative = _is_narrative(prev_sentence) if prev_sentence else False
        prev_was_complete = _is_complete_quote(prev_sentence) if prev_sentence else False

        # Determine if this sentence starts a new paragraph
        should_start_new_para = False

        if not current_para:
            # First sentence always starts a new paragraph
            should_start_new_para = True
        elif in_quote:
            # Inside an open quote - continue current paragraph
            should_start_new_para = False
        elif starts_quote:
            # New quote starting - always new paragraph
            should_start_new_para = True
        elif is_narrative and prev_was_narrative:
            # Consecutive narrative sentences - each gets its own paragraph
            # This gives clean ebook formatting with paragraph breaks
            should_start_new_para = True
        elif is_narrative and prev_was_complete and not prev_was_narrative:
            # Narrative after complete dialog - new paragraph
            should_start_new_para = True
        elif is_narrative and not prev_was_narrative and _ends_dialog_turn(prev_sentence):
            # Narrative after dialog that ends a turn - new paragraph
            should_start_new_para = True

        if should_start_new_para and current_para:
            paragraphs.append(current_para)
            current_para = []

        current_para.append(sentence)

        # Update quote tracking
        if quote_count % 2 == 1:
            in_quote = not in_quote

    # Don't forget the last paragraph
    if current_para:
        paragraphs.append(current_para)

    # Format: join sentences in paragraph with newline, paragraphs with double newline
    return "\n\n".join("\n".join(para) for para in paragraphs)
