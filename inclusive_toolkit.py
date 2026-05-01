#!/usr/bin/env python3
"""
Inclusive Language Toolkit

This script provides functions to analyze and transform text to be more inclusive.
Features:
- Replace gendered pronouns with gender-neutral alternatives.
- Replace common non-inclusive words with inclusive alternatives.
- Provide sentiment analysis using TextBlob.
"""
from textblob import TextBlob

NON_INCLUSIVE_MAP = {
    "guys": "folks",
    "chairman": "chairperson",
    "manpower": "workforce",
    "man-made": "human-made",
    "he": "they",
    "she": "they",
    "his": "their",
    "her": "their",
    # Additional replacements
}

def make_inclusive(text: str) -> str:
    """Return an inclusive version of the input text by replacing non-inclusive words."""
    words = text.split()
    inclusive_words = []
    for word in words:
        lower = word.lower()
        # Extract alphabetic characters to match dictionary keys
        root = "".join(filter(str.isalpha, lower))
        if root in NON_INCLUSIVE_MAP:
            replacement = NON_INCLUSIVE_MAP[root]
            # Preserve capitalization
            if word.istitle():
                replacement = replacement.capitalize()
            inclusive_words.append(replacement)
        else:
            inclusive_words.append(word)
    return " ".join(inclusive_words)

def analyze_sentiment(text: str) -> float:
    """Return the sentiment polarity of the text using TextBlob."""
    blob = TextBlob(text)
    return blob.sentiment.polarity

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Inclusive Language Toolkit")
    parser.add_argument("text", help="Input text to analyze and transform")
    parser.add_argument("--sentiment", action="store_true", help="Show sentiment analysis")
    args = parser.parse_args()

    inclusive_text = make_inclusive(args.text)
    print("Inclusive version:")
    print(inclusive_text)
    if args.sentiment:
        sentiment = analyze_sentiment(args.text)
        print(f"Sentiment polarity: {sentiment:.3f}")

if __name__ == "__main__":
    main()
