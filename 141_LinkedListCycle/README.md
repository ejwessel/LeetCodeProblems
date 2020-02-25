## Linked List Cycle

optimal solution doesn't use a set
inoptimal can use a set

Runtime: O(n) / O(n + k)
- iterate over all elements in the list. 
- analysis for iterative solution is a bit more complex
  - k is the cycle length
  - once in the cycle the double node needs to catch up to the single node

Space: O(n) / O(1)
- O(n) when using a set
- O(1) when only using two pointers
