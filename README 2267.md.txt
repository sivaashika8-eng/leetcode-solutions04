# Valid Parentheses String Path

LeetCode 2267: Check if There is a Valid Parentheses String Path

## Problem
Given an `m x n` grid of `'('` and `')'`, determine whether a path from the top-left to the bottom-right cell, moving only down or right, forms a valid parentheses string.

## Approach
Dynamic programming over `(row, col, balance)` with a bitset optimization.

- Every path has length `m + n - 1`. If it is odd, return `False`.
- Each cell stores a bitmask of reachable balances (opens minus closes).
- `'('` shifts the mask left (`balance + 1`), and `')'` shifts it right (`balance - 1`). Invalid prefixes (balance < 0) drop out automatically.
- Balance is capped at `(m + n - 1) // 2`.
- The answer is `True` if bit 0 is set at the bottom-right cell.

## Complexity
- Time: O(m · n · (m + n) / w), where w is the word size
- Space: O(n)

## Usage
```python
from valid_parentheses_string_path import Solution

grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
print(Solution().hasValidPath(grid))  # True

grid = [[")",")"],["(","("]]
print(Solution().hasValidPath(grid))  # False
```

## Files
- `valid_parentheses_string_path.py`: solution
- `README.md`: this file