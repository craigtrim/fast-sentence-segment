#!/usr/bin/env python
"""Debug script to see how spaCy splits the problematic text"""

from fast_sentence_segment import segment

# Test case from the issue
text1 = "Try crossing this street in India!! Part 2. (May 6, 2008) [Video File]"
text2 = "Bush Taxi Part 2. (Sept 29, 2015)"
text3 = "Part 8. The conclusion brings everything together."

print("Test 1:")
print(f"Input: {text1}")
result = segment(text1)
print(f"Output ({len(result)} segments):")
for i, seg in enumerate(result):
    print(f"  [{i}]: {repr(seg)}")
print()

print("Test 2:")
print(f"Input: {text2}")
result = segment(text2)
print(f"Output ({len(result)} segments):")
for i, seg in enumerate(result):
    print(f"  [{i}]: {repr(seg)}")
print()

print("Test 3:")
print(f"Input: {text3}")
result = segment(text3)
print(f"Output ({len(result)} segments):")
for i, seg in enumerate(result):
    print(f"  [{i}]: {repr(seg)}")
