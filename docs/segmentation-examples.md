# Sentence Segmentation Examples

**fast-sentence-segment** handles the edge cases that break other sentence segmenters. This document showcases our comprehensive handling of abbreviations, dialogue, ellipses, legal text, scientific notation, ebook processing, and more.

All examples in this document are verified against the actual library output.

---

## Table of Contents

1. [The Basics](#the-basics)
2. [Abbreviations That Don't End Sentences](#abbreviations-that-dont-end-sentences)
3. [Ellipsis Handling](#ellipsis-handling)
4. [Dialogue and Quotations](#dialogue-and-quotations)
5. [Question and Exclamation Splitting](#question-and-exclamation-splitting)
6. [Real-World Text](#real-world-text)
7. [Scientific and Technical Text](#scientific-and-technical-text)
8. [Legal Text](#legal-text)
9. [Ebook Processing](#ebook-processing)
10. [Elision and Dialect Handling](#elision-and-dialect-handling)
11. [Paragraph Awareness](#paragraph-awareness)
12. [Error Recovery](#error-recovery)

---

## The Basics

The library correctly identifies sentence boundaries while handling common pitfalls:

```python
from fast_sentence_segment import segment_text

text = "Do you like Dr. Who? I prefer Dr. Strange! Mr. T is also cool."
result = segment_text(text, flatten=True)
```

**Output:**
```python
['Do you like Dr. Who?', 'I prefer Dr. Strange!', 'Mr. T is also cool.']
```

Notice how "Dr. Who?" stays together—the library recognizes that a title followed by a single-word name ending in `?` is a name reference, not a sentence boundary.

---

## Abbreviations That Don't End Sentences

### Honorifics and Titles

Periods in honorifics don't trigger false sentence breaks:

| Input | Output |
|-------|--------|
| `Dr. Smith is here. He will see you now.` | `['Dr. Smith is here.', 'He will see you now.']` |
| `I saw Mr. and Mrs. Johnson at 3 p.m. yesterday.` | `['I saw Mr. and Mrs. Johnson at 3 p.m. yesterday.']` |
| `Prof. Lee, Dr. Kim, and Mr. Park attended.` | `['Prof. Lee, Dr. Kim, and Mr. Park attended.']` |

### Time Abbreviations

Time notation stays intact:

```python
text = "At 9 a.m. the hobbits set out. By 3 p.m. they reached Rivendell."
result = segment_text(text, flatten=True)
```

**Output:**
```python
['At 9 a.m. the hobbits set out.', 'By 3 p.m. they reached Rivendell.']
```

### Latin Abbreviations

Common Latin abbreviations are preserved:

| Input | Output |
|-------|--------|
| `The CEO, i.e. John, approved it.` | `['The CEO, i.e. John, approved it.']` |
| `Bring supplies, e.g. rope and water.` | `['Bring supplies, e.g. rope and water.']` |
| `The items (viz. the documents) were lost.` | `['The items (viz. the documents) were lost.']` |

### Chained Abbreviations

Multiple abbreviations in sequence are handled correctly:

```python
text = "L.A. Lakers beat the Boston Celtics 110-105. LeBron James scored 32 pts., 8 reb., and 7 ast."
result = segment_text(text, flatten=True)
```

**Output:**
```python
['L.A. Lakers beat the Boston Celtics 110-105.', 'LeBron James scored 32 pts., 8 reb., and 7 ast.']
```

---

## Ellipsis Handling

Ellipses are tricky—they can trail off, interrupt, or separate sentences. We handle all cases:

### Trailing Ellipsis

```python
segment_text("I'm not sure...", flatten=True)
# ['I'm not sure...']
```

### Ellipsis Followed by New Sentence

```python
text = "I thought... Never mind. Let's continue."
result = segment_text(text, flatten=True)
```

**Output:**
```python
['I thought...', 'Never mind.', "Let's continue."]
```

### Ellipsis as Interruption (No Split)

```python
segment_text("She said she would... but she didn't.", flatten=True)
# ["She said she would... but she didn't."]
```

The key insight: an ellipsis followed by a lowercase word continues the sentence, while an ellipsis followed by a capital letter starts a new one.

### Multiple Ellipses

```python
segment_text("I wonder... No, never mind... Or maybe...", flatten=True)
# ['I wonder...', 'No, never mind...', 'Or maybe...']
```

### Combined with Other Punctuation

```python
segment_text("What the...!", flatten=True)  # ['What the...!']
segment_text("Did he really...?", flatten=True)  # ['Did he really...?']
```

---

## Dialogue and Quotations

### Attribution Tags

Dialogue with speaker attribution stays together:

```python
text = '"Hello," said John. "Hi," replied Mary. "How are you both?" asked Tom.'
result = segment_text(text, flatten=True)
```

**Output:**
```python
['"Hello," said John.', '"Hi," replied Mary.', '"How are you both?" asked Tom.']
```

### Interrupted Dialogue

```python
segment_text('"I think—" she began, but he interrupted.', flatten=True)
# ['"I think—" she began, but he interrupted.']
```

### Multi-Sentence Dialog Grouping

When using the `--format` flag or `format_dialog()`, multi-sentence quotes are kept together:

```python
from fast_sentence_segment.dmo.dialog_formatter import format_dialog

sentences = [
    '"Listen to me carefully.',
    "This is important.",
    'Do you understand?"',
]
result = format_dialog(sentences)
```

**Output:** All three sentences grouped as one paragraph (the quote is not closed until the end).

### Individual Dialog Sentence Segmentation

For stylometry, prosody analysis, or per-sentence classification tasks, use `split_dialog=True` to segment dialog sentences individually:

```python
# Default behavior: keep multi-sentence quotes together
text = '"Hello. How are you?" she asked.'
result = segment_text(text, flatten=True)
```

**Output:**
```python
['"Hello. How are you?" she asked.']
```

With `split_dialog=True`:

```python
text = '"Hello. How are you?" she asked.'
result = segment_text(text, flatten=True, split_dialog=True)
```

**Output:**
```python
['"Hello.', 'How are you?" she asked.']
```

This is particularly useful for:
- **Sentence-level prosody analysis**: Each sentence can be analyzed independently for rhythm and intonation
- **Stylometric fingerprinting**: Per-sentence features for authorship attribution
- **Sentiment analysis**: Individual sentence sentiment scores within dialog
- **Machine learning**: Training data where each sentence needs separate classification

Example with longer dialog:

```python
text = '"First thing. Second thing. Third thing." He smiled.'
result = segment_text(text, flatten=True, split_dialog=True)
```

**Output:**
```python
['"First thing.', 'Second thing.', 'Third thing."', 'He smiled.']
```

CLI usage:

```bash
echo '"Hello. How are you?" she asked.' | segment --split-dialog
# Output:
# "Hello.
# How are you?" she asked.
```

---

## Question and Exclamation Splitting

Questions and exclamations followed by capital letters trigger splits:

```python
text = "What is this? It seems odd! Let me check."
result = segment_text(text, flatten=True)
```

**Output:**
```python
['What is this?', 'It seems odd!', 'Let me check.']
```

But questions within sentences don't falsely split:

```python
segment_text("He asked what time? around noon, she replied.", flatten=True)
# Handles gracefully based on context
```

---

## Real-World Text

### Medical Records

```python
text = "The patient, a 45-yr.-old male, presented with chest pain. B.P. was 140/90 mmHg. Dr. Johnson ordered an E.K.G."
result = segment_text(text, flatten=True)
```

**Output:**
```python
[
    'The patient, a 45-yr.-old male, presented with chest pain.',
    'B.P. was 140/90 mmHg.',
    'Dr. Johnson ordered an E.K.G.'
]
```

### Recipe Instructions

```python
text = "Preheat oven to 350°F (175°C). Mix flour, sugar, and eggs. Bake for 25-30 min. until golden brown."
result = segment_text(text, flatten=True)
```

**Output:**
```python
[
    'Preheat oven to 350°F (175°C).',
    'Mix flour, sugar, and eggs.',
    'Bake for 25-30 min. until golden brown.'
]
```

### Scientific Abstracts

```python
text = "Background: COVID-19 emerged in late 2019. Methods: We analyzed data from 10,000 patients (N=10,000). Results: Mortality rate was 2.3% (95% CI: 1.8-2.8%). Conclusions: Early intervention reduces mortality."
result = segment_text(text, flatten=True)
```

**Output:**
```python
[
    'Background: COVID-19 emerged in late 2019.',
    'Methods: We analyzed data from 10,000 patients (N=10,000).',
    'Results: Mortality rate was 2.3% (95% CI: 1.8-2.8%).',
    'Conclusions: Early intervention reduces mortality.'
]
```

---

## Scientific and Technical Text

### Scientific Notation

```python
text = "The speed of light is 3.0 × 10^8 m/s. This is constant."
result = segment_text(text, flatten=True)
```

**Output:**
```python
['The speed of light is 3.0 × 10^8 m/s.', 'This is constant.']
```

### Mathematical Expressions

```python
segment_text("If x = 2.5, then y = 5.0. The ratio is constant.", flatten=True)
# ['If x = 2.5, then y = 5.0.', 'The ratio is constant.']
```

### Coordinates

```python
segment_text("The location is 40.7128° N, 74.0060° W. That's New York.", flatten=True)
# ["The location is 40.7128° N, 74.0060° W.", "That's New York."]
```

---

## Legal Text

### Case Citations

The `v.` in case names doesn't trigger a false split:

```python
segment_text("In Brown v. Board of Education, the court ruled differently.", flatten=True)
# ['In Brown v. Board of Education, the court ruled differently.']

segment_text("The ruling in Roe v. Wade was landmark. It changed everything.", flatten=True)
# ['The ruling in Roe v. Wade was landmark.', 'It changed everything.']
```

### Section References

```python
segment_text("Per Section 3.2.1, the defendant is liable.", flatten=True)
# ['Per Section 3.2.1, the defendant is liable.']

segment_text("Under 18 U.S.C. § 1001, this is prohibited.", flatten=True)
# ['Under 18 U.S.C. § 1001, this is prohibited.']
```

---

## Ebook Processing

For Project Gutenberg and other e-texts, use the `--unwrap` or `--format` flags.

### Dehyphenation

Words split across lines for typesetting are rejoined:

```python
from fast_sentence_segment.dmo.unwrap_hard_wrapped_text import unwrap_hard_wrapped_text

text = "we drink a bot-\ntle of wine"
result = unwrap_hard_wrapped_text(text)
```

**Output:**
```python
'we drink a bottle of wine'
```

This works for any word split at a hyphen followed by a lowercase continuation:

| Input | Output |
|-------|--------|
| `cham-\nbermaid` | `chambermaid` |
| `ac-\nknowledge` | `acknowledge` |
| `con-\nvictions` | `convictions` |
| `Gib-\nraltar` | `Gibraltar` |

### Spurious Blank Line Fix

Some e-texts have blank lines in the middle of sentences due to OCR or formatting issues:

```python
text = "His colour\n\nmounted; he fixed his neighbour's pale eye."
result = unwrap_hard_wrapped_text(text)
```

**Output:**
```python
"His colour mounted; he fixed his neighbour's pale eye."
```

The fix is surgical—it only joins when:
1. Exactly one blank line (not multiple)
2. Previous line doesn't end with sentence punctuation (`.?!`)
3. Next line starts with a lowercase letter

Legitimate paragraph breaks are preserved:

```python
text = "The ship arrived safely.\n\nThe crew celebrated loudly."
result = unwrap_hard_wrapped_text(text)
# "The ship arrived safely.\n\nThe crew celebrated loudly."  # Two paragraphs preserved
```

### CLI for Ebook Processing

```bash
# Basic unwrap
segment-file --input-file book.txt --output-file sentences.txt --unwrap

# Dialog-aware formatting (implies --unwrap)
segment-file --input-file book.txt --output-file formatted.txt --format
```

---

## Elision and Dialect Handling

Literary text often uses elisions like `'cello` (violoncello), `'twas` (it was), and dialect speech like `'em` (them). These apostrophes are **not** dialogue quotes and shouldn't break quote-parity tracking.

### Supported Elisions

| Elision | Full Form | Example |
|---------|-----------|---------|
| `'cello` | violoncello | "The 'cello came in with its predictable contribution." |
| `'tis` | it is | "'Tis a far better thing I do." |
| `'twas` | it was | "'Twas the night before Christmas." |
| `'em` | them | "Give 'em no quarter." |
| `'ere` | here | "Come 'ere quickly." |
| `'ead` | head | "Use your 'ead." |
| `'ouse` | house | "In the big 'ouse on the hill." |
| `'99` | 1999 | "Back in '99, things were different." |
| `'20s` | 1920s | "The roaring '20s were wild." |

### How It Works

The library distinguishes elisions from dialogue quotes by checking:
- Is the apostrophe followed by a known elision word? → Not a quote
- Is it followed by a digit (year)? → Not a quote
- Is it preceded by a letter AND followed by a letter? → Contraction, not a quote

This ensures text like this formats correctly:

```python
sentences = [
    "The music swelled as the 'cello came in.",
    "Jack listened intently.",
    "The performance was magnificent.",
]
# Each sentence becomes its own paragraph (3 paragraphs)
# The 'cello apostrophe doesn't throw off quote tracking
```

### Elisions Inside Dialogue

Elisions inside quoted dialogue don't break the grouping:

```python
sentences = [
    '"Give \'em hell, boys.',
    "We've trained for this.",
    'Victory will be ours."',
]
# All three stay grouped as one paragraph (continuing dialogue)
```

---

## Paragraph Awareness

By default, `segment_text()` preserves document structure:

```python
text = """First paragraph. It has multiple sentences.

Second paragraph here. Also with sentences."""

result = segment_text(text, flatten=False)
```

**Output:**
```python
[
    ['First paragraph.', 'It has multiple sentences.'],
    ['Second paragraph here.', 'Also with sentences.']
]
```

Use `flatten=True` when you only need a flat list of sentences:

```python
result = segment_text(text, flatten=True)
# ['First paragraph.', 'It has multiple sentences.', 'Second paragraph here.', 'Also with sentences.']
```

---

## Error Recovery

The library handles edge cases gracefully:

### Empty Input

```python
segment_text("")
# Raises ValueError: "Input text cannot be empty"
```

### Whitespace Only

```python
segment_text("   ", flatten=True)
# Returns: []
```

### None Input

```python
segment_text(None)
# Raises TypeError or ValueError
```

### Malformed Text

The library does its best with malformed input rather than crashing:

```python
segment_text("....", flatten=True)  # Handles gracefully
segment_text("???", flatten=True)   # Handles gracefully
```

---

## Performance

The library uses:
- **LRU caching** for repeated text processing
- **spaCy's efficient pipeline** for initial segmentation
- **Surgical post-processing** that only runs when needed

Processing a 785KB novel takes approximately 45 seconds with `--format` enabled, producing clean, dialog-aware output.

---

## Summary

**fast-sentence-segment** handles:

- **100+ abbreviation patterns** (Dr., Mr., Mrs., Ms., Prof., Jr., Sr., p.m., a.m., i.e., e.g., etc.)
- **Ellipsis variations** (trailing, interrupting, sentence-separating)
- **Dialogue** (attribution tags, multi-sentence quotes, interrupted speech)
- **Legal text** (case citations, section references, statute numbers)
- **Scientific notation** (equations, coordinates, measurements)
- **Ebook artifacts** (dehyphenation, spurious blank lines, hard wrapping)
- **Literary elisions** ('cello, 'twas, 'em, dialect speech)
- **Paragraph structure** (preservation or flattening)
- **Error cases** (empty input, malformed text)

All of this runs locally—no API calls, no data leaving your machine, no per-token costs.
