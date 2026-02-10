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
    "approx.",
    "dept.",

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
    "M.B.A.",
    "LL.B.",
    "LL.M.",

    # Business (when at end of sentence)
    "Inc.",
    "Corp.",
    "Ltd.",
    "Co.",
    "Bros.",
    "LLC.",
    "LLP.",

    # Academic/legal citations (can end sentences)
    "ibid.",
    "Ibid.",
    "cf.",
    "Cf.",

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
    "Hon.",
    "Esq.",

    # French/formal titles (common in translated literature)
    "Mme.",
    "Mlle.",
    "Messrs.",

    # Military ranks
    "Gen.",
    "Col.",
    "Capt.",
    "Lt.",
    "Sgt.",
    "Maj.",
    "Cpl.",
    "Pvt.",
    "Adm.",
    "Cmdr.",

    # Political titles
    "Rep.",
    "Sen.",
    "Gov.",
    "Pres.",

    # Ecclesiastical titles
    "Fr.",
    "Msgr.",

    # Geographic prefixes
    "St.",
    "Mt.",
    "Ft.",
    "Ave.",
    "Blvd.",
    "Rd.",

    # Latin terms (never end sentences -- always introduce clauses)
    # Include common inconsistent forms: with/without internal periods,
    # and with trailing comma (the most common real-world form)
    "i.e.",
    "i.e.,",
    "ie.",
    "ie.,",
    "e.g.",
    "e.g.,",
    "eg.",
    "eg.,",
    "viz.",
    "viz.,",

    # Reference/numbering prefixes
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

    # Legal / adversarial
    "vs.",
    "Vs.",
]


# Proper nouns that commonly follow country/organization abbreviations.
# When U.S., U.K., etc. are followed by these words, do NOT split.
# Example: "The U.S. Senate voted" should NOT become "The U.S." + "Senate voted"
COUNTRY_ABBREV_PROPER_NOUNS: List[str] = [
    # U.S. Government bodies
    "Senate",
    "Congress",
    "House",
    "Capitol",
    "Supreme",
    "Federal",
    "National",
    "State",
    "Department",
    "Administration",
    "Agency",
    "Bureau",
    "Commission",
    "Committee",
    "Council",
    "Court",
    "Office",
    "Service",

    # Military
    "Army",
    "Navy",
    "Marines",
    "Marine",
    "Air",
    "Coast",
    "Guard",
    "Military",
    "Forces",
    "Pentagon",

    # Executive
    "President",
    "Vice",
    "Secretary",
    "Attorney",
    "General",
    "Ambassador",

    # U.S. Cabinet Departments
    "Agriculture",
    "Commerce",
    "Labor",
    "Health",
    "Housing",
    "Transportation",
    "Energy",
    "Education",
    "Veterans",

    # Other government entities
    "Postal",
    "Census",
    "Treasury",
    "Interior",
    "Justice",
    "Defense",
    "Homeland",
    "Security",
    "Border",
    "Customs",
    "Immigration",
    "Representatives",  # House of Representatives
    "White",  # White House

    # U.K. specific
    "Parliament",
    "Commons",
    "Lords",
    "Crown",
    "Royal",
    "Prime",
    "Minister",
    "Cabinet",
    "Monarchy",
    "Queen",
    "King",

    # U.N. specific
    "Security",
    "General",
    "Assembly",
    "Peacekeeping",
    "Charter",
    "Resolution",

    # E.U. specific
    "Commission",
    "Parliament",
    "Council",
    "Court",
    "Central",
    "Bank",

    # Generic institutional words
    "Government",
    "Embassy",
    "Consulate",
    "Constitution",
    "Citizen",
    "Citizens",
    "Territory",
    "Dollar",
    "Dollars",
    "Economy",
    "Policy",
    "Law",
    "Code",
]


# Company names that contain exclamation marks as part of the brand.
# Do NOT split on "!" when it's part of these company names.
EXCLAMATION_COMPANY_NAMES: List[str] = [
    "Yahoo!",
    "E!",
    "Jeopardy!",
    "Bam!",
    "Go!",
    "Wham!",
    "Kaboom!",
    "Yum!",
    "FreshDirect!",
    "Boost!",
]
