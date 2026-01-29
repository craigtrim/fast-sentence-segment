# -*- coding: UTF-8 -*-
"""Group sentences that belong to the same open-quote span.

When outputting segmented text with blank-line separators, sentences
that open with a double quote but do not close it should be grouped
with subsequent sentences (no blank line between them) until the
closing quote is found.

Related GitHub Issue:
    #5 - Normalize quotes and group open-quote sentences in unwrap mode
    https://github.com/craigtrim/fast-sentence-segment/issues/5
"""

from typing import List


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
