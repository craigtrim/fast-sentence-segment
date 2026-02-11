#!/usr/bin/env python
"""Debug the segmentation pipeline step by step"""

from fast_sentence_segment.svc import PerformSentenceSegmentation

segmenter = PerformSentenceSegmentation()

# Test cases
test_cases = [
    "Try crossing this street in India!! Part 2. (May 6, 2008) [Video File]",
    "Part 8. The conclusion brings everything together.",
    "Watch Part 5. It contains the final revelations.",
]

for text in test_cases:
    print(f"\n{'='*70}")
    print(f"Input: {text}")
    print(f"{'='*70}")

    result = segmenter.process(text)

    print(f"Output ({len(result)} segments):")
    for i, seg in enumerate(result):
        print(f"  [{i}]: {repr(seg)}")
