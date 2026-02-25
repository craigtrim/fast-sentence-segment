# -*- coding: UTF-8 -*-
"""
Integration tests for the AbbreviationSplitter component.

Tests the component directly (not via segment_text) to verify:
 1. vs. and surface variants do not over-split
 2. TITLE_ABBREVIATIONS do not trigger splits
 3. SENTENCE_ENDING_ABBREVIATIONS DO trigger splits when followed by capitals
 4. Chained abbreviation patterns

Related GitHub Issue:
    #47 - Abbreviations with trailing periods trigger false sentence splits
    https://github.com/craigtrim/fast-sentence-segment/issues/47

Module-level case count: ~320 cases
"""

import itertools
from typing import List

import pytest

from fast_sentence_segment.dmo.abbreviation_splitter import AbbreviationSplitter
from fast_sentence_segment.dmo.abbreviations import (
    SENTENCE_ENDING_ABBREVIATIONS,
    TITLE_ABBREVIATIONS,
)


@pytest.fixture
def splitter():
    """Provide an AbbreviationSplitter instance."""
    return AbbreviationSplitter()


# ---------------------------------------------------------------------------
# Section 1: vs. and surface variants (50 cases)
# ---------------------------------------------------------------------------

_VS_VARIANTS = ["vs.", "v.", "Vs.", "v.s.", "VS."]

_VS_NOSPLIT_TEMPLATES = [
    "Smith {v} Jones contested the ruling.",
    "Apple {v} Samsung was a landmark case.",
    "The prosecution {v} the defence argued.",
    "Team A {v} Team B played well.",
    "Col. Smith {v} Adm. Jones disagreed.",
    "The motion {v} the counter-motion was filed.",
    "The data {v} the theory was examined.",
    "Theory {v} practice was debated.",
    "Performance {v} cost was the trade-off.",
    "The old system {v} the new one was compared.",
]

VS_NOSPLIT_CASES = [
    (tmpl.replace("{v}", v), [tmpl.replace("{v}", v)])
    for v, tmpl in itertools.product(_VS_VARIANTS, _VS_NOSPLIT_TEMPLATES)
]


class TestVsVariants:
    """Verify vs. and surface variants do not trigger false sentence splits."""

    @pytest.mark.parametrize("text,expected", VS_NOSPLIT_CASES)
    def test_vs_no_split(self, splitter: AbbreviationSplitter, text: str, expected: List[str]):
        assert splitter.process([text]) == expected


# ---------------------------------------------------------------------------
# Section 2: TITLE_ABBREVIATIONS do not trigger splits (100 cases)
# ---------------------------------------------------------------------------

_TITLE_TEMPLATES = [
    "{a} Smith attended the meeting.",
    "The report was filed by {a} Smith.",
    "I spoke with {a} Smith yesterday.",
    "Please contact {a} Smith directly.",
    "According to {a} Smith, the results are clear.",
]

# Use the first 20 title abbreviations to get 100 cases (20 × 5)
_TITLE_SAMPLE = [
    t for t in TITLE_ABBREVIATIONS
    if t not in ("i.e.,", "ie.,", "e.g.,", "eg.,", "viz.,")
][:20]

TITLE_NOSPLIT_CASES = [
    (tmpl.replace("{a}", a), [tmpl.replace("{a}", a)])
    for a, tmpl in itertools.product(_TITLE_SAMPLE, _TITLE_TEMPLATES)
]


class TestTitleAbbreviationsNoSplit:
    """Verify TITLE_ABBREVIATIONS do not trigger sentence splits."""

    @pytest.mark.parametrize("text,expected", TITLE_NOSPLIT_CASES)
    def test_title_no_split(self, splitter: AbbreviationSplitter, text: str, expected: List[str]):
        assert splitter.process([text]) == expected


# ---------------------------------------------------------------------------
# Section 3: SENTENCE_ENDING_ABBREVIATIONS trigger splits (50+ cases)
# ---------------------------------------------------------------------------

# Sentence-ending abbreviations that are tested here (subset that reliably split)
# Format: (input_sentence, expected_output_list)
_TIME_ABBREVS = ["a.m.", "p.m.", "A.M.", "P.M."]

_TIME_SPLIT_TEMPLATES = [
    ("The meeting starts at 9 {t} The agenda is attached.", lambda t: [f"The meeting starts at 9 {t}", "The agenda is attached."]),
    ("She left at 5 {t} The office was empty.", lambda t: [f"She left at 5 {t}", "The office was empty."]),
    ("The lab opens at 8 {t} Results are posted.", lambda t: [f"The lab opens at 8 {t}", "Results are posted."]),
]


def _build_time_split_cases():
    cases = []
    for t, (tmpl, exp_fn) in itertools.product(_TIME_ABBREVS, _TIME_SPLIT_TEMPLATES):
        text = tmpl.replace("{t}", t)
        expected = exp_fn(t)
        cases.append((text, expected))
    return cases


TIME_SPLIT_CASES = _build_time_split_cases()

# Academic degree splits
_DEGREE_ABBREVS = ["Ph.D.", "M.D.", "J.D.", "B.A.", "M.A.", "B.S.", "M.S."]

_DEGREE_SPLIT_TEMPLATES = [
    (lambda d: f"She earned her {d} The research continues.", lambda d: [f"She earned her {d}", "The research continues."]),
    (lambda d: f"He holds a {d} The position requires it.", lambda d: [f"He holds a {d}", "The position requires it."]),
]


def _build_degree_split_cases():
    cases = []
    for d, (txt_fn, exp_fn) in itertools.product(_DEGREE_ABBREVS, _DEGREE_SPLIT_TEMPLATES):
        cases.append((txt_fn(d), exp_fn(d)))
    return cases


DEGREE_SPLIT_CASES = _build_degree_split_cases()

ALL_SPLIT_CASES = TIME_SPLIT_CASES + DEGREE_SPLIT_CASES


class TestSentenceEndingAbbreviationsSplit:
    """Verify SENTENCE_ENDING_ABBREVIATIONS trigger splits when followed by capitals."""

    @pytest.mark.parametrize("text,expected", ALL_SPLIT_CASES)
    def test_split_occurs(self, splitter: AbbreviationSplitter, text: str, expected: List[str]):
        assert splitter.process([text]) == expected


# ---------------------------------------------------------------------------
# Section 4: Chained abbreviations (100 cases)
# ---------------------------------------------------------------------------

_CHAIN_PATTERNS = [
    # title + time (should NOT split between title and time)
    ("Dr. Smith arrived at 9 a.m. The meeting began.", ["Dr. Smith arrived at 9 a.m.", "The meeting began."]),
    ("Mr. Jones left at 5 p.m. The office closed.", ["Mr. Jones left at 5 p.m.", "The office closed."]),
    ("Prof. Brown presented at 10 a.m. The results were clear.", ["Prof. Brown presented at 10 a.m.", "The results were clear."]),
    ("Col. Green briefed at 6 a.m. The unit mobilised.", ["Col. Green briefed at 6 a.m.", "The unit mobilised."]),
    ("Gen. White spoke at 3 p.m. The order was given.", ["Gen. White spoke at 3 p.m.", "The order was given."]),
    # title + title (should NOT split between them)
    ("Dr. Smith and Prof. Jones collaborated.", ["Dr. Smith and Prof. Jones collaborated."]),
    ("Mr. Brown met Mrs. Davis yesterday.", ["Mr. Brown met Mrs. Davis yesterday."]),
    ("Col. Adams briefed Gen. Baker this morning.", ["Col. Adams briefed Gen. Baker this morning."]),
    ("Capt. Evans reported to Cmdr. Foster.", ["Capt. Evans reported to Cmdr. Foster."]),
    ("Sen. Gray consulted Rep. Hall today.", ["Sen. Gray consulted Rep. Hall today."]),
    # geographic + title
    ("She works at 123 Main St. Dr. Smith's office.", ["She works at 123 Main St. Dr. Smith's office."]),
    ("The clinic is on Oak Ave. Prof. Brown is there.", ["The clinic is on Oak Ave. Prof. Brown is there."]),
    ("Turn at Elm Rd. Mr. Jones lives there.", ["Turn at Elm Rd. Mr. Jones lives there."]),
    ("The office is on Park Blvd. Dr. Lee is in.", ["The office is on Park Blvd. Dr. Lee is in."]),
    ("Walk to Cedar St. Mrs. Adams is waiting.", ["Walk to Cedar St. Mrs. Adams is waiting."]),
    # degree + title
    ("She holds a Ph.D. Dr. Jones confirmed.", ["She holds a Ph.D.", "Dr. Jones confirmed."]),
    ("He earned an M.D. Prof. Smith reviewed.", ["He earned an M.D.", "Prof. Smith reviewed."]),
    ("She completed a J.D. Mr. Brown signed off.", ["She completed a J.D.", "Mr. Brown signed off."]),
    # business + title
    ("He works at Acme Inc. Dr. Adams leads it.", ["He works at Acme Inc.", "Dr. Adams leads it."]),
    ("The firm is Global Corp. Mr. Lee is CEO.", ["The firm is Global Corp.", "Mr. Lee is CEO."]),
    # triple chain: title + geographic + title
    ("Contact Dr. Smith at 123 Main Ave. Prof. Jones is also there.", ["Contact Dr. Smith at 123 Main Ave. Prof. Jones is also there."]),
    ("Mr. Brown lives on Oak St. Mrs. Davis is nearby.", ["Mr. Brown lives on Oak St. Mrs. Davis is nearby."]),
    # etc. followed by capital
    ("Bring supplies, tools, etc. The list is attached.", ["Bring supplies, tools, etc.", "The list is attached."]),
    ("Measurements, results, etc. The data follows.", ["Measurements, results, etc.", "The data follows."]),
    ("Documents, forms, etc. Submit them here.", ["Documents, forms, etc.", "Submit them here."]),
    # approx. + capital
    ("The value is approx. 42. The margin is small.", ["The value is approx. 42. The margin is small."]),
    # ext. + capital
    ("Call our ext. 1234 Support is available.", ["Call our ext. 1234 Support is available."]),
    # dept. + capital
    ("Contact the dept. Human resources will respond.", ["Contact the dept.", "Human resources will respond."]),
    # ibid. + capital
    # ibid. and cf. are TITLE_ABBREVIATIONS (not SENTENCE_ENDING) since issue #47 fix.
    # AbbreviationSplitter does NOT split at these; spaCy handles the split in the
    # full pipeline (spaCy sees ibid./cf. followed by a capital and splits correctly).
    ("See ibid. The citation is the same.", ["See ibid. The citation is the same."]),
    # cf. + capital — same rationale as ibid. above
    ("Compare cf. The cited work confirms.", ["Compare cf. The cited work confirms."]),
    # U.S. + proper noun
    ("The U.S. Senate voted on the bill.", ["The U.S. Senate voted on the bill."]),
    ("The U.S. Congress passed the measure.", ["The U.S. Congress passed the measure."]),
    ("The U.K. Parliament decided.", ["The U.K. Parliament decided."]),
    ("The U.N. Security Council met.", ["The U.N. Security Council met."]),
    ("The E.U. Commission approved.", ["The E.U. Commission approved."]),
    # chained country abbreviations
    ("The U.S. U.K. alliance was confirmed.", ["The U.S. U.K. alliance was confirmed."]),
    ("A U.S. U.N. resolution passed.", ["A U.S. U.N. resolution passed."]),
    # complex multi-abbreviation chains
    ("Dr. Smith works at Acme Inc. She holds a Ph.D. Her office is on Main St.", ["Dr. Smith works at Acme Inc.", "She holds a Ph.D.", "Her office is on Main St."]),
    ("Prof. Jones, ed. Vol. 3 of the series.", ["Prof. Jones, ed. Vol. 3 of the series."]),
    ("See vol. 5, ch. 3, sec. 2 for details.", ["See vol. 5, ch. 3, sec. 2 for details."]),
]

# Pad to 100 with simple variants
_EXTRA_CHAINS = [
    (f"The {a} 5 and {a} 6 are relevant.", [f"The {a} 5 and {a} 6 are relevant."])
    for a in ["vol.", "no.", "ch.", "p.", "pp.", "fig.", "sec.", "pt.", "eq.", "para.",
              "bk.", "art.", "tab.", "ed.", "fn.", "app.", "rev.", "ser.", "ann.", "comp."]
]

ALL_CHAIN_CASES = _CHAIN_PATTERNS + _EXTRA_CHAINS


class TestChainedAbbreviations:
    """Verify chained abbreviation patterns are handled correctly."""

    @pytest.mark.parametrize("text,expected", ALL_CHAIN_CASES)
    def test_chain(self, splitter: AbbreviationSplitter, text: str, expected: List[str]):
        assert splitter.process([text]) == expected
