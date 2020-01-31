# CombinationSum

## Solution 1
- This is a really inoptimal solution, but I wasn't able to come up with anything better.
- every number is visited in non sorted order O(n) on every recursive depth
- the used numers are added up O(n)
- the numbers are sorted when creating an answer O(logn)
- This is a strict O(b^n) as every number is inspected at every depth
- I think I could have done a lot better if I sorted the input.

## Solution 2
- I did not come up with this solution. This was an optimal solution that I read about and analyzed. I was close to identifying this solution, but I didn't know how to formalize it into code.
- All the numbers are sorted first. O(logn)
- This solution is O(b^n) 
  - b is the branching factor which in the best case is 1 less than previous since the list is shrinking
  - n is the recursive depth that needs to be reached in order to find or reject a particular path
- What makes this algorithm really fast is the problem space is reduced when (target-num). Given the numbers are sorted it makes the problem space to search really efficient as we aren't checking a bunch of numbers that could otherwise be ignored.
