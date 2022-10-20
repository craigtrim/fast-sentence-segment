# Fast Sentence Segmentation (fast-sentence-segment)
Fast and Efficient Sentence Segmentation

Usage
```python
from fast_sentence_segment import segment_text

results = segment_text(
    'here is a dr. who says something.  and then again, what else?  i dont know.  Do you?')

assert results == [
    [
        'here is a dr. who says something.',
        'and then again, what else?',
        'i dont know.',
        'Do you?'
    ]
]
```

Why use a double-scripted list?

The segementation process will segment into paragraphs and sentences.  A paragraph is composed of 1..* sentences, hence each list of lists is equivalent to a paragraph.

This usage
```python
results = segment_text(input_text, flatten=True)
```
Will return a list of strings, regardless of paragraph delimitation.
