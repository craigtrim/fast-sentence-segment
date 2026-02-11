#!/usr/bin/env python
"""Debug using the actual segment_text function that tests use"""

from fast_sentence_segment import segment_text

text = "Try crossing this street in India!! Part 2. (May 6, 2008) [Video File]"

print(f"Input: {text}")
print()

result = segment_text(text, flatten=True)

print(f"Output ({len(result)} segments):")
for i, seg in enumerate(result):
    print(f"  [{i}]: {repr(seg)}")
