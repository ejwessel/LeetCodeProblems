## Kth Largest Element in an Array

When I first did this problem I was nearly stumped.
- I immediately identified the usage of a heap or some sorting. Which would be O(nlogn).
- I thought that this method could be done in linear time with some 'trick'
- After about 20 minutes I gave up on looking for a linear method and looked at the descriptions and found that using
a heap was the correct answer but of a fixed size.

Runtime: O(nlogk)
- look through all elements of size n
- height of heap is of of size k
- need to upheap n elements for the height of the tree

Space: O(k)
- heap uses at most k space