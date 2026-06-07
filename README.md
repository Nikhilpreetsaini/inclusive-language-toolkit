# Inclusive Language Toolkit

A Python toolkit for analyzing and transforming text to be more inclusive, accessible, and neutral. It can highlight non-inclusive terms, replace them with inclusive alternatives, compute basic statistics, and perform sentiment analysis. The toolkit includes a CLI for batch processing files or strings.

## Features

- **Non-inclusive term detection:** Recognizes terms such as "guys", "chairman", "manpower", etc., and reports their positions.
- **Inclusive replacements:** Provides recommended inclusive alternatives (e.g., "folks" instead of "guys", "chairperson" instead of "chairman").
- **Highlighting:** Highlights non-inclusive terms in red and replacements in green for easy visualization.
- **Statistics:** Generates counts of inclusive and non-inclusive words, number of replacements, and overall text statistics.
- **Suggestions:** Offers a list of suggested inclusive alternatives for each non-inclusive word.
- **Sentiment analysis:** Performs sentiment analysis using TextBlob to categorize text polarity (positive, negative, neutral).
- **Command -line interface:** Supports reading from stdin or files, writing output to another file, toggling modes (replace, highlight, stats, suggest), and controlling color output.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Nikhilpreetsaini/inclusive-language-toolkit.git
   cd inclusive-language-toolkit
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the toolkit script on a file or provide text directly. By default, it replaces non-inclusive words with their inclusive alternatives and prints the result.

### Examples

Replace non-inclusive terms in a text file and save the output:
```bash
python inclusive_toolkit.py --file input.txt --output inclusive_output.txt
```

Print statistics about non-inclusive usage:
```bash
python inclusive_toolkit.py --file input.txt --stats
```

Highlight non-inclusive words instead of replacing them:
```bash
python inclusive_toolkit.py --file input.txt --highlight
```

List suggestions for improving inclusivity:
```bash
python inclusive_toolkit.py --file input.txt --suggest
```

Run sentiment analysis only:
```bash
python inclusive_toolkit.py --file input.txt --sentiment
```

Process a string of text from stdin:
```bash
echo "Hi guys! The chairman will speak soon." | python inclusive_toolkit.py --highlight
```

For help on all CLI options:
```bash
python inclusive_toolkit.py --help
```

## Contributing

Contributions are welcome! If you have ideas for new features or improvements:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with clear messages.
4. Open a pull request describing your changes.

Please ensure new code is tested and maintainers will review your contribution.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
