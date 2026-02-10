#!/usr/bin/env python
"""Check if denormalization is causing the split"""

from fast_sentence_segment.dmo import NumberedListNormalizer

text = "Part 2. (May 6, 2008)"

normalizer = NumberedListNormalizer()

print(f"Original: {repr(text)}")
normalized = normalizer.process(text)
print(f"After normalization: {repr(normalized)}")

denorm = normalizer.process(normalized, denormalize=True)
print(f"After denormalization: {repr(denorm)}")
