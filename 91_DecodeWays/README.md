## Decode Ways

When I first did this problem I did it the inoptimal way which was to traverse all the paths

Turns out there is a more optimal way that uses DP

inoptimal way is O(2^n)
branching factor of 2 at every level and a depth of n in the worst case scenario

Runtime: O(n)
- every character is looked at once
Space: O(1)
- a queue of constant size 2 is used