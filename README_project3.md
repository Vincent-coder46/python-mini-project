# Word Replacer

A simple command-line Python tool that performs find-and-replace operations on user-provided text. It processes two independent replacements in a single run: a general statement and a "word of faith" phrase.

## Features

- Interactive CLI prompts for all inputs
- Replaces a target word/phrase within a given statement
- Performs a separate character/substring replacement within a second phrase
- Clean, formatted console output

## Requirements

- Python 3.x (no external dependencies)

## Usage

Run the script from your terminal:

```bash
python word_replacer.py
```

You will be prompted for the following inputs, in order:

| Prompt | Description |
|---|---|
| `Enter a statement or word` | The base sentence to modify |
| `Enter an old_word` | The word/phrase to be replaced in the statement |
| `Enter a new_word` | The replacement word/phrase |
| `Enter a word_of_faith` | A second phrase to modify |
| `Enter a character` | The substring to replace in the word of faith |
| `Enter a new_character` | The replacement substring |

## Example

```
Enter a statement or word: I will fail this exam
Enter an old_word: fail
Enter a new_word: pass
Enter a word_of_faith: I am weak
Enter a character: weak
Enter a new_character: strong

=======================================
              WORD REPLACER
========================================

Updated sentence: I will pass this exam
Word_of_Faith: I am strong

========================================
SO SHALL IT BE! BY GOD'S GRACE
```

## How It Works

The script uses Python's built-in `str.replace(old, new)` method, which replaces **all** non-overlapping occurrences of `old` with `new` in the target string. It performs this operation twice — once on the `statement` and once on the `word_of_faith` — using two independent pairs of search/replacement terms.

## Notes

- Replacement is case-sensitive.
- If `old_word` or `character` is not found in the corresponding input, the original text is returned unchanged.
- Input values are not validated or sanitized; the tool assumes well-formed text input.

## Author

**Vincent-coder46**

## License

Free to use, modify, and distribute.