# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        second_head = None

        while head is not None:
            eval = head
            head = head.next
            eval.next = None

            if second_head is None:
                second_head = eval
                continue

            tail = None
            current = second_head
            while current is not None:
                if eval.val > current.val:
                    tail = current
                    current = current.next
                else:
                    if tail is None:
                        eval.next = current
                        second_head = eval
                        break
                    else:
                        tail.next = eval
                        eval.next = current
                        break

            if current is None:
                tail.next = eval
        return second_head

def outputlist(head: ListNode):
    output = []
    current = head
    while current:
        output.append(current.val)
        current = current.next
    return output

if __name__ == "__main__":
    sol = Solution()

    node_1 = ListNode(1)
    node_3 = ListNode(3)
    node_2 = ListNode(2)
    node_4 = ListNode(4)
    node_6 = ListNode(6)
    node_5 = ListNode(5)
    node_1.next = node_3
    node_3.next = node_2
    node_2.next = node_4
    node_4.next = node_6
    node_6.next = node_5
    new_head = sol.insertionSortList(node_1)
    output = outputlist(new_head)
    assert output == [1, 2, 3, 4, 5, 6]

    new_head = sol.insertionSortList(None)
    output = outputlist(new_head)
    assert output == []

    node_1 = ListNode(1)
    node_3 = ListNode(3)
    node_2 = ListNode(2)
    node_4 = ListNode(4)
    node_6 = ListNode(6)
    node_5 = ListNode(5)
    node_3.next = node_2
    node_2.next = node_4
    node_4.next = node_6
    node_6.next = node_5
    node_5.next = node_1
    new_head = sol.insertionSortList(node_3)
    output = outputlist(new_head)
    assert output == [1, 2, 3, 4, 5, 6]
