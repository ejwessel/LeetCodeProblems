## Solution 1, 2, 3
These were all a combination of various methods I used to try and get the answer accepted on hacker rank.
The problem was that I would get 311/313 of the test cases to pass, but I'd run out of time, hitting a, "time limit exceeded", error.

The main problem with all of these methods is that they rely on sets to give me a complement value.
I think this is best understood with Solution 3 where I use a `Counter()` object to keep track of elements I've used in a frequency table and then look up if there an `a + b` complement after I've used `a` and `b`. This doesn't guarantee against seeing duplicate tuples of elements. 

with `[-1, 0, 1, 2, -1, -4]`
it is best seen in the output 
```
a: -1, b: 0
freq count Counter({1: 1, -4: 1, 2: 1, -1: 1})
looking for: 1
evaluating [-1, 0, 1]
adding [-1, 0, 1] to answer list

a: -1, b: 1
freq count Counter({-4: 1, 2: 1, -1: 1, 0: 1})
looking for: 0
evaluating [-1, 0, 1]
already saw: [-1, 0, 1]
```

In second output we identify `[-1, 0, 1]` has already been seen and we ignore adding it to the answer list. This is because the algorithms double backs on tuples of values it's already seen since it's querying against `freqCount` to see if an element exists.

Solution 4 doesn't have this problem.

### Runtime Analysis
The two for loops go through `O(n^2)`. While there is a `newList.sort()` it only ever sorts a constant amount of elements
`O(n^2)`

### Space Analysis
I use  `Counter()` object to store frequency of items
`O(n)` since in the worst case every element is unique and needs a space in the counter

## Solution 4
The most optimal solution. 
Key components are sorted first, then iterated through with two pointers

### Runtime Analysis
All tuples of elements are evaluated once, there are no duplicate evaluations
Whenever evaluating the `i` in the outer loop, all inner loops evaluation sizes get progressively smaller.
There are a few other optimizations in here that skip over duplicate is and `left` and `right` pointers

This follows the pattern of 
`n + (n-1) + (n-2) + ...`
which is known to be `O(n^2)`

### Space Analysis
`O(1)`
No extra space is used
