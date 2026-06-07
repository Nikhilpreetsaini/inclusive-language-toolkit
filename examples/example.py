"""Example script demonstrating usage of the inclusive_language_toolkit package.

This script shows how to use the functions provided by inclusive_toolkit to
make text more inclusive, highlight non-inclusive words, gather statistics,
suggest alternative terms, and analyze sentiment.
"""

import inclusive_toolkit as it


def main() -> None:
    """Run an example demonstrating the toolkit's features."""
    text = (
        "Hey guys, the fireman said mankind was doomed. "
        "She said he/she will never know."
    )
    print("Original text:")
    print(text)
    print("\nInclusive version:")
    inclusive = it.make_inclusive(text)
    print(inclusive)

    print("\nHighlighted non-inclusive words:")
    print(it.highlight_non_inclusive(text))

    print("\nStatistics:")
    stats = it.get_stats(text)
    for key, value in stats.items():
        print(f"{key}: {value}")

    print("\nAlternative suggestions:")
    print(it.suggest_alternatives(text))

    print("\nSentiment score:")
    sentiment = it.analyze_sentiment(text)
    print(sentiment)


if __name__ == "__main__":
    main()
