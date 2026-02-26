# -*- coding: UTF-8 -*-
"""
Programmatically generated tests for scholarly and domain abbreviations.

Related GitHub Issue:
    #47 - Abbreviations with trailing periods trigger false sentence splits
    https://github.com/craigtrim/fast-sentence-segment/issues/47

Module-level case count: 5,250 no-split + 21 must-split = 5,271 total cases
"""

import itertools
import re
from typing import Callable, List

import pytest

SegmentationFunc = Callable[[str], List[str]]

# ---------------------------------------------------------------------------
# Full abbreviation registry
# ---------------------------------------------------------------------------
ABBREVS = {
    "scholarly": [
        "cf.", "viz.", "ibid.", "et al.", "et seq.", "op. cit.", "loc. cit.",
        "ca.", "c.", "fl.", "sc.", "s.v.", "N.B.", "P.S.", "P.P.S.",
        "pro tem.", "sic.", "inf.", "sup.", "ad loc.", "scil.", "vid.",
        "resp.", "ad fin.", "ad init.", "ad inf.", "in loc.", "in re.",
        "in ext.", "in toto.", "ut sup.", "ut inf.", "id.", "ead.",
        "ap.", "ff.", "a.k.a.", "n.b.", "q.v.", "q.e.d.", "r.i.p.",
        "s.a.", "s.l.", "s.n.", "v.i.", "v.s.", "e.a.", "c.f.",
    ],
    "titles": [
        "Mr.", "Mrs.", "Ms.", "Dr.", "Prof.", "Sr.", "Jr.", "Rev.", "Hon.",
        "Esq.", "Msgr.", "Fr.", "Br.", "Insp.", "Supt.", "Asst.", "Atty.",
        "Dir.", "Mgr.", "Pres.", "Mme.", "Mlle.", "Messrs.",
    ],
    "military": [
        "Gen.", "Col.", "Maj.", "Capt.", "Lt.", "Sgt.", "Cpl.", "Pvt.",
        "Adm.", "Cmdr.", "Ens.", "Brig.", "Spec.", "Pfc.",
    ],
    "government": [
        "Gov.", "Sen.", "Rep.", "Sec.", "Amb.", "Commr.", "Cllr.",
        "Cong.", "Del.", "Dep.", "Min.",
    ],
    "geographic": [
        "St.", "Ave.", "Blvd.", "Mt.", "Ft.", "Rd.", "Ln.", "Ct.", "Pl.",
        "Sq.", "Ter.", "Hwy.", "Pkwy.", "Rte.", "Twp.", "Bldg.", "Ste.",
        "Apt.", "Jct.", "Ctr.", "Isl.", "Pen.", "Riv.", "Lk.", "Mtn.",
    ],
    "months": [
        "Jan.", "Feb.", "Mar.", "Apr.", "Jun.", "Jul.", "Aug.",
        "Sep.", "Sept.", "Oct.", "Nov.", "Dec.",
    ],
    "days": [
        "Mon.", "Tue.", "Tues.", "Wed.", "Thu.", "Thur.", "Thurs.",
        "Fri.", "Sat.", "Sun.",
    ],
    "business": [
        "Inc.", "Corp.", "Ltd.", "Co.", "Bros.", "Assoc.", "Grp.",
        "Intl.", "Mfg.", "Dist.", "Mgmt.", "Ent.", "Tech.", "vs.",
    ],
    "academic": [
        "vol.", "p.", "pp.", "ed.", "eds.", "fig.", "eq.", "no.", "ch.",
        "sec.", "para.", "app.", "rev.", "trans.", "repr.", "suppl.", "bk.",
        "pt.", "ser.", "fn.", "ann.", "abr.", "illus.", "comp.", "tab.",
        "art.", "introd.", "def.", "ex.", "pref.", "lit.",
        "vols.", "nos.", "chs.", "figs.", "n.", "nn.", "secs.", "arts.",
        "paras.", "l.", "ll.", "bks.", "mss.", "ms.", "pars.",
        "fol.", "fols.", "cols.", "frag.", "id.", "rpt.", "supp.", "annot.",
        "corr.", "appx.",
    ],
    "measurements": [
        "approx.", "est.", "min.", "max.", "avg.", "std.", "sq.", "wt.",
        "ht.", "temp.", "alt.", "lat.", "lon.", "diam.", "deg.", "qty.", "cap.",
    ],
    "medical": [
        "dept.", "diag.", "symp.", "anat.", "biol.", "chem.", "phys.",
        "psych.", "surg.", "ped.", "pharm.", "vet.", "neuro.", "cardio.",
        "derm.", "ortho.", "path.", "rad.", "sp.", "ssp.", "var.", "fam.", "ord.",
    ],
    "grammar": [
        "adj.", "adv.", "prep.", "conj.", "pron.", "pl.", "sing.", "colloq.",
        "dial.", "arch.", "obs.", "esp.", "prob.", "usu.", "occas.", "attrib.",
        "compar.", "superl.", "refl.", "subj.", "imper.",
    ],
    "latin_extended": [
        "s.vv.", "ad med.", "ad litt.", "ad rem.", "in ext.", "ut cit.",
        "ut al.", "cap.", "lib.", "libb.", "tit.", "gl.", "gloss.", "schol.",
        "cod.", "codd.", "fr.", "serm.", "hom.", "lect.", "quaest.", "disp.",
        "art. cit.", "a.d.", "a.c.", "b.c.", "a.u.c.", "i.q.", "i.c.",
        "l.c.", "l.s.", "m.s.", "n.d.", "n.p.", "n.s.", "n.t.", "p.c.",
        "p.p.", "t.b.",
    ],
    "general": [
        "anon.", "b.", "d.", "r.", "auth.", "bibl.", "biog.", "calc.", "cat.",
        "cent.", "cit.", "cl.", "coll.", "comm.", "conc.", "conf.", "const.",
        "cont.", "crit.", "deriv.", "dict.", "disc.", "doc.", "dram.", "eccl.",
        "encyc.", "eval.", "excl.", "exec.", "expl.", "gram.", "hist.", "incl.",
        "juris.", "lang.", "misc.", "mod.", "natl.", "orig.", "phil.", "proc.",
        "prov.", "pub.", "rec.", "ref.", "reg.", "rel.", "sched.", "sect.",
        "spec.", "stat.", "struct.", "symb.", "syn.", "trad.",
    ],
}

# ---------------------------------------------------------------------------
# Template sets (15 per category)
# ---------------------------------------------------------------------------

_SCHOLARLY_TEMPLATES = [
    "Refer to {a} Week 7 for context.",
    "See {a} the overview for details.",
    "The text, {a} the cited source, demonstrates this.",
    "As noted in {a} the report, this is correct.",
    "Per {a} Smith 2024, the result is positive.",
    "Compare {a} Week 5 for the earlier result.",
    "The finding {a} the prior work confirms this.",
    "Note {a} the appendix for further reading.",
    "This approach, {a} the original paper, works well.",
    "The rule, {a} the specification, applies here.",
    "The committee reviewed {a} Week 3 materials.",
    "Findings presented in {a} Week 9 were discussed.",
    "Background information in {a} Week 1 is relevant.",
    "Supplementary material in {a} Week 12 confirms this.",
    "Details from {a} Week 4 are summarised below.",
]

_PERSON_TEMPLATES = [
    "{a} Smith attended the meeting.",
    "The report was filed by {a} Smith.",
    "I spoke with {a} Smith yesterday.",
    "Please contact {a} Smith directly.",
    "According to {a} Smith, the results are clear.",
    "We consulted {a} Smith on this matter.",
    "The decision was made by {a} Smith.",
    "{a} Smith and the team completed the work.",
    "We await {a} Smith's response.",
    "The project lead is {a} Smith.",
    "The committee chair was {a} Smith.",
    "All parties deferred to {a} Smith.",
    "Documents were signed by {a} Smith.",
    "The review board included {a} Smith.",
    "Final approval came from {a} Smith.",
]

_GEOGRAPHIC_TEMPLATES = [
    "He lives on Main {a} near the park.",
    "The office is at 123 Main {a}.",
    "She works near Fifth {a} and Oak.",
    "Turn left at Elm {a} and proceed north.",
    "The building is on Park {a}.",
    "Walk down Maple {a} for two blocks.",
    "The clinic is on Oak {a} near downtown.",
    "I passed through Oak {a} this morning.",
    "The school is at the corner of {a} and Oak.",
    "Proceed along River {a} until you reach the bridge.",
    "The station is on Cedar {a} downtown.",
    "She met him at Birch {a} and Pine.",
    "Drive along Willow {a} for a mile.",
    "The park entrance is on Spruce {a}.",
    "The hospital is located on Walnut {a}.",
]

_MONTH_TEMPLATES = [
    "The meeting is on {a} 15.",
    "He was born on {a} 3, 1990.",
    "The deadline is {a} 31.",
    "Last {a} 5, the report was filed.",
    "Submit by {a} 1 at the latest.",
    "The event runs from {a} 10 to {a} 20.",
    "The quarter ends on {a} 30.",
    "Results are due {a} 7.",
    "The review period begins {a} 1.",
    "The fiscal year starts {a} 15.",
    "The conference opens {a} 8.",
    "The grant deadline is {a} 14.",
    "Registration closes {a} 22.",
    "The study period ends {a} 28.",
    "Payments are due by {a} 10.",
]

_DAY_TEMPLATES = [
    "The meeting is on {a} at 3pm.",
    "We meet every {a} morning.",
    "The deadline falls on {a} this week.",
    "Sessions run from {a} through {a}.",
    "The office is closed on {a}.",
    "Submit your work by {a} afternoon.",
    "The seminar is scheduled for {a}.",
    "Attendance is required on {a}.",
    "The report is due by {a} noon.",
    "Office hours are held on {a}.",
    "The lab is open on {a} only.",
    "Team check-ins happen on {a}.",
    "The review session is on {a}.",
    "Deliverables are expected on {a}.",
    "The workshop runs on {a}.",
]

_NUMERIC_TEMPLATES = [
    "See {a} 3 for the full breakdown.",
    "Refer to {a} 42 of the document.",
    "As noted in {a} 7, the rule applies.",
    "The result appears in {a} 15.",
    "Compare {a} 8 with the earlier version.",
    "The data in {a} 12 confirms this finding.",
    "See {a} 100 for the complete listing.",
    "Refer to {a} 5 and also {a} 6.",
    "The table in {a} 23 shows the breakdown.",
    "Per {a} 2, this is the correct interpretation.",
    "The committee reviewed {a} 3 materials.",
    "Findings presented in {a} 9 were discussed.",
    "Background in {a} 1 is relevant.",
    "Supplementary data in {a} 12 confirms this.",
    "Details from {a} 4 are summarised below.",
]

_BUSINESS_TEMPLATES = [
    "Apple {a} released a new product.",
    "Contact Acme {a} for further details.",
    "The filing was submitted by Global {a}.",
    "We work with National {a} on projects.",
    "The contract was signed by Pacific {a}.",
    "Regional {a} confirmed the order.",
    "Allied {a} announced their earnings.",
    "Summit {a} is expanding operations.",
    "Apex {a} filed the quarterly report.",
    "Vanguard {a} hired fifty new staff.",
    "The committee reviewed Global {a} proposals.",
    "Findings from Premier {a} were discussed.",
    "Background on Coastal {a} is relevant.",
    "Supplementary data from Delta {a} confirms this.",
    "Details from Meridian {a} are summarised below.",
]

# ---------------------------------------------------------------------------
# Helper: pick template set per category
# ---------------------------------------------------------------------------

def _templates_for(category: str) -> list:
    if category == "scholarly":
        return _SCHOLARLY_TEMPLATES
    elif category in ("titles", "military", "government"):
        return _PERSON_TEMPLATES
    elif category == "geographic":
        return _GEOGRAPHIC_TEMPLATES
    elif category == "months":
        return _MONTH_TEMPLATES
    elif category == "days":
        return _DAY_TEMPLATES
    elif category == "business":
        return _BUSINESS_TEMPLATES
    else:
        return _NUMERIC_TEMPLATES


# ---------------------------------------------------------------------------
# Build no-split cases
# ---------------------------------------------------------------------------

def _build_no_split_cases():
    cases = []
    for category, abbrevs in ABBREVS.items():
        templates = _templates_for(category)
        for abbrev, template in itertools.product(abbrevs, templates):
            text = template.replace("{a}", abbrev)
            # PostProcessStructure normalizes isolated ".." (not ellipsis) to ".".
            # When a template ends with "." and the abbreviation also ends with
            # ".", the combined text has a trailing "..".  The expected output
            # reflects the cleaned form.
            expected = re.sub(r'(?<!\.)\.\.(?!\.)$', '.', text)
            cases.append((text, [expected]))
    return cases


NO_SPLIT_CASES = _build_no_split_cases()

# ---------------------------------------------------------------------------
# Must-split cases (terminal abbreviations only)
# ---------------------------------------------------------------------------

_TERMINAL_ABBREVS = ["Inc.", "Corp.", "Ltd.", "Co.", "Bros."]

MUST_SPLIT_CASES = []
for _a in _TERMINAL_ABBREVS:
    MUST_SPLIT_CASES.extend([
        (
            f"I work at Acme {_a} Dr. Smith is my boss.",
            [f"I work at Acme {_a}", "Dr. Smith is my boss."],
        ),
        (
            f"The document notes {_a} The analysis follows.",
            [f"The document notes {_a}", "The analysis follows."],
        ),
        (
            f"She holds a degree, {_a} Her research continues.",
            [f"She holds a degree, {_a}", "Her research continues."],
        ),
    ])

ALL_CASES = NO_SPLIT_CASES + MUST_SPLIT_CASES

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestScholarlyNoSplit:
    """Verify that abbreviations mid-clause do not trigger sentence splits."""

    @pytest.mark.parametrize("text,expected", NO_SPLIT_CASES)
    def test_no_split(self, segment: SegmentationFunc, text: str, expected: list):
        assert segment(text) == expected


class TestTerminalAbbreviationSplit:
    """Verify that terminal abbreviations (Inc., Corp., etc.) do trigger splits."""

    @pytest.mark.parametrize("text,expected", MUST_SPLIT_CASES)
    def test_must_split(self, segment: SegmentationFunc, text: str, expected: list):
        assert segment(text) == expected
