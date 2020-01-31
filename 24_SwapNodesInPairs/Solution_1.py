# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def printList(self, head):
        current = head
        while current is not None:
            print(current.val)
            current = current.next

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return head
        if head.next is None:
            return head

        tail = None
        current = head
        forward = head.next

        while forward is not None:
            current.next = forward.next
            forward.next = current
            if tail is not None:
                tail.next = forward

            # handle when the head is swapped
            if current == head:
                head = forward

            # move forward
            tail = current
            current = current.next
            if current is not None:
                forward = current.next
            else:
                forward = None

        return head


if __name__ == "__main__":

    sol = Solution()
    new_head = sol.swapPairs(None)
    sol.printList(new_head)

    print("---------")
    node_1 = ListNode("1")
    sol = Solution()
    head = node_1
    new_head = sol.swapPairs(head)
    sol.printList(new_head)

    print("---------")

    node_1 = ListNode("1")
    node_2 = ListNode("2")
    node_3 = ListNode("3")
    node_4 = ListNode("4")
    node_5 = ListNode("5")
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    head = node_1
    sol = Solution()
    new_head = sol.swapPairs(head)
    sol.printList(new_head)

    print("---------")

    node_1 = ListNode("1")
    node_2 = ListNode("2")
    node_3 = ListNode("3")
    node_4 = ListNode("4")
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    head = node_1
    sol = Solution()
    new_head = sol.swapPairs(head)
    sol.printList(new_head)

