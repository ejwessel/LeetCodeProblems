# RomanToInteger

## Solution 1:
- I use a Roman numeral to number mapping for the main distinctive numerals
- I use an index to loop over all the characters
- I look at the current char + 1 and identify if that is an element in the map
- I sum the numbers integers value I look at the numerals are visited
- Runtime:
  - worst case scenario we look at every character 
  - O(n)
- Space:
  - No datastructures are used
  - O(1)
  
## Solution 2:
- This solution I worked on with Brian. 
- It is arguably much simpler to look at, but does not perform as well as solution 1. I believe this is due to the list splitting that creates a new string
- Runtime: O(n)
  - every character still need to be look at
- Space: O(n^2)
  - the method is called recursively and causes the stack to increase
  - New strings are created intermittently as it recursively goes down
  - s[::] create a new string, but altogether every depth is -1 the previous length. This is a well known summation pattern and is O(n^2)
