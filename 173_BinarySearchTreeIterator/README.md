## Binary Search Tree Iterator

I had a bit of initial difficulty with this problem. It wasn't due to me not understanding what was needed of the problem, but it's representation in code and how to properly traverse the list the way it was wanted.

I started with the usage of a stack and keeping the previous element on top so that I could reference it before traversing down the right tree. This worked, but it looked a lot more complicated in code than it needed to be.

I later improved my solution and it improved the runtime

Runtime: O(n)
- all nodes need to be visited

Space: O(n)
- the tree is not balanced and all nodes can be represented in the stack