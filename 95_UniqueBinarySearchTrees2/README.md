## Unique Binary Search Trees 2

I was not able to get this problem without difficulty

I immediately identified that the tree is a permutation of all the numbers from [1, n + 1], however when working with examples I found that there were duplicates given a permutation.

** A permutation is unique, but it does not generate unique binary trees.

I tried to find sub problems that I could perhaps solve, but I couldn't identify any

My first solution is really bad. It's runtime is gigantic and didn't even register on the leetcode times. It passed, but was terrible.
It's space complexity is also really bad.

I'm not going to evaluate that first solution. I will only evaluate the second solution

Runtime: O(2^n)
- every node is used a root
- every node moving downward has a left and right of allowed nodes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
- I reconstruct all subtrees at a depth
- d = n max number of nodes in tree
- b = 2 get left and right subtree 
- each depth removes a root and shrinks by 1

Space: O(n!)
- recursive approach to creating trees
- possible # of trees O(n!) ignoring there are duplicates