# -*- coding: UTF-8 -*-
"""Title abbreviations followed by single-word names ending in punctuation.

The key insight: when a title (Dr., Mr., Mrs., Ms., Prof.) is followed by a
single capitalized word ending in punctuation, it's almost certainly a name,
not a one-word sentence.

Examples:
    "Dr. Who?" - This is asking about the name, not a sentence break
    "Dr. Strange?" - Same pattern, a name inquiry

This file tests three distinct patterns:
    1. Standalone: "Dr. Who?" as the entire input
    2. End-text: "Have you seen Dr. Who?" - title+name at end of sentence
    3. Mid-text: "Do you like Dr. Who? I do." - title+name followed by more text
"""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestTitleSingleWordStandalone:
    """Title + single word as the entire input (standalone pattern)."""

    @pytest.mark.parametrize("text,expected", [
        # Dr. + single word name with question mark
        ("Dr. Who?", ["Dr. Who?"]),
        ("Dr. Strange?", ["Dr. Strange?"]),
        ("Dr. Doom?", ["Dr. Doom?"]),
        ("Dr. Seuss?", ["Dr. Seuss?"]),
        ("Dr. Pepper?", ["Dr. Pepper?"]),
        ("Dr. Dre?", ["Dr. Dre?"]),

        # Dr. + single word name with exclamation
        ("Dr. Doom!", ["Dr. Doom!"]),
        ("Dr. Strange!", ["Dr. Strange!"]),
        ("Dr. Pepper!", ["Dr. Pepper!"]),

        # Mr. + single word name with punctuation
        ("Mr. T?", ["Mr. T?"]),
        ("Mr. Bean?", ["Mr. Bean?"]),
        ("Mr. Rogers?", ["Mr. Rogers?"]),
        ("Mr. T!", ["Mr. T!"]),

        # Mrs./Ms. + single word name with punctuation
        ("Mrs. Doubtfire?", ["Mrs. Doubtfire?"]),
        ("Ms. Frizzle?", ["Ms. Frizzle?"]),

        # Prof. + single word name with punctuation
        ("Prof. Xavier?", ["Prof. Xavier?"]),
        ("Prof. Snape?", ["Prof. Snape?"]),

        # Multiple punctuation marks
        ("Dr. Who?!", ["Dr. Who?!"]),
        ("Dr. Doom!!!", ["Dr. Doom!!!"]),
        ("Mr. T?!?", ["Mr. T?!?"]),
    ])
    def test_standalone(self, segment: SegmentationFunc, text: str, expected: list[str]):
        """Title + single word name as entire input stays together."""
        assert segment(text) == expected


class TestTitleSingleWordEndText:
    """Title + single word at end of sentence (end-text pattern)."""

    @pytest.mark.parametrize("text,expected", [
        # Dr. at end of sentence
        ("Have you seen Dr. Who?", ["Have you seen Dr. Who?"]),
        ("Do you like Dr. Strange?", ["Do you like Dr. Strange?"]),
        ("Have you met Dr. Doom?", ["Have you met Dr. Doom?"]),
        ("Who is Dr. Seuss?", ["Who is Dr. Seuss?"]),
        ("I love Dr. Pepper!", ["I love Dr. Pepper!"]),
        ("It's Dr. Doom!", ["It's Dr. Doom!"]),
        ("Look, it's Dr. Strange!", ["Look, it's Dr. Strange!"]),

        # Mr. at end of sentence
        ("Remember Mr. T?", ["Remember Mr. T?"]),
        ("Who is Mr. Bean?", ["Who is Mr. Bean?"]),
        ("I love Mr. Rogers!", ["I love Mr. Rogers!"]),
        ("Do you know Mr. T?", ["Do you know Mr. T?"]),

        # Mrs./Ms. at end of sentence
        ("Have you met Mrs. Doubtfire?", ["Have you met Mrs. Doubtfire?"]),
        ("Who is Ms. Frizzle?", ["Who is Ms. Frizzle?"]),

        # Prof. at end of sentence
        ("Is that Prof. Xavier?", ["Is that Prof. Xavier?"]),
        ("Remember Prof. Snape?", ["Remember Prof. Snape?"]),

        # Longer sentences ending with title+name
        ("I went to the store and saw Dr. Who?", ["I went to the store and saw Dr. Who?"]),
        ("The villain in the movie is Dr. Doom!", ["The villain in the movie is Dr. Doom!"]),
        ("My favorite character is Mr. T!", ["My favorite character is Mr. T!"]),
    ])
    def test_end_text(self, segment: SegmentationFunc, text: str, expected: list[str]):
        """Title + single word name at end of sentence stays together."""
        assert segment(text) == expected


class TestTitleSingleWordMidText:
    """Title + single word in middle of text, followed by more sentences (mid-text pattern)."""

    @pytest.mark.parametrize("text,expected", [
        # Original failing case from user
        ("Hi Man!  The Dr. Wasn't here?  Dr. Who? Dr. Me.",
         ["Hi Man!", "The Dr. Wasn't here?", "Dr. Who?", "Dr. Me."]),

        # Dr. mid-text followed by more content
        ("Do you like Dr. Who? I do.", ["Do you like Dr. Who?", "I do."]),
        ("Do you like Dr. Who? I prefer Dr. Strange.", ["Do you like Dr. Who?", "I prefer Dr. Strange."]),
        ("Have you seen Dr. Who? It was great.", ["Have you seen Dr. Who?", "It was great."]),
        ("I love Dr. Pepper! It's refreshing.", ["I love Dr. Pepper!", "It's refreshing."]),
        ("It's Dr. Doom! Run away!", ["It's Dr. Doom!", "Run away!"]),

        # Mr. mid-text
        ("Remember Mr. T? He was great.", ["Remember Mr. T?", "He was great."]),
        ("I saw Mr. Bean! So funny.", ["I saw Mr. Bean!", "So funny."]),

        # Multiple title+names in sequence
        ("Dr. Who? Dr. Strange? Dr. Doom?", ["Dr. Who?", "Dr. Strange?", "Dr. Doom?"]),
        ("Mr. T! Mr. Bean! Mr. Rogers!", ["Mr. T!", "Mr. Bean!", "Mr. Rogers!"]),

        # Mixed with regular sentences
        ("I went to the store. Have you seen Dr. Who? It was great.",
         ["I went to the store.", "Have you seen Dr. Who?", "It was great."]),
        ("Hello there. Do you like Dr. Pepper? I love it.",
         ["Hello there.", "Do you like Dr. Pepper?", "I love it."]),

        # Title+name at start, then more sentences
        ("Dr. Doom! He's the villain. Watch out!",
         ["Dr. Doom!", "He's the villain.", "Watch out!"]),
        ("Dr. Who? That's a great show. I watch it weekly.",
         ["Dr. Who?", "That's a great show.", "I watch it weekly."]),
    ])
    def test_mid_text(self, segment: SegmentationFunc, text: str, expected: list[str]):
        """Title + single word name mid-text correctly splits surrounding sentences."""
        assert segment(text) == expected


class TestTitleSingleWordEdgeCases:
    """Edge cases for title + single word pattern."""

    @pytest.mark.parametrize("text,expected", [
        # Lowercase after title - not a name, part of same sentence
        ("Ask Dr. who can help.", ["Ask Dr. who can help."]),
        ("See Mr. who arrived.", ["See Mr. who arrived."]),

        # Single word but no ending punctuation - existing abbreviation logic
        ("Dr. Smith is here.", ["Dr. Smith is here."]),
        ("Mr. Jones arrived.", ["Mr. Jones arrived."]),
        ("Mrs. Brown called.", ["Mrs. Brown called."]),

        # Title at very end of sentence (no name after)
        ("I need to see the Dr.", ["I need to see the Dr."]),
        ("She's a Dr.", ["She's a Dr."]),
        ("He became a Prof.", ["He became a Prof."]),

        # Title followed by multi-word sentence (should break)
        ("Contact Dr. Smith. He can help you with that problem.",
         ["Contact Dr. Smith.", "He can help you with that problem."]),
        ("I saw Mr. Jones. What did he say to you?",
         ["I saw Mr. Jones.", "What did he say to you?"]),
    ])
    def test_edge_cases(self, segment: SegmentationFunc, text: str, expected: list[str]):
        """Edge cases are handled correctly."""
        assert segment(text) == expected
