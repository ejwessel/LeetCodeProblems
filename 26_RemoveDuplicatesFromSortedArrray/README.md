## Remove Duplicates from Sorted Array

The way to solve these kinds of problem it's to solve them as you would 'not in place' - use a second array
Then after you solve that one translate the 'not in place' to 'in place'.

Runtime: O(n)
- all elements are looked at once

Space: O(1)
- all changes are done in place