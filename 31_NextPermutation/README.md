# NextPermutation

This was a hard problem but we figured it out.
I like to think of it as a rolodex in some effect. Where when the least significiant digit counts it up roll the next number over.

The specific rules are as follows:
- numbers to the left determine the numbers to the right; numbers to the right depend on numbers to the left
- When looking to identify what a number can become, It looks to the right for the min number that is larger than the current number. 
- When it finds this. It swaps the digits at those indices and then sorts the remianing list on the right.
- This becomes the new number

I had a lot of trouble coding this up not due to not understanding the problem, but because of the assumptions I made about what python was doing for me.
My first issue was that I was using `max()` on the right list. This caused the max number to the right of the current number to be found and caused the wrong numbers to swap. I instead needed to find the next smallest number on the right that was largest than the current number.
I also made bad assumptions about min too. At the end of the day I was using a of python shortcuts and screwing myself over. 

I ended up getting this problem though.

Runtime:
- Sorting the right nums takes O(nlogn)
- Swap takes O(1)
- finding the next best index is O(n)
- There are n positions that need to be evaluated in the worst cast to identify what the next number should be.
- O(n^2)

Space: O(1)
- list is held onto. Indicies are only looked at
