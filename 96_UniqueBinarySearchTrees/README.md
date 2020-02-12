## Unique Binary Search Trees

This problem took me a long time to understand. I did get close to a DP solution, but I needed to read somebody elses solution to validate the path I was on

I identified two things about this problem.

The first, the problem is symmetric and we only need to compute half the tree. This can be applied to all subtrees as well.

Second, we can cache the amount of work for a given type of tree. When computing over a tree, no matter where we are, if there are 3 elements, it doesn't matter what those 3 elements are it's the same number of trees. This work can be cached.

The most optimal solution can be found in constant time since it's the Catalan Number.
I never would have gotten the Catalan Number. It's was not apparent to me unless I was a mathematician


Runtime: O(n)
- every depth we look at a range, the ranges go from n, n-1, n-2 to 0
- the values at that range are cached for all future range computations that have yet to be done
- If our range is 4, the one below is 3, the one below is 2, the one below 1.
- Caching the work while coming back up, when the range moves over, we just use that work
- The next time we come across 1, 2, 3, or 4 we can just look at the cache

Space: O(n)
- we need to cache all the range values up to n
- our recursive stack is upwards of the length of the number of numbers we have
- as we move through our ranges the recursive depth gets smaller since we've caching all that work