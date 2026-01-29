# Fast Sentence Segmentation

[![PyPI version](https://img.shields.io/pypi/v/fast-sentence-segment.svg)](https://pypi.org/project/fast-sentence-segment/)
[![Python versions](https://img.shields.io/pypi/pyversions/fast-sentence-segment.svg)](https://pypi.org/project/fast-sentence-segment/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![spaCy](https://img.shields.io/badge/spaCy-3.8-blue.svg)](https://spacy.io/)
[![Downloads](https://static.pepy.tech/badge/fast-sentence-segment)](https://pepy.tech/project/fast-sentence-segment)
[![Downloads/Month](https://static.pepy.tech/badge/fast-sentence-segment/month)](https://pepy.tech/project/fast-sentence-segment)

Fast and efficient sentence segmentation using spaCy with surgical post-processing fixes. Handles complex edge cases like abbreviations (Dr., Mr., etc.), ellipses, quoted text, and multi-paragraph documents.

## Why This Library?

1. **Keep it local**: LLM API calls cost money and send your data to third parties. Run sentence segmentation entirely on your machine.
2. **spaCy perfected**: spaCy is a great local model, but it makes mistakes. This library fixes most of spaCy's shortcomings.

## Features

- **Paragraph-aware segmentation**: Returns sentences grouped by paragraph
- **Abbreviation handling**: Correctly handles "Dr.", "Mr.", "etc.", "p.m.", "a.m." without false splits
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

Notice how "Dr. Who?" stays together as a single sentence—the library correctly recognizes that a title followed by a single-word name ending in `?` or `!` is a name reference, not a sentence boundary.

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
```

## API Reference

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `segment_text()` | `input_text: str`, `flatten: bool = False`, `unwrap: bool = False` | `list` | Main entry point for segmentation |
| `Segmenter.input_text()` | `input_text: str` | `list[list[str]]` | Cached paragraph-aware segmentation |

### CLI Commands

| Command | Description |
|---------|-------------|
| `segment [text]` | Segment text from argument, `-f FILE`, or stdin. Use `-n` for numbered output. |
| `segment-file --input-file IN --output-file OUT [--unwrap]` | Segment a file and write one sentence per line. Use `--unwrap` for hard-wrapped e-texts. |

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

## How It Works

This library uses spaCy for initial sentence segmentation, then applies surgical post-processing fixes for cases where spaCy's default behavior is incorrect:

1. **Pre-processing**: Normalize numbered lists, preserve ellipses with placeholders
2. **spaCy segmentation**: Use spaCy's sentence boundary detection
3. **Post-processing**: Split on abbreviation boundaries, handle `?`/`!` + capital patterns
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
