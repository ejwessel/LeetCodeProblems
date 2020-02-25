## Word Break

Runtime: O(mn^2)
- I cache duplicate work to not travel down a particular path
- only paths that are in the dictionary are traversed however

Space: O(n)
- I need to save representations of the strings I see that don't work this will take linear space
- recursive depth is at most the length of the entire string, meaning all characters