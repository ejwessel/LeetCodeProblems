## JumpGame

I had a a pretty good intuition about this problem and needing to use DP.
I went as far as implementing the DP problem correctly and then I got to passing 74/75 test cases.

I identified that in the worst case my algo would be O(n^2)

I tried to find ways that I could optimize my solution and came up with a loss. I knew there was something there,
but felt it was necessary to scan in my memo table since there was a bunch of work done to get me to that point.

I gave up and read the first paragraph of the solution and saw they just kept the last best index.
I thought this was cheap since we did all this work for DP, but then didn't even use DP. 
Instead, we used the intuition learned from DP to then solve the problem in a non DP manner.

I implemented the final solution

### Solution 1
Runtime:
- O(n^2) because in the worst case we need to scan over backwards.

Space:
- O(n) keep a byte array of if indices can reach the end.

### Solution 2
Runtime:
- O(n) walk though each element once.

Solution 2 Space: 
- O(1) the only data we keep around is a last good index variable.
