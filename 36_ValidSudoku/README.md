# ValidSudoku

- Runtime: O(n^2)
  - Every element needs to be looked at 3 times on an O(n^2) board
  - row; horizontally
  - column; vertically
  - 3x3 grid
- Space: O(1)
  - worse case a set() is created with 9 elements
