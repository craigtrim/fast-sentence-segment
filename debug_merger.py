#!/usr/bin/env python
"""Debug what the numbered_title_merger receives"""

import spacy
from fast_sentence_segment.dmo import NumberedTitleMerger

nlp = spacy.load("en_core_web_sm")

# Simulate what spaCy produces
test_sentences = [
    ['Try crossing this street in India!!', 'Part', '2. (May 6, 2008) [Video File]'],
    ['Part', '8. The conclusion brings everything together.'],
    ['Watch Part 5.', 'It contains the final revelations.'],
]

merger = NumberedTitleMerger()

for i, sentences in enumerate(test_sentences):
    print(f"\nTest {i+1}:")
    print(f"  Input: {sentences}")
    result = merger.process(sentences)
    print(f"  Output: {result}")
    print(f"  Merged? {len(result) < len(sentences)}")
