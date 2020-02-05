## Combinations

Runtime: O(n^k)
- start moves forward each depth
- end moves forward each depth
- window between start and bound is at most n so branching factor is n and depth is k
- The reason the runtime is 'not' nCk is because NOT all the combinations need to be iterated over
- However O(n^k) and O(nCk) are functionally equivalent depending on values of k

Space: O(n^2)
- solution is built iteratively at each recursive depth
- solution increases by 1 each level 1, 2, 3, ..., n -> O(n^2)
- depth is at max k recursive stack is O(k)
- space id dominated by the increasing solution