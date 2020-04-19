## Longest Substring with At Most Two Distinct Characters

This was my first problem after weeks of not practicing. I tried to be clever when I did my first solution only to
realize that it was a window problem and I just needed to move the start and end pointers

Solution 2 was much easier and faster to write

Runtime: O(n)
- every character is looked at once

Space: O(1)
- the hashmap size is at most 2 and keeps track of a single digit for a key
