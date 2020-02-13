## Construct Binary Tree from Preorder and Inorder Traversal

My method builds the tree from the bottom up

Runtime: O(n)
- every node is only looked at once

Space: O(n)
- tree can be unbalanced and therefore all nodes would be in memory stack
- all nodes need to be created and represented as a tree tha is eventually returned