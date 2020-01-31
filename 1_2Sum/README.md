# 2Sum

Solution 1: 
- Runtime: O(n^2)
  - loops through all the elements multiple times
- Space: O(1)
  - doesn't save any data intermittently for computing 

Solution 2: 
- Runtime: O(n)
  - uses a seen list and a list to keep track of the indicies of numbers
  - loops through all elements once and populates the sets
  - as it loops through it checks the set to see if we've seen a required num. 
  - if so it tries to compare the indices to see if the number is not at the same index as the current number being inspected
- Space: O(n)
  - keeps track of a seen set
  - keeps track of of a num to idx
