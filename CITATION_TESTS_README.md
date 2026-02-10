# Citation Tests for Issue #31

## Overview
Comprehensive test suite for APA, MLA, and pseudo-citation pattern handling in the sentence segmenter.

## Test Files Created

### 1. test_apa_citations_comprehensive.py
**Location:** `tests/hard/test_apa_citations_comprehensive.py`
**Test Cases:** 58+
**Coverage:**
- Single author (full name and initials)
- Multiple authors (2, 3, 4+)
- Et al. format
- Organizational authors
- Date variations (year, month, full date)
- Special dates (n.d., in press)
- Edition and volume patterns
- Online source patterns
- Name variations (hyphens, suffixes, prefixes)
- Multiple citations in sequence
- Subtitle patterns
- Editor/translator patterns
- Journal articles
- Conference papers
- Dissertations and theses
- Report formats

### 2. test_mla_citations_comprehensive.py
**Location:** `tests/hard/test_mla_citations_comprehensive.py`
**Test Cases:** 53+
**Coverage:**
- Single, dual, and multiple author book citations
- Books with editions
- Edited anthologies
- Chapters in edited books
- Journal articles
- Magazine articles
- Newspaper articles
- Web sources
- Anonymous works
- Corporate authors
- Names with suffixes and hyphens
- Multivolume works
- Series
- Translations
- Republished books
- Dissertations
- Conference papers
- Reviews
- Introductions/prefaces
- Book subtitles
- Government publications
- Sacred texts
- Films

### 3. test_pseudo_citations_comprehensive.py
**Location:** `tests/hard/test_pseudo_citations_comprehensive.py`
**Test Cases:** 60+
**Coverage:**
- Journalistic/news style (By Author, Date)
- Blog/web style
- Legal citations (case law, statutes)
- Technical/academic informal
- Patent citations
- Conference/proceedings informal
- Social media style
- Archive/manuscript citations
- Mixed format citations
- Press releases
- Interview citations
- Email citations
- Lecture/speech citations
- Wikipedia style
- Database/software citations
- Music/audio citations
- Video/multimedia
- Art citations
- Map/chart citations
- Advertisement citations
- Performance citations
- Repository/code citations
- Standard/specification citations

### 4. test_citation_edge_cases_comprehensive.py
**Location:** `tests/hard/test_citation_edge_cases_comprehensive.py`
**Test Cases:** 78+
**Coverage:**
- **CORE ISSUE #31:** Parenthetical years after periods (e.g., "Name. (2011). Title")
- Multiple parentheticals in citations
- Abbreviations that look like initials (Dr., Prof., St., Mt.)
- Multiple sentences within citations
- Numeric and special date patterns (2023a, 2023b, date ranges)
- Institutional names with periods (U.S., U.K., A.C.L.U., N.A.S.A.)
- Quotes and titles with periods in citations
- Citations with multiple author abbreviations
- Citations at sentence boundaries
- Citations with URLs
- Mixed citation and regular text
- Volume and issue numbers
- Editor abbreviations
- Very short author names
- Very long author names
- Citations with ampersand vs "and"
- Parenthetical authors
- Multiple periods in close proximity
- Citations with brackets
- Citations with slashes
- Question/exclamation marks in titles
- No date variations
- Forthcoming publications
- Season dates
- Personal communications
- Reprint editions
- Translated works with original dates
- Advance online publications
- Initials without spaces
- Middle names spelled out
- Compound last names
- Apostrophes in names (O'Brien, D'Angelo)
- Mac/Mc prefixes
- Names from different cultures

### 5. test_citation_patterns_comprehensive.py
**Location:** `tests/hard/test_citation_patterns_comprehensive.py`
**Test Cases:** 84+
**Coverage:**
- Pattern: Name. (Year). - Basic APA
- Pattern: LastName, FirstName. (Year). - Full name APA
- Pattern: LastName, F. (Year). - Initial APA
- Pattern: LastName, F. M. (Year). - Multiple initials
- Pattern: Author. (Year, Month). - Month included
- Pattern: Author. (Year, Month Day). - Full date
- Pattern: Organization. (Year). - Organizational author
- Pattern: Multiple authors with &
- Pattern: et al.
- Pattern: MLA book citation
- Pattern: MLA article citation
- Pattern: By Author, Date (Journalistic)
- Pattern: Legal case citation
- Pattern: Numbered reference [1]
- Pattern: Superscript reference ¹
- Sequential citations
- Citations mixed with regular sentences
- Title case preservation
- Subtitle patterns
- Edition markers
- Volume markers
- Page ranges
- DOI patterns
- Retrieval dates
- In press / no date
- Editor patterns
- Translator patterns
- Multiple works by same author (a, b, c)
- Proceedings patterns
- Presented at patterns
- Dissertation patterns
- Report patterns
- Complex nested parentheses
- Citations with brackets
- Very complex real-world examples
- Institutional abbreviations
- Names with prefixes
- Names with suffixes in patterns

## Total Test Coverage

**Total Test Cases:** 334+ across 5 files

## Test Execution

Run all citation tests:
```bash
pytest tests/hard/test_*citations*.py tests/hard/test_citation*.py -v
```

Run individual test files:
```bash
pytest tests/hard/test_apa_citations_comprehensive.py -v
pytest tests/hard/test_mla_citations_comprehensive.py -v
pytest tests/hard/test_pseudo_citations_comprehensive.py -v
pytest tests/hard/test_citation_edge_cases_comprehensive.py -v
pytest tests/hard/test_citation_patterns_comprehensive.py -v
```

## Current Status

As of creation (2026-02-10), these tests are expected to FAIL. This is intentional for Test-Driven Development (TDD). The implementation to fix Issue #31 should make these tests pass.

## Key Testing Focus

The primary issue being addressed is:
> **APA-style citations are being incorrectly split, with parenthetical year information isolated on separate lines.**

Example problematic input:
```
Matolino, Bernard. (2011). The (Mal) Function of "it" in Ifeanyi Menkiti's Normative Account of Person.
```

Current (incorrect) output:
```
Matolino, Bernard.
(2011).
The (Mal) Function of "it" in Ifeanyi Menkiti's Normative Account of Person.
```

Expected (correct) output:
```
Matolino, Bernard. (2011). The (Mal) Function of "it" in Ifeanyi Menkiti's Normative Account of Person.
```

## Implementation Notes

The test suite validates that:
1. Author names followed by periods should not split if followed by (Year)
2. Citations should remain as cohesive units
3. Various citation formats (APA, MLA, informal) are handled correctly
4. Edge cases with abbreviations, special characters, and complex names work properly
5. Citation boundaries are detected accurately when mixed with regular text
