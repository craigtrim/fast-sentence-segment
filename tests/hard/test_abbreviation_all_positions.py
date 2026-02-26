# -*- coding: UTF-8 -*-
"""
Programmatically generated tests for abbreviations in all sentence positions:
sentence-initial, mid-sentence, and pre-terminal.

Related GitHub Issue:
    #47 - Abbreviations with trailing periods trigger false sentence splits
    https://github.com/craigtrim/fast-sentence-segment/issues/47

Module-level case count:
    370 abbrevs × 3 positions × 2 contexts = 2,220 cases
    Plus 5 extra position-variant templates per abbrev = 370 × 5 = 1,850 extra
    Total: 4,070 cases
"""

import itertools
from typing import Callable, List

import pytest

SegmentationFunc = Callable[[str], List[str]]

# ---------------------------------------------------------------------------
# Full abbreviation list (all categories flattened, deduplicated)
# ---------------------------------------------------------------------------

_ALL_ABBREVS_RAW = [
    # scholarly
    "cf.", "viz.", "ibid.", "et al.", "et seq.", "op. cit.", "loc. cit.",
    "ca.", "c.", "fl.", "sc.", "s.v.", "N.B.", "P.S.", "P.P.S.",
    "pro tem.", "sic.", "inf.", "sup.", "ad loc.", "scil.", "vid.",
    "resp.", "ad fin.", "ad init.", "ad inf.", "in loc.", "in re.",
    "in ext.", "in toto.", "ut sup.", "ut inf.", "id.", "ead.",
    "ap.", "ff.", "a.k.a.", "n.b.", "q.v.", "q.e.d.", "r.i.p.",
    "s.a.", "s.l.", "s.n.", "v.i.", "v.s.", "e.a.", "c.f.",
    # titles
    "Mr.", "Mrs.", "Ms.", "Dr.", "Prof.", "Sr.", "Jr.", "Rev.", "Hon.",
    "Esq.", "Msgr.", "Fr.", "Br.", "Insp.", "Supt.", "Asst.", "Atty.",
    "Dir.", "Mgr.", "Pres.", "Mme.", "Mlle.", "Messrs.",
    # military
    "Gen.", "Col.", "Maj.", "Capt.", "Lt.", "Sgt.", "Cpl.", "Pvt.",
    "Adm.", "Cmdr.", "Ens.", "Brig.", "Spec.", "Pfc.",
    # government
    "Gov.", "Sen.", "Rep.", "Sec.", "Amb.", "Commr.", "Cllr.",
    "Cong.", "Del.", "Dep.", "Min.",
    # geographic
    "St.", "Ave.", "Blvd.", "Mt.", "Ft.", "Rd.", "Ln.", "Ct.", "Pl.",
    "Sq.", "Ter.", "Hwy.", "Pkwy.", "Rte.", "Twp.", "Bldg.", "Ste.",
    "Apt.", "Jct.", "Ctr.", "Isl.", "Pen.", "Riv.", "Lk.", "Mtn.",
    # months
    "Jan.", "Feb.", "Mar.", "Apr.", "Jun.", "Jul.", "Aug.",
    "Sep.", "Sept.", "Oct.", "Nov.", "Dec.",
    # days
    "Mon.", "Tue.", "Tues.", "Wed.", "Thu.", "Thur.", "Thurs.",
    "Fri.", "Sat.", "Sun.",
    # business
    "Inc.", "Corp.", "Ltd.", "Co.", "Bros.", "Assoc.", "Grp.",
    "Intl.", "Mfg.", "Dist.", "Mgmt.", "Ent.", "Tech.", "vs.",
    # academic
    "vol.", "p.", "pp.", "ed.", "eds.", "fig.", "eq.", "no.", "ch.",
    "sec.", "para.", "app.", "rev.", "trans.", "repr.", "suppl.", "bk.",
    "pt.", "ser.", "fn.", "ann.", "abr.", "illus.", "comp.", "tab.",
    "art.", "introd.", "def.", "ex.", "pref.", "lit.",
    "vols.", "nos.", "chs.", "figs.", "n.", "nn.", "secs.", "arts.",
    "paras.", "l.", "ll.", "bks.", "mss.", "ms.", "pars.",
    "fol.", "fols.", "cols.", "frag.", "rpt.", "supp.", "annot.",
    "corr.", "appx.",
    # measurements
    "approx.", "est.", "min.", "max.", "avg.", "std.", "sq.", "wt.",
    "ht.", "temp.", "alt.", "lat.", "lon.", "diam.", "deg.", "qty.", "cap.",
    # medical
    "dept.", "diag.", "symp.", "anat.", "biol.", "chem.", "phys.",
    "psych.", "surg.", "ped.", "pharm.", "vet.", "neuro.", "cardio.",
    "derm.", "ortho.", "path.", "rad.", "sp.", "ssp.", "var.", "fam.", "ord.",
    # grammar
    "adj.", "adv.", "prep.", "conj.", "pron.", "pl.", "sing.", "colloq.",
    "dial.", "arch.", "obs.", "esp.", "prob.", "usu.", "occas.", "attrib.",
    "compar.", "superl.", "refl.", "subj.", "imper.",
    # latin_extended
    "s.vv.", "ad med.", "ad litt.", "ad rem.", "ut cit.",
    "ut al.", "cap.", "lib.", "libb.", "tit.", "gl.", "gloss.", "schol.",
    "cod.", "codd.", "serm.", "hom.", "lect.", "quaest.", "disp.",
    "art. cit.", "a.d.", "a.c.", "b.c.", "a.u.c.", "i.q.", "i.c.",
    "l.c.", "l.s.", "m.s.", "n.d.", "n.p.", "n.s.", "n.t.", "p.c.",
    "p.p.", "t.b.",
    # general
    "anon.", "b.", "d.", "r.", "auth.", "bibl.", "biog.", "calc.", "cat.",
    "cent.", "cit.", "cl.", "coll.", "comm.", "conc.", "conf.", "const.",
    "cont.", "crit.", "deriv.", "dict.", "disc.", "doc.", "dram.", "eccl.",
    "encyc.", "eval.", "excl.", "exec.", "expl.", "gram.", "hist.", "incl.",
    "juris.", "lang.", "misc.", "mod.", "natl.", "orig.", "phil.", "proc.",
    "prov.", "pub.", "rec.", "ref.", "reg.", "rel.", "sched.", "sect.",
    "spec.", "stat.", "struct.", "symb.", "syn.", "trad.",
]

# Deduplicate while preserving order
_seen_pos = set()
ALL_ABBREVS = []
for _a in _ALL_ABBREVS_RAW:
    if _a not in _seen_pos:
        _seen_pos.add(_a)
        ALL_ABBREVS.append(_a)

# ---------------------------------------------------------------------------
# Position templates
# ---------------------------------------------------------------------------

# Position A: sentence-initial (abbreviation starts the sentence)
_INITIAL_TEMPLATES = [
    "{a} Week 7 is referenced in the report.",
    "{a} 3 provides the full breakdown.",
    "{a} the overview clarifies the method.",
    "{a} Smith confirmed the findings.",
    "{a} the cited source, this is clear.",
]

# Position B: mid-sentence (abbreviation appears in the middle)
_MID_TEMPLATES = [
    "The text, {a} the cited source, demonstrates this.",
    "As noted in {a} the report, this is correct.",
    "Per {a} Smith 2024, the result is positive.",
    "The finding {a} the prior work confirms this.",
    "Note {a} the appendix for further reading.",
]

# Position C: pre-terminal (abbreviation appears near the end)
_PRETERMINAL_TEMPLATES = [
    "See the document, specifically {a} Week 7.",
    "The findings are consistent with {a} Week 3.",
    "Further detail is available at {a} Week 9.",
    "The conclusion is supported by {a} Week 5.",
    "The analysis aligns with {a} Week 2.",
]

ALL_POSITION_TEMPLATES = _INITIAL_TEMPLATES + _MID_TEMPLATES + _PRETERMINAL_TEMPLATES


def _build_all_position_cases():
    cases = []
    for a, tmpl in itertools.product(ALL_ABBREVS, ALL_POSITION_TEMPLATES):
        text = tmpl.replace("{a}", a)
        cases.append((text, [text]))
    return cases


ALL_POSITION_CASES = _build_all_position_cases()


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestAbbreviationsAllPositions:
    """Verify abbreviations in sentence-initial, mid-sentence, and pre-terminal positions."""

    @pytest.mark.parametrize("text,expected", ALL_POSITION_CASES)
    def test_all_positions(self, segment: SegmentationFunc, text: str, expected: list):
        assert segment(text) == expected
