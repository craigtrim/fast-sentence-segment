#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Known abbreviations that end with periods.

Reference: https://github.com/craigtrim/fast-sentence-segment/issues/3
"""

# Abbreviations that can END a sentence and be followed by a new sentence.
# When these are followed by a capital letter, it likely indicates a sentence break.
from typing import List

SENTENCE_ENDING_ABBREVIATIONS: List[str] = [
    # Time
    "a.m.",
    "p.m.",
    "A.M.",
    "P.M.",

    # Common sentence-enders
    "etc.",
    "ext.",

    # Academic degrees (when at end of sentence)
    "Ph.D.",
    "M.D.",
    "B.A.",
    "B.S.",
    "M.A.",
    "M.S.",
    "Ed.D.",
    "J.D.",
    "D.D.S.",
    "R.N.",

    # Business (when at end of sentence)
    "Inc.",
    "Corp.",
    "Ltd.",
    "Co.",
    "Bros.",

    # Countries/Regions (when at end of sentence)
    "U.S.",
    "U.S.A.",
    "U.K.",
    "U.N.",
    "E.U.",
    "D.C.",
]

# Abbreviations that are NEVER sentence-enders because they're
# typically followed by a name or noun (e.g., "Dr. Smith", "Mt. Everest").
# Do NOT split after these even when followed by a capital letter.
TITLE_ABBREVIATIONS: List[str] = [
    # Personal titles
    "Dr.",
    "Mr.",
    "Mrs.",
    "Ms.",
    "Prof.",
    "Sr.",
    "Jr.",
    "Rev.",
    "Gen.",
    "Col.",
    "Capt.",
    "Lt.",
    "Sgt.",
    "Rep.",
    "Sen.",
    "Gov.",
    "Pres.",
    "Hon.",

    # Geographic prefixes
    "St.",
    "Mt.",
    "Ft.",

    # Other prefixes
    "Fig.",
    "fig.",
    "Sec.",
    "sec.",
    "Ch.",
    "ch.",
    "Art.",
    "art.",
    "Vol.",
    "vol.",
    "No.",
    "no.",
    "Pt.",
    "pt.",
]
