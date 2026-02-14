# -*- coding: UTF-8 -*-
"""CLI for fast-sentence-segment."""

import argparse
import itertools
import logging
import os
import sys
import threading
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


class Spinner:
    """Animated spinner for long-running operations."""

    def __init__(self, message: str):
        self.message = message
        self.running = False
        self.thread = None
        self.frames = itertools.cycle(["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"])

    def _spin(self):
        while self.running:
            frame = next(self.frames)
            print(f"\r  {YELLOW}{frame}{RESET} {self.message}", end="", flush=True)
            time.sleep(0.08)

    def __enter__(self):
        self.running = True
        self.thread = threading.Thread(target=self._spin)
        self.thread.start()
        return self

    def __exit__(self, *args):
        self.running = False
        if self.thread:
            self.thread.join()
        print(f"\r  {' ' * (len(self.message) + 4)}\r", end="", flush=True)


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
    parser.add_argument(
        "--unwrap",
        action="store_true",
        help="Unwrap hard-wrapped lines and dehyphenate split words",
    )
    parser.add_argument(
        "--format",
        action="store_true",
        help="Format output with dialog-aware paragraph grouping (implies --unwrap)",
    )
    parser.add_argument(
        "--split-dialog",
        action="store_true",
        help="Segment dialog sentences individually (for stylometry/prosody analysis)",
    )
    args = parser.parse_args()

    # --format implies --unwrap
    unwrap = args.unwrap or args.format

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
    result = segment_text(
        text.strip(), flatten=True, unwrap=unwrap,
        format="dialog" if args.format else None,
        split_dialog=args.split_dialog,
    )

    # If format is used, result is a string
    if args.format:
        print(result)
    else:
        # Result is a list of sentences
        for i, sentence in enumerate(result, 1):
            if args.numbered:
                print(f"{i}. {sentence}")
            else:
                print(sentence)


def _generate_output_path(input_path: str) -> str:
    """Generate output path by inserting -clean before extension."""
    base, ext = os.path.splitext(input_path)
    return f"{base}-clean{ext}"


def _process_single_file(
    input_file: str, output_file: str, unwrap: bool, normalize: bool, format: str = None,
    split_dialog: bool = False
):
    """Process a single file and write output."""
    # Show configuration
    _param("Input", input_file)
    _param("Output", output_file)
    _param("Size", _file_size(input_file))
    _param("Unwrap", "enabled" if unwrap else "disabled")
    _param("Normalize quotes", "disabled" if not normalize else "enabled")
    _param("Format", format if format else "default (one sentence per line)")
    _param("Split dialog", "enabled" if split_dialog else "disabled")
    print()

    # Step 1: Read file
    print(f"  {YELLOW}→{RESET} Reading input file...")
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
    print(f"  {GREEN}✓{RESET} Read {len(text):,} characters")

    # Step 2: Segment text
    print(f"  {YELLOW}→{RESET} Segmenting text...", end="", flush=True)
    start = time.perf_counter()
    result = segment_text(
        text.strip(), flatten=True, unwrap=unwrap, normalize=normalize, format=format,
        split_dialog=split_dialog,
    )
    elapsed = time.perf_counter() - start

    # Step 3: Write output
    if format:
        # Format mode returns a string
        print(f"\r  {GREEN}✓{RESET} Segmented text ({elapsed:.2f}s)")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result + "\n")
        print(f"  {GREEN}✓{RESET} Written formatted output to {output_file}")
    else:
        # Default mode returns a list
        sentences = result
        print(f"\r  {GREEN}✓{RESET} Segmented into {len(sentences):,} sentences ({elapsed:.2f}s)")
        total = len(sentences)
        with open(output_file, "w", encoding="utf-8") as f:
            if unwrap:
                f.write(format_grouped_sentences(sentences) + "\n")
                print(f"  {GREEN}✓{RESET} Written {total:,} sentences to {output_file}")
            else:
                for i, sentence in enumerate(sentences, 1):
                    f.write(sentence + "\n")
                    if i % 500 == 0 or i == total:
                        pct = (i / total) * 100
                        print(f"\r  {YELLOW}→{RESET} Writing... {pct:.0f}% ({i:,}/{total:,})", end="", flush=True)
                print(f"\r  {GREEN}✓{RESET} Written {total:,} sentences to {output_file}       ")


def file_main():
    parser = argparse.ArgumentParser(
        prog="segment-file",
        description="Segment a text file into sentences and write to an output file",
    )
    parser.add_argument(
        "--input-file",
        help="Path to input text file",
    )
    parser.add_argument(
        "--input-dir",
        help="Path to directory containing text files to process",
    )
    parser.add_argument(
        "--output-file",
        help="Path to output file (optional, defaults to input-file with -clean suffix)",
    )
    parser.add_argument(
        "--unwrap", action="store_true",
        help="Unwrap hard-wrapped lines (e.g., Project Gutenberg e-texts)",
    )
    parser.add_argument(
        "--no-normalize-quotes", action="store_true",
        help="Disable unicode quote normalization to ASCII equivalents",
    )
    parser.add_argument(
        "--format",
        action="store_true",
        help="Format output with dialog-aware paragraph grouping (implies --unwrap)",
    )
    parser.add_argument(
        "--split-dialog",
        action="store_true",
        help="Segment dialog sentences individually (for stylometry/prosody analysis)",
    )
    args = parser.parse_args()

    # --format implies --unwrap
    unwrap = args.unwrap or args.format

    # Validate arguments
    if not args.input_file and not args.input_dir:
        print(f"  {YELLOW}Error:{RESET} Either --input-file or --input-dir is required")
        sys.exit(1)
    if args.input_file and args.input_dir:
        print(f"  {YELLOW}Error:{RESET} Cannot specify both --input-file and --input-dir")
        sys.exit(1)
    if args.input_dir and args.output_file:
        print(f"  {YELLOW}Error:{RESET} --output-file cannot be used with --input-dir")
        sys.exit(1)

    normalize = not args.no_normalize_quotes

    # Process directory
    if args.input_dir:
        input_dir = os.path.expanduser(args.input_dir)
        if not os.path.isdir(input_dir):
            print(f"  {YELLOW}Error:{RESET} Directory not found: {input_dir}")
            sys.exit(1)

        # Find all .txt files
        txt_files = sorted([
            f for f in os.listdir(input_dir)
            if f.endswith(".txt") and not f.endswith("-clean.txt")
        ])

        if not txt_files:
            print(f"  {YELLOW}Error:{RESET} No .txt files found in {input_dir}")
            sys.exit(1)

        _header("segment-file (batch)")
        print(f"  {DIM}Processing {len(txt_files)} files in directory{RESET}")
        print()
        _param("Directory", input_dir)
        _param("Files", str(len(txt_files)))
        _param("Unwrap", "enabled" if unwrap else "disabled")
        _param("Normalize quotes", "disabled" if not normalize else "enabled")
        _param("Format", "dialog" if args.format else "default (one sentence per line)")
        _param("Split dialog", "enabled" if args.split_dialog else "disabled")
        print()

        format_value = "dialog" if args.format else None
        for i, filename in enumerate(txt_files, 1):
            input_path = os.path.join(input_dir, filename)
            output_path = _generate_output_path(input_path)
            print(f"  {BOLD}[{i}/{len(txt_files)}]{RESET} {filename}")
            _process_single_file(input_path, output_path, unwrap, normalize, format_value, args.split_dialog)
            print()

        print(f"  {GREEN}Done! Processed {len(txt_files)} files.{RESET}")
        print()
        return

    # Process single file
    input_file = os.path.expanduser(args.input_file)
    if not os.path.isfile(input_file):
        print(f"  {YELLOW}Error:{RESET} File not found: {input_file}")
        sys.exit(1)

    output_file = args.output_file or _generate_output_path(input_file)
    output_file = os.path.expanduser(output_file)

    _header("segment-file")
    print(f"  {DIM}Segmenting text file into sentences{RESET}")
    print()

    format_value = "dialog" if args.format else None
    _process_single_file(input_file, output_file, unwrap, normalize, format_value, args.split_dialog)

    print(f"\n  {GREEN}Done!{RESET}")
    print()


if __name__ == "__main__":
    main()
