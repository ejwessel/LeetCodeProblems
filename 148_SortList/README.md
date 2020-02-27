## Sort List

This problem is extremely difficult.
A lot of individuals online use recursion. This is incorrect.

- You cannot use recursion.
- You cannot use an external array or data structure

In fact under the constraints O(nlogn) runtime and O(1) space. I do not think this problem is realistically possible.
This is because if the solution is to use an in place merge sort then it is O(n(logn)^2)
This would violate the constraints

I believe this would be possible if the node was also a graph node. In which case we could use heapsort to sort this by rearrancing the list as a tree and then reordering as a list.

I cannot do this however given the current problem because wrapping nodes would result in additional space

The solution saved is not my solution, but one I took from leetcode because

Runtime: O(n(logn)^2)

Runtime: O(1)
