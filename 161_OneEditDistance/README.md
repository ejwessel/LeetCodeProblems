When I first attempted this problem I immediately saw it as Levenshtein Distance. I was able to successfully write the algorithm. However, since we only care about when distance is 1, we can be more clever

## Solution 1:
Runtime: O(mn)
- need to create the distance matrix
Space: O(nm)
- a distance matrix needed

## Solution 2:
Runtime: O(min(n, m))
- go through both strings at the same time looking for a misplaced character
- allows for only 1 misplaced character
Space: O(1)
- no extra space is used
