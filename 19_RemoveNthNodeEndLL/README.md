# RemoveNthNodeEndLL

## Solution 1

- This is a naive solution that loops through one time to compute the size of the linked list
- It then loops through list again with a previous pointer and a current pointer. It stops at the correct index (size - n)
- It then removes the item from the list using general singly linked list removal

- Runtime: O(n)
- Space: O(1)

## Solution 2
- This is my most opitmized solution
- I loop through the linked list once and index every element into a hash
- I then compute the index that needs to be removed (size - n)
- I also capture the index before and the index after the element that needs to be removed and link them

- Runtime: O(n)
- Space: O(n)

## Solution 3
- This is my second most optimized solution
- It uses 3 pointers.
- The first pointer is the end pointer
- The second pointer is the current pointer
- The third pointer is the previous pointer
- The first pointer and the second pointer are n distance apart
- When the endpointer reaches the end I link the previous pointer with the current pointer's next node

- Runtime: O(n)
- Space: O(1)
