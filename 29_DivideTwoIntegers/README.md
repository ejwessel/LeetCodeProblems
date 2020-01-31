# DivideTwoIntegers

This was a hard problem. 
I came up with a naive solution, but did not pass because the runtime was too high.
I tried looking into faster ways to run the algorithms, but never got to identify the rule that allowed the code to run faster.
I got close, but no dice

Solution 1:
- Since division is glorified subtraction I subtract the denominator as many times as possible from the numerator.
- This solution is O(n). In the worse case scenario N is very large and the denominator is 1. This means I'd need to subtract N times into the numerator, which can take forever.

Solution 2:
- This approach uses bit shifting. It doesn't need to be done with bit shifting, but is much simpler to handle
- The approach is to identify the largest (denominator * 2^n) that can be subtracted from the numerator. 
- If we have N/D, then (N - D*2^n)
- By identifying the largest number we can cut down on computations drastically due to powers of 2
- The algorithm uses power of 2 and makes a dramatic improvment over the number of computations that need to be done.
- Runtime: O(logn)
- Space: O(1)
