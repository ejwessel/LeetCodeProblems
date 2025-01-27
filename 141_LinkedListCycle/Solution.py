# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycleSet(self, head: ListNode) -> bool:
        seen_set = set()
        current = head
        while current is not None:
            if current in seen_set:
                return True
            seen_set.add(current)
            current = current.next
        return False

    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        single = head
        double = head.next

        while double is not None:
            # iterate double once
            double = double.next
            # check if we've seen single
            if double is single:
                return True
            # iterate double twice
            if double is not None:
                double = double.next

            # check if we've seen single
            if double is single:
                return True

            # move single forward
            single = single.next

        return False

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
    result = sol.hasCycleSet(node_3)
    assert result

    node_3 = ListNode(3)
    node_2 = ListNode(2)
    node_3.next = node_2
    node_2.next = node_3
    result = sol.hasCycleSet(node_3)
    assert result

    result = sol.hasCycleSet(None)
    assert not result

    node_2 = ListNode(2)
    result = sol.hasCycleSet(node_2)
    assert not result

    node_3 = ListNode(3)
    node_2 = ListNode(2)
    node_0 = ListNode(0)
    node_n4 = ListNode(-4)
    node_3.next = node_2
    node_2.next = node_0
    node_0.next = node_n4
    node_n4.next = node_2
    sol = Solution()
    result = sol.hasCycle(node_3)
    assert result

    node_3 = ListNode(3)
    node_2 = ListNode(2)
    node_3.next = node_2
    node_2.next = node_3
    result = sol.hasCycle(node_3)
    assert result

    result = sol.hasCycle(None)
    assert not result

    node_2 = ListNode(2)
    result = sol.hasCycle(node_2)
    assert not result

