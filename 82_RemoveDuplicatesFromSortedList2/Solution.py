from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tail = None
        current = head
        while current is not None:
            duplicate_detected = False
            next_node = current.next
            while next_node is not None and next_node.val == current.val:
                duplicate_detected = True
                current.next = next_node.next
                next_node.next = None
                next_node = current.next

            # this case handles if we need to remove the head
            if duplicate_detected and tail is None:
                head = current.next
                current.next = None
                current = head
            elif duplicate_detected:
                after_current = current.next
                tail.next = after_current
                current.next = None
                current = tail

            tail = current
            # can't move current forward if there is nothing to move it to
            if current is not None:
                current = current.next
        return head



def printList(head):
    current = head
    output = []
    while current is not None:
        output.append(current.val)
        current = current.next
    return output

if __name__ == "__main__":
    sol = Solution()

    node_1 = ListNode(1)
    node_2 = ListNode(1)
    node_3 = ListNode(2)
    node_4 = ListNode(2)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    output = printList(node_1)
    print(output)
    head = sol.deleteDuplicates(node_1)
    output = printList(head)
    print()

    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(3)
    node_5 = ListNode(4)
    node_6 = ListNode(4)
    node_7 = ListNode(5)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7
    output = printList(node_1)
    print(output)

    head = sol.deleteDuplicates(node_1)
    output = printList(head)
    print(output)
    assert output == [1, 2, 5]
    print()

    node_1 = ListNode(1)
    node_2 = ListNode(1)
    node_3 = ListNode(1)
    node_4 = ListNode(2)
    node_5 = ListNode(3)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    output = printList(node_1)
    print(output)
    head = sol.deleteDuplicates(node_1)
    output = printList(head)
    print(output)
    assert output == [2, 3]
    print()

    node_1 = ListNode(1)
    node_2 = ListNode(1)
    node_3 = ListNode(1)
    node_1.next = node_2
    node_2.next = node_3
    output = printList(node_1)
    print(output)
    head = sol.deleteDuplicates(node_1)
    output = printList(head)
    print(output)
    assert output == []
    print()

    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(3)
    node_5 = ListNode(3)
    node_6 = ListNode(4)
    node_7 = ListNode(5)
    node_8 = ListNode(5)
    node_9 = ListNode(5)
    node_10 = ListNode(5)
    node_11 = ListNode(5)
    node_12 = ListNode(5)
    node_13 = ListNode(5)
    node_14 = ListNode(5)
    node_15 = ListNode(9)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7
    node_7.next = node_8
    node_8.next = node_9
    node_9.next = node_10
    node_10.next = node_11
    node_11.next = node_12
    node_12.next = node_13
    node_13.next = node_14
    node_14.next = node_15
    output = printList(node_1)
    print(output)

    head = sol.deleteDuplicates(node_1)
    output = printList(head)
    print(output)
    assert output == [1, 2, 4, 9]
    print()

    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(3)
    node_5 = ListNode(3)
    node_6 = ListNode(4)
    node_7 = ListNode(5)
    node_8 = ListNode(5)
    node_9 = ListNode(5)
    node_10 = ListNode(5)
    node_11 = ListNode(5)
    node_12 = ListNode(5)
    node_13 = ListNode(5)
    node_14 = ListNode(5)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7
    node_7.next = node_8
    node_8.next = node_9
    node_9.next = node_10
    node_10.next = node_11
    node_11.next = node_12
    node_12.next = node_13
    node_13.next = node_14
    output = printList(node_1)
    print(output)

    head = sol.deleteDuplicates(node_1)
    output = printList(head)
    print(output)
    assert output == [1, 2, 4]
    print()
