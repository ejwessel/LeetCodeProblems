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


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        '''
        reverses a linked list between the two elements
        1 <= m <= n <= length of list
        :param head: the head of the linked list
        :param m: the number of the element to begin reversing
        :param n: the number of the last element that will be reversed
        :return: the new head
        '''
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
            # handle when current is at head
            if tail is None:
                head = current.next
                current.next = None
                reversed_list.insert(current)
                current = head
            else:
                tail.next = current.next
                current.next = None
                reversed_list.insert(current)
                current = tail.next

            # move count forward
            count += 1

        # relink with reversed list
        if tail is None:
            reversed_list.last_node.next = head
            head = reversed_list.head
        else:
            last_node = tail.next
            tail.next = reversed_list.head
            reversed_list.last_node.next = last_node

        return head


def printLL(head: ListNode):
    output = []
    current = head
    while current is not None:
        output.append(current.val)
        current = current.next
    return output


if __name__ == "__main__":
    # m < n
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
    output = printLL(head)
    assert output == [1, 4, 3, 2, 5]

    # m = n
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
    head = sol.reverseBetween(node_1, 4, 4)
    output = printLL(head)
    assert output == [1, 2, 3, 4, 5]

    # m = n
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
    head = sol.reverseBetween(node_1, 5, 5)
    output = printLL(head)
    assert output == [1, 2, 3, 4, 5]

    # move head
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
    head = sol.reverseBetween(node_1, 1, 3)
    output = printLL(head)
    assert output == [3, 2, 1, 4, 5]

    # move head
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
    head = sol.reverseBetween(node_1, 1, 1)
    output = printLL(head)
    assert output == [1, 2, 3, 4, 5]

    # move head
    node_1 = ListNode(1)
    output = printLL(node_1)
    assert output == [1]
    sol = Solution()
    head = sol.reverseBetween(node_1, 1, 1)
    output = printLL(head)
    assert output == [1]
