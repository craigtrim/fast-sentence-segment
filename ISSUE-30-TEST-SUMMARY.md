# Issue #30: Numbered Titles Test Suite

## Overview
Comprehensive test suite for incorrect sentence breaks on numbered titles (e.g., 'Part 2.', 'Module 3.', 'Chapter IV.').

**Total Test Cases: 468**

## Test Coverage Breakdown

### By Keyword (Arabic Numerals)
- **Part** (TestNumberedTitlesArabicNumerals): 28 tests
  - Numbers 1-25, 100, 999
  - Various positions in text

- **Module** (TestNumberedTitlesModule): 27 tests
  - Educational/course context
  - Numbers 1-27

- **Chapter** (TestNumberedTitlesChapter): 27 tests
  - Book/document context
  - Numbers 1-27

- **Section** (TestNumberedTitlesSection): 27 tests
  - Academic/documentation context
  - Including subsections (3.1, 3.2)

- **Week** (TestNumberedTitlesWeek): 27 tests
  - Course/schedule context
  - Numbers 1-27

- **Step** (TestNumberedTitlesStep): 27 tests
  - Tutorial/instruction context
  - Numbers 1-27

- **Phase** (TestNumberedTitlesPhase): 27 tests
  - Project management context
  - Numbers 1-27

- **Unit** (TestNumberedTitlesUnit): 27 tests
  - Educational/curriculum context
  - Numbers 1-27

- **Level** (TestNumberedTitlesLevel): 27 tests
  - Gaming/progression context
  - Numbers 1-27

- **Stage** (TestNumberedTitlesStage): 27 tests
  - Process/development context
  - Numbers 1-27

### By Number Format
- **Roman Numerals** (TestNumberedTitlesRomanNumerals): 42 tests
  - I, II, III, IV, V, VI, VII, VIII, IX, X
  - XI, XII, XIII, XIV, XV, XVI, XVII, XVIII, XIX, XX
  - XXI, XXV, XXX, L, C
  - Applied to Part, Chapter, Module, Section

- **Letters** (TestNumberedTitlesLetters): 34 tests
  - A-Z coverage
  - Applied to Part, Section, Module, Chapter, Appendix

### By Format Variation
- **Abbreviated Forms** (TestNumberedTitlesAbbreviatedForms): 32 tests
  - Ch. (Chapter)
  - Sec. (Section)
  - Mod. (Module)
  - Vol. (Volume)
  - Pt. (Part)

- **Case Variations** (TestNumberedTitlesCaseVariations): 14 tests
  - UPPERCASE
  - lowercase
  - Title Case
  - Mixed case in same text

### Edge Cases and Special Scenarios
- **With Parentheticals** (TestNumberedTitlesWithParentheticals): 18 tests
  - Dates: (May 6, 2008), (Sept 29, 2015)
  - Descriptors: (Revised), (Optional), (Advanced)
  - Notes: (See also Part 3), (Contains spoilers)
  - Brackets: [Video File], [PDF Download]
  - Multiple parentheticals

- **Edge Cases** (TestNumberedTitlesEdgeCases): 33 tests
  - Multiple numbered titles in sequence
  - Mixed keywords
  - Start/end of text
  - With questions/exclamations
  - With quotations
  - With colons/semicolons
  - Leading zeros (Part 01, Chapter 007)
  - Three-digit numbers (Part 100, Chapter 365)
  - Decimal subsections (2.1, 2.1.1, 3.14)
  - Hyphens (2-A, 3-1)
  - Mixed Roman/Arabic (II.3)

- **Real World Examples** (TestNumberedTitlesRealWorldExamples): 25 tests
  - Video series
  - Educational materials
  - Tutorial content
  - Book series
  - Course materials
  - Documentation
  - Podcasts
  - Training materials
  - And more...

### Negative Cases
- **Should NOT Match** (TestNumberedTitlesNegativeCases): 10 tests
  - Cost patterns (Cost 5.)
  - Regular words + numbers (bought 3.)
  - Numbers at sentence end
  - Non-title abbreviations (ext., page)
  - Date patterns

## Test Status
As of initial commit, **tests are expected to FAIL** because the implementation has not been added yet.

Many tests show failures, while some pass (likely abbreviated forms already handled by existing `abbreviation_merger.py`).

## Pattern Reference
The tests validate that these patterns are kept together as single units:

```
[Keyword] [Number].
```

Where:
- **Keyword**: Part, Module, Chapter, Section, Week, Step, Phase, Unit, Level, Stage
- **Number**: Arabic (1, 2, 3), Roman (I, II, III), or Letter (A, B, C)

## Next Steps
1. Implementation of numbered title handling logic
2. Run full test suite to validate implementation
3. Address any edge cases revealed by failing tests
4. Update existing tests if behavior changes are needed

## Related Files
- Implementation target: `fast_sentence_segment/dmo/` (new component needed)
- Related code: `abbreviation_merger.py`, `numbered_list_normalizer.py`, `title_name_merger.py`
- Test file: `tests/regression/test_numbered_titles_issue_30.py`

## Issue Reference
https://github.com/craigtrim/fast-sentence-segment/issues/30
