# Fast Sentence Segmentation

[![PyPI version](https://img.shields.io/pypi/v/fast-sentence-segment.svg)](https://pypi.org/project/fast-sentence-segment/)
[![Python versions](https://img.shields.io/pypi/pyversions/fast-sentence-segment.svg)](https://pypi.org/project/fast-sentence-segment/)
[![Tests](https://img.shields.io/badge/tests-3513-brightgreen)](https://github.com/craigtrim/fast-sentence-segment/tree/master/tests)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Downloads](https://static.pepy.tech/badge/fast-sentence-segment)](https://pepy.tech/project/fast-sentence-segment)
[![Downloads/Month](https://static.pepy.tech/badge/fast-sentence-segment/month)](https://pepy.tech/project/fast-sentence-segment)

Fast and efficient sentence segmentation using spaCy with surgical post-processing fixes. Handles complex edge cases like abbreviations (Dr., Mr., etc.), ellipses, quoted text, and multi-paragraph documents.

## Philosophy

This library is not for people who are casual about accuracy.

Some NLP tools take a "good enough" approach: throw some machine learning at the problem and call it done. This library takes the opposite stance. Every edge case matters. Every false split is a bug. Every missed boundary is a failure.

This library is utterly pedantic and obsessive because some people are built that way, and for some people that matters. If you need sentence segmentation that handles "Dr. Smith went to Washington D.C. at 9 a.m." without flinching, "The U.S. Senate voted today" without splitting on the abbreviation, and "I work at Yahoo! Inc." without treating the exclamation mark as a sentence boundary, this is your library.

If "close enough" is fine for your use case, there are simpler options. But if you have ever debugged a downstream model failure caused by a sentence segmenter that split "Fig. 1" into two sentences, you understand why this library exists.

---

## Comparison with wtpsplit-lite

We ran a [comprehensive benchmark](https://github.com/craigtrim/fast-sentence-segment/issues/15) comparing this library against [wtpsplit-lite](https://github.com/superlinear-ai/wtpsplit-lite), a neural network approach using ONNX models.

### Performance

| Metric | fast-sentence-segment | wtpsplit-lite | Winner |
|--------|:---------------------:|:-------------:|:------:|
| Cold start | **1.4 sec** | 79 sec | FSS (57x) |
| Short text (3 sentences) | **0.12 ms** | 3.6 ms | FSS (30x) |
| Long text (44 sentences) | **1.5 ms** | 146 ms | FSS (100x) |
| Memory footprint | **~0 MB** | 0.1 MB | FSS |

### Accuracy (28 edge case tests)

| Library | Passed | Failed | Accuracy |
|---------|:------:|:------:|:--------:|
| fast-sentence-segment | **24** | 4 | **85.7%** |
| wtpsplit-lite | 16 | 12 | 57.1% |

### Where This Library Wins

- **Technical content**: Correctly splits after version numbers (`2.0.1.`), IP addresses (`192.168.1.1.`), decimals (`3.14.`)
- **Lists**: Recognizes numbered and bullet list boundaries
- **Hard-wrapped text**: Properly unwraps Project Gutenberg style line breaks
- **Clean output**: No trailing whitespace or embedded newlines
- **Offline operation**: No network dependency or model downloads

### Where This Library Loses

- **Non-English text**: Limited support for CJK (Chinese, Japanese, Korean), Thai, Hindi, and other scripts without clear period-based boundaries. If you need multilingual support, consider other libraries.

Full benchmark details: [Issue #15](https://github.com/craigtrim/fast-sentence-segment/issues/15)

---

## Why This Library?

1. **Keep it local**: LLM API calls cost money and send your data to third parties. Run sentence segmentation entirely on your machine.
2. **spaCy perfected**: spaCy is a great local model, but it makes mistakes. This library fixes most of spaCy's shortcomings.

## Features

- **Paragraph-aware segmentation**: Returns sentences grouped by paragraph
- **Abbreviation handling**: Correctly handles "Dr.", "Mr.", "etc.", "p.m.", "a.m." without false splits
- **Country abbreviation awareness**: "The U.S. Senate" stays together (not split after "U.S.")
- **Company name handling**: "Yahoo! Inc." recognized as a single entity
- **Ellipsis preservation**: Keeps `...` intact while detecting sentence boundaries
- **Question/exclamation splitting**: Properly splits on `?` and `!` followed by capital letters
- **Cached processing**: LRU cache for repeated text processing
- **Flexible output**: Nested lists (by paragraph) or flattened list of sentences
- **Bullet point & numbered list normalization**: Cleans common list formats
- **CLI tool**: Command-line interface for quick segmentation

## Installation

```bash
pip install fast-sentence-segment
```

After installation, download the spaCy model:

```bash
python -m spacy download en_core_web_sm
```

## Quick Start

```python
from fast_sentence_segment import segment_text

text = "Do you like Dr. Who? I prefer Dr. Strange! Mr. T is also cool."

results = segment_text(text, flatten=True)
```

```json
[
  "Do you like Dr. Who?",
  "I prefer Dr. Strange!",
  "Mr. T is also cool."
]
```

Notice how "Dr. Who?" stays together as a single sentence: the library correctly recognizes that a title followed by a single-word name ending in `?` or `!` is a name reference, not a sentence boundary.

## Usage

### Basic Segmentation

The `segment_text` function returns a list of lists, where each inner list represents a paragraph containing its sentences:

```python
from fast_sentence_segment import segment_text

text = """Gandalf spoke softly. "All we have to decide is what to do with the time given us."

Frodo nodded. The weight of the Ring pressed against his chest."""

results = segment_text(text)
```

```json
[
  [
    "Gandalf spoke softly.",
    "\"All we have to decide is what to do with the time given us.\"."
  ],
  [
    "Frodo nodded.",
    "The weight of the Ring pressed against his chest."
  ]
]
```

### Flattened Output

If you don't need paragraph boundaries, use the `flatten` parameter:

```python
text = "At 9 a.m. the hobbits set out. By 3 p.m. they reached Rivendell. Mr. Frodo was exhausted."

results = segment_text(text, flatten=True)
```

```json
[
  "At 9 a.m. the hobbits set out.",
  "By 3 p.m. they reached Rivendell.",
  "Mr. Frodo was exhausted."
]
```

### Direct Segmenter Access

For more control, use the `Segmenter` class directly:

```python
from fast_sentence_segment import Segmenter

segmenter = Segmenter()
results = segmenter.input_text("Your text here.")
```

### Command Line Interface

```bash
# Inline text
segment "Gandalf paused... You shall not pass! The Balrog roared."

# Pipe from stdin
echo "Have you seen Dr. Who? It's brilliant!" | segment

# Numbered output
segment -n -f silmarillion.txt

# File-to-file (one sentence per line)
segment-file --input-file book.txt --output-file sentences.txt

# Unwrap hard-wrapped e-texts (Project Gutenberg, etc.)
segment-file --input-file book.txt --output-file sentences.txt --unwrap

# Dialog-aware formatting (implies --unwrap)
segment -f book.txt --format
```

## API Reference

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `segment_text()` | `input_text: str`, `flatten: bool = False`, `unwrap: bool = False`, `format: str = None` | `list` or `str` | Main entry point for segmentation. Use `format="dialog"` for dialog-aware output. |
| `Segmenter.input_text()` | `input_text: str` | `list[list[str]]` | Cached paragraph-aware segmentation |

### CLI Commands

| Command | Description |
|---------|-------------|
| `segment [text]` | Segment text from argument, `-f FILE`, or stdin. Use `-n` for numbered output, `--format` for dialog-aware paragraph grouping. |
| `segment-file --input-file IN --output-file OUT [--unwrap] [--format]` | Segment a file and write one sentence per line. Use `--unwrap` for hard-wrapped e-texts, `--format` for dialog-aware formatting. |

## Why Nested Lists?

The segmentation process preserves document structure by segmenting into both paragraphs and sentences. Each outer list represents a paragraph, and each inner list contains that paragraph's sentences. This is useful for:

- Document structure analysis
- Paragraph-level processing
- Maintaining original text organization

Use `flatten=True` when you only need sentences without paragraph context.

## Requirements

- Python 3.9+
- spaCy 3.8+
- en_core_web_sm spaCy model
- **English text only**: This library uses spaCy's English model and applies English-specific rules. It will not produce correct results for Chinese, Japanese, Korean, Thai, Hindi, or other non-English text.

## How It Works

This library uses spaCy for initial sentence segmentation, then applies surgical post-processing fixes for cases where spaCy's default behavior is incorrect:

1. **Pre-processing**: Normalize numbered lists, preserve ellipses with placeholders
2. **spaCy segmentation**: Use spaCy's sentence boundary detection
3. **Post-processing**: Split on abbreviation boundaries, handle `?`/`!` + capital patterns, protect company names and country abbreviation + proper noun combinations
4. **Denormalization**: Restore placeholders to original text

## License

MIT License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Run tests (`make test`)
4. Commit your changes
5. Push to the branch
6. Open a Pull Request
