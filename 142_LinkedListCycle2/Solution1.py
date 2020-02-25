# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
            # move slow forward
            slow = slow.next
            # check if we've seen slow
            if fast is slow:
                break

        if fast is None:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

if __name__ == "__main__":
    node_a = ListNode('A')
    node_b = ListNode('B')
    node_c = ListNode('C')
    node_d = ListNode('D')
    node_e = ListNode('E')
    node_a.next = node_b
    node_b.next = node_c
    node_c.next = node_d
    node_d.next = node_e
    node_e.next = node_a
    sol = Solution()
    result = sol.detectCycle(node_a)
    assert result == node_a


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
