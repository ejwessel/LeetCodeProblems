## Search in Rotated Sorted Array 2

This was an interesting problem. I really enjoyed that I thought it was very similar to part 1.
However, the addition of duplicates changes the problem in a subtle way.

It can 'sometimes' break the assumption that at either the left or the right is sorted when in reality one is not

In that case it's important to identify which side is actually sorted

Runtime: Average O(logn); Worst O(n)
- in the situation when given something like [1, 1, 1, 1, 1, 1, 2, 1]
- [1, 1, 1, 1] and [1, 1, 2, 1]
- both segments when divided look like they're sorted, when comparing the end elements
- having to identify which side is sorted forces a linear search on one side to identify what side is sorted or not
- worse case scenario is when an element is at the end and the rest of the list is the same element

Space: O(1)
- no data is held