# MultiplyStrings

## Solution 1:
- doesn't work. I was trying to be creative

## Solution 2: 
- Works, but is not very fast
- It essentially performs multiplication by iterating through the first numbers (while taking the power of 10 into consideration) and multipliying it by digits in the second number
- everytime it loops over a digit in the first number it's added with it's added to the result sum

- Runtime: O(n^4)
  - for all digits in first number, loop through all digits in second number O(n^2)
  - add all digits in current answer with all digits in answer to be added O(n^2)
- Space: O(n+m)
  - a itermittent sum is held at each iteration which is the length of the longest string
  - that intermittent sum is then added and continually added to for each digit in the first number, but the lenght of that number is not more than O(n1 + n2)
