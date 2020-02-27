# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode('D')
        dummy.next = head
        length = 0
        p = dummy
        while p:
            p = p.next
            length += 1
        steps = 1
        while steps < length:
            tail, cur = dummy, dummy.next
            while cur:
                left = cur
                right = self.split(left, steps)
                cur = self.split(right, steps)
                tail = self.merge(left, right, tail)
            steps <<= 1
        head = dummy.next
        del dummy
        return head

    def split(self, head, n):
        for _ in range(n-1):
            if head:
                head = head.next
            else:
                break
        if not head:
            return None
        second = head.next
        head.next = None
        return second

    def merge(self, left, right, tail):
        dummy = ListNode('d')
        dummy.next = left
        p, p1 = dummy, dummy.next
        p2 = right
        while p1 and p2:
            if p1.val > p2.val:
                p.next = p2
                p2 = p2.next
                p = p.next
                p.next = p1
            else:
                p1 = p1.next
                p = p.next
        p.next = p1 or p2
        while p.next:
            p = p.next
        tail.next = dummy.next
        del dummy
        return p

if __name__ == "__main__":

    node_4 = ListNode(4)
    node_2 = ListNode(2)
    node_1 = ListNode(1)
    node_3 = ListNode(3)
    node_4.next = node_2
    node_2.next = node_1
    node_1.next = node_3
    sol = Solution()
    sol.sortList(node_4)
