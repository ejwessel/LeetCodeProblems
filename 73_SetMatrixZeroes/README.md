## Set Matrix Zeroes

Its important to keep track of the rows and columns independently before modifying them to see if 0th row or column is marked
This is because the 0th rows and columns are used as indicators for the remaining matrix

Runtime: O(mn)
- need to look at every cell in the input

Space: O(1)
- the work is done in place on the original matrix
- the only data we keep around is length, and if the 0th rows and columns are marked to be 0s
