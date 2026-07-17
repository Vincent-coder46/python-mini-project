# Book Info Formatter

A simple Python script that takes messy, semicolon-separated book data and turns it into clean, readable output.

## What it does

Each book's info comes in as one raw string like this:

```
"harper lee ; to kill a mockingbird ; 1960 ; ISN 978-0-06-112008-4 ; 324 ; 2999.4789"
```

The script splits it up, cleans it, and prints something like:

```
The book To Kill A Mockingbird was written by Harper Lee and published in 1960.
It has 324 pages and ISBN 978-0-06-112008-4 and costs #2999.4789
```

## How it works

For each book entry:

1. Split the raw string on `;` to get each piece (author, title, year, isbn, pages, cost).
2. `.strip()` to remove extra whitespace from splitting.
3. `.title()` on author and title so names/titles look properly capitalized.
4. `.replace("ISN", "ISBN")` to fix the typo in the raw data.
5. `float()` on the cost so it's treated as a number, not just text.
6. Print it all out in a formatted sentence using an f-string.

## Data covered

There are 10 sample entries (`book_info` through `book_info9`), each a different classic book — 1984, The Great Gatsby, The Hobbit, War and Peace, A Tale of Two Cities, and a few others. Every entry goes through the same cleanup process, printed one after another with separators between them.

## Running it

```bash
python book_info_formatter.py
```

No inputs needed — it just runs through all the sample data and prints the formatted results for each book.

## Notes / things to improve later

- Right now every book is basically copy-pasted code with a different variable name (`book_info`, `book_info1`, `book_info2`... `book_info9`). The obvious next step is to put this in a list and loop through it with a function instead of repeating the same block 10 times.
- The "ISN" → "ISBN" replace is fixing a typo that's baked into the raw data on purpose, just to practice string cleanup.
- Cost is left as a raw float, so some entries print long decimals (e.g. `1820.33434`) instead of being rounded to 2 decimal places — could add `round(cost, 2)` or format with `:.2f` later.