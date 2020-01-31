# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def print_list(self, head):
        current_node = head
        while current_node != None:
            print(current_node.val)
            current_node = current_node.next
        print()

    def getListSize(self, head):
        list_size = 0
        current_node = head
        while (current_node != None):
            list_size += 1
            current_node = current_node.next

        return list_size

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if head is None:
            return head
        if n == 0:
            return head

        size = self.getListSize(head)
        if n > size:
            return head

        tail_node = None
        current_node = head
        idx_to_stop = size - n
        for i in range(size):
            # break out of the loop if we have the node we want to remove
            if i == idx_to_stop:
                break

            # move the pointers forward
            tail_node = current_node
            current_node = current_node.next

        # remove the node
        if tail_node is None:
            head = head.next
        else:
            tail_node.next = current_node.next
            current_node.next = None

        # return the head
        return head


if __name__ == "__main__":
    a_node = ListNode("A")
    b_node = ListNode("B")
    c_node = ListNode("C")
    d_node = ListNode("D")
    e_node = ListNode("E")
    a_node.next = b_node
    b_node.next = c_node
    c_node.next = d_node
    d_node.next = e_node
    solution = Solution()

    listSize = solution.getListSize(a_node)
    assert listSize == 5

    listSize = solution.getListSize(d_node)
    assert listSize == 2

    listSize = solution.getListSize(e_node)
    assert listSize == 1


    head = solution.removeNthFromEnd(a_node, 100)
    solution.print_list(head)
    assert head == a_node

    head = solution.removeNthFromEnd(a_node, 0)
    solution.print_list(head)
    assert head == a_node

    head = solution.removeNthFromEnd(a_node, 2)
    assert solution.getListSize(head) == 4
    # should check that the list is the correct list
    solution.print_list(head)

    head = solution.removeNthFromEnd(a_node, 1)
    assert solution.getListSize(head) == 3
    # should check that the list is the correct list
    solution.print_list(head)

    size = solution.getListSize(head)
    head = solution.removeNthFromEnd(a_node, size)
    assert solution.getListSize(head) == 2
    # should check that the list is the correct list
    solution.print_list(head)

    size = solution.getListSize(head)
    head = solution.removeNthFromEnd(head, size)
    assert solution.getListSize(head) == 1
    # should check that the list is the correct list
    solution.print_list(head)

    size = solution.getListSize(head)
    head = solution.removeNthFromEnd(head, size)
    assert solution.getListSize(head) == 0
    # should check that the list is the correct list
    solution.print_list(head)

    size = solution.getListSize(head)
    solution.print_list(head)
    head = solution.removeNthFromEnd(head, size)
    # should check that the list is the correct list
    assert solution.getListSize(head) == 0
    solution.print_list(head)
