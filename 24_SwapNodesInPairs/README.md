# SwapNodesInPairs

- There are 3 pointers:
  - current
  - tail
  - forward
- these span over 3 nodes and relink the nodes when necessary

- Runtime: O(n/2) -> O(n)
  - Every other node is looked at so the list is effectively cut in half, however it's still linear time
- Space: O(1)
  - There is no storage, just 3 pointers
