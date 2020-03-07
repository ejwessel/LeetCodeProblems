## Convert Binary Search Tree to Sorted Doubly Linked List

I misunderstood this problem when I read it. 
I didn't see the BST part and though that the in order representation of the tree would not be sorted.
I ended up spending a lot more work on something I didn't need.

I later saw that everything was sorted and I could therefore just rearrange the nodes by linking them together.
This was much easier.

Runtime: O(n)
- all nodes in the BST need to be looked at

Space: O(n)
- BST may not be balanced and therefore the recursive stack will be the height of the tree (all nodes)