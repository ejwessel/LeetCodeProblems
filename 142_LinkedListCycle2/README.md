## Linked List Cycle 2

I had trouble with implementing this problem with O(1) space. It had to do with the tediousness of the pointers and when they should overlap.

I originally identified it in the linked cycle 1 problem, but that was a premature identification of the overlap. 
My first solution would check every time the fast pointer moved if it ran into the slow pointer. This was very fast, but breaks the consistency of movement forward.

Instead the pointers need to remain consistent with their movements and only when those movements overlap can we solve the problem. This is because when they do overlap they are now a certain distance apart.
That distance allows us to iterate the respective pointers individually until they meet

Runtime: O(n) / O(n + k)
- run through all elements once
- k is the cycle length

Space: O(n) / O(1)
- set uses n space to store seen nodes
- no additional space is used