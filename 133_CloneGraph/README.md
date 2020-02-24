## Clone Graph

Runtime: O(m)
- m is the total number of edges
- in the worst case scenario all nodes are connected to all nodes and therefore you have clique.
- the total number of edges in a clique is n(n-1)/2


Space: O(n)
- cache of seen nodes is saved
- it's possible all the nodes exist in the queue