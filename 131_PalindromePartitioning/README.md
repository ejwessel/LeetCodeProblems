## Palindrome Partitioning

Runtime: O(b^d)
- this is essentially a DFS
- it has a branching factor at every level 1 less than the level above it
- the depth is the size of the string

Space: O(b^d)
- the palindromes are saved 
- the solutions of palindromes are saved
- worst case scenario everything is a palindrome. ex: "aaaaaaaaaa"
- all solutions need to be saved. If that's the case then there are the total number of paths are your solution...

I actually don't have any idea how to analyze this problem deeply...