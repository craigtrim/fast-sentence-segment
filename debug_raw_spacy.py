#!/usr/bin/env python
"""Check raw spaCy output before any processing"""

import spacy

nlp = spacy.load("en_core_web_sm")

test_texts = [
    "Try crossing this street in India!! Part 2. (May 6, 2008) [Video File]",
    "Part 8. The conclusion brings everything together.",
    "Watch Part 5. It contains the final revelations.",
]

for text in test_texts:
    print(f"\nInput: {text}")
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    print(f"spaCy output ({len(sentences)} segments):")
    for i, sent in enumerate(sentences):
        print(f"  [{i}]: {repr(sent)}")
