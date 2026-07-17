# String Capitalize & Strip Practice

A small script that plays around with `.capitalize()`, `.strip()`, `.lstrip()`, and `.rstrip()` on a bunch of different strings, then adds a period at the end of each one like a proper sentence.

## What it does

Takes a bunch of test strings — some with mixed casing (`"hello WORLD"`), some with extra spaces at the start, end, or both — and cleans them up so each one:

1. Has its whitespace trimmed off (where needed).
2. Starts with a capital letter, rest lowercase (that's what `.capitalize()` does).
3. Ends with a period.

Example:

```
text5 = " and spaces at both ends "
print(text5.strip().capitalize() + ".")
```

Output:

```
And spaces at both ends.
```

## The strings being tested

- `text` through `text_3` — just messing with different casing (all lowercase, mixed, all caps) to see how `.capitalize()` handles each one.
- `text1` through `text5` — whitespace tests: leading spaces, trailing spaces, spaces on both ends.
- `text6` through `text9` — single character or short strings, some with whitespace, to check edge cases.
- `text10` — a longer sentence with no whitespace issue, just to confirm capitalize still only capitalizes the first letter.

## Key things this practices

- `.capitalize()` lowercases everything except the first letter — so `"hello WORLD".capitalize()` becomes `"Hello world"`, not `"Hello World"`. Good to see that behavior clearly on `text_1` to `text_3`.
- `.strip()` removes whitespace from both ends, `.lstrip()` only the left, `.rstrip()` only the right — used deliberately on `text7` and `text8` to isolate one side at a time.
- Order matters: `.strip().capitalize()` vs `.capitalize().strip()` can give different results if the leftover whitespace is at the start (since `.capitalize()` only affects the first character it sees).

## Running it

```bash
python simple_text_formatter.py
```

No inputs needed, just runs straight through and prints all 14 formatted lines.

## Notes / things to improve later

- Right now everything's hardcoded as separate variables — could easily be a list of strings looped through instead.
- `text` uses `str(text.capitalize() + ".")` which wraps an already-string result in `str()` — that's redundant since `.capitalize()` already returns a string.