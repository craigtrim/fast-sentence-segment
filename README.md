# Fast Sentence Segmentation

[![PyPI version](https://img.shields.io/pypi/v/fast-sentence-segment.svg)](https://pypi.org/project/fast-sentence-segment/)
[![Python versions](https://img.shields.io/pypi/pyversions/fast-sentence-segment.svg)](https://pypi.org/project/fast-sentence-segment/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![spaCy](https://img.shields.io/badge/spaCy-3.8-blue.svg)](https://spacy.io/)

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

text = "Here is a Dr. who says something. And then again, what else? I don't know. Do you?"

results = segment_text(text)
# Returns: [['Here is a Dr. who says something.', 'And then again, what else?', "I don't know.", 'Do you?']]
```

## Usage

### Basic Segmentation

The `segment_text` function returns a list of lists, where each inner list represents a paragraph containing its sentences:

```python
from fast_sentence_segment import segment_text

text = """First paragraph here. It has two sentences.

Second paragraph starts here. This one also has multiple sentences. And a third."""

results = segment_text(text)
# Returns:
# [
#     ['First paragraph here.', 'It has two sentences.'],
#     ['Second paragraph starts here.', 'This one also has multiple sentences.', 'And a third.']
# ]
```

### Flattened Output

If you don't need paragraph boundaries, use the `flatten` parameter:

```python
results = segment_text(text, flatten=True)
# Returns: ['First paragraph here.', 'It has two sentences.', 'Second paragraph starts here.', ...]
```

### Direct Segmenter Access

For more control, use the `Segmenter` class directly:

```python
from fast_sentence_segment import Segmenter

segmenter = Segmenter()
results = segmenter.input_text("Your text here.")
```

### Command Line Interface

Segment text directly from the terminal:

```bash
# Direct text input
segment "Hello world. How are you? I am fine."

# Numbered output
segment -n "First sentence. Second sentence."

# From stdin
echo "Some text here. Another sentence." | segment

# From file
segment -f document.txt
```

## API Reference

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `segment_text()` | `input_text: str`, `flatten: bool = False` | `list` | Main entry point for segmentation |
| `Segmenter.input_text()` | `input_text: str` | `list[list[str]]` | Cached paragraph-aware segmentation |

### CLI Options

| Option | Description |
|--------|-------------|
| `text` | Text to segment (positional argument) |
| `-f, --file` | Read text from file |
| `-n, --numbered` | Number output lines |

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
