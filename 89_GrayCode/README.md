## GrayCode

This problem is interesting for the reason of how one can think about it.

It can be thought of as a graph problem or a sequence generation problem.
There are lot of interesting properties about this, but the easiest way to approach this problem is as the following:

You can generate any sequence of numbers by doubling the list, reversing the second half, prepending 0 to the first half, and prepending 1 to the second half

example:

0 is a unique case

n = 0
```
[0]
```

n = 1
```
[]
[ , ]
[0, 1]  ------------------------------------------------> #n=1
```

n = 2
```
[]
[ , ]
[0, 1]  ------------------------------------------------> #n=1
[0, 1] + [1, 0]
[00, 01] + [11, 10]
[00, 01, 11, 10] ---------------------------------------> #n=2
```

n = 3
```
[]
[ , ]
[0, 1]  ------------------------------------------------> #n=1
[0, 1] + [1, 0]
[00, 01] + [11, 10]
[00, 01, 11, 10] ---------------------------------------> #n=2
[00, 01, 11, 10] + [10, 11, 01, 00]
[000, 001, 011, 010] + [110, 111, 101, 100]
[000, 001, 011, 010, 110, 111, 101, 100] ---------------> #n=3
```

Runtime: O(2^n)
- the total number of elements that need to be generated are O(2^n)

Space: O(2^n)
- the total number of elements that need to be generated and returned are O(2^n)
