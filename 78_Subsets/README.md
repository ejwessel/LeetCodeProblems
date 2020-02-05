## Subsets

Runtime: O(n*2^n)
- every combination can be represented as O(2^n), this needs to happen n times

Space: O(2^n)
- this is exactly how many solutions exist for a given number of elements

I wasn't able to identify the runtime and space complexity of this problem without difficulty. 

I believed it's runtime was n * the combination's runtime. Technically this is correct, but can be further reduced 
to a much tighter bound

I believed it's space was n * the combinations space. Technically this is kind of correct, but also can be better
bounded. Turns out the exact amount of elements you get follows a binomial representation and therefore can be exactly determined.
