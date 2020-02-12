## Validate Binary Search Tree

I use a range and pass it down and compare the root node to the range to see if it's in the allowable range

Runtime:O(n)
- all nodes need to be evaluated

Space: O(n)
- no mention about a balanced BST, could be right or left heavy
- therefore it could be that the recursive stack is the total number of nodes