## Convert Sorted List to Binary Search Tree

When I first started this problem I thought that I needed to insert the nodes into a binary tree and continually rebalance when necessary
It wasn't until I had an inclination that I could take a list and perform a

Runtime: O(n)
- create a list representation of the linked list O(n)
- go through list representation and create all nodes linking them up O(n)

Space: O(n)
- need a list to store all the nodes O(n)
- need to construct a graph recursively over the total number of nodes in the list. Construction of the graph is O(logn)
- total number of nodes created that need to be returned is still O(n), but in a tree form
