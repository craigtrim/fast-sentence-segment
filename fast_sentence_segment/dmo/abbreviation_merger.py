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

# Abbreviations that can legitimately START a new sentence when followed by a
# capitalised proper name.  When the secondary (semicolon/colon) check
# encounters one of these after a clause-level separator it treats it as a
# real sentence boundary and does NOT merge.
# Examples: "…; Dr. Smith …"  "…; Gen. Patton …"
#
# Intentionally NARROWER than TITLE_ABBREVIATIONS — excludes geographic
# (Rd., St.), scholarly (n.b., N.B.), Latin (i.e., e.g.) and reference
# (Fig., Sec.) abbreviations that NEVER legitimately start new sentences.
#
# Related GitHub Issue:
#     #34 - Citation / middle-initial handling
#     https://github.com/craigtrim/fast-sentence-segment/issues/34
_PERSONAL_TITLE_ABBREV_SET: frozenset = frozenset({
    # Personal / honorific titles
    "Dr.", "Mr.", "Mrs.", "Ms.", "Prof.", "Sr.", "Jr.",
    "Rev.", "Hon.", "Esq.", "Mme.", "Mlle.", "Messrs.",
    # Military ranks
    "Gen.", "Col.", "Capt.", "Lt.", "Sgt.", "Maj.", "Cpl.", "Pvt.", "Adm.", "Cmdr.",
    "Ens.", "Brig.", "Spec.", "Pfc.",
    # Political / government titles
    "Rep.", "Sen.", "Gov.", "Pres.", "Del.", "Amb.", "Min.",
    # Ecclesiastical
    "Fr.", "Msgr.",
    # Professional
    "Atty.", "Dir.", "Supt.", "Insp.", "Asst.", "Mgr.", "Dep.", "Commr.", "Cllr.", "Cong.",
})


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


# Alternation of function words / prepositions that, when the word immediately
# preceding an entity-suffix abbreviation (Inc., Corp., etc.) in the current
# sentence is one of these, the abbreviation is being used as a reference
# abbreviation (not a company-name suffix) and the following fragment should
# always be merged regardless of its starting capitalisation.
#
# This mirrors the _NON_SPLIT_PRECEDING_WORDS set in AbbreviationSplitter.
_FUNC_WORD_SEQ = (
    r"(?:a|an|the|and|or|but|nor|yet|so|"
    r"in|on|at|by|to|of|for|as|via|re|per|with|from|into|onto|upon|"
    r"about|above|across|after|against|along|amid|among|around|"
    r"before|behind|below|beneath|beside|between|beyond|despite|"
    r"down|during|except|inside|near|off|outside|over|past|since|"
    r"than|throughout|toward|through|under|until|unto|up|within|without|"
    r"not|also|even|only|just|both|either|neither|see|note|"
    r"specifically|particularly|especially|including|excluding|"
    r"containing|covering)"
)

# Same as _FUNC_WORD_SEQ but without coordinating conjunctions (and, or, but,
# nor, yet, so).  Used for company-suffix abbreviations (Co., Inc., Corp.,
# Ltd., Bros.) so that the idiomatic phrase "and co." / "or inc." does NOT
# trigger a merge with a following independent clause.
# e.g. "Let's ask Jane and co. They should know." → must NOT merge.
_COMPANY_FUNC_WORD_SEQ = (
    r"(?:a|an|the|"
    r"in|on|at|by|to|of|for|as|via|re|per|with|from|into|onto|upon|"
    r"about|above|across|after|against|along|amid|among|around|"
    r"before|behind|below|beneath|beside|between|beyond|despite|"
    r"down|during|except|inside|near|off|outside|over|past|since|"
    r"than|throughout|toward|through|under|until|unto|up|within|without|"
    r"not|also|even|only|just|both|either|neither|see|note|"
    r"specifically|particularly|especially|including|excluding|"
    r"containing|covering)"
)


# Patterns where spaCy incorrectly splits after an abbreviation.
# Format: (ending_pattern, extract_pattern)
#   - ending_pattern: regex to match end of current sentence
#   - extract_pattern: regex to extract the portion to merge from next sentence
#
# The extract_pattern MUST have a capture group for the portion to merge.
# Whatever is NOT captured remains as a separate sentence.

MERGE_PATTERNS: List[Tuple[str, str]] = [

    # ── Academic reference prefixes ───────────────────────────────────────────
    # All of these introduce a reference (number, name, or clause) and never
    # legitimately end a sentence on their own.
    #
    # Dual-pattern strategy for each abbreviation:
    #   Pattern 1 (digit-only): fires first when the next fragment starts with
    #              a digit (e.g., "5 is here.") — extracts ONLY the reference
    #              number (e.g., "5"), leaving the continuation ("is here.") as
    #              a separate sentence.  This matches the expected behaviour in
    #              contexts like "Item no. 5 is here." where spaCy splits at
    #              "no." and produces ["Item no.", "5 is here."].
    #   Pattern 2 (full capture): fallback for non-digit continuations (e.g.,
    #              "Smith 2024", "the overview") — merges the full next fragment
    #              so continuations like "vol. 3 of the atlas." stay together.
    #
    # Related GitHub Issue:
    #     #47 - Abbreviations with trailing periods cause false sentence splits
    #     https://github.com/craigtrim/fast-sentence-segment/issues/47

    # Academic reference abbreviations — dual-pattern strategy per abbreviation.
    # These abbreviations (vol., no., fig., p., pp., art., etc.) introduce
    # a reference (number, name, or clause) and never legitimately end a
    # sentence on their own.
    #
    # Dual-pattern strategy:
    #   Pattern 1 (digit-only): fires first when the next fragment starts with
    #              a digit.  Extracts ONLY the numeric reference (including any
    #              trailing period that forms part of "abbrev. N." at sentence
    #              end), leaving the remainder as a separate sentence.
    #              Example: "See vol. 3. Results vary."
    #              spaCy → ["See vol.", "3. Results vary."]
    #              digit extract → "3." merged → "See vol. 3.", "Results vary."
    #   Pattern 2 (Roman-numeral full-capture): fires when the next fragment
    #              starts with a Roman numeral.  Captures the Roman numeral
    #              AND all following text so the entire reference phrase stays
    #              in one sentence.
    #              Example: "See vol. III for reference."
    #              spaCy → ["See vol.", "III for reference."]
    #              Roman capture → merged → "See vol. III for reference."
    #
    # Non-digit, non-Roman continuations (proper nouns like "Annals", "Alpha",
    # "Methodology") do NOT match either pattern and are left as separate
    # segments, which is the correct behaviour for those constructs.
    #
    # Related GitHub Issue:
    #     #47 - Abbreviations with trailing periods cause false sentence splits
    #     https://github.com/craigtrim/fast-sentence-segment/issues/47

    # "no." / "nos." as abbreviation for "number(s)".
    # Three-pattern strategy to handle the three cases:
    #   Pattern 1a (isolated lowercase "no."): the abbreviation for "number" in
    #              sentence-initial position — merge with any multi-word continuation,
    #              including capital-starting fragments like "Week 7 covers this."
    #              e.g. "He arrived. no. Week 7." → "He arrived." / "no. Week 7."
    #   Pattern 1b (isolated capital "No."): the English word "No" used as a
    #              standalone response/interjection.  Only merge when the next
    #              fragment starts with lowercase/digit to avoid merging genuine
    #              sentence pairs: "No. The implementation..." → split at "No."
    #              e.g. "No. The plan failed." → ["No.", "The plan failed."]
    #   Pattern 2+3 (digit-only + Roman): when "no." ends a longer sentence.
    (r"^no\.$", r"^(.+\s.+)$"),
    (r"^No\.$", r"^([a-z0-9].+\s.+)$"),
    # Negative lookbehind (?<![Nn][oO]) prevents matching "no no." (English
    # word repetition) so "No no no. Yes." is not incorrectly merged.
    (r"(?i)(?<![Nn][oO])\s+no\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)(?<![Nn][oO])\s+no\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    (r"(?i)^nos\.$", r"^(.+\s.+)$"),
    (r"(?i)(?<![Nn][oO][Ss])\s+nos\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)(?<![Nn][oO][Ss])\s+nos\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # vol. / vols.
    (r"(?i)\bvol\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bvol\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    (r"(?i)\bvols\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bvols\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # pt. (part)
    (r"(?i)\bpt\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bpt\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # ch. / chs. (chapter)
    (r"(?i)\bch\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bch\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    (r"(?i)\bchs\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bchs\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # sec. / secs. / sect.
    (r"(?i)\bsec\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bsec\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    (r"(?i)\bsecs\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bsecs\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    (r"(?i)\bsect\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bsect\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # fig. / figs.
    (r"(?i)\bfig\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bfig\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    (r"(?i)\bfigs\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bfigs\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # p. / pp. (page / pages)
    (r"(?i)\bp\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bp\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    (r"(?i)\bpp\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bpp\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # art. / arts.
    (r"(?i)\bart\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bart\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    (r"(?i)\barts\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\barts\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # para. / paras. / pars.
    (r"(?i)\bpara\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bpara\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    (r"(?i)\bparas\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bparas\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    (r"(?i)\bpars\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bpars\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # app. / appx.
    # Note: no negative lookahead guard here — "app. A of this article." must merge
    # even though "A" would otherwise trigger the guard for other abbreviations.
    (r"(?i)\bapp\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bapp\.$", r"^(.+)$"),
    (r"(?i)\bappx\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bappx\.$", r"^(.+)$"),
    # eq. (equation)
    (r"(?i)\beq\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\beq\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # tab. (table)
    (r"(?i)\btab\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\btab\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # fn. (footnote)
    (r"(?i)\bfn\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bfn\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # ann. / annot. (annotation)
    (r"(?i)\bann\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bann\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    (r"(?i)\bannot\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bannot\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # abr. (abridged)
    (r"(?i)\babr\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\babr\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # illus. (illustrated by)
    (r"(?i)\billus\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\billus\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # introd. (introduction)
    (r"(?i)\bintrod\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bintrod\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # def. (definition)
    (r"(?i)\bdef\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bdef\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # ex. (example)
    (r"(?i)\bex\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bex\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # pref. (preface)
    (r"(?i)\bpref\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bpref\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # lit. (literally / literature)
    (r"(?i)\blit\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\blit\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # n. / nn. (note / notes)
    (r"(?i)\bn\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bn\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    (r"(?i)\bnn\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bnn\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # l. / ll. (line / lines)
    (r"(?i)\bl\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bl\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    (r"(?i)\bll\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bll\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # bk. / bks.
    (r"(?i)\bbks?\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bbks?\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # ms. / mss. (manuscript / manuscripts)
    (r"(?i)\bmss?\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bmss?\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # fol. / fols. (folio / folios)
    (r"(?i)\bfols?\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bfols?\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # cols. (columns)
    (r"(?i)\bcols\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bcols\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # frag. (fragment)
    (r"(?i)\bfrag\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bfrag\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # rpt. (reprint)
    (r"(?i)\brpt\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\brpt\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # suppl. / suppl (supplement)
    (r"(?i)\bsuppl?\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bsuppl?\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),
    # corr. (correction)
    (r"(?i)\bcorr\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bcorr\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),

    # ── Ambiguous abbreviations also in SENTENCE_ENDING_ABBREVIATIONS ────────
    # These can legitimately end a sentence (e.g., "Contact the dept. HR follows.")
    # but also appear mid-sentence (e.g., "dept. Week 7 is referenced.").
    # Dual-pattern strategy:
    #   Pattern 1 (^abbrev.$): fires when the sentence IS just the abbreviation
    #              (sentence-initial position after spaCy splits) → merge anything
    #   Pattern 2 (\babbrev.$): fires when followed by lowercase/digit continuation
    #              (never capital → avoids merging legitimate sentence boundaries)

    # ext. — extension number reference
    # Sentence-initial "ext." (spaCy isolated it) → merge anything
    (r"(?i)^ext\.$", r"^(.+)$"),
    # Mid-sentence: digit followed by a period then space → terminal extension
    # number (e.g. "5. Ask for John." → extract "5.", leave "Ask for John.")
    (r"(?i)\bext\.$", r"^(\d[\d.\-–]*\.)(?=\s)"),
    # Mid-sentence: bare digit with no continuation (e.g. "42" with no text
    # after) → merge the digit alone
    (r"(?i)\bext\.$", r"^(\d[\d.\-–]*)$"),
    # Mid-sentence: lowercase continuation → merge everything
    (r"(?i)\bext\.$", r"^([a-z].+)$"),

    # approx. — approximation qualifier
    (r"(?i)^approx\.$", r"^(.+)$"),
    (r"(?i)\bapprox\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),

    # dept. — department reference
    (r"(?i)^dept\.$", r"^(.+)$"),
    (r"(?i)\bdept\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),

    # ── Scholarly / Latin abbreviations ──────────────────────────────────────

    # viz. (namely, to wit)
    (r"(?i)\bviz\.$", r"^(.+)$"),

    # cf. (compare) — guard: do NOT merge if next fragment is a complete sentence
    # (article + lowercase word heuristic)
    (r"(?i)\bcf\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),

    # ibid., / ibid.;
    (r"(?i)\bibid\.[,;]\.?$", r"^(.+)$"),

    # ibid. bare — same article+lowercase guard as cf.
    (r"(?i)\bibid\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),

    # N.B. / n.b. (nota bene)
    (r"(?i)\bN\.B\.$", r"^(.+)$"),

    # q.v. (which see)
    (r"(?i)\bq\.v\.$", r"^(.+)$"),

    # s.v. / s.vv. (sub verbo/verbis)
    (r"(?i)\bs\.vv?\.$", r"^(.+)$"),

    # op. cit. — Step 1: op. → cit.; Step 2: op. cit. → context
    (r"(?i)\bop\.$", r"^(.+)$"),
    (r"(?i)\bop\.\s+cit\.$", r"^(.+)$"),

    # loc. cit. — Step 1: loc.; Step 2: loc. cit.
    (r"(?i)\bloc\.$", r"^(.+)$"),
    (r"(?i)\bloc\.\s+cit\.$", r"^(.+)$"),

    # ca. (circa) — only full word "ca.", not single "c." (too ambiguous)
    (r"(?i)\bca\.$", r"^(.+)$"),

    # c. (circa) — single-letter form; guard against °C. (temperature unit)
    # The (?<!°) negative lookbehind prevents matching "25.5°C."
    (r"(?i)(?<!°)\bc\.$", r"^(.+)$"),

    # c.f. (alternate spelling of cf.)
    (r"(?i)\bc\.f\.$", r"^(.+)$"),

    # bk. / bks. (book/books)
    (r"(?i)\bbks?\.$", r"^(.+)$"),

    # ser. (series)
    (r"(?i)\bser\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bser\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),

    # fl. (floruit)
    (r"(?i)\bfl\.$", r"^(.+)$"),

    # a.k.a. (also known as)
    (r"(?i)\ba\.k\.a\.$", r"^(.+)$"),

    # sc. (scilicet — namely)
    (r"(?i)\bsc\.$", r"^(.+)$"),

    # scil. (alternate of scilicet)
    (r"(?i)\bscil\.$", r"^(.+)$"),

    # sic. (thus)
    (r"(?i)\bsic\.$", r"^(.+)$"),

    # ad loc.
    (r"(?i)\bad\s+loc\.$", r"^(.+)$"),

    # ad fin. (ad finem — at the end)
    (r"(?i)\bad\s+fin\.$", r"^(.+)$"),

    # ad init. (ad initium — at the beginning)
    (r"(?i)\bad\s+init\.$", r"^(.+)$"),

    # ad inf. (ad infinitum)
    (r"(?i)\bad\s+inf\.$", r"^(.+)$"),

    # ad med. (ad medium)
    (r"(?i)\bad\s+med\.$", r"^(.+)$"),

    # ad litt. (ad litteram)
    (r"(?i)\bad\s+litt\.$", r"^(.+)$"),

    # ad rem. (ad rem)
    (r"(?i)\bad\s+rem\.$", r"^(.+)$"),

    # in loc. (in loco)
    (r"(?i)\bin\s+loc\.$", r"^(.+)$"),

    # in re. (in re)
    (r"(?i)\bin\s+re\.$", r"^(.+)$"),

    # in ext. (in extenso)
    (r"(?i)\bin\s+ext\.$", r"^(.+)$"),

    # in toto.
    (r"(?i)\bin\s+toto\.$", r"^(.+)$"),

    # ut sup. (ut supra)
    (r"(?i)\but\s+sup\.$", r"^(.+)$"),

    # ut inf. (ut infra)
    (r"(?i)\but\s+inf\.$", r"^(.+)$"),

    # ut cit. (ut citatum)
    (r"(?i)\but\s+cit\.$", r"^(.+)$"),

    # ut al. (ut alii)
    (r"(?i)\but\s+al\.$", r"^(.+)$"),

    # art. cit. (articulo citato)
    (r"(?i)\bart\.\s+cit\.$", r"^(.+)$"),

    # et seq.
    (r"(?i)\bet\s+seq\.$", r"^(.+)$"),

    # et al., / et al.;
    (r"(?i)\bet\s+al\.[,;]\.?$", r"^(.+)$"),

    # et al. bare — same article+lowercase guard
    (r"(?i)\bet\s+al\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),

    # id. (idem)
    (r"(?i)\bid\.$", r"^(.+)$"),

    # ead. (eadem)
    (r"(?i)\bead\.$", r"^(.+)$"),

    # ap. (apud)
    (r"(?i)\bap\.$", r"^(.+)$"),

    # ff. (and following folios)
    (r"(?i)\bff\.$", r"^(.+)$"),

    # inf. (infra — below)
    (r"(?i)\binf\.$", r"^(.+)$"),

    # sup. (supra — above)
    (r"(?i)\bsup\.$", r"^(.+)$"),

    # vid. (vide — see)
    (r"(?i)\bvid\.$", r"^(.+)$"),

    # resp. (respectively)
    (r"(?i)\bresp\.$", r"^(.+)$"),

    # pro tem.
    (r"(?i)\bpro\s+tem\.$", r"^(.+)$"),

    # P.S. (postscript)
    (r"(?i)\bP\.S\.$", r"^(.+)$"),

    # P.P.S. (post postscript)
    (r"(?i)\bP\.P\.S\.$", r"^(.+)$"),

    # q.e.d. (quod erat demonstrandum) — mid-sentence use
    (r"(?i)\bq\.e\.d\.$", r"^(.+)$"),

    # r.i.p. (requiescat in pace)
    (r"(?i)\br\.i\.p\.$", r"^(.+)$"),

    # n.b. (lowercase nota bene)
    (r"(?i)\bn\.b\.$", r"^(.+)$"),

    # s.a. (sine anno — without year)
    (r"(?i)\bs\.a\.$", r"^(.+)$"),

    # s.l. (sine loco — without place)
    (r"(?i)\bs\.l\.$", r"^(.+)$"),

    # s.n. (sine nomine — without name)
    (r"(?i)\bs\.n\.$", r"^(.+)$"),

    # v.i. (vide infra — see below)
    (r"(?i)\bv\.i\.$", r"^(.+)$"),

    # v.s. (vide supra — see above)
    (r"(?i)\bv\.s\.$", r"^(.+)$"),

    # e.a. (et aliis — and others)
    (r"(?i)\be\.a\.$", r"^(.+)$"),

    # cap. (caput — chapter/head)
    (r"(?i)\bcap\.$", r"^(.+)$"),

    # lib. / libb. (liber / libri — book/books)
    (r"(?i)\blibb?\.$", r"^(.+)$"),

    # tit. (titulus — title)
    (r"(?i)\btit\.$", r"^(.+)$"),

    # gl. (glossa — gloss)
    (r"(?i)\bgl\.$", r"^(.+)$"),

    # gloss. (glossary)
    (r"(?i)\bgloss\.$", r"^(.+)$"),

    # schol. (scholium)
    (r"(?i)\bschol\.$", r"^(.+)$"),

    # cod. / codd. (codex / codices)
    (r"(?i)\bcodd?\.$", r"^(.+)$"),

    # serm. (sermo — sermon)
    (r"(?i)\bserm\.$", r"^(.+)$"),

    # hom. (homilia — homily)
    (r"(?i)\bhom\.$", r"^(.+)$"),

    # lect. (lectio — reading)
    (r"(?i)\blect\.$", r"^(.+)$"),

    # quaest. (quaestio — question)
    (r"(?i)\bquaest\.$", r"^(.+)$"),

    # disp. (disputatio)
    (r"(?i)\bdisp\.$", r"^(.+)$"),

    # a.d. (anno Domini)
    (r"(?i)\ba\.d\.$", r"^(.+)$"),

    # a.c. / b.c. / a.u.c.
    (r"(?i)\ba\.c\.$", r"^(.+)$"),
    (r"(?i)\bb\.c\.$", r"^(.+)$"),
    (r"(?i)\ba\.u\.c\.$", r"^(.+)$"),

    # i.q. / i.c. / l.c. / l.s.
    (r"(?i)\bi\.q\.$", r"^(.+)$"),
    (r"(?i)\bi\.c\.$", r"^(.+)$"),
    (r"(?i)\bl\.c\.$", r"^(.+)$"),
    (r"(?i)\bl\.s\.$", r"^(.+)$"),

    # m.s. / n.d. / n.p. / n.s. / n.t.
    (r"(?i)\bm\.s\.$", r"^(.+)$"),
    (r"(?i)\bn\.d\.$", r"^(.+)$"),
    (r"(?i)\bn\.p\.$", r"^(.+)$"),
    (r"(?i)\bn\.s\.$", r"^(.+)$"),
    (r"(?i)\bn\.t\.$", r"^(.+)$"),

    # p.c. / p.p. / t.b.
    (r"(?i)\bp\.c\.$", r"^(.+)$"),
    (r"(?i)\bp\.p\.$", r"^(.+)$"),
    (r"(?i)\bt\.b\.$", r"^(.+)$"),

    # ed. / eds.
    (r"(?i)\beds?\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\beds?\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),

    # trans.
    (r"(?i)\btrans\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\btrans\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),

    # comp. / comps.
    (r"(?i)\bcomps?\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\bcomps?\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),

    # repr.
    (r"(?i)\brepr\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\brepr\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),

    # rev.
    (r"(?i)\brev\.$", r"^(\d[\d\-–]*\.)(?=\s+[A-Z]|\s*$)"),
    (r"(?i)\brev\.$", r"^(?!(?:The|A|An)\s+[a-z])(.+)$"),

    # anon. / b. (born) / d. (died) / r. (reigned)
    (r"(?i)\banon\.$", r"^(.+)$"),
    (r"(?i)\bb\.$", r"^(.+)$"),
    (r"(?i)\bd\.$", r"^(.+)$"),
    (r"(?i)\br\.$", r"^(.+)$"),

    # ── Personal title abbreviations ─────────────────────────────────────────
    # spaCy claims to know Dr., Mr., Mrs., Ms., Prof., Gen., Col., Capt., Lt.,
    # Sgt., Maj. — but in practice en_core_web_sm still splits at them when
    # the following word is not a proper name (e.g. "Maj. Week 7").  Explicit
    # patterns here ensure the merger always corrects these false splits.

    (r"(?i)\bMr\.$", r"^(.+)$"),
    (r"(?i)\bMrs\.$", r"^(.+)$"),
    (r"(?i)\bMs\.$", r"^(.+)$"),
    (r"(?i)\bDr\.$", r"^(.+)$"),
    (r"(?i)\bProf\.$", r"^(.+)$"),
    # Sr./Jr. — three-pattern strategy (mirrors Inc./Corp./Co. approach):
    #   Pattern 1 (^abbrev.$): isolated token (spaCy split before and after)
    #              → merge with anything, e.g. "Jr. Week 7 covers this."
    #   Pattern 2 (func-word + abbrev.$): reference context after a function
    #              word, e.g. "Refer to SR. Week 7" → merge with anything.
    #   Pattern 3 (\babbrev.$): general fallback for name-suffix position,
    #              e.g. "John Smith Jr." — merge only with lowercase/digit next
    #              fragment to avoid merging real boundaries like
    #              "John Smith Jr. His son took over." (capital H → no merge).
    # Surface-form variants SR./JR. are handled case-insensitively throughout.
    (r"(?i)^Sr\.$", r"^(.+)$"),
    (rf"(?i)\b{_FUNC_WORD_SEQ}\s+Sr\.$", r"^(.+)$"),
    (r"(?i)\bSr\.$", r"^([a-z0-9].+)$"),
    (r"(?i)^Jr\.$", r"^(.+)$"),
    (rf"(?i)\b{_FUNC_WORD_SEQ}\s+Jr\.$", r"^(.+)$"),
    (r"(?i)\bJr\.$", r"^([a-z0-9].+)$"),
    (r"(?i)\bRev\.$", r"^(.+)$"),

    # ── Military titles ───────────────────────────────────────────────────────

    (r"(?i)\bGen\.$", r"^(.+)$"),
    (r"(?i)\bCol\.$", r"^(.+)$"),
    (r"(?i)\bMaj\.$", r"^(.+)$"),
    (r"(?i)\bCapt\.$", r"^(.+)$"),
    (r"(?i)\bLt\.$", r"^(.+)$"),
    (r"(?i)\bSgt\.$", r"^(.+)$"),
    (r"(?i)\bAdm\.$", r"^(.+)$"),

    # ── Government titles ────────────────────────────────────────────────────

    (r"(?i)\bGov\.$", r"^(.+)$"),
    (r"(?i)\bSen\.$", r"^(.+)$"),
    (r"(?i)\bRep\.$", r"^(.+)$"),

    # ── Other personal titles not in spaCy's internal list ───────────────────

    (r"(?i)\bCpl\.$", r"^(.+)$"),
    (r"(?i)\bPvt\.$", r"^(.+)$"),
    (r"(?i)\bCmdr\.$", r"^(.+)$"),
    (r"(?i)\bPres\.$", r"^(.+)$"),
    (r"(?i)\bHon\.$", r"^(.+)$"),
    (r"(?i)\bFr\.$", r"^(.+)$"),
    (r"(?i)\bMsgr\.$", r"^(.+)$"),
    (r"(?i)\bMme\.$", r"^(.+)$"),
    (r"(?i)\bMlle\.$", r"^(.+)$"),
    (r"(?i)\bEns\.$", r"^(.+)$"),
    (r"(?i)\bBrig\.$", r"^(.+)$"),
    (r"(?i)\bSpec\.$", r"^(.+)$"),
    (r"(?i)\bPfc\.$", r"^(.+)$"),
    (r"(?i)\bAmb\.$", r"^(.+)$"),
    (r"(?i)\bAtty\.$", r"^(.+)$"),
    (r"(?i)\bDir\.$", r"^(.+)$"),
    (r"(?i)\bInsp\.$", r"^(.+)$"),
    (r"(?i)\bAsst\.$", r"^(.+)$"),
    (r"(?i)\bDep\.$", r"^(.+)$"),
    (r"(?i)\bCommr\.$", r"^(.+)$"),
    (r"(?i)\bCllr\.$", r"^(.+)$"),
    (r"(?i)\bCong\.$", r"^(.+)$"),
    (r"(?i)\bBr\.$", r"^(.+)$"),
    (r"(?i)\bEsq\.$", r"^(.+)$"),
    (r"(?i)\bMessrs\.$", r"^(.+)$"),
    (r"(?i)\bMgr\.$", r"^(.+)$"),
    (r"(?i)\bSupt\.$", r"^(.+)$"),
    (r"(?i)\bDel\.$", r"^(.+)$"),
    (r"(?i)\bMin\.$", r"^(.+)$"),
    (r"(?i)\bSec\.$", r"^(.+)$"),

    # ── Geographic abbreviations not in spaCy's internal list ────────────────

    (r"(?i)\bSq\.$", r"^(.+)$"),
    (r"(?i)\bTer\.$", r"^(.+)$"),
    (r"(?i)\bRte\.$", r"^(.+)$"),
    (r"(?i)\bTwp\.$", r"^(.+)$"),
    (r"(?i)\bJct\.$", r"^(.+)$"),
    (r"(?i)\bCtr\.$", r"^(.+)$"),
    (r"(?i)\bIsl\.$", r"^(.+)$"),
    (r"(?i)\bPen\.$", r"^(.+)$"),
    (r"(?i)\bRiv\.$", r"^(.+)$"),
    (r"(?i)\bLk\.$", r"^(.+)$"),
    (r"(?i)\bMtn\.$", r"^(.+)$"),
    (r"(?i)\bApt\.$", r"^(.+)$"),
    (r"(?i)\bPkwy\.$", r"^(.+)$"),
    (r"(?i)\bHwy\.$", r"^(.+)$"),
    (r"(?i)\bBldg\.$", r"^(.+)$"),
    (r"(?i)\bSte\.$", r"^(.+)$"),
    (r"(?i)\bLn\.$", r"^(.+)$"),
    (r"(?i)\bCt\.$", r"^(.+)$"),
    (r"(?i)\bPl\.$", r"^(.+)$"),
    (r"(?i)\bRd\.$", r"^(.+)$"),
    (r"(?i)\bBlvd\.$", r"^(.+)$"),
    (r"(?i)\bAve\.$", r"^(.+)$"),
    (r"(?i)\bSt\.$", r"^(.+)$"),
    (r"(?i)\bMt\.$", r"^(.+)$"),
    (r"(?i)\bFt\.$", r"^(.+)$"),

    # ── Month abbreviations ───────────────────────────────────────────────────

    (r"(?i)\bJan\.$", r"^(.+)$"),
    (r"(?i)\bFeb\.$", r"^(.+)$"),
    (r"(?i)\bMar\.$", r"^(.+)$"),
    (r"(?i)\bApr\.$", r"^(.+)$"),
    (r"(?i)\bJun\.$", r"^(.+)$"),
    (r"(?i)\bJul\.$", r"^(.+)$"),
    (r"(?i)\bAug\.$", r"^(.+)$"),
    (r"(?i)\bSept?\.$", r"^(.+)$"),
    (r"(?i)\bOct\.$", r"^(.+)$"),
    (r"(?i)\bNov\.$", r"^(.+)$"),
    (r"(?i)\bDec\.$", r"^(.+)$"),

    # ── Day abbreviations ─────────────────────────────────────────────────────

    (r"(?i)\bMon\.$", r"^(.+)$"),
    (r"(?i)\bTues?\.$", r"^(.+)$"),
    (r"(?i)\bWed\.$", r"^(.+)$"),
    (r"(?i)\bThurs?\.$", r"^(.+)$"),
    (r"(?i)\bThu\.$", r"^(.+)$"),
    (r"(?i)\bFri\.$", r"^(.+)$"),
    (r"(?i)\bSat\.$", r"^(.+)$"),
    (r"(?i)\bSun\.$", r"^(.+)$"),

    # ── Business abbreviations ────────────────────────────────────────────────

    (r"(?i)\bAssoc\.$", r"^(.+)$"),
    (r"(?i)\bGrp\.$", r"^(.+)$"),
    (r"(?i)\bIntl\.$", r"^(.+)$"),
    (r"(?i)\bMfg\.$", r"^(.+)$"),
    (r"(?i)\bDist\.$", r"^(.+)$"),
    (r"(?i)\bMgmt\.$", r"^(.+)$"),
    (r"(?i)\bEnt\.$", r"^(.+)$"),
    (r"(?i)\bTech\.$", r"^(.+)$"),
    (r"(?i)\bvs\.$", r"^(.+)$"),

    # Inc., Corp., Ltd., Co., Bros. can legitimately end sentences
    # (e.g. "He works at Apple Inc."), so use a multi-pattern strategy:
    #   Pattern 1 (^abbrev.$): fires when the sentence IS just the abbreviation
    #              (sentence-initial position after spaCy splits) → merge anything
    #   Pattern 2 (colon + abbrev.$): fires when a colon directly precedes the
    #              abbreviation (e.g. "The rule is: Inc. Week 7") indicating it
    #              is used in a definitional/reference context → always merge.
    #   Pattern 3 (func-word + abbrev.$): fires when a function word / preposition
    #              immediately precedes the abbreviation, indicating it is used as
    #              a reference abbreviation (not a company-name suffix), so the
    #              following fragment should always merge regardless of case
    #              e.g. "specifically Inc. Week 7." / "consistent with Corp. Week 3."
    #   Pattern 4 (\babbrev.$): fallback for mid-sentence — merge only when the
    #              next fragment starts with lowercase/digit (avoids merging real
    #              sentence boundaries like "Apple Inc. They are hiring.")
    #
    # Related GitHub Issue:
    #     https://github.com/craigtrim/fast-sentence-segment/issues/47
    (r"(?i)^Inc\.$", r"^(.+)$"),
    (r"(?i):\s*Inc\.$", r"^(.+)$"),      # colon context → always merge
    (r"(?i);\s*Inc\.$", r"^(.+)$"),      # semicolon context → always merge
    (rf"(?i)\b{_COMPANY_FUNC_WORD_SEQ}\s+Inc\.$", r"^(.+)$"),
    (r"(?i)[—–]\s*Inc\.$", r"^(.+)$"),   # em/en-dash → inside parenthetical
    (r"(?i)\bInc\.$", r"^([a-z0-9].+)$"),
    (r"(?i)^Corp\.$", r"^(.+)$"),
    (r"(?i):\s*Corp\.$", r"^(.+)$"),
    (r"(?i);\s*Corp\.$", r"^(.+)$"),
    (rf"(?i)\b{_COMPANY_FUNC_WORD_SEQ}\s+Corp\.$", r"^(.+)$"),
    (r"(?i)[—–]\s*Corp\.$", r"^(.+)$"),
    (r"(?i)\bCorp\.$", r"^([a-z0-9].+)$"),
    (r"(?i)^Ltd\.$", r"^(.+)$"),
    (r"(?i):\s*Ltd\.$", r"^(.+)$"),
    (r"(?i);\s*Ltd\.$", r"^(.+)$"),
    (rf"(?i)\b{_COMPANY_FUNC_WORD_SEQ}\s+Ltd\.$", r"^(.+)$"),
    (r"(?i)[—–]\s*Ltd\.$", r"^(.+)$"),
    (r"(?i)\bLtd\.$", r"^([a-z0-9].+)$"),
    (r"(?i)^Co\.$", r"^(.+)$"),
    (r"(?i):\s*Co\.$", r"^(.+)$"),
    (r"(?i);\s*Co\.$", r"^(.+)$"),
    (rf"(?i)\b{_COMPANY_FUNC_WORD_SEQ}\s+Co\.$", r"^(.+)$"),
    (r"(?i)[—–]\s*Co\.$", r"^(.+)$"),
    (r"(?i)\bCo\.$", r"^([a-z0-9].+)$"),
    (r"(?i)^Bros\.$", r"^(.+)$"),
    (r"(?i):\s*Bros\.$", r"^(.+)$"),
    (r"(?i);\s*Bros\.$", r"^(.+)$"),
    (rf"(?i)\b{_COMPANY_FUNC_WORD_SEQ}\s+Bros\.$", r"^(.+)$"),
    (r"(?i)[—–]\s*Bros\.$", r"^(.+)$"),
    (r"(?i)\bBros\.$", r"^([a-z0-9].+)$"),

    # ── Measurement abbreviations ─────────────────────────────────────────────

    (r"(?i)\best\.$", r"^(.+)$"),
    (r"(?i)\bmin\.$", r"^(.+)$"),
    (r"(?i)\bmax\.$", r"^(.+)$"),
    (r"(?i)\bavg\.$", r"^(.+)$"),
    (r"(?i)\bstd\.$", r"^(.+)$"),
    (r"(?i)\bsq\.$", r"^(.+)$"),
    (r"(?i)\bwt\.$", r"^(.+)$"),
    (r"(?i)\bht\.$", r"^(.+)$"),
    (r"(?i)\btemp\.$", r"^(.+)$"),
    (r"(?i)\balt\.$", r"^(.+)$"),
    (r"(?i)\blat\.$", r"^(.+)$"),
    (r"(?i)\blon\.$", r"^(.+)$"),
    (r"(?i)\bdiam\.$", r"^(.+)$"),
    (r"(?i)\bdeg\.$", r"^(.+)$"),
    (r"(?i)\bqty\.$", r"^(.+)$"),

    # ── Medical / scientific abbreviations ───────────────────────────────────

    (r"(?i)\bdiag\.$", r"^(.+)$"),
    (r"(?i)\bsymp\.$", r"^(.+)$"),
    (r"(?i)\banat\.$", r"^(.+)$"),
    (r"(?i)\bbiol\.$", r"^(.+)$"),
    (r"(?i)\bchem\.$", r"^(.+)$"),
    (r"(?i)\bphys\.$", r"^(.+)$"),
    (r"(?i)\bpsych\.$", r"^(.+)$"),
    (r"(?i)\bsurg\.$", r"^(.+)$"),
    (r"(?i)\bped\.$", r"^(.+)$"),
    (r"(?i)\bpharm\.$", r"^(.+)$"),
    (r"(?i)\bvet\.$", r"^(.+)$"),
    (r"(?i)\bneuro\.$", r"^(.+)$"),
    (r"(?i)\bcardio\.$", r"^(.+)$"),
    (r"(?i)\bderm\.$", r"^(.+)$"),
    (r"(?i)\bortho\.$", r"^(.+)$"),
    (r"(?i)\bpath\.$", r"^(.+)$"),
    (r"(?i)\brad\.$", r"^(.+)$"),
    (r"(?i)\bsp\.$", r"^(.+)$"),
    (r"(?i)\bssp\.$", r"^(.+)$"),
    (r"(?i)\bvar\.$", r"^(.+)$"),
    (r"(?i)\bfam\.$", r"^(.+)$"),
    (r"(?i)\bord\.$", r"^(.+)$"),

    # ── Grammar / linguistic abbreviations ───────────────────────────────────

    (r"(?i)\badj\.$", r"^(.+)$"),
    (r"(?i)\badv\.$", r"^(.+)$"),
    (r"(?i)\bprep\.$", r"^(.+)$"),
    (r"(?i)\bconj\.$", r"^(.+)$"),
    (r"(?i)\bpron\.$", r"^(.+)$"),
    (r"(?i)\bpl\.$", r"^(.+)$"),
    (r"(?i)\bsing\.$", r"^(.+)$"),
    (r"(?i)\bcolloq\.$", r"^(.+)$"),
    (r"(?i)\bdial\.$", r"^(.+)$"),
    (r"(?i)\barch\.$", r"^(.+)$"),
    (r"(?i)\bobs\.$", r"^(.+)$"),
    (r"(?i)\besp\.$", r"^(.+)$"),
    (r"(?i)\bprob\.$", r"^(.+)$"),
    (r"(?i)\busu\.$", r"^(.+)$"),
    (r"(?i)\boccas\.$", r"^(.+)$"),
    (r"(?i)\battrib\.$", r"^(.+)$"),
    (r"(?i)\bcompar\.$", r"^(.+)$"),
    (r"(?i)\bsuperl\.$", r"^(.+)$"),
    (r"(?i)\brefl\.$", r"^(.+)$"),
    (r"(?i)\bsubj\.$", r"^(.+)$"),
    (r"(?i)\bimper\.$", r"^(.+)$"),

    # ── General / editorial abbreviations ────────────────────────────────────

    (r"(?i)\bauth\.$", r"^(.+)$"),
    (r"(?i)\bbibl\.$", r"^(.+)$"),
    (r"(?i)\bbiog\.$", r"^(.+)$"),
    (r"(?i)\bcalc\.$", r"^(.+)$"),
    (r"(?i)\bcat\.$", r"^(.+)$"),
    (r"(?i)\bcent\.$", r"^(.+)$"),
    (r"(?i)\bcit\.$", r"^(.+)$"),
    (r"(?i)\bcl\.$", r"^(.+)$"),
    (r"(?i)\bcoll\.$", r"^(.+)$"),
    (r"(?i)\bcomm\.$", r"^(.+)$"),
    (r"(?i)\bconc\.$", r"^(.+)$"),
    (r"(?i)\bconf\.$", r"^(.+)$"),
    (r"(?i)\bconst\.$", r"^(.+)$"),
    (r"(?i)\bcont\.$", r"^(.+)$"),
    (r"(?i)\bcrit\.$", r"^(.+)$"),
    (r"(?i)\bderiv\.$", r"^(.+)$"),
    (r"(?i)\bdict\.$", r"^(.+)$"),
    (r"(?i)\bdisc\.$", r"^(.+)$"),
    (r"(?i)\bdoc\.$", r"^(.+)$"),
    (r"(?i)\bdram\.$", r"^(.+)$"),
    (r"(?i)\beccl\.$", r"^(.+)$"),
    (r"(?i)\bencyc\.$", r"^(.+)$"),
    (r"(?i)\beval\.$", r"^(.+)$"),
    (r"(?i)\bexcl\.$", r"^(.+)$"),
    (r"(?i)\bexec\.$", r"^(.+)$"),
    (r"(?i)\bexpl\.$", r"^(.+)$"),
    (r"(?i)\bgram\.$", r"^(.+)$"),
    (r"(?i)\bhist\.$", r"^(.+)$"),
    (r"(?i)\bincl\.$", r"^(.+)$"),
    (r"(?i)\bjuris\.$", r"^(.+)$"),
    (r"(?i)\blang\.$", r"^(.+)$"),
    (r"(?i)\bmisc\.$", r"^(.+)$"),
    (r"(?i)\bmod\.$", r"^(.+)$"),
    (r"(?i)\bnatl\.$", r"^(.+)$"),
    (r"(?i)\borig\.$", r"^(.+)$"),
    (r"(?i)\bphil\.$", r"^(.+)$"),
    (r"(?i)\bproc\.$", r"^(.+)$"),
    (r"(?i)\bprov\.$", r"^(.+)$"),
    (r"(?i)\bpub\.$", r"^(.+)$"),
    (r"(?i)\brec\.$", r"^(.+)$"),
    (r"(?i)\bref\.$", r"^(.+)$"),
    (r"(?i)\breg\.$", r"^(.+)$"),
    (r"(?i)\brel\.$", r"^(.+)$"),
    (r"(?i)\bsched\.$", r"^(.+)$"),
    (r"(?i)\bspec\.$", r"^(.+)$"),
    (r"(?i)\bstat\.$", r"^(.+)$"),
    (r"(?i)\bstruct\.$", r"^(.+)$"),
    (r"(?i)\bsymb\.$", r"^(.+)$"),
    (r"(?i)\bsyn\.$", r"^(.+)$"),
    (r"(?i)\btrad\.$", r"^(.+)$"),

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
        # Pattern to detect an interior sentence break inside a spaCy-merged
        # fragment.  When spaCy fails to split at a lowercase abbreviation
        # (e.g. "frag.", "path."), it groups the abbreviation with the preceding
        # sentence: "He arrived early. frag."  This pattern matches such fragments
        # so the merger can split them before attempting a merge.
        #
        # Pattern: ends with a single-word lowercase abbreviation (no spaces
        # inside), preceded by a period+space that follows a sentence-closing word.
        # e.g. "He arrived early. frag." → ("He arrived early.", "frag.")
        #
        # Constraints:
        # - The trailing abbreviation starts with [a-z] and has no spaces inside
        # - The period before the space is a sentence-end marker (not part of an
        #   abbreviation like "ad loc.")
        self._interior_break_re = re.compile(r'^(.*)\.\s+([a-z][^\s.]+\.)$')

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

        # Strip double-period artifact created by _clean_spacing(): when the
        # source text had a double-space after an abbreviation (e.g. "Sgt.  next"),
        # _clean_spacing() converts it to "Sgt.. next", then spaCy splits at
        # "Sgt.." leaving a sentence that ends with "..".  Strip one period so
        # the standard MERGE_PATTERNS can fire against the expected single ".".
        # Guard: do NOT strip ellipsis ("...") — only exact double-period ("..").
        if current.endswith('..') and not current.endswith('...'):
            current = current[:-1]

        # Parenthetical context: if the next fragment contains a closing
        # parenthesis and the current sentence has an unclosed opening
        # parenthesis, the split is inside a parenthetical phrase — always
        # merge fully so the parenthetical is kept intact.
        # Example: "Results (nos. Week 3) confirm the hypothesis."
        # spaCy splits at "nos." → ["Results (nos.", "Week 3) confirm…"]
        # The closing ")" in next_sent and the unclosed "(" in current signal
        # that this is a mid-parenthetical split.
        #
        # Related GitHub Issue:
        #     #34 - Citation / middle-initial handling
        #     https://github.com/craigtrim/fast-sentence-segment/issues/34
        if ')' in next_sent:
            last_open = current.rfind('(')
            if last_open >= 0 and ')' not in current[last_open:]:
                return (current + " " + next_sent.strip(), "")

        for ending_pattern, extract_pattern in self._patterns:
            if ending_pattern.search(current):
                match = extract_pattern.match(next_sent)
                if match:
                    # Extract the portion to merge
                    extracted = match.group(1)
                    # Fix spaCy tokenization artifact: when spaCy splits
                    # "abbrev. Word" as ["abbrev", ". Word"], the extracted
                    # content starts with ". " which creates "abbrev. . Word"
                    # (double period+space) after merging.  Strip the leading
                    # ". " so the result is "abbrev. Word" (single period+space).
                    if current.endswith('.') and extracted.startswith('. '):
                        extracted = extracted[2:]
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

                # Pre-check: detect fragments where spaCy grouped a lowercase
                # abbreviation with the preceding complete sentence.
                # e.g. "He arrived early. frag." is produced as one segment when
                # spaCy does not recognise "frag."/"path." as sentence starters.
                # Split the fragment and merge the abbreviation piece with the
                # next sentence instead.
                # e.g. "He arrived early. frag." + "Week 7 covers this."
                # →  "He arrived early." (committed)
                # →  "frag." merged with "Week 7 covers this."
                #    → "frag. Week 7 covers this." (committed)
                interior_match = self._interior_break_re.match(current)
                if interior_match:
                    before_part = interior_match.group(1) + '.'
                    abbrev_part = interior_match.group(2)
                    inner_merge = self._try_merge(abbrev_part, next_sent)
                    if inner_merge:
                        inner_merged, inner_remainder = inner_merge
                        result.append(before_part)
                        result.append(inner_merged)
                        if inner_remainder:
                            sentences = sentences[:i+2] + [inner_remainder] + sentences[i+2:]
                            sentences[i+1] = inner_remainder
                        i += 2
                        continue

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

                # Secondary check: when spaCy splits at a clause-level
                # punctuation mark (";", ":"), the following fragment is still
                # part of the same sentence.  If that fragment's first token
                # matches one of our known MERGE_PATTERNS abbreviations, re-join.
                # e.g. "Two sources agree;" + "n.b. Week 3..." → one sentence
                # e.g. "The rule is:" + "c.f. Week 7 provides the answer." → one
                # Note: only fires for abbreviations that remain in MERGE_PATTERNS
                # (personal-title abbreviations that have been removed will not
                # trigger this path).
                #
                # SpacyDocSegmenter appends a "." to any fragment lacking terminal
                # punctuation, so a sentence that ended with ";" becomes ";." after
                # segmentation.  We must also detect this artifact so the check
                # fires correctly.
                # Related GitHub Issue:
                #     https://github.com/craigtrim/fast-sentence-segment/issues/47
                _current_stripped = current.rstrip('.')
                _ends_with_clause_punct = (
                    current and current[-1] in (';', ':')
                ) or (
                    _current_stripped and _current_stripped[-1] in (';', ':')
                )
                if _ends_with_clause_punct and next_sent:
                    first_tok = next_sent.split()[0]
                    _merged = False
                    for ep, _ in self._patterns:
                        if ep.search(first_tok):
                            # Guard: when the fragment following the
                            # semicolon/colon is longer than just the
                            # abbreviation token AND the token is a personal
                            # title (Dr., Sgt., Gen., …) followed by an
                            # uppercase word, the semicolon is a sentence
                            # boundary — not a clause separator.
                            # e.g. "The report was completed;\nDr. Smith…"
                            #       → two sentences (newline was converted to ";."
                            #         by NewlinesToPeriods; Dr. starts a new sentence)
                            # e.g. "Two sources agree; Sgt. Week 3…"
                            #       → one sentence (inline; spaCy isolated "Sgt."
                            #         as a standalone token = next_sent is just "Sgt.")
                            rest = next_sent[len(first_tok):].strip()
                            if (
                                rest
                                and first_tok in _PERSONAL_TITLE_ABBREV_SET
                                and rest[0].isupper()
                            ):
                                # Title abbrev + proper name continuation →
                                # real sentence boundary; do not merge.
                                break
                            # Use _current_stripped (without the period that
                            # SpacyDocSegmenter appended to ";"-ending fragments)
                            # to avoid double-space after PostProcessStructure
                            # replaces ";." → "; ".
                            result.append(_current_stripped + " " + next_sent.strip())
                            i += 2
                            _merged = True
                            break
                    if not _merged:
                        result.append(current)
                        i += 1
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
