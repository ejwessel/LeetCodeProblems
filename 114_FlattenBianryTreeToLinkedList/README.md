## Flatten Binary Tree to Linked List

Runtime: O(n)
- all nodes need to be visited

Space: O(n)
- tree is not balanced, entirety of tree could exist in the recursive stack

The iterative solution is very simple, but seeing the pattern amongst the stack was not intuitive to me.
I needed to understand that no 'None' nodes are added to the stack and that the next element in the stack is what the element should link to