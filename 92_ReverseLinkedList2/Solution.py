from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class ReverseLinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def insert(self, new_node: ListNode):
        if self.head is None:
            self.head = new_node
            self.last_node = new_node
        else:
            new_node.next = self.head
            self.head = new_node

def printLL(head: ListNode):
    output = []
    current = head
    while current is not None:
       output.append(current.val)
       current = current.next
    return output


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        reversed_list = ReverseLinkedList()
        count = 1
        tail = None
        current = head

        # get into position
        while count != m:
            tail = current
            current = current.next
            count += 1

        # reverse insert all in between elements
        while count != (n + 1):
            tail.next = current.next
            current.next = None
            reversed_list.insert(current)
            current = tail.next
            count += 1

        # relink with reversed list
        last_node = tail.next
        tail.next = reversed_list.head
        reversed_list.last_node.next = last_node

        return head

if __name__ == "__main__":
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    output = printLL(node_1)
    assert output == [1, 2, 3, 4, 5]
    sol = Solution()
    head = sol.reverseBetween(node_1, 2, 4)
    output = printLL(node_1)
    assert output == [1, 4, 3, 2, 5]

