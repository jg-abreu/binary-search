# Binary Search

![Language: Python](https://img.shields.io/badge/language-Python-3776AB?style=flat) [![License: MIT](https://img.shields.io/badge/license-MIT-39764D?style=flat)](LICENSE)

I built this interactive Python script to see how many comparisons binary search makes. Enter a list size and a target to find out whether the target is present, its zero-based index if found, and how many attempts the search took.

[Run the script](#run-the-script) · [See examples](#examples)

## Run the script

You need Python 3 and Git to follow these steps. The script uses only the Python standard library.

```sh
git clone https://github.com/jg-abreu/binary-search.git
cd binary-search
python binary_search.py
```

Enter a positive list size and an integer to search for. The script builds a sorted list from `0` through `size - 1`.

## Examples

Each attempt checks one midpoint. These are two runs of the script:

| List size | Target | Result | Attempts |
| ---: | ---: | --- | ---: |
| 1,000,000 | 999,999 | Found at index 999,999 | 20 |
| 8 | 8 | Target absent | 4 |

## How it works

The search compares the target with the middle element of the current range. If they differ, it keeps the half that can still contain the target. It stops when it finds a match or the range is empty.

For a list of size *n*, the search takes **O(log n)** time in the worst case and uses **O(1)** extra space. Building the list with `list(range(size))` takes **O(n)** time and **O(n)** space, so list creation determines the overall time and space complexity of this script.

[Read the Python source](binary_search.py)

## License

This project is available under the [MIT License](LICENSE).
