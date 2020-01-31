# GenerateParentheses

This problem was hard for me. I thought I understood it at first, but there was a false assertion I made that ended up having me hung on the problem for a while.
I nearly looked at the solution, but I took a break and as I was on the break I identified another potential approach and effectively solved it.

## Solution 1:
- This solution approaches adding parentheses in 3 different ways:
  - left -> () + str
  - right -> str + ()
  - middle -> ( + str + )
- however this did not work. It fails to generate some fo the patterns and results in the wrong answer
- I was convinced this was a possible solution, but the more I played with it, the more impossible I found it to be.

## Solution 2:
- This approach is the same as Solution 1 except that it's recursive
- There was originally a bunch of other code that was surrounding this, but at the end of the day this had the same output as solution 1

## Solution 3:
- I'm quite proud that I found this solution.
- Basically, left and right index usage are kept track of in addition to the current string generated
- during each recursive stack call only a left or right parenthese is added - not two
- when out of left and right parentheses to use there should be a solution
- it's important to denote that left_used > right_used to prevent right parentheses added before left parentheses

Each recursive stack has 2 potential paths ( or ). This can be considered a branching factor
The total depth is 2*n
- Runtime: O(2^2n) -> (2^n)
- Space: O(2^2n)) -> (2^n)

End of the day the number of solutions grows by the catalan number for both runtime and space: O(4^n / n^(1/2))
