# -*- coding: UTF-8 -*-
"""CLI for fast-sentence-segment."""

import argparse
import logging
import sys

from fast_sentence_segment import segment_text

logging.disable(logging.CRITICAL)


def main():
    parser = argparse.ArgumentParser(
        prog="segment",
        description="Segment text into sentences",
    )
    parser.add_argument(
        "text",
        nargs="?",
        help="Text to segment (or use stdin)",
    )
    parser.add_argument(
        "-f", "--file",
        help="Read text from file",
    )
    parser.add_argument(
        "-n", "--numbered",
        action="store_true",
        help="Number output lines",
    )
    args = parser.parse_args()

    # Get input text
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
    elif args.text:
        text = args.text
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        parser.print_help()
        sys.exit(1)

    # Segment and output
    sentences = segment_text(text.strip(), flatten=True)
    for i, sentence in enumerate(sentences, 1):
        if args.numbered:
            print(f"{i}. {sentence}")
        else:
            print(sentence)


if __name__ == "__main__":
    main()
