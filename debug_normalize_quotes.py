#!/usr/bin/env python
"""Check if normalize_quotes affects the text"""

from fast_sentence_segment import normalize_quotes, segment_text

text = "Try crossing this street in India!! Part 2. (May 6, 2008) [Video File]"

print(f"Original: {repr(text)}")
normalized = normalize_quotes(text)
print(f"After normalize_quotes: {repr(normalized)}")
print(f"Changed? {text != normalized}")
print()

# Test with and without normalization
print("WITH normalization:")
result_with = segment_text(text, flatten=True, normalize=True)
for i, seg in enumerate(result_with):
    print(f"  [{i}]: {repr(seg)}")

print("\nWITHOUT normalization:")
result_without = segment_text(text, flatten=True, normalize=False)
for i, seg in enumerate(result_without):
    print(f"  [{i}]: {repr(seg)}")
