# -*- coding: UTF-8 -*-
"""Test segmentation of a full-length book (The Hound of the Baskervilles)."""

import os
import random
import time

from fast_sentence_segment import segment_text

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
BOOK_PATH = os.path.join(DATA_DIR, "doyle-the-hound-of-the-baskervilles.txt")


def test_segment_full_book():
    with open(BOOK_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    start = time.perf_counter()
    sentences = segment_text(text, flatten=True)
    elapsed = time.perf_counter() - start

    print(f"\n{'=' * 60}")
    print(f"Book: The Hound of the Baskervilles")
    print(f"Characters: {len(text):,}")
    print(f"Sentences: {len(sentences):,}")
    print(f"Time: {elapsed:.3f}s")
    print(f"{'=' * 60}")

    # Print a random contiguous block of 10 sentences
    random.seed(42)
    max_start = len(sentences) - 10
    idx = random.randint(0, max_start)

    print(f"\nRandom sample (sentences {idx}–{idx + 9}):\n")
    for i in range(idx, idx + 10):
        print(f"  [{i}] {sentences[i]}")
    print()

    assert len(sentences) > 100, f"Expected many sentences, got {len(sentences)}"
