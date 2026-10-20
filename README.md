# Binary Search

![Python 3](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

An interactive command-line implementation of the binary search algorithm in Python that shows where the number was found and how many attempts it took.

## Why binary search

Binary search finds an item in a **sorted** list by checking the middle element and discarding the half where the item can't be. Each attempt halves the search range, so it takes at most about log₂(n) attempts instead of n:

| List size | Linear search (worst case) | Binary search (worst case) |
|---|---|---|
| 100 | 100 attempts | 7 attempts |
| 1,000,000 | 1,000,000 attempts | 20 attempts |

Showing the number of attempts makes that difference visible when you run the script.

## Features

- Builds a sorted list from `0` to `size - 1` with the size you choose
- Searches for the number you enter, halving the range on every attempt
- Reports whether the number was found, its index and the total number of attempts

## Tech stack

Python 3 — no external dependencies.

## Running

```bash
git clone https://github.com/jg-abreu/binary-search.git
cd binary-search
python binary_search.py
```

Example:

```
Enter the size of the list: 1000000
Which number do you want to find? 999999

✅ Found the number 999999.
📍 Position in the list (index): 999999
🔢 Total attempts: 20
```

## License

Released under the [MIT License](LICENSE).

## Author

**João Abreu** — back-end developer and Computer Science student in Rio de Janeiro, Brazil.

[GitHub](https://github.com/jg-abreu) · [LinkedIn](https://www.linkedin.com/in/jo%C3%A3o-abreuuu) · jgabreudev@gmail.com
