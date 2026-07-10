# Word Analyzer

A simple command-line Python tool that analyzes a user-provided sentence, displaying it in different letter cases and reporting basic character-level statistics.

## Features

- Converts an input sentence to uppercase, lowercase, and title case
- Counts the total number of characters in the sentence
- Extracts the first and last letters of a fixed reference word (`"Python programming"`)
- Clean, formatted console output

## Requirements

- Python 3.x (no external dependencies)

## Usage

Run the script from your terminal:

```bash
python word_analyzer.py
```

You will be prompted for the following inputs:

| Prompt | Description |
|---|---|
| `Enter a statement` | The sentence to analyze |
| `Enter a word` | Currently not used for analysis (see **Notes** below) |

## Example

```
Enter a statement: Hello World
Enter a word: anything

===================================================
           WORD ANALYZER
====================================================
Actual text: Hello World
Uppercase: HELLO WORLD
Lowercase: hello world
Titlecase: Hello World
Firstletter: P
Lastletter: g
Characters: 11
======================================================

Thank you for using Word Analyzer!
```

## How It Works

- `.upper()`, `.lower()`, and `.title()` transform the entered `sentence` into different letter cases.
- `len(sentence)` counts every character in the sentence, including spaces and punctuation.
- `word[0]` and `word[17]` extract the first and last letters — but from the fixed string `"Python programming"`, not from the `word` typed in by the user.

## Notes

- **The `word` input is currently overwritten** by the line `word = "Python programming"` immediately after it's entered, so whatever you type for "Enter a word" has no effect on the output. If you want the first/last-letter analysis to reflect user input, remove that line.
- The last-letter index (`word[17]`) is hardcoded to match the length of `"Python programming"`. If the reference word changes, this index must be updated too (or use `word[-1]` for a more robust solution).
- Input is not validated; an empty statement will simply produce empty/zero-length output.

## Author

**Vincent-coder46**

## License

Free to use, modify, and distribute.