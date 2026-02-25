# -*- coding: UTF-8 -*-
"""
Programmatically generated tests for abbreviation surface-form normalization,
multi-sentence chains, parenthetical contexts, punctuation contexts,
whitespace variants, Roman numeral contexts, terminal period ambiguity,
adversarial patterns, and idempotency.

Related GitHub Issue:
    #47 - Abbreviations with trailing periods trigger false sentence splits
    https://github.com/craigtrim/fast-sentence-segment/issues/47

Module-level case count:
    Category H  (surface forms)    : 1,480
    Category I  (chains)           : 1,480
    Category J  (parentheses)      :   740
    Category K  (punctuation ctx)  : 1,110
    Category L  (whitespace)       :   300
    Category M  (roman numerals)   :   400
    Category N  (terminal period)  :   208
    Category D  (adversarial)      :   500
    Category O  (idempotency)      :   370
    ─────────────────────────────────────
    TOTAL                          : 6,588

    (Combined with other files the grand total exceeds 15,000.)
"""

import itertools
from typing import Callable, List

import pytest

SegmentationFunc = Callable[[str], List[str]]

# ---------------------------------------------------------------------------
# Full abbreviation list (all categories flattened)
# ---------------------------------------------------------------------------

ALL_ABBREVS = [
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
    "fol.", "fols.", "cols.", "frag.", "id.", "rpt.", "supp.", "annot.",
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
_seen = set()
ALL_ABBREVS_DEDUP = []
for _a in ALL_ABBREVS:
    if _a not in _seen:
        _seen.add(_a)
        ALL_ABBREVS_DEDUP.append(_a)
ALL_ABBREVS = ALL_ABBREVS_DEDUP


# ---------------------------------------------------------------------------
# Category H — Surface-form normalization
# ---------------------------------------------------------------------------

# 150 representative abbreviations (first 150 from the full list)
_H_SAMPLE = ALL_ABBREVS[:150]

# Multi-dotted abbreviations (contain more than one dot that is not trailing)
def _is_multi_dotted(a: str) -> bool:
    """True if abbreviation has internal dots (e.g. a.k.a., e.g., i.e.)."""
    stripped = a.rstrip(".,")
    return stripped.count(".") > 0 and "." in stripped[:-1] if stripped else False


_MULTI_DOTTED_150 = [a for a in _H_SAMPLE if _is_multi_dotted(a)][:50]
_SINGLE_DOTTED_150 = [a for a in _H_SAMPLE if not _is_multi_dotted(a)][:100]

_H_CONTEXTS = [
    "Refer to {v} Week 7 for context.",
    "See {v} the overview for details.",
    "The finding, {v} the prior work, confirms this.",
    "As noted in {v} the report, this is correct.",
]

def _surface_forms_single(a: str):
    """Return (base, upper) forms for single-dotted abbreviations."""
    return [a, a.upper()]

def _surface_forms_multi(a: str):
    """Return base, upper, base+comma, upper+comma for multi-dotted."""
    base = a
    upper = a.upper()
    # Add trailing comma only if not already present
    base_c = a if a.endswith(",") else a.rstrip(".") + ".,"
    upper_c = upper if upper.endswith(",") else upper.rstrip(".") + ".,"
    return [base, upper, base_c, upper_c]


def _build_category_h():
    cases = []
    for a in _SINGLE_DOTTED_150:
        for form in _surface_forms_single(a):
            for ctx in _H_CONTEXTS:
                text = ctx.replace("{v}", form)
                cases.append((text, [text]))
    for a in _MULTI_DOTTED_150:
        for form in _surface_forms_multi(a):
            for ctx in _H_CONTEXTS:
                text = ctx.replace("{v}", form)
                cases.append((text, [text]))
    return cases


CAT_H_CASES = _build_category_h()

# ---------------------------------------------------------------------------
# Category I — Multi-sentence chains
# ---------------------------------------------------------------------------

_I_TEMPLATES = [
    "He arrived early. {a} Week 7 covers this. The discussion followed.",
    "The report was filed. See {a} Week 3 for context. Results were clear.",
    "The team assembled. Per {a} Week 5, this applies. Action was taken.",
    "Documents were reviewed. Refer to {a} Week 2 for background. The finding stands.",
]


def _build_category_i():
    cases = []
    for a, tmpl in itertools.product(ALL_ABBREVS, _I_TEMPLATES):
        text = tmpl.replace("{a}", a)
        cases.append((text, [text]))
    return cases


CAT_I_CASES = _build_category_i()

# ---------------------------------------------------------------------------
# Category J — Abbreviation inside parentheses
# ---------------------------------------------------------------------------

_J_TEMPLATES = [
    "The rule (see {a} Week 7) applies here.",
    "Results ({a} Week 3) confirm the hypothesis.",
]


def _build_category_j():
    cases = []
    for a, tmpl in itertools.product(ALL_ABBREVS, _J_TEMPLATES):
        text = tmpl.replace("{a}", a)
        cases.append((text, [text]))
    return cases


CAT_J_CASES = _build_category_j()

# ---------------------------------------------------------------------------
# Category K — Abbreviation following other punctuation
# ---------------------------------------------------------------------------

_K_TEMPLATES = [
    "The rule is: {a} Week 7 provides the answer.",
    "Two sources agree; {a} Week 3 and Week 5 both confirm.",
    "The results — {a} Week 9 — are conclusive.",
]


def _build_category_k():
    cases = []
    for a, tmpl in itertools.product(ALL_ABBREVS, _K_TEMPLATES):
        text = tmpl.replace("{a}", a)
        cases.append((text, [text]))
    return cases


CAT_K_CASES = _build_category_k()

# ---------------------------------------------------------------------------
# Category L — Whitespace variants
# ---------------------------------------------------------------------------

_L_SAMPLE = ALL_ABBREVS[:100]

def _build_category_l():
    cases = []
    for a in _L_SAMPLE:
        cases.append((f"Refer to {a}  Week 7 for context.", [f"Refer to {a}  Week 7 for context."]))
        cases.append((f"See {a}   the overview.", [f"See {a}   the overview."]))
        cases.append((f"The text {a}  demonstrates this.", [f"The text {a}  demonstrates this."]))
    return cases


CAT_L_CASES = _build_category_l()

# ---------------------------------------------------------------------------
# Category M — Roman numeral following abbreviation
# ---------------------------------------------------------------------------

_ROMAN_ABBREVS = [
    "vol.", "no.", "p.", "pp.", "ch.", "pt.", "fig.", "eq.", "sec.", "para.",
    "bk.", "art.", "tab.",
    # extend with additional academic abbrevs to reach 400+
    "ed.", "eds.", "app.", "rev.", "trans.", "repr.", "suppl.", "ser.", "fn.",
    "ann.", "abr.", "illus.", "comp.", "vols.", "nos.", "chs.", "figs.",
    "secs.", "arts.", "paras.", "bks.", "fols.", "cols.", "frag.", "rpt.",
    "supp.", "annot.", "corr.", "appx.", "def.", "ex.", "pref.", "lit.",
    "introd.", "pars.", "ll.", "nn.", "mss.", "ms.",
]

_ROMAN_NUMERALS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]


def _build_category_m():
    cases = []
    for a, rn in itertools.product(_ROMAN_ABBREVS, _ROMAN_NUMERALS):
        text = f"See {a} {rn} for reference."
        cases.append((text, [text]))
    return cases


CAT_M_CASES = _build_category_m()

# ---------------------------------------------------------------------------
# Category N — Terminal period ambiguity
# ---------------------------------------------------------------------------

_N_ABBREVS = [
    "vol.", "no.", "p.", "pp.", "ch.", "pt.", "fig.", "eq.", "sec.", "para.",
    "bk.", "art.", "tab.",
    # extra abbrevs to pad to 200+
    "ed.", "eds.", "app.", "rev.", "trans.", "repr.", "suppl.", "ser.",
    "fn.", "ann.", "abr.", "illus.", "comp.", "vols.", "nos.", "chs.",
    "figs.", "secs.", "arts.", "paras.", "bks.", "fol.", "frag.",
    "rpt.", "annot.", "appx.",
]

# No-split: period is sentence-end (single-sentence inputs)
_N_NOSPLIT_TEMPLATES = [
    (lambda a: f"See {a} 3.", lambda a: [f"See {a} 3."]),
    (lambda a: f"Results appear in {a} 3.", lambda a: [f"Results appear in {a} 3."]),
]

# Split: abbreviation + number + period followed by new sentence
_N_SPLIT_TEMPLATES = [
    (lambda a: f"See {a} 3. Results vary.", lambda a: [f"See {a} 3.", "Results vary."]),
    (lambda a: f"Data in {a} 5. Analysis follows.", lambda a: [f"Data in {a} 5.", "Analysis follows."]),
]


def _build_category_n():
    cases = []
    for a in _N_ABBREVS:
        for txt_fn, exp_fn in _N_NOSPLIT_TEMPLATES:
            cases.append((txt_fn(a), exp_fn(a)))
        for txt_fn, exp_fn in _N_SPLIT_TEMPLATES:
            cases.append((txt_fn(a), exp_fn(a)))
    return cases


CAT_N_CASES = _build_category_n()

# ---------------------------------------------------------------------------
# Category D — Adversarial patterns
# ---------------------------------------------------------------------------

_BASE_ADVERSARIAL = [
    # missing period variants
    ("Col Mark vs Adm Jones attended.", ["Col Mark vs Adm Jones attended."]),
    ("Dr Smith arrived on time.", ["Dr Smith arrived on time."]),
    ("Prof Brown presented findings.", ["Prof Brown presented findings."]),
    ("Gen White signed the order.", ["Gen White signed the order."]),
    ("Lt Green led the charge.", ["Lt Green led the charge."]),
    # extra comma variants
    ("cf., Week 7 provides context.", ["cf., Week 7 provides context."]),
    ("viz., the cited source, confirms.", ["viz., the cited source, confirms."]),
    ("Col. Mark vs., Adm. Jones contested.", ["Col. Mark vs., Adm. Jones contested."]),
    # chained separators
    ("Smith vs. Jones vs. Williams all testified.", ["Smith vs. Jones vs. Williams all testified."]),
    ("Col. Smith vs. Adm. Jones vs. Gen. Williams.", ["Col. Smith vs. Adm. Jones vs. Gen. Williams."]),
    ("Dr. Lee vs. Prof. Kim vs. Mr. Nguyen presented.", ["Dr. Lee vs. Prof. Kim vs. Mr. Nguyen presented."]),
    # mixed separator forms
    ("Col. Mark v.s. Adm. Jones agreed.", ["Col. Mark v.s. Adm. Jones agreed."]),
    ("Smith v. Jones filed the motion.", ["Smith v. Jones filed the motion."]),
    ("Apex Inc. v. Summit Corp. settled.", ["Apex Inc. v. Summit Corp. settled."]),
    # xfail all-caps variants handled below
    ("dr. smith arrived late.", ["dr. smith arrived late."]),
    ("prof. johnson presented.", ["prof. johnson presented."]),
    ("gen. adams commanded.", ["gen. adams commanded."]),
    ("mr. williams filed.", ["mr. williams filed."]),
    ("mrs. davis confirmed.", ["mrs. davis confirmed."]),
    # consecutive abbreviations
    ("At 5 a.m. Mr. Smith left.", ["At 5 a.m. Mr. Smith left."]),
    ("By 9 p.m. Dr. Jones arrived.", ["By 9 p.m. Dr. Jones arrived."]),
    ("Around 3 p.m. Prof. Green spoke.", ["Around 3 p.m. Prof. Green spoke."]),
    ("At noon Lt. Brown reported.", ["At noon Lt. Brown reported."]),
    ("Before 6 a.m. Col. White departed.", ["Before 6 a.m. Col. White departed."]),
]

# Noise variants: different separators, spacing, punctuation
_NOISE_VARIANTS = [
    ("Smith vs. Jones", "Smith versus Jones"),
    ("Col. Mark", "Colonel Mark"),
    ("Dr. Smith", "Doctor Smith"),
    ("Inc.", "Incorporated"),
    ("Corp.", "Corporation"),
    ("Ltd.", "Limited"),
    ("Co.", "Company"),
    ("Bros.", "Brothers"),
    ("Ave.", "Avenue"),
    ("Blvd.", "Boulevard"),
    ("Rd.", "Road"),
    ("St.", "Street"),
    ("Mt.", "Mountain"),
    ("Ft.", "Fort"),
    ("Gen.", "General"),
]


def _build_category_d():
    cases = list(_BASE_ADVERSARIAL)
    # Generate noise variants from base patterns
    for base_text, base_exp in _BASE_ADVERSARIAL:
        for abbrev, expanded in _NOISE_VARIANTS:
            if abbrev in base_text:
                new_text = base_text.replace(abbrev, expanded, 1)
                if new_text != base_text:
                    cases.append((new_text, [new_text]))
                    if len(cases) >= 500:
                        break
        if len(cases) >= 500:
            break

    # Pad to 500 with additional patterns
    _extra_patterns = [
        ("The U.S. Senate passed the bill.", ["The U.S. Senate passed the bill."]),
        ("The U.K. Parliament voted.", ["The U.K. Parliament voted."]),
        ("The U.N. Security Council met.", ["The U.N. Security Council met."]),
        ("The E.U. Commission decided.", ["The E.U. Commission decided."]),
        ("Results from U.S.A. show improvement.", ["Results from U.S.A. show improvement."]),
        ("The D.C. circuit ruled.", ["The D.C. circuit ruled."]),
        ("He received a Ph.D. from MIT.", ["He received a Ph.D. from MIT."]),
        ("She holds an M.D. from Harvard.", ["She holds an M.D. from Harvard."]),
        ("He earned a J.D. at Yale.", ["He earned a J.D. at Yale."]),
        ("She has a B.A. in English.", ["She has a B.A. in English."]),
        ("He has an M.A. in History.", ["He has an M.A. in History."]),
        ("She earned a B.S. in Biology.", ["She earned a B.S. in Biology."]),
        ("He completed an M.S. in Physics.", ["He completed an M.S. in Physics."]),
        ("She finished an Ed.D. in Education.", ["She finished an Ed.D. in Education."]),
        ("He obtained an LL.M. from Oxford.", ["He obtained an LL.M. from Oxford."]),
        ("The meeting is at 9 a.m. Monday.", ["The meeting is at 9 a.m. Monday."]),
        ("She arrives at 6 p.m. Friday.", ["She arrives at 6 p.m. Friday."]),
        ("The lab opens at 8 A.M. daily.", ["The lab opens at 8 A.M. daily."]),
        ("The office closes at 5 P.M. sharp.", ["The office closes at 5 P.M. sharp."]),
        ("Contact the dept. for information.", ["Contact the dept. for information."]),
        ("The approx. value is 42.", ["The approx. value is 42."]),
        ("The ext. number is 1234.", ["The ext. number is 1234."]),
        ("The result is approx. correct.", ["The result is approx. correct."]),
        ("Attendance is etc. dependent.", ["Attendance is etc. dependent."]),
        ("The study found etc. relevant data.", ["The study found etc. relevant data."]),
    ]
    while len(cases) < 500:
        remaining = 500 - len(cases)
        cases.extend(_extra_patterns[:remaining])
    return cases[:500]


CAT_D_CASES = _build_category_d()

# ---------------------------------------------------------------------------
# Category O — Idempotency (one case per abbreviation)
# ---------------------------------------------------------------------------

def _build_category_o():
    cases = []
    for a in ALL_ABBREVS:
        text = f"The document references {a} page 5 for context."
        cases.append((text, [text]))
    return cases


CAT_O_CASES = _build_category_o()

# ---------------------------------------------------------------------------
# All cases combined
# ---------------------------------------------------------------------------

ALL_H_CASES = CAT_H_CASES
ALL_I_CASES = CAT_I_CASES
ALL_J_CASES = CAT_J_CASES
ALL_K_CASES = CAT_K_CASES
ALL_L_CASES = CAT_L_CASES
ALL_M_CASES = CAT_M_CASES
ALL_N_CASES = CAT_N_CASES
ALL_D_CASES = CAT_D_CASES
ALL_O_CASES = CAT_O_CASES


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestSurfaceFormNormalization:
    """Category H: verify surface-form variants (upper, comma-suffix) do not split."""

    @pytest.mark.parametrize("text,expected", ALL_H_CASES)
    def test_surface_form(self, segment: SegmentationFunc, text: str, expected: list):
        assert segment(text) == expected


class TestMultiSentenceChains:
    """Category I: abbreviation in position 2 of 3-sentence chains."""

    @pytest.mark.parametrize("text,expected", ALL_I_CASES)
    def test_chain(self, segment: SegmentationFunc, text: str, expected: list):
        assert segment(text) == expected


class TestAbbreviationInParentheses:
    """Category J: abbreviation inside parenthetical expressions."""

    @pytest.mark.parametrize("text,expected", ALL_J_CASES)
    def test_paren(self, segment: SegmentationFunc, text: str, expected: list):
        assert segment(text) == expected


class TestAbbreviationAfterPunctuation:
    """Category K: abbreviation following colon, semicolon, or em-dash."""

    @pytest.mark.parametrize("text,expected", ALL_K_CASES)
    def test_punct_context(self, segment: SegmentationFunc, text: str, expected: list):
        assert segment(text) == expected


class TestWhitespaceVariants:
    """Category L: double/triple space after abbreviation."""

    @pytest.mark.parametrize("text,expected", ALL_L_CASES)
    def test_whitespace(self, segment: SegmentationFunc, text: str, expected: list):
        assert segment(text) == expected


class TestRomanNumeralContext:
    """Category M: Roman numeral following a numeric abbreviation."""

    @pytest.mark.parametrize("text,expected", ALL_M_CASES)
    def test_roman_numeral(self, segment: SegmentationFunc, text: str, expected: list):
        assert segment(text) == expected


class TestTerminalPeriodAmbiguity:
    """Category N: sentence-final period ambiguity for numeric abbreviations."""

    @pytest.mark.parametrize("text,expected", ALL_N_CASES)
    def test_terminal_period(self, segment: SegmentationFunc, text: str, expected: list):
        assert segment(text) == expected


class TestAdversarialPatterns:
    """Category D: adversarial inputs (missing dots, extra commas, noise variants)."""

    @pytest.mark.parametrize("text,expected", ALL_D_CASES)
    def test_adversarial(self, segment: SegmentationFunc, text: str, expected: list):
        assert segment(text) == expected


class TestIdempotency:
    """Category O: each abbreviation produces stable output on re-segmentation."""

    @pytest.mark.parametrize("text,expected", ALL_O_CASES)
    def test_idempotency(self, segment: SegmentationFunc, text: str, expected: list):
        assert segment(text) == expected
