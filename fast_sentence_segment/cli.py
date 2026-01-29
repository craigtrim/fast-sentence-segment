# -*- coding: UTF-8 -*-
"""CLI for fast-sentence-segment."""

import argparse
import logging
import os
import sys
import time

from fast_sentence_segment import segment_text
from fast_sentence_segment.dmo.group_quoted_sentences import format_grouped_sentences

logging.disable(logging.CRITICAL)

# ANSI color codes
BOLD = "\033[1m"
DIM = "\033[2m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"


def _header(title: str):
    print(f"\n{BOLD}{CYAN}{title}{RESET}")
    print(f"{DIM}{'─' * 40}{RESET}")


def _param(label: str, value: str):
    print(f"  {DIM}{label}:{RESET} {value}")


def _done(msg: str):
    print(f"\n  {GREEN}✓{RESET} {msg}")


def _file_size(path: str) -> str:
    size = os.path.getsize(path)
    if size < 1024:
        return f"{size} B"
    elif size < 1024 * 1024:
        return f"{size / 1024:.1f} KB"
    return f"{size / (1024 * 1024):.1f} MB"


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


def file_main():
    parser = argparse.ArgumentParser(
        prog="segment-file",
        description="Segment a text file into sentences and write to an output file",
    )
    parser.add_argument(
        "--input-file", required=True,
        help="Path to input text file",
    )
    parser.add_argument(
        "--output-file", required=True,
        help="Path to output file",
    )
    parser.add_argument(
        "--unwrap", action="store_true",
        help="Unwrap hard-wrapped lines (e.g., Project Gutenberg e-texts)",
    )
    parser.add_argument(
        "--no-normalize-quotes", action="store_true",
        help="Disable unicode quote normalization to ASCII equivalents",
    )
    args = parser.parse_args()

    _header("segment-file")
    _param("Input", args.input_file)
    _param("Output", args.output_file)
    _param("Size", _file_size(args.input_file))
    if args.unwrap:
        _param("Unwrap", "enabled")

    print(f"\n  {YELLOW}Segmenting...{RESET}", end="", flush=True)

    with open(args.input_file, "r", encoding="utf-8") as f:
        text = f.read()

    start = time.perf_counter()
    normalize = not args.no_normalize_quotes
    sentences = segment_text(
        text.strip(), flatten=True, unwrap=args.unwrap, normalize=normalize,
    )
    elapsed = time.perf_counter() - start

    with open(args.output_file, "w", encoding="utf-8") as f:
        if args.unwrap:
            f.write(format_grouped_sentences(sentences) + "\n")
        else:
            for sentence in sentences:
                f.write(sentence + "\n")

    print(f"\r  {' ' * 20}\r", end="")
    _done(f"{len(sentences):,} sentences in {elapsed:.2f}s")
    _done(f"Written to {args.output_file}")
    print()


if __name__ == "__main__":
    main()
