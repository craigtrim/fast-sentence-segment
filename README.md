# Fast Sentence Segmentation

[![PyPI version](https://img.shields.io/pypi/v/fast-sentence-segment.svg)](https://pypi.org/project/fast-sentence-segment/)
[![Python versions](https://img.shields.io/pypi/pyversions/fast-sentence-segment.svg)](https://pypi.org/project/fast-sentence-segment/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![spaCy](https://img.shields.io/badge/spaCy-3.5-blue.svg)](https://spacy.io/)

Fast and efficient sentence segmentation using spaCy. Handles complex edge cases like abbreviations (Dr., Mr., etc.), quoted text, and multi-paragraph documents.

## Features

- **Paragraph-aware segmentation**: Returns sentences grouped by paragraph
- **Abbreviation handling**: Correctly handles "Dr.", "Mr.", "etc." without false splits
- **Cached processing**: LRU cache for repeated text processing
- **Flexible output**: Nested lists (by paragraph) or flattened list of sentences
- **Bullet point & numbered list normalization**: Cleans common list formats

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

## API Reference

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `segment_text()` | `input_text: str`, `flatten: bool = False` | `list` | Main entry point for segmentation |
| `Segmenter.input_text()` | `input_text: str` | `list[list[str]]` | Cached paragraph-aware segmentation |

## Why Nested Lists?

The segmentation process preserves document structure by segmenting into both paragraphs and sentences. Each outer list represents a paragraph, and each inner list contains that paragraph's sentences. This is useful for:

- Document structure analysis
- Paragraph-level processing
- Maintaining original text organization

Use `flatten=True` when you only need sentences without paragraph context.

## Requirements

- Python 3.8.5+
- spaCy 3.5.3
- en_core_web_sm spaCy model

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
