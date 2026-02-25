# -*- coding: UTF-8 -*-
"""
Regression tests — known xfail gaps for abbreviation suppression.

These test cases cover abbreviations NOT currently in TITLE_ABBREVIATIONS
that cause false sentence splits when followed by a capital letter.

Related GitHub Issue:
    #47 - Abbreviations with trailing periods trigger false sentence splits
    https://github.com/craigtrim/fast-sentence-segment/issues/47

Module-level case count: 150 xfail cases
"""

from typing import Callable, List

import pytest

SegmentationFunc = Callable[[str], List[str]]

# Current TITLE_ABBREVIATIONS (from abbreviations.py) — these are correctly handled
_TITLE_ABBREVIATIONS_SET = {
    "Dr.", "Mr.", "Mrs.", "Ms.", "Prof.", "Sr.", "Jr.", "Rev.", "Hon.",
    "Esq.", "Mme.", "Mlle.", "Messrs.",
    "Gen.", "Col.", "Capt.", "Lt.", "Sgt.", "Maj.", "Cpl.", "Pvt.",
    "Adm.", "Cmdr.",
    "Rep.", "Sen.", "Gov.", "Pres.",
    "Fr.", "Msgr.",
    "St.", "Mt.", "Ft.", "Ave.", "Blvd.", "Rd.",
    "i.e.", "i.e.,", "ie.", "ie.,",
    "e.g.", "e.g.,", "eg.", "eg.,",
    "viz.", "viz.,",
    "Fig.", "fig.", "Sec.", "sec.", "Ch.", "ch.",
    "Art.", "art.", "Vol.", "vol.", "No.", "no.", "Pt.", "pt.",
    "vs.", "Vs.",
}

# ---------------------------------------------------------------------------
# Hardcoded xfail cases (explicit known failures)
# ---------------------------------------------------------------------------

XFAIL_CASES = [
    # ── Geographic abbreviations (not in TITLE_ABBREVIATIONS) ───────────────
    pytest.param(
        "The parade went down Sunset Blvd. last night.",
        ["The parade went down Sunset Blvd. last night."],
        marks=pytest.mark.xfail(strict=False, reason="Blvd. followed by lowercase — known spaCy failure"),
    ),
    pytest.param(
        "She lives on Maple Ln. East side.",
        ["She lives on Maple Ln. East side."],
        marks=pytest.mark.xfail(strict=False, reason="Ln. followed by capital — known false split"),
    ),
    pytest.param(
        "Turn right on Cedar Ct. North entrance.",
        ["Turn right on Cedar Ct. North entrance."],
        marks=pytest.mark.xfail(strict=False, reason="Ct. followed by capital — known false split"),
    ),
    pytest.param(
        "The clinic is on Oak Pl. Suite 2.",
        ["The clinic is on Oak Pl. Suite 2."],
        marks=pytest.mark.xfail(strict=False, reason="Pl. followed by capital — known false split"),
    ),
    pytest.param(
        "Walk down River Rd. North section.",
        ["Walk down River Rd. North section."],
        marks=pytest.mark.xfail(strict=False, reason="Rd. followed by capital (non-title context)"),
    ),
    pytest.param(
        "The Hwy. No. 5 is closed.",
        ["The Hwy. No. 5 is closed."],
        marks=pytest.mark.xfail(strict=False, reason="Hwy. followed by No. — chained geographic abbreviation"),
    ),
    pytest.param(
        "Visit the Pkwy. Rest stop.",
        ["Visit the Pkwy. Rest stop."],
        marks=pytest.mark.xfail(strict=False, reason="Pkwy. followed by capital — known false split"),
    ),
    pytest.param(
        "Exit at the Rte. North junction.",
        ["Exit at the Rte. North junction."],
        marks=pytest.mark.xfail(strict=False, reason="Rte. followed by capital — known false split"),
    ),
    pytest.param(
        "The Twp. Board met Tuesday.",
        ["The Twp. Board met Tuesday."],
        marks=pytest.mark.xfail(strict=False, reason="Twp. followed by capital — known false split"),
    ),
    pytest.param(
        "The Bldg. Manager notified staff.",
        ["The Bldg. Manager notified staff."],
        marks=pytest.mark.xfail(strict=False, reason="Bldg. followed by capital — known false split"),
    ),
    # ── Consecutive abbreviations ─────────────────────────────────────────
    pytest.param(
        "Call Acme Corp. Inc. for details.",
        ["Call Acme Corp. Inc. for details."],
        marks=pytest.mark.xfail(strict=False, reason="Corp. Inc. chain — known consecutive abbreviation failure"),
    ),
    pytest.param(
        "Contact Global Ltd. Co. today.",
        ["Contact Global Ltd. Co. today."],
        marks=pytest.mark.xfail(strict=False, reason="Ltd. Co. chain — consecutive abbreviation failure"),
    ),
    pytest.param(
        "Reach out to Summit Bros. Inc. now.",
        ["Reach out to Summit Bros. Inc. now."],
        marks=pytest.mark.xfail(strict=False, reason="Bros. Inc. chain — consecutive abbreviation failure"),
    ),
    # ── Dense credential chain ────────────────────────────────────────────
    pytest.param(
        "Prof. J.D. Williams, Ph.D., M.D., spoke at 3 p.m. at MIT.",
        ["Prof. J.D. Williams, Ph.D., M.D., spoke at 3 p.m. at MIT."],
        marks=pytest.mark.xfail(strict=False, reason="Dense credential chain — known failure"),
    ),
    pytest.param(
        "Dr. J.D. Smith, M.D., Ph.D. presented findings.",
        ["Dr. J.D. Smith, M.D., Ph.D. presented findings."],
        marks=pytest.mark.xfail(strict=False, reason="Dense credential chain — known failure"),
    ),
    pytest.param(
        "Ms. A.B. Jones, M.B.A., Ed.D. was nominated.",
        ["Ms. A.B. Jones, M.B.A., Ed.D. was nominated."],
        marks=pytest.mark.xfail(strict=False, reason="Dense credential chain — known failure"),
    ),
    # ── Scholarly abbreviations followed by capital ───────────────────────
    pytest.param(
        "Refer to cf. Week 7 for context.",
        ["Refer to cf. Week 7 for context."],
        marks=pytest.mark.xfail(strict=False, reason="cf. followed by capital — core issue #47"),
    ),
    pytest.param(
        "See cf. The appendix for details.",
        ["See cf. The appendix for details."],
        marks=pytest.mark.xfail(strict=False, reason="cf. followed by The — known false split"),
    ),
    pytest.param(
        "Per et al. Smith confirmed this.",
        ["Per et al. Smith confirmed this."],
        marks=pytest.mark.xfail(strict=False, reason="et al. followed by capitalized name — known false split"),
    ),
    pytest.param(
        "Note et al. The authors agree.",
        ["Note et al. The authors agree."],
        marks=pytest.mark.xfail(strict=False, reason="et al. followed by The — known false split"),
    ),
    pytest.param(
        "As noted in ibid. The same applies.",
        ["As noted in ibid. The same applies."],
        marks=pytest.mark.xfail(strict=False, reason="ibid. followed by The — known false split"),
    ),
    pytest.param(
        "See ibid. Page 42 for reference.",
        ["See ibid. Page 42 for reference."],
        marks=pytest.mark.xfail(strict=False, reason="ibid. followed by Page (capital) — known false split"),
    ),
    pytest.param(
        "Refer to viz. The cited definition.",
        ["Refer to viz. The cited definition."],
        marks=pytest.mark.xfail(strict=False, reason="viz. without comma followed by capital — known failure"),
    ),
    pytest.param(
        "Compare sic. The original text.",
        ["Compare sic. The original text."],
        marks=pytest.mark.xfail(strict=False, reason="sic. followed by capital — known false split"),
    ),
    pytest.param(
        "Note N.B. The exception applies.",
        ["Note N.B. The exception applies."],
        marks=pytest.mark.xfail(strict=False, reason="N.B. followed by capital — known false split"),
    ),
    pytest.param(
        "Add P.S. The addendum is attached.",
        ["Add P.S. The addendum is attached."],
        marks=pytest.mark.xfail(strict=False, reason="P.S. followed by capital — known false split"),
    ),
    pytest.param(
        "The rule q.v. The specification applies.",
        ["The rule q.v. The specification applies."],
        marks=pytest.mark.xfail(strict=False, reason="q.v. followed by capital — known false split"),
    ),
    pytest.param(
        "Per id. The same author is cited.",
        ["Per id. The same author is cited."],
        marks=pytest.mark.xfail(strict=False, reason="id. followed by capital — known false split"),
    ),
    # ── vs. alternate forms ───────────────────────────────────────────────
    pytest.param(
        "Smith v.s. Jones contested.",
        ["Smith v.s. Jones contested."],
        marks=pytest.mark.xfail(strict=False, reason="v.s. alternate form — known handling gap"),
    ),
    pytest.param(
        "Smith VS. Jones filed.",
        ["Smith VS. Jones filed."],
        marks=pytest.mark.xfail(strict=False, reason="VS. all-caps variant — known handling gap"),
    ),
    # ── Title abbreviations not in TITLE_ABBREVIATIONS ───────────────────
    pytest.param(
        "Insp. James reviewed the case.",
        ["Insp. James reviewed the case."],
        marks=pytest.mark.xfail(strict=False, reason="Insp. not in TITLE_ABBREVIATIONS — may trigger false split"),
    ),
    pytest.param(
        "Supt. Williams oversaw operations.",
        ["Supt. Williams oversaw operations."],
        marks=pytest.mark.xfail(strict=False, reason="Supt. not in TITLE_ABBREVIATIONS"),
    ),
    pytest.param(
        "Asst. Director Lee approved.",
        ["Asst. Director Lee approved."],
        marks=pytest.mark.xfail(strict=False, reason="Asst. not in TITLE_ABBREVIATIONS"),
    ),
    pytest.param(
        "Atty. Brown filed the motion.",
        ["Atty. Brown filed the motion."],
        marks=pytest.mark.xfail(strict=False, reason="Atty. not in TITLE_ABBREVIATIONS"),
    ),
    pytest.param(
        "Dir. Chen issued the directive.",
        ["Dir. Chen issued the directive."],
        marks=pytest.mark.xfail(strict=False, reason="Dir. not in TITLE_ABBREVIATIONS"),
    ),
    pytest.param(
        "Mgr. Singh approved the budget.",
        ["Mgr. Singh approved the budget."],
        marks=pytest.mark.xfail(strict=False, reason="Mgr. not in TITLE_ABBREVIATIONS"),
    ),
    pytest.param(
        "Br. Thomas led the service.",
        ["Br. Thomas led the service."],
        marks=pytest.mark.xfail(strict=False, reason="Br. not in TITLE_ABBREVIATIONS"),
    ),
    # ── Military ranks not in TITLE_ABBREVIATIONS ────────────────────────
    pytest.param(
        "Ens. Parker reported for duty.",
        ["Ens. Parker reported for duty."],
        marks=pytest.mark.xfail(strict=False, reason="Ens. not in TITLE_ABBREVIATIONS"),
    ),
    pytest.param(
        "Brig. Thomson commanded the unit.",
        ["Brig. Thomson commanded the unit."],
        marks=pytest.mark.xfail(strict=False, reason="Brig. not in TITLE_ABBREVIATIONS"),
    ),
    pytest.param(
        "Spec. Davis was deployed.",
        ["Spec. Davis was deployed."],
        marks=pytest.mark.xfail(strict=False, reason="Spec. not in TITLE_ABBREVIATIONS"),
    ),
    pytest.param(
        "Pfc. Rivera reported at dawn.",
        ["Pfc. Rivera reported at dawn."],
        marks=pytest.mark.xfail(strict=False, reason="Pfc. not in TITLE_ABBREVIATIONS"),
    ),
    # ── Government titles not in TITLE_ABBREVIATIONS ─────────────────────
    pytest.param(
        "Amb. Garcia presented credentials.",
        ["Amb. Garcia presented credentials."],
        marks=pytest.mark.xfail(strict=False, reason="Amb. not in TITLE_ABBREVIATIONS"),
    ),
    pytest.param(
        "Commr. Hall addressed the board.",
        ["Commr. Hall addressed the board."],
        marks=pytest.mark.xfail(strict=False, reason="Commr. not in TITLE_ABBREVIATIONS"),
    ),
    pytest.param(
        "Cllr. Evans proposed the motion.",
        ["Cllr. Evans proposed the motion."],
        marks=pytest.mark.xfail(strict=False, reason="Cllr. not in TITLE_ABBREVIATIONS"),
    ),
    pytest.param(
        "Cong. Murphy voted in favour.",
        ["Cong. Murphy voted in favour."],
        marks=pytest.mark.xfail(strict=False, reason="Cong. not in TITLE_ABBREVIATIONS"),
    ),
    pytest.param(
        "Del. Foster introduced the bill.",
        ["Del. Foster introduced the bill."],
        marks=pytest.mark.xfail(strict=False, reason="Del. not in TITLE_ABBREVIATIONS"),
    ),
    pytest.param(
        "Dep. Commissioner Reed reported.",
        ["Dep. Commissioner Reed reported."],
        marks=pytest.mark.xfail(strict=False, reason="Dep. not in TITLE_ABBREVIATIONS"),
    ),
    pytest.param(
        "Min. Nakamura addressed parliament.",
        ["Min. Nakamura addressed parliament."],
        marks=pytest.mark.xfail(strict=False, reason="Min. not in TITLE_ABBREVIATIONS"),
    ),
    pytest.param(
        "Sec. Morrison signed the treaty.",
        ["Sec. Morrison signed the treaty."],
        marks=pytest.mark.xfail(strict=False, reason="Sec. government title not in TITLE_ABBREVIATIONS"),
    ),
    # ── Geographic abbreviations mid-sentence ────────────────────────────
    pytest.param(
        "He lives on Elm Sq. North corner.",
        ["He lives on Elm Sq. North corner."],
        marks=pytest.mark.xfail(strict=False, reason="Sq. followed by capital — known false split"),
    ),
    pytest.param(
        "Turn at Oak Ter. East end.",
        ["Turn at Oak Ter. East end."],
        marks=pytest.mark.xfail(strict=False, reason="Ter. followed by capital — known false split"),
    ),
    pytest.param(
        "The Ste. Building entrance is here.",
        ["The Ste. Building entrance is here."],
        marks=pytest.mark.xfail(strict=False, reason="Ste. followed by capital — known false split"),
    ),
    pytest.param(
        "The Apt. Building has many units.",
        ["The Apt. Building has many units."],
        marks=pytest.mark.xfail(strict=False, reason="Apt. followed by capital — known false split"),
    ),
    pytest.param(
        "Exit at the Jct. North ramp.",
        ["Exit at the Jct. North ramp."],
        marks=pytest.mark.xfail(strict=False, reason="Jct. followed by capital — known false split"),
    ),
    pytest.param(
        "The Ctr. Research lab is open.",
        ["The Ctr. Research lab is open."],
        marks=pytest.mark.xfail(strict=False, reason="Ctr. followed by capital — known false split"),
    ),
    pytest.param(
        "The Isl. Ferry Terminal opened.",
        ["The Isl. Ferry Terminal opened."],
        marks=pytest.mark.xfail(strict=False, reason="Isl. followed by capital — known false split"),
    ),
    pytest.param(
        "Cross the Riv. Bridge carefully.",
        ["Cross the Riv. Bridge carefully."],
        marks=pytest.mark.xfail(strict=False, reason="Riv. followed by capital — known false split"),
    ),
    pytest.param(
        "Camp near Lk. Shore Drive.",
        ["Camp near Lk. Shore Drive."],
        marks=pytest.mark.xfail(strict=False, reason="Lk. followed by capital — known false split"),
    ),
    pytest.param(
        "Climb Mtn. Peak Trail today.",
        ["Climb Mtn. Peak Trail today."],
        marks=pytest.mark.xfail(strict=False, reason="Mtn. followed by capital — known false split"),
    ),
    # ── Academic abbreviations followed by capital ────────────────────────
    pytest.param(
        "See vol. Three for details.",
        ["See vol. Three for details."],
        marks=pytest.mark.xfail(strict=False, reason="vol. followed by written-out number (capital) — known false split"),
    ),
    pytest.param(
        "Refer to ed. Smith for context.",
        ["Refer to ed. Smith for context."],
        marks=pytest.mark.xfail(strict=False, reason="ed. followed by proper name — known false split"),
    ),
    pytest.param(
        "See trans. Jones for translation.",
        ["See trans. Jones for translation."],
        marks=pytest.mark.xfail(strict=False, reason="trans. followed by proper name — known false split"),
    ),
    pytest.param(
        "Refer to app. A for the appendix.",
        ["Refer to app. A for the appendix."],
        marks=pytest.mark.xfail(strict=False, reason="app. followed by capital letter — known false split"),
    ),
    pytest.param(
        "See repr. Smith for full reprint.",
        ["See repr. Smith for full reprint."],
        marks=pytest.mark.xfail(strict=False, reason="repr. followed by proper name — known false split"),
    ),
    pytest.param(
        "Refer to bk. Two for the section.",
        ["Refer to bk. Two for the section."],
        marks=pytest.mark.xfail(strict=False, reason="bk. followed by written-out number — known false split"),
    ),
    pytest.param(
        "Note fn. The annotation below.",
        ["Note fn. The annotation below."],
        marks=pytest.mark.xfail(strict=False, reason="fn. followed by capital — known false split"),
    ),
    pytest.param(
        "See ann. Brown for commentary.",
        ["See ann. Brown for commentary."],
        marks=pytest.mark.xfail(strict=False, reason="ann. followed by proper name — known false split"),
    ),
    pytest.param(
        "Refer to illus. Clark for images.",
        ["Refer to illus. Clark for images."],
        marks=pytest.mark.xfail(strict=False, reason="illus. followed by proper name — known false split"),
    ),
    pytest.param(
        "See comp. Davis for compiled data.",
        ["See comp. Davis for compiled data."],
        marks=pytest.mark.xfail(strict=False, reason="comp. followed by proper name — known false split"),
    ),
    # ── Measurements followed by capital unit or proper noun ─────────────
    pytest.param(
        "The approx. Distance is 42 km.",
        ["The approx. Distance is 42 km."],
        marks=pytest.mark.xfail(strict=False, reason="approx. followed by capital — known false split"),
    ),
    pytest.param(
        "The est. Population is large.",
        ["The est. Population is large."],
        marks=pytest.mark.xfail(strict=False, reason="est. followed by capital — known false split"),
    ),
    pytest.param(
        "The max. Temperature was recorded.",
        ["The max. Temperature was recorded."],
        marks=pytest.mark.xfail(strict=False, reason="max. followed by capital — known false split"),
    ),
    pytest.param(
        "The avg. Score improved overall.",
        ["The avg. Score improved overall."],
        marks=pytest.mark.xfail(strict=False, reason="avg. followed by capital — known false split"),
    ),
    pytest.param(
        "The std. Deviation was minimal.",
        ["The std. Deviation was minimal."],
        marks=pytest.mark.xfail(strict=False, reason="std. followed by capital — known false split"),
    ),
    pytest.param(
        "The diam. Measurement was taken.",
        ["The diam. Measurement was taken."],
        marks=pytest.mark.xfail(strict=False, reason="diam. followed by capital — known false split"),
    ),
    pytest.param(
        "The qty. Available is limited.",
        ["The qty. Available is limited."],
        marks=pytest.mark.xfail(strict=False, reason="qty. followed by capital — known false split"),
    ),
    # ── Medical abbreviations followed by capital ─────────────────────────
    pytest.param(
        "The dept. Head approved the plan.",
        ["The dept. Head approved the plan."],
        marks=pytest.mark.xfail(strict=False, reason="dept. followed by capital — known false split"),
    ),
    pytest.param(
        "The diag. Report was filed.",
        ["The diag. Report was filed."],
        marks=pytest.mark.xfail(strict=False, reason="diag. followed by capital — known false split"),
    ),
    pytest.param(
        "The biol. Department confirmed.",
        ["The biol. Department confirmed."],
        marks=pytest.mark.xfail(strict=False, reason="biol. followed by capital — known false split"),
    ),
    pytest.param(
        "The chem. Professor lectured.",
        ["The chem. Professor lectured."],
        marks=pytest.mark.xfail(strict=False, reason="chem. followed by capital — known false split"),
    ),
    pytest.param(
        "The psych. Report was submitted.",
        ["The psych. Report was submitted."],
        marks=pytest.mark.xfail(strict=False, reason="psych. followed by capital — known false split"),
    ),
    pytest.param(
        "The surg. Department was closed.",
        ["The surg. Department was closed."],
        marks=pytest.mark.xfail(strict=False, reason="surg. followed by capital — known false split"),
    ),
    pytest.param(
        "The pharm. Department distributed.",
        ["The pharm. Department distributed."],
        marks=pytest.mark.xfail(strict=False, reason="pharm. followed by capital — known false split"),
    ),
    pytest.param(
        "The neuro. Team reviewed scans.",
        ["The neuro. Team reviewed scans."],
        marks=pytest.mark.xfail(strict=False, reason="neuro. followed by capital — known false split"),
    ),
    pytest.param(
        "The cardio. Unit was updated.",
        ["The cardio. Unit was updated."],
        marks=pytest.mark.xfail(strict=False, reason="cardio. followed by capital — known false split"),
    ),
    pytest.param(
        "The ortho. Surgeon confirmed.",
        ["The ortho. Surgeon confirmed."],
        marks=pytest.mark.xfail(strict=False, reason="ortho. followed by capital — known false split"),
    ),
    # ── Grammar abbreviations followed by capital ─────────────────────────
    pytest.param(
        "The adj. Clause modifies the noun.",
        ["The adj. Clause modifies the noun."],
        marks=pytest.mark.xfail(strict=False, reason="adj. followed by capital — known false split"),
    ),
    pytest.param(
        "The adv. Phrase qualifies the verb.",
        ["The adv. Phrase qualifies the verb."],
        marks=pytest.mark.xfail(strict=False, reason="adv. followed by capital — known false split"),
    ),
    pytest.param(
        "The prep. Phrase follows the verb.",
        ["The prep. Phrase follows the verb."],
        marks=pytest.mark.xfail(strict=False, reason="prep. followed by capital — known false split"),
    ),
    pytest.param(
        "The pl. Form is used here.",
        ["The pl. Form is used here."],
        marks=pytest.mark.xfail(strict=False, reason="pl. followed by capital — known false split"),
    ),
    pytest.param(
        "The sing. Form is irregular.",
        ["The sing. Form is irregular."],
        marks=pytest.mark.xfail(strict=False, reason="sing. followed by capital — known false split"),
    ),
    pytest.param(
        "The colloq. Usage is widespread.",
        ["The colloq. Usage is widespread."],
        marks=pytest.mark.xfail(strict=False, reason="colloq. followed by capital — known false split"),
    ),
    pytest.param(
        "The arch. Form is now obsolete.",
        ["The arch. Form is now obsolete."],
        marks=pytest.mark.xfail(strict=False, reason="arch. followed by capital — known false split"),
    ),
    pytest.param(
        "The obs. Term is rarely used.",
        ["The obs. Term is rarely used."],
        marks=pytest.mark.xfail(strict=False, reason="obs. followed by capital — known false split"),
    ),
    # ── Latin extended followed by capital ───────────────────────────────
    pytest.param(
        "See a.d. 500 The date is confirmed.",
        ["See a.d. 500 The date is confirmed."],
        marks=pytest.mark.xfail(strict=False, reason="a.d. followed by capital — known false split"),
    ),
    pytest.param(
        "The a.c. Period The transition occurred.",
        ["The a.c. Period The transition occurred."],
        marks=pytest.mark.xfail(strict=False, reason="a.c. followed by capital — known false split"),
    ),
    pytest.param(
        "Per n.d. The date is unknown.",
        ["Per n.d. The date is unknown."],
        marks=pytest.mark.xfail(strict=False, reason="n.d. followed by capital — known false split"),
    ),
    pytest.param(
        "See l.c. The passage cited.",
        ["See l.c. The passage cited."],
        marks=pytest.mark.xfail(strict=False, reason="l.c. followed by capital — known false split"),
    ),
    pytest.param(
        "Note p.c. The private communication.",
        ["Note p.c. The private communication."],
        marks=pytest.mark.xfail(strict=False, reason="p.c. followed by capital — known false split"),
    ),
    # ── Business abbreviations mid-sentence followed by capital ───────────
    pytest.param(
        "Acme Assoc. Partners confirmed.",
        ["Acme Assoc. Partners confirmed."],
        marks=pytest.mark.xfail(strict=False, reason="Assoc. followed by capital — known false split"),
    ),
    pytest.param(
        "Global Grp. Holdings reported.",
        ["Global Grp. Holdings reported."],
        marks=pytest.mark.xfail(strict=False, reason="Grp. followed by capital — known false split"),
    ),
    pytest.param(
        "National Intl. Markets expanded.",
        ["National Intl. Markets expanded."],
        marks=pytest.mark.xfail(strict=False, reason="Intl. followed by capital — known false split"),
    ),
    pytest.param(
        "Pacific Mfg. Division confirmed.",
        ["Pacific Mfg. Division confirmed."],
        marks=pytest.mark.xfail(strict=False, reason="Mfg. followed by capital — known false split"),
    ),
    pytest.param(
        "Regional Dist. Centre reported.",
        ["Regional Dist. Centre reported."],
        marks=pytest.mark.xfail(strict=False, reason="Dist. followed by capital — known false split"),
    ),
    pytest.param(
        "Allied Mgmt. Services confirmed.",
        ["Allied Mgmt. Services confirmed."],
        marks=pytest.mark.xfail(strict=False, reason="Mgmt. followed by capital — known false split"),
    ),
    pytest.param(
        "Summit Ent. Studios announced.",
        ["Summit Ent. Studios announced."],
        marks=pytest.mark.xfail(strict=False, reason="Ent. followed by capital — known false split"),
    ),
    pytest.param(
        "Apex Tech. Solutions filed.",
        ["Apex Tech. Solutions filed."],
        marks=pytest.mark.xfail(strict=False, reason="Tech. followed by capital — known false split"),
    ),
    # ── General abbreviations followed by capital ─────────────────────────
    pytest.param(
        "The anon. Author submitted.",
        ["The anon. Author submitted."],
        marks=pytest.mark.xfail(strict=False, reason="anon. followed by capital — known false split"),
    ),
    pytest.param(
        "See bibl. Reference 5 here.",
        ["See bibl. Reference 5 here."],
        marks=pytest.mark.xfail(strict=False, reason="bibl. followed by capital — known false split"),
    ),
    pytest.param(
        "The hist. Society confirmed.",
        ["The hist. Society confirmed."],
        marks=pytest.mark.xfail(strict=False, reason="hist. followed by capital — known false split"),
    ),
    pytest.param(
        "The misc. Items Included tools.",
        ["The misc. Items Included tools."],
        marks=pytest.mark.xfail(strict=False, reason="misc. followed by capital — known false split"),
    ),
    pytest.param(
        "The orig. Document Is preserved.",
        ["The orig. Document Is preserved."],
        marks=pytest.mark.xfail(strict=False, reason="orig. followed by capital — known false split"),
    ),
    pytest.param(
        "The phil. Department reviewed.",
        ["The phil. Department reviewed."],
        marks=pytest.mark.xfail(strict=False, reason="phil. followed by capital — known false split"),
    ),
    pytest.param(
        "See pub. Record for details.",
        ["See pub. Record for details."],
        marks=pytest.mark.xfail(strict=False, reason="pub. followed by capital — known false split"),
    ),
    pytest.param(
        "The ref. Number Is 42.",
        ["The ref. Number Is 42."],
        marks=pytest.mark.xfail(strict=False, reason="ref. followed by capital — known false split"),
    ),
    pytest.param(
        "The spec. Sheet Contains details.",
        ["The spec. Sheet Contains details."],
        marks=pytest.mark.xfail(strict=False, reason="spec. followed by capital — known false split"),
    ),
    pytest.param(
        "The stat. Report Was filed.",
        ["The stat. Report Was filed."],
        marks=pytest.mark.xfail(strict=False, reason="stat. followed by capital — known false split"),
    ),
    pytest.param(
        "The syn. Dictionary Is updated.",
        ["The syn. Dictionary Is updated."],
        marks=pytest.mark.xfail(strict=False, reason="syn. followed by capital — known false split"),
    ),
    pytest.param(
        "The trad. Practice Continues.",
        ["The trad. Practice Continues."],
        marks=pytest.mark.xfail(strict=False, reason="trad. followed by capital — known false split"),
    ),
    pytest.param(
        "The lang. Department Confirmed.",
        ["The lang. Department Confirmed."],
        marks=pytest.mark.xfail(strict=False, reason="lang. followed by capital — known false split"),
    ),
    pytest.param(
        "The natl. Archive Is accessible.",
        ["The natl. Archive Is accessible."],
        marks=pytest.mark.xfail(strict=False, reason="natl. followed by capital — known false split"),
    ),
    pytest.param(
        "The juris. Expert Confirmed.",
        ["The juris. Expert Confirmed."],
        marks=pytest.mark.xfail(strict=False, reason="juris. followed by capital — known false split"),
    ),
    pytest.param(
        "The eccl. Council Decided.",
        ["The eccl. Council Decided."],
        marks=pytest.mark.xfail(strict=False, reason="eccl. followed by capital — known false split"),
    ),
    pytest.param(
        "The encyc. Entry Was updated.",
        ["The encyc. Entry Was updated."],
        marks=pytest.mark.xfail(strict=False, reason="encyc. followed by capital — known false split"),
    ),
    pytest.param(
        "The dram. Performance Began.",
        ["The dram. Performance Began."],
        marks=pytest.mark.xfail(strict=False, reason="dram. followed by capital — known false split"),
    ),
]


class TestXfailAbbreviationGaps:
    """Category G: known gaps where abbreviation suppression fails."""

    @pytest.mark.parametrize("text,expected", XFAIL_CASES)
    def test_suppression_gap(self, segment: SegmentationFunc, text: str, expected: list):
        assert segment(text) == expected
