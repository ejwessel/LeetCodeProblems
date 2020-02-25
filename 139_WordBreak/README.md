## Word Break

Runtime: O(n^2)
- I cache duplicate work to not travel down a particular path

Space: O(n)
- I need to save representations of the strings I see that don't work
- recursive depth is at most the length of the entire string, meaning all characters