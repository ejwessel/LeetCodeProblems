## Verifying An Alien Dictionary

When I first saw this problem I immediately thought of radix sort. 
However, I wasn't sorting I needed to verify

#### First Solution:
Runtime: O(n)
- scan over the characters for every word ensuring the proper order
- the number of times I need to scan over words is the length of the longest word * n

Space: O(1)
- no space is used

#### Second Solution:
My second solution does one pass through all characters and compares their indices

Runtime: O(n)
- scan over ever word
- compare every character between words

Space: O(1)
- no extra space is used


