# Path Sum 2

I have three solutions for this problem

The first two solutions are in optimal because of the creation of the list when passing down and up the recursive stack.

The third solution uses a class stack that is pushed and popped from. When we reach a leaf node it is copied to a solution set.

Runtime: O(n)
- all nodes need to be visited

Space: O(n)
- recursive stack of the height of the tree; tree is not balanced
- usage of 'path' stack keeps up to the total number of elements for that path
