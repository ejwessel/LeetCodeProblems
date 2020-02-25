# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        seen_set = set()
        current = head
        while current is not None:
            if current in seen_set:
                return current
            seen_set.add(current)
            current = current.next

if __name__ == "__main__":
    node_3 = ListNode(3)
    node_2 = ListNode(2)
    node_0 = ListNode(0)
    node_n4 = ListNode(-4)
    node_3.next = node_2
    node_2.next = node_0
    node_0.next = node_n4
    node_n4.next = node_2
    sol = Solution()
    result = sol.detectCycle(node_3)
    assert result == node_2

    node_3 = ListNode(3)
    node_2 = ListNode(2)
    node_3.next = node_2
    node_2.next = node_3
    result = sol.detectCycle(node_3)
    assert result == node_3

    result = sol.detectCycle(None)
    assert not result

    node_2 = ListNode(2)
    result = sol.detectCycle(node_2)
    assert not result
