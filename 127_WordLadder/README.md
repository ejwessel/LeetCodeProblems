## Word Ladder

Runtime: O(mn^2)
- Likely have to look at the word list multiple times.
- In the best case scenario we can always reduce the size of the words by 1
- This means n, n-1, n-2, etc until 0; well known pattern 
- Words need to be compared each time

Space: O(n)
- It's possible the entirety of the word list can exist in the queue