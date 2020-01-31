# Longest_Palindromic_Substring

**Solution 1** is suboptimal and still O(n^3) worst case.
The set of strings and the length checks help to some degree, but not the worst case scenarios.
The algorithm breaks down when I am unable to use the cache or the length of the string to speed up execution.

If for example a string was provided where every character was unique then I would need to check *every* size palindrome candidate. 

Because the recursive levels reduce the size of the string by 1, the worst case is to traverse all the way down the tree n times.

n, n-1, n-2, ..., n-k

This reduction in size of the string is n(n-1)/2 ; O(n^2)

Because every chracter is unique I would then iterate over all element combinations on that level that I haven't seen, O(n)

Therefore O(n^3)

sum_(i=1)^n i (n - (i - 1)) 
