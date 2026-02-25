#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Merge sentences that spaCy incorrectly split at abbreviation boundaries.

When spaCy incorrectly splits after an abbreviation (e.g., "ext. 5" becomes
["ext.", "5. Ask for help."]), this component merges them back together
using specific known patterns.

Reference: https://github.com/craigtrim/fast-sentence-segment/issues/3
"""

import re
from typing import List, Optional, Tuple

from fast_sentence_segment.core import BaseObject


# Guard pattern for the targeted lowercase-continuation fallback.
# Matches a current sentence that ends with "[abbrev]. N[.]":
#   - a letter-word (1+ letters) ending with a period (an abbreviation)
#   - followed by a space and one or more digits
#   - optionally followed by a trailing period
# Examples that MATCH:  "p. 88."  "vol. 3."  "ibid. p. 34."
# Examples that do NOT: "part 1."  "chapter 2."  (no abbreviation period before digit)
#
# Related GitHub Issue:
#     #47 - Abbreviations with trailing periods cause false sentence splits
#     https://github.com/craigtrim/fast-sentence-segment/issues/47
_ABBREV_DIGIT_END = re.compile(r'[a-zA-Z]+\. \d+\.?$')


# Patterns where spaCy incorrectly splits after an abbreviation.
# Format: (ending_pattern, extract_pattern)
#   - ending_pattern: regex to match end of current sentence
#   - extract_pattern: regex to extract the portion to merge from next sentence
#
# The extract_pattern MUST have a capture group for the portion to merge.
# Whatever is NOT captured remains as a separate sentence.

MERGE_PATTERNS: List[Tuple[str, str]] = [

    # ext. 5, Ext. 123, EXT. 42 — digit-only: extension numbers are
    # standalone; whatever follows is typically a new sentence.
    (r"(?i)\bext\.$", r"^(\d+\.?)\s*"),

    # no. 5, No. 42, NO. 100
    (r"(?i)\bno\.$", r"^(\d+\.?)\s*"),

    # vol. 3, Vol. 42, VOL. 1
    (r"(?i)\bvol\.$", r"^(\d+\.?)\s*"),

    # pt. 2, Pt. 1, PT. 3
    (r"(?i)\bpt\.$", r"^(\d+\.?)\s*"),

    # ch. 5, Ch. 10, CH. 3
    (r"(?i)\bch\.$", r"^(\d+\.?)\s*"),

    # sec. 3, Sec. 14, SEC. 2
    (r"(?i)\bsec\.$", r"^(\d+(?:\.\d+)?\.?)\s*"),

    # fig. 1, Fig. 3.2, FIG. 10
    (r"(?i)\bfig\.$", r"^(\d+(?:\.\d+)?\.?)\s*"),

    # p. 42, P. 100
    (r"(?i)\bp\.$", r"^(\d+\.?)\s*"),

    # pp. 42-50, PP. 100-110
    (r"(?i)\bpp\.$", r"^(\d+(?:-\d+)?\.?)\s*"),

    # art. 5, Art. 12, ART. 1
    (r"(?i)\bart\.$", r"^(\d+\.?)\s*"),

    # para. 3, Para. 12, para. Schedule 2 — may follow a section or item number
    (r"(?i)\bpara\.$", r"^(.+)$"),

    # app. A, App. Glossary — appendix reference prefix; never ends a sentence
    (r"(?i)\bapp\.$", r"^(.+)$"),

    # Scholarly / Latin abbreviations that NEVER end sentences.
    # When spaCy incorrectly splits after these, merge with the full following sentence.
    # The extract_pattern r"^(.+)$" captures the entire following sentence.
    # This is safe because these abbreviations always introduce content — they
    # cannot legitimately be the last token of a complete sentence.
    #
    # Related GitHub Issue:
    #     #47 - Abbreviations with trailing periods cause false sentence splits
    #     https://github.com/craigtrim/fast-sentence-segment/issues/47

    # viz. (namely, to wit) — always introduces a clarification or enumeration
    (r"(?i)\bviz\.$", r"^(.+)$"),

    # cf. (compare) — introduces a reference.
    # Guard: do NOT merge if the next fragment looks like a complete sentence.
    # Heuristic: a sentence is detected when it starts with a definite/indefinite
    # article ("The", "A", "An") followed immediately by a LOWERCASE word.
    # This distinguishes complete sentences from book/article titles, which
    # start with articles followed by capitalised title words.
    #   "Compare cf. The cited work confirms." → "cited" is lowercase → SPLIT ✓
    #   "cf. The Structure of Scientific Revolutions." → "Structure" is uppercase
    #       (book title) → MERGE ✓
    #
    # Related GitHub Issue:
    #     #34 - Middle initial handling
    (r"(?i)\bcf\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),

    # ibid., / ibid.; (in the same place with comma or semicolon) — the trailing
    # comma/semicolon variant is always mid-reference; never ends a sentence.
    # The \.? handles a trailing period appended by SpacyDocSegmenter when the
    # sentence ends with a comma (e.g. "ibid.," → "ibid.,." after period append).
    (r"(?i)\bibid\.[,;]\.?$", r"^(.+)$"),

    # ibid. bare (no trailing comma) — can be sentence-ending or mid-reference.
    # Guard: do NOT merge if next fragment looks like a complete sentence.
    # Same article+lowercase heuristic as cf. above:
    # "See ibid. The citation is the same." → "citation" is lowercase → SPLIT ✓
    # "ibid. vol. 3, p. 22 covers..." → "vol." not an article → MERGE ✓
    (r"(?i)\bibid\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),

    # N.B. (nota bene) — always introduces a note; never a sentence ender
    (r"(?i)\bN\.B\.$", r"^(.+)$"),

    # q.v. (which see) — always a cross-reference; never a sentence ender
    (r"(?i)\bq\.v\.$", r"^(.+)$"),

    # s.v. (sub verbo / under the word) — always a lexical reference
    (r"(?i)\bs\.v\.$", r"^(.+)$"),

    # op. (opus; first word of op. cit.) — Step 1: merge with following cit.
    # op. alone never ends a sentence; always introduces a citation.
    (r"(?i)\bop\.$", r"^(.+)$"),

    # op. cit. — Step 2: after the two-word form is assembled, merge with context.
    # With iterative processing, the Step 1 pass assembles "op. cit." and
    # Step 2 in a subsequent pass merges it with whatever follows.
    (r"(?i)\bop\.\s+cit\.$", r"^(.+)$"),

    # loc. (locus; first word of loc. cit.) — Step 1
    (r"(?i)\bloc\.$", r"^(.+)$"),

    # loc. cit. — Step 2 (mirrors op. cit. handling)
    (r"(?i)\bloc\.\s+cit\.$", r"^(.+)$"),

    # ca. (circa) — always introduces an approximate date; never ends a sentence.
    # NOTE: Only match "ca." (full word), NOT "c." alone, because:
    #   - "c." is too ambiguous: matches list markers (a. b. c.), temperature unit "°C.",
    #     and corporate suffixes like "Inc." (ends with single c.)
    #   - The "circa" abbreviation is canonically written as "ca." in scholarly text
    #
    # Related GitHub Issue:
    #     #47 - Abbreviations with trailing periods cause false sentence splits
    (r"(?i)\bca\.$", r"^(.+)$"),

    # bk. (book) — reference prefix; never ends a sentence
    (r"(?i)\bbk\.$", r"^(.+)$"),

    # ser. (series) — reference prefix; never ends a sentence
    (r"(?i)\bser\.$", r"^(.+)$"),

    # illus. (illustrated by) — always introduces a name or number; never ends a sentence
    (r"(?i)\billus\.$", r"^(.+)$"),

    # fl. (floruit — flourished) — introduces a date range; never ends a sentence
    (r"(?i)\bfl\.$", r"^(.+)$"),

    # a.k.a. (also known as) — always introduces an alias; never ends a sentence
    (r"(?i)\ba\.k\.a\.$", r"^(.+)$"),

    # sc. (scilicet — namely) — always introduces a clarification; never ends a sentence
    (r"(?i)\bsc\.$", r"^(.+)$"),

    # sic. (thus; deliberate marker in quotations) — never ends a sentence in academic context
    (r"(?i)\bsic\.$", r"^(.+)$"),

    # ad loc. (ad locum — at the place) — two-word reference prefix; never ends a sentence
    (r"(?i)\bad\s+loc\.$", r"^(.+)$"),

    # et seq. (et sequentes — and the following) — always appends to a reference; never ends a sentence
    (r"(?i)\bet\s+seq\.$", r"^(.+)$"),

    # et al., / et al.; (et alia — and others, trailing comma/semicolon) — always mid-reference.
    # The \.? handles the SpacyDocSegmenter artifact (e.g. "et al.," → "et al.,." after period append).
    (r"(?i)\bet\s+al\.[,;]\.?$", r"^(.+)$"),

    # et al. bare — may precede continuation text (verb or reference) or end a sentence.
    # Guard: do NOT merge if next fragment looks like a complete sentence.
    # Same article+lowercase heuristic as cf./ibid. above:
    # "Evans et al. The results show..." → "results" lowercase after "The" → SPLIT ✓
    # "Evans et al. Showed that..." → "Showed" is uppercase non-article → MERGE ✓
    #
    # Related GitHub Issue:
    #     #47 - Abbreviations with trailing periods cause false sentence splits
    #     https://github.com/craigtrim/fast-sentence-segment/issues/47
    (r"(?i)\bet\s+al\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),

    # P.S. (postscript) — introduces additional content; never ends the main letter body
    (r"(?i)\bP\.S\.$", r"^(.+)$"),

    # ed. / eds. (editor/editors) — reference prefix; never ends a sentence
    (r"(?i)\beds?\.$", r"^(.+)$"),

    # trans. (translated by) — reference prefix; never ends a sentence
    (r"(?i)\btrans\.$", r"^(.+)$"),

    # comp. / comps. (compiled by) — reference prefix; never ends a sentence
    (r"(?i)\bcomps?\.$", r"^(.+)$"),

    # repr. (reprinted) — reference metadata; never ends a sentence
    (r"(?i)\brepr\.$", r"^(.+)$"),

    # rev. (revised) — reference metadata; never ends a sentence
    (r"(?i)\brev\.$", r"^(.+)$"),

]


class AbbreviationMerger(BaseObject):
    """Merge sentences incorrectly split at abbreviation boundaries."""

    def __init__(self):
        """
        Created:
            27-Dec-2024
            craigtrim@gmail.com
        Reference:
            https://github.com/craigtrim/fast-sentence-segment/issues/3
        """
        BaseObject.__init__(self, __name__)
        # Compile patterns for efficiency
        self._patterns = [
            (re.compile(ending), re.compile(extract))
            for ending, extract in MERGE_PATTERNS
        ]

    def _try_merge(self, current: str, next_sent: str) -> Optional[Tuple[str, str]]:
        """Try to merge two sentences based on known patterns.

        Args:
            current: Current sentence
            next_sent: Next sentence

        Returns:
            Tuple of (merged_sentence, remainder) if merge needed, else None
        """
        current = current.strip()
        next_sent = next_sent.strip()

        # Strip SpacyDocSegmenter artifact: a trailing period appended to
        # sentences that originally ended with comma or semicolon.
        # e.g. "ibid.,." → "ibid.," so the merge produces "ibid., p."
        # instead of "ibid.,. p." which PostProcessStructure would mangle
        # into "ibid.,  p." via the ",." → ", " replacement rule.
        if len(current) >= 2 and current[-1] == '.' and current[-2] in ',;':
            current = current[:-1]

        for ending_pattern, extract_pattern in self._patterns:
            if ending_pattern.search(current):
                match = extract_pattern.match(next_sent)
                if match:
                    # Extract the portion to merge
                    extracted = match.group(1)
                    # Get the remainder (everything after the match)
                    remainder = next_sent[match.end():].strip()
                    # Build merged sentence
                    merged = current + " " + extracted
                    return (merged, remainder)

        return None

    def _process_once(self, sentences: List[str]) -> List[str]:
        """Run one pass of merge logic over the sentence list.

        Each pass greedily merges adjacent sentences that match a known
        pattern.  Calling this repeatedly (until stable) handles chains
        of abbreviations such as ``cf. ibid. p. 23 for…`` that need
        multiple rounds of merging.

        Args:
            sentences: List of sentences to process

        Returns:
            List with all detected merges applied in this single pass
        """
        result = []
        i = 0

        while i < len(sentences):
            current = sentences[i]

            # Check if we should merge with next sentence
            if i + 1 < len(sentences):
                next_sent = sentences[i + 1]
                merge_result = self._try_merge(current, next_sent)

                if merge_result:
                    merged, remainder = merge_result
                    result.append(merged)

                    # If there's a remainder, it becomes a new sentence to process
                    if remainder:
                        # Insert remainder back for processing
                        sentences = sentences[:i+2] + [remainder] + sentences[i+2:]
                        sentences[i+1] = remainder

                    i += 2
                    continue

                # Targeted fallback: merge when current ends with an abbreviation
                # followed by a digit (e.g. "p. 88.") and the next sentence starts
                # with a lowercase continuation (e.g. "for more details.").
                # This handles post-segmentation artifacts where spaCy splits at
                # the end of a page/section reference even though the following
                # text is a grammatical continuation, e.g.:
                #   "Cf. Jackson et al. 2009, p. 88." + "for a more detailed treatment."
                #   → "Cf. Jackson et al. 2009, p. 88 for a more detailed treatment."
                #
                # Guard: `current` must end with "[abbrev]. N[.]" — i.e., a
                # letter-word ending with a period (an abbreviation), followed by
                # a space and one or more digits, optionally with a trailing period.
                # This prevents incorrectly merging list-item titles such as
                # "part 1." with a lowercase-starting next sentence, because "part"
                # has no trailing period and therefore does not match the guard.
                #
                # Related GitHub Issue:
                #     #47 - Abbreviations with trailing periods cause false sentence splits
                #     https://github.com/craigtrim/fast-sentence-segment/issues/47
                if (next_sent
                        and next_sent[0].islower()
                        and current.endswith('.')
                        and _ABBREV_DIGIT_END.search(current)):
                    current_for_merge = current
                    if current.endswith('.') and len(current) >= 2 and current[-2].isdigit():
                        current_for_merge = current[:-1]
                    result.append(current_for_merge + " " + next_sent.strip())
                    i += 2
                    continue

            result.append(current)
            i += 1

        return result

    def process(self, sentences: List[str]) -> List[str]:
        """Process a list of sentences, merging incorrectly split ones.

        Applies :meth:`_process_once` repeatedly until the sentence list
        stabilises.  This handles chains of abbreviations that require
        multiple rounds of merging, e.g. ``["op.", "cit.", "p. 45."]``
        first collapses ``op.`` + ``cit.`` → ``"op. cit."``, then on the
        next pass collapses ``"op. cit."`` + ``"p. 45."`` → final result.

        Args:
            sentences: List of sentences from spaCy

        Returns:
            List of sentences with incorrect splits merged

        Related GitHub Issue:
            #47 - Abbreviations with trailing periods cause false sentence splits
            https://github.com/craigtrim/fast-sentence-segment/issues/47
        """
        if not sentences:
            return sentences

        prev: List[str] = []
        while sentences != prev:
            prev = sentences[:]
            sentences = self._process_once(sentences)

        return sentences
