# 4Sum

I did not solve this problem. I looked at a solution to complete it.

Turns out that I got pretty close, but I was still out of bounds for the runtime that was possbile.

My first solution was O(n^4)
- This was a recursive solution that looked four levels deep amongst all numbers and checked the sums

My second solution was O(n^3)
- This was also a recurive solution, but looked 3 levels deep.
- I have a map of number sum to a list of lists. The map is to keep track of what numbers add up to a sum and reference that later
- I stop at 3 levels becasue at that point I have all the 3 sums and can compute the required value and check if it's available in the remaining numbers that I've yet to use

The last solution which is the most optimal at O(n^2)
Is similar to the other solutions except for the fact that it is not recursive and it keeps track of the indices of used numbers rather than the numbers themselves.
This prevents double counting a number in the result list.
I had this idea before, but I wasn't able to get around this particular limitation and kept working with lists. 
