## Pancake Sorting

Runtime: O(n*3n) => O(n^2)
- look through all elements O(n)
- scan for the list for the largest element O(n)
- when finding the largest element reverse the sublist at that point O(n)
- after reversing sublist reverse at the current element we're at O(n)
- when visiting an element 3 linear operations need to be performed

Space: O(n)
- I need to construct a new list intermittently when flipping the left and right portions of the list
