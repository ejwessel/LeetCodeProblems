## Populating Next Right Pointers in Each Node

identifying this problem the naive way, was easy.
I immediately saw that I could pass a depth along and keep a pointer to the previously seen node at a depth

Runtime: O(n)
- all nodes need to be looked at

Space: O(logn)
- need to keep log n pointers for the total elements in the perfect binary tree

The optimal route is to use the fact that a node has next
It was Brian that identified the usage of being able to leverage next

In both the iterative and the recursive manner if a node has next then we can 'bridge' a gap

Runtime: O(n)
- all nodes need to be looked at

Space: O(log n) - recursive
Space: O(log n) - iterative
- recursive stack doesn't count, but could be considered to use space at the height of the tree
- iterative is DFS and keeps the right node in the stack at most the height of the tree

It's possible to instead traverse levels with root.left and then at every level continue connecting lower level children gaps
