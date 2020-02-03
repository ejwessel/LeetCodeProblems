## Permutation Sequence

Runtime: O(n^2)
- every element is looked at
- when in a recursive depth we need to look at all other elements at worst n times

Space: O(n^2)
- I reconstruct the list removing one element each time, this is 1 + 2 + 3 ... + n
- If I were to use the same list then the space would be O(n) because it would just be the stack
- the more optimized verison is O(n) space since it modifies the existing list
