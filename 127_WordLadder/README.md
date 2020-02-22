## Word Ladder

Runtime: O(mn^2)
- Likely have to look at the word list multiple times.
- In the best case scenario we can always reduce the size of the words by 1
- This means n, n-1, n-2, etc until 0; well known pattern 
- Words need to be compared each time

Space: O(n)
- It's possible the entirety of the word list can exist in the queue

I had a very difficult time with the bidirectional solution. 
It had mainly to do with when to mark a node visited and when it's solution should be returned.

I narrowed it down to two methods:
When should we add to queue based off other queue?
1. check before adding to queue if other node has seen some node
2. check when visiting if other node has seen node

Method 1 works because the depth is available at the time it's discovered
Method 2 doesn't work because I could be visiting a node late instead of earlier in the discovery

Bidirectional Runtime: O(b^d)
- branching factor is unknown for a given known
- total depth is unknown but search space only need to go through half the graph for each node

Bidirectional Space: O(b^d)
- possibly need to keep all the potential branches in memory
