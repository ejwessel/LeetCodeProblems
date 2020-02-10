## Binary Tree Inorder Traversal

### Recursive (Solution 1)
Runtime: O(n)
- all nodes need to be visited

Space: O(n)
- if the tree is unbalanced then all nodes exist in memory in a recursive depth

### Recursive (Solution 2)
Runtime: O(n)
- all nodes need to be visited

Space: O(n)
- a set is kept to determine if we've visited a node
- it's possible to use O(1) space if we can mark the nodes
