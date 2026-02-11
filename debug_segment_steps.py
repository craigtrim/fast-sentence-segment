#!/usr/bin/env python
"""Step by step debugging"""

from fast_sentence_segment.svc import PerformSentenceSegmentation
from fast_sentence_segment.svc import PerformParagraphSegmentation

text = "Try crossing this street in India!! Part 2. (May 6, 2008) [Video File]"

print(f"Input: {text}\n")

# Step 1: Paragraph segmentation
para_seg = PerformParagraphSegmentation()
paragraphs = para_seg.process(text)
print(f"After paragraph segmentation ({len(paragraphs)} paragraphs):")
for i, para in enumerate(paragraphs):
    print(f"  [{i}]: {repr(para)}")
print()

# Step 2: Sentence segmentation on first paragraph
sent_seg = PerformSentenceSegmentation()
sentences = sent_seg.process(paragraphs[0])
print(f"After sentence segmentation ({len(sentences)} sentences):")
for i, sent in enumerate(sentences):
    print(f"  [{i}]: {repr(sent)}")
