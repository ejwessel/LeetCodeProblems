# CombinationSum2

This solution is very similar to Combination Sum 1

## Solution 1 and Solution 2
- These two solutions are pretty much the same. The second solution just uses a set to check if an element exists or not. This prevents doing a linear search in the list.
- The second solution optimization is offset by the fact that a tuple needs to be converted into a list in order to be saved to the results

- Runtime: O(b^n)
  - b is the branching factor
  - n is the depth
Space: O(b^n)
  - I'm not sure 100% what the space complexit is, but it's definitely less than O(b^n)
  - every number can only be used once
  - there are no duplicates
  - This will never be the same size as runtime as the answer is always a subset of the total input
