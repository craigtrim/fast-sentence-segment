# -*- coding: UTF-8 -*-
"""Group sentences that belong to the same open-quote span.

When outputting segmented text with blank-line separators, sentences
that open with a double quote but do not close it should be grouped
with subsequent sentences (no blank line between them) until the
closing quote is found.

Related GitHub Issues:
    #5 - Normalize quotes and group open-quote sentences in unwrap mode
    https://github.com/craigtrim/fast-sentence-segment/issues/5

    #6 - Review findings from Issue #5
    https://github.com/craigtrim/fast-sentence-segment/issues/6
"""

from typing import List

# Maximum number of sentences that can be grouped under a single
# open-quote span before the quote state is forcibly reset. This
# bounds the damage from a stray quote character (e.g., OCR artifact)
# which would otherwise corrupt grouping for all subsequent sentences.
#
# A typical quoted passage in literature rarely exceeds 20 sentences.
# This limit is deliberately generous to avoid false resets on
# legitimately long quoted passages while still preventing runaway
# grouping on malformed input.
MAX_QUOTE_GROUP_SIZE = 20


def group_quoted_sentences(sentences: List[str]) -> List[List[str]]:
    """Group sentences into blocks based on open/close quote tracking.

    Sentences within an unclosed double-quote span are grouped together
    into the same block. Sentences outside of a quote span each form
    their own block.

    When rendered, each block is joined by newlines, and blocks are
    separated by blank lines (double newlines).

    The algorithm tracks the quote state by counting ASCII double quote
    characters in each sentence. An odd count toggles the open/close
    state. When a quote is open, subsequent sentences are appended to
    the current group rather than starting a new one.

    A safety limit (MAX_QUOTE_GROUP_SIZE) prevents a stray or malformed
    quote from swallowing all remaining sentences into one group. When
    the limit is reached, the current group is flushed and the quote
    state is reset. This bounds corruption from OCR artifacts or
    encoding errors to a bounded window rather than the entire document.

    Args:
        sentences: Flat list of segmented sentences.

    Returns:
        List of sentence groups. Each group is a list of sentences
        that should be rendered together without blank-line separators.

    Example:
        >>> groups = group_quoted_sentences([
        ...     '"The probability lies in that direction.',
        ...     'And if we take this as a working hypothesis."',
        ...     'He paused.',
        ... ])
        >>> groups
        [['"The probability lies in that direction.',
          'And if we take this as a working hypothesis."'],
         ['He paused.']]

    Related GitHub Issues:
        #5 - Normalize quotes and group open-quote sentences in unwrap mode
        https://github.com/craigtrim/fast-sentence-segment/issues/5

        #6 - Review findings from Issue #5
        https://github.com/craigtrim/fast-sentence-segment/issues/6
    """
    if not sentences:
        return []

    groups: List[List[str]] = []
    current_group: List[str] = []
    quote_open = False

    for sentence in sentences:
        quote_count = sentence.count('"')

        if not quote_open:
            # Starting a new group
            if current_group:
                groups.append(current_group)
            current_group = [sentence]
        else:
            # Inside an open quote span -- append to current group
            current_group.append(sentence)

        # Toggle quote state on odd quote count
        if quote_count % 2 == 1:
            quote_open = not quote_open

        # Safety: if a group grows beyond the limit, the quote is
        # likely corrupted (stray quote character). Flush the group
        # and reset state to prevent runaway grouping.
        if quote_open and len(current_group) >= MAX_QUOTE_GROUP_SIZE:
            groups.append(current_group)
            current_group = []
            quote_open = False

    # Flush the final group
    if current_group:
        groups.append(current_group)

    return groups


def format_grouped_sentences(sentences: List[str]) -> str:
    """Format sentences with quote-aware blank-line separation.

    Sentences within the same quoted span are separated by single
    newlines. Sentence groups are separated by blank lines (double
    newlines).

    Args:
        sentences: Flat list of segmented sentences.

    Returns:
        Formatted string with appropriate line separation.

    Example:
        >>> text = format_grouped_sentences([
        ...     '"The probability lies in that direction.',
        ...     'And if we take this as a working hypothesis."',
        ...     'He paused.',
        ... ])
        >>> print(text)
        "The probability lies in that direction.
        And if we take this as a working hypothesis."
        <BLANKLINE>
        He paused.
    """
    groups = group_quoted_sentences(sentences)
    return '\n\n'.join('\n'.join(group) for group in groups)
