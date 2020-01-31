# LongestCommonPrefix

## Solution 1:
- the algorithm first looks at all the words and identifies the minimum length O(n^2)
  - all words
  - full length of words
- It it then iterates through i until the min length comparing the all the words at the selected index
- As long as all the characters match at an index we continue to append to the longest common prefix, otherwise we return
- The only space that is used is the longest common prefix. If for example only 1 word was given then the size we hold is the string again
- Runtime: O(n^2)
- Space: O(n)


## Solution 2: 
- This was a solution I worked on with Brian since he identified an alternative way to go about the problem.
- This performs much better and is considerably easier to look at
- First, the first word in the word list is extracted; we are effectively removing it from the word list
- We loop over the first word's length at indices [0, len(first_word))
- We compare each index to all the other indices for all the other words
- Runtime: O(n^2)
  - still need to search over all words and all strings
- Space: O(n)
  - The only space that is used is the longest common prefix. If for example only 1 word was given then the size we hold is the string again
