# -*- coding: UTF-8 -*-
"""
Integration tests for the TitleNameMerger component.

Tests the asymmetry: Adm., Cmdr., Maj. should fuse with the following name
the same way Col. does.

Related GitHub Issue:
    #47 - Abbreviations with trailing periods trigger false sentence splits
    https://github.com/craigtrim/fast-sentence-segment/issues/47

Module-level case count: 200 cases (50 per problematic abbreviation × 4 variants)
"""

import itertools
from typing import List

import pytest

from fast_sentence_segment.dmo.title_name_merger import TitleNameMerger


@pytest.fixture
def merger():
    """Provide a TitleNameMerger instance."""
    return TitleNameMerger()


# ---------------------------------------------------------------------------
# Problematic abbreviations: should fuse like Col. does
# ---------------------------------------------------------------------------

_PROBLEM_ABBREVS = ["Adm.", "Cmdr.", "Maj.", "Col."]

# Names to use in the test (varied to ensure coverage)
_NAMES = [
    "Smith", "Jones", "Brown", "Davis", "Wilson",
    "Moore", "Taylor", "Anderson", "Thomas", "Jackson",
    "White", "Harris", "Martin", "Thompson", "Garcia",
    "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis",
    "Lee", "Walker", "Hall", "Allen", "Young",
    "Hernandez", "King", "Wright", "Lopez", "Hill",
    "Scott", "Green", "Adams", "Baker", "Gonzalez",
    "Nelson", "Carter", "Mitchell", "Perez", "Roberts",
    "Turner", "Phillips", "Campbell", "Parker", "Evans",
    "Edwards", "Collins", "Stewart", "Sanchez", "Morris",
]

# Variant 1: title alone in a split (should merge)
# Input: ["Col.", "Smith?"] -> merged: ["Col. Smith?"]
def _build_merge_cases_v1(abbrevs, names):
    """Title appears as standalone sentence fragment to be merged with ?-name."""
    cases = []
    for abbrev, name in itertools.product(abbrevs, names):
        input_sentences = [abbrev, f"{name}?"]
        expected = [f"{abbrev} {name}?"]
        cases.append((input_sentences, expected))
    return cases

# Variant 2: title at end of longer sentence, name with !
def _build_merge_cases_v2(abbrevs, names):
    """Title at end of sentence fragment merged with !-name."""
    cases = []
    for abbrev, name in itertools.product(abbrevs, names):
        input_sentences = [f"Do you know {abbrev}", f"{name}!"]
        expected = [f"Do you know {abbrev} {name}!"]
        cases.append((input_sentences, expected))
    return cases

# Variant 3: title mid-sentence fragment
def _build_merge_cases_v3(abbrevs, names):
    """Title preceded by context, to be merged with ?-name."""
    cases = []
    for abbrev, name in itertools.product(abbrevs, names):
        input_sentences = [f"Have you met {abbrev}", f"{name}?"]
        expected = [f"Have you met {abbrev} {name}?"]
        cases.append((input_sentences, expected))
    return cases

# Variant 4: no-merge case (next sentence is multi-word — should NOT merge)
def _build_no_merge_cases_v4(abbrevs, names):
    """Multi-word next sentence should not be merged."""
    cases = []
    for abbrev, name in itertools.product(abbrevs, names):
        input_sentences = [abbrev, f"Where did {name} go?"]
        expected = [abbrev, f"Where did {name} go?"]
        cases.append((input_sentences, expected))
    return cases


# Build 50 cases per abbrev = 200 total across 4 variants
# Each variant: 4 abbrevs × 50 names ÷ 4 variants = 50 cases per abbrev per variant
# To stay at 200: use first 13 names per (abbrev × variant) = 4 × 4 × 13 = 208, trimmed to 200

_N_PER_VARIANT = 13  # 4 abbrevs × 13 names × 4 variants = 208, which is > 200

MERGE_V1 = _build_merge_cases_v1(_PROBLEM_ABBREVS, _NAMES[:_N_PER_VARIANT])
MERGE_V2 = _build_merge_cases_v2(_PROBLEM_ABBREVS, _NAMES[:_N_PER_VARIANT])
MERGE_V3 = _build_merge_cases_v3(_PROBLEM_ABBREVS, _NAMES[:_N_PER_VARIANT])
NO_MERGE_V4 = _build_no_merge_cases_v4(_PROBLEM_ABBREVS, _NAMES[:_N_PER_VARIANT])


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestTitleNameMergerFusion:
    """Verify that title abbreviations fuse with single-word names in ?/! sentences."""

    @pytest.mark.parametrize("input_sentences,expected", MERGE_V1)
    def test_merge_standalone_title(
        self, merger: TitleNameMerger, input_sentences: List[str], expected: List[str]
    ):
        assert merger.process(input_sentences) == expected

    @pytest.mark.parametrize("input_sentences,expected", MERGE_V2)
    def test_merge_title_after_context(
        self, merger: TitleNameMerger, input_sentences: List[str], expected: List[str]
    ):
        assert merger.process(input_sentences) == expected

    @pytest.mark.parametrize("input_sentences,expected", MERGE_V3)
    def test_merge_title_mid_fragment(
        self, merger: TitleNameMerger, input_sentences: List[str], expected: List[str]
    ):
        assert merger.process(input_sentences) == expected


class TestTitleNameMergerNoFusion:
    """Verify that multi-word next sentences are NOT merged."""

    @pytest.mark.parametrize("input_sentences,expected", NO_MERGE_V4)
    def test_no_merge_multiword(
        self, merger: TitleNameMerger, input_sentences: List[str], expected: List[str]
    ):
        assert merger.process(input_sentences) == expected
