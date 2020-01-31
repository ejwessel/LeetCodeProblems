## Runtime Analysis:

If n is the number of characters

I look at every character once
O(n)

After placing characters into their respective buckets, I append the buckets to one bucket
O(n)

I then join all elements in the one bucket into one string
O(n)

O(3n) => O(n)

## Space Analysis:
I use a map. The map is an interger to list mapping. It will use as much space as there are characters in the given string
O(n)
