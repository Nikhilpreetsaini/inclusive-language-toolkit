#!/usr/bin/env python3
"""
Inclusive Language Toolkit (Advanced)

This module provides a set of functions and a command‑line interface to help
identify and transform potentially non‑inclusive language in text. It also
provides sentiment analysis and statistics about the inclusivity of the input.

Features
========
- Replace gendered pronouns and terms with gender‑neutral alternatives.
- Suggest inclusive alternatives for non‑inclusive words without altering the
  original text.
- Highlight non‑inclusive words for quick review.
- Compute basic statistics on the occurrence of non‑inclusive language.
- Analyze sentiment of the provided text using TextBlob.
- Supports processing from files or direct text input via the command line.

Usage
-----
This script can be run as a standalone program or imported as a module.
When run directly, use the ``--mode`` option to select the operation:

```
python inclusive_toolkit.py --mode inclusive --text "Hello guys!"
python inclusive_toolkit.py --mode highlight --file input.txt
python inclusive_toolkit.py --mode stats --text "The chairman and his team..."
python inclusive_toolkit.py --mode suggest --text "Man-made objects"
python inclusive_toolkit.py --mode sentiment --text "I love this project!"
```

You can also specify ``--output`` to save results to a file instead of printing
it to stdout.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from typing import Dict, List, Tuple, Iterable

from textblob import TextBlob

# Mapping of non‑inclusive terms to inclusive alternatives. Keys should be
# lowercase to facilitate case‑insensitive matching. The values are always
# strings; if multiple alternatives exist, they can be provided as a comma‑
# separated string or you can update the function to return a list.
NON_INCLUSIVE_MAP: Dict[str, str] = {
    "guys": "folks",
    "guy": "person",
    "chairman": "chairperson",
    "manpower": "workforce",
    "man-made": "human-made",
    "he": "they",
    "she": "they",
    "his": "their",
    "her": "their",
    "him": "them",
    "hers": "theirs",
    "mankind": "humankind",
    "policeman": "police officer",
    "fireman": "firefighter",
    "waiter": "server",
    "waitress": "server",
    "postman": "mail carrier",
    "salesman": "salesperson",
    "businessman": "businessperson",
    "congressman": "legislator",
    "middleman": "intermediary",
    "housewife": "homemaker",
    "master": "primary",
    "slave": "secondary",
    "disabled": "person with a disability",
    "handicapped": "person with a disability",
    # Add more terms as needed
}

# Compile regex patterns for efficient repeated use.
_WORD_RE = re.compile(r"\b\w+[-']?\w*\b")


def _tokenize(text: str) -> List[Tuple[str, int, int]]:
    """Tokenize the text into a list of (word, start_index, end_index).

    Punctuation is preserved outside the tokens. Indexes refer to positions in
    the original string.
    """
    tokens: List[Tuple[str, int, int]] = []
    for match in _WORD_RE.finditer(text):
        tokens.append((match.group(0), match.start(), match.end()))
    return tokens


def make_inclusive(text: str) -> str:
    """Return a version of the input text where non‑inclusive words are
    replaced with their inclusive alternatives. Case is preserved based on
    the original word.

    Words not in ``NON_INCLUSIVE_MAP`` are left unchanged.
    """
    result: List[str] = []
    last_index = 0
    for word, start, end in _tokenize(text):
        # Append any intervening characters (punctuation, whitespace)
        result.append(text[last_index:start])
        lower_word = word.lower()
        replacement = NON_INCLUSIVE_MAP.get(lower_word)
        if replacement:
            # Preserve capitalization if the original word starts with a capital letter
            if word[0].isupper():
                replacement = replacement.capitalize()
            result.append(replacement)
        else:
            result.append(word)
        last_index = end
    result.append(text[last_index:])
    return "".join(result)


def analyze_sentiment(text: str) -> str:
    """Classify the sentiment of the text as 'positive', 'negative', or 'neutral'.

    Uses TextBlob to compute the polarity. Thresholds can be adjusted as
    needed.
    """
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.05:
        return "positive"
    if polarity < -0.05:
        return "negative"
    return "neutral"


def highlight_non_inclusive(text: str, marker: str = "**") -> str:
    """Return the text with non‑inclusive words highlighted using the given marker.

    By default, words are wrapped with double asterisks (e.g., **chairman**).
    You can change the marker to any string (e.g., brackets) as needed.
    """
    result: List[str] = []
    last_index = 0
    for word, start, end in _tokenize(text):
        result.append(text[last_index:start])
        lower_word = word.lower()
        if lower_word in NON_INCLUSIVE_MAP:
            highlighted = f"{marker}{word}{marker}"
            result.append(highlighted)
        else:
            result.append(word)
        last_index = end
    result.append(text[last_index:])
    return "".join(result)


def get_stats(text: str) -> Dict[str, int]:
    """Return statistics about the text related to inclusivity.

    The returned dictionary contains:
    - total_words: total number of word tokens in the text
    - non_inclusive_count: how many non‑inclusive words were found
    - unique_non_inclusive: number of unique non‑inclusive words found
    """
    tokens = _tokenize(text)
    total_words = len(tokens)
    found: List[str] = []
    for word, _, _ in tokens:
        if word.lower() in NON_INCLUSIVE_MAP:
            found.append(word.lower())
    return {
        "total_words": total_words,
        "non_inclusive_count": len(found),
        "unique_non_inclusive": len(set(found)),
    }


def suggest_alternatives(text: str) -> Dict[str, str]:
    """Return a mapping of non‑inclusive words found in the text to their
    inclusive alternatives.

    If a word appears multiple times, it will be listed only once in the
    result. Case of the returned keys is normalized to lowercase.
    """
    suggestions: Dict[str, str] = {}
    for word, _, _ in _tokenize(text):
        lower_word = word.lower()
        if lower_word in NON_INCLUSIVE_MAP:
            suggestions[lower_word] = NON_INCLUSIVE_MAP[lower_word]
    return suggestions


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    """Parse command‑line arguments.

    Arguments:
        argv: Iterable of argument strings. Defaults to ``sys.argv[1:]``.
    """
    parser = argparse.ArgumentParser(description="Inclusive Language Toolkit")
    parser.add_argument(
        "--mode",
        choices=[
            "inclusive",
            "sentiment",
            "highlight",
            "stats",
            "suggest",
        ],
        required=True,
        help="Mode of operation: inclusive, sentiment, highlight, stats, or suggest.",
    )
    parser.add_argument(
        "--text", help="Direct input text. Overrides --file if provided."
    )
    parser.add_argument(
        "--file", help="Path to an input file. Used if --text is not supplied."
    )
    parser.add_argument(
        "--output",
        help="Path to an output file. If omitted, results are printed to stdout.",
    )
    parser.add_argument(
        "--marker",
        default="**",
        help="Marker string to use for highlighting non‑inclusive words (default '**').",
    )
    return parser.parse_args(list(argv) if argv is not None else None)


def _read_input(args: argparse.Namespace) -> str:
    """Read text input from the provided --text or --file argument.

    Raises ValueError if neither source is provided.
    """
    if args.text is not None:
        return args.text
    if args.file is not None:
        if not os.path.exists(args.file):
            raise FileNotFoundError(f"Input file not found: {args.file}")
        with open(args.file, "r", encoding="utf-8") as f:
            return f.read()
    raise ValueError("No input provided. Use --text or --file.")


def _write_output(output: str, output_path: str | None) -> None:
    """Write output to the given path or print to stdout if no path given."""
    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(output)
    else:
        print(output)


def main(argv: Iterable[str] | None = None) -> None:
    args = parse_args(argv)
    try:
        text = _read_input(args)
    except Exception as exc:
        print(f"Error reading input: {exc}", file=sys.stderr)
        sys.exit(1)

    mode = args.mode
    if mode == "inclusive":
        result = make_inclusive(text)
        _write_output(result, args.output)
    elif mode == "sentiment":
        sentiment = analyze_sentiment(text)
        _write_output(sentiment, args.output)
    elif mode == "highlight":
        highlighted = highlight_non_inclusive(text, marker=args.marker)
        _write_output(highlighted, args.output)
    elif mode == "stats":
        stats = get_stats(text)
        # Pretty print statistics as JSON
        _write_output(json.dumps(stats, indent=2), args.output)
    elif mode == "suggest":
        suggestions = suggest_alternatives(text)
        _write_output(json.dumps(suggestions, indent=2), args.output)
    else:
        print(f"Unknown mode: {mode}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":  # pragma: no cover
    main()
