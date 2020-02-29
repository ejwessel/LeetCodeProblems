## Sqrt(x)

there is a pattern to the numbers 

len: val
                                      
1, 2, 3,                                
3: 1

4, 5, 6, 7, 8,                          
5: 2

9, 10, 11, 12, 13, 14, 15,              
7: 3 

16, 17, 18, 19, 20, 21, 22, 23, 24,     
9: 4

the previous len + 2 is the next val


Runtime: O(n)
- the number length increases by 2, while the values increase by 1 every time
- The range of numbers increases at a much faster rate than the count, but still linearly

Space: O(1)
- no extra space is used

This can probably be represented as a summation or sequence
