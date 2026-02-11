#!/usr/bin/env python
"""Full trace to see where the split happens"""

from fast_sentence_segment.svc import PerformSentenceSegmentation

# Monkey-patch to add logging
original_process = PerformSentenceSegmentation._process

def logged_process(self, input_text):
    sentences = original_process(input_text)
    print(f"\nFINAL OUTPUT from _process ({len(sentences)} sentences):")
    for i, sent in enumerate(sentences):
        print(f"  [{i}]: {repr(sent)}")
    return sentences

PerformSentenceSegmentation._process = logged_process

# Now test
from fast_sentence_segment import segment_text

text = "Try crossing this street in India!! Part 2. (May 6, 2008) [Video File]"
print(f"Input: {text}\n")

result = segment_text(text, flatten=True)
print(f"\nFINAL FLATTENED ({len(result)} segments):")
for i, seg in enumerate(result):
    print(f"  [{i}]: {repr(seg)}")
