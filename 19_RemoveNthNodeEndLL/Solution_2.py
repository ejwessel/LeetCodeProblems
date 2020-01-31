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

        index_to_node = {}
        current_idx = 0
        current_node = head
        while current_node != None:
            index_to_node[current_idx] = current_node
            current_node = current_node.next
            current_idx += 1

        if n > len(index_to_node.keys()):
            return head

        idx_to_remove = len(index_to_node.keys()) - n

        # actual removal of the node
        if idx_to_remove == 0:
            head = head.next
        else:
            index_to_node[idx_to_remove].next = None

            before_idx = idx_to_remove - 1
            after_idx = idx_to_remove + 1

            if after_idx >= len(index_to_node.keys()):
                index_to_node[before_idx].next = None
            else:
                index_to_node[before_idx].next = index_to_node[after_idx]

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

    head = solution.removeNthFromEnd(a_node, 100)
    solution.print_list(head)

    head = solution.removeNthFromEnd(head, 0)
    solution.print_list(head)

    head = solution.removeNthFromEnd(head, 2)
    solution.print_list(head)

    head = solution.removeNthFromEnd(head, 4)
    solution.print_list(head)

    head = solution.removeNthFromEnd(head, 1)
    solution.print_list(head)

    head = solution.removeNthFromEnd(head, 1)
    solution.print_list(head)

    head = solution.removeNthFromEnd(head, 1)
    solution.print_list(head)

    assert head == None
