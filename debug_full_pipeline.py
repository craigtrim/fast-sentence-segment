#!/usr/bin/env python
"""Trace through the full pipeline with logging"""

import spacy
from fast_sentence_segment.dmo import (
    NumberedListNormalizer,
    EllipsisNormalizer,
    NewlinesToPeriods,
    BulletPointCleaner,
    SpacyDocSegmenter,
    AbbreviationMerger,
    QuoteAttributionMerger,
    TitleNameMerger,
    NumberedTitleMerger,
)

text = "Try crossing this street in India!! Part 2. (May 6, 2008) [Video File]"

print(f"Original: {repr(text)}")
print()

# Normalize
normalizer = NumberedListNormalizer()
text_normalized = normalizer.process(text)
print(f"After numbered list normalization: {repr(text_normalized)}")

ellipsis_norm = EllipsisNormalizer()
text_normalized = ellipsis_norm.process(text_normalized)
print(f"After ellipsis normalization: {repr(text_normalized)}")
print()

# SpaCy segmentation
nlp = spacy.load("en_core_web_sm")
segmenter = SpacyDocSegmenter(nlp)
sentences = segmenter.process(text_normalized)
print(f"After spaCy segmentation ({len(sentences)} sentences):")
for i, sent in enumerate(sentences):
    print(f"  [{i}]: {repr(sent)}")
print()

# Abbreviation merger
abbrev_merger = AbbreviationMerger()
sentences = abbrev_merger.process(sentences)
print(f"After abbreviation merger ({len(sentences)} sentences):")
for i, sent in enumerate(sentences):
    print(f"  [{i}]: {repr(sent)}")
print()

# Title name merger
title_merger = TitleNameMerger()
sentences = title_merger.process(sentences)
print(f"After title name merger ({len(sentences)} sentences):")
for i, sent in enumerate(sentences):
    print(f"  [{i}]: {repr(sent)}")
print()

# Numbered title merger
numbered_title_merger = NumberedTitleMerger()
sentences = numbered_title_merger.process(sentences)
print(f"After numbered title merger ({len(sentences)} sentences):")
for i, sent in enumerate(sentences):
    print(f"  [{i}]: {repr(sent)}")
print()

# Denormalize
sentences = [normalizer.process(s, denormalize=True) for s in sentences]
sentences = [ellipsis_norm.process(s, denormalize=True) for s in sentences]
print(f"After denormalization ({len(sentences)} sentences):")
for i, sent in enumerate(sentences):
    print(f"  [{i}]: {repr(sent)}")
