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

        end_pointer = head
        for i in range(n):
            end_pointer = end_pointer.next
            # this conditon properly ensures that end_pointer is at the correct spot
            if (i + 1) == n and end_pointer is None:
                break
            # condition checks if the end_pointer has reached the end before I could place it in the right spot
            # this means that the list is shorter than n and therefore n cannot be removed
            if end_pointer is None:
                return head

        current_node = head
        prev_node = None

        # as the end_pointer is moved through the list current node and prev node are moved in tandem
        while end_pointer is not None:
            end_pointer = end_pointer.next
            prev_node = current_node
            current_node = current_node.next

        # actual removal of the node
        if prev_node is None:
            head = head.next
        else:
            prev_node.next = current_node.next
            current_node.next = None

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

    print("remove nothing")
    head = solution.removeNthFromEnd(a_node, 100)
    solution.print_list(head)

    print("remove nothing")
    head = solution.removeNthFromEnd(head, 0)
    solution.print_list(head)

    print("remove D")
    head = solution.removeNthFromEnd(head, 2)
    solution.print_list(head)

    print("remove A")
    head = solution.removeNthFromEnd(head, 4)
    solution.print_list(head)

    print("Remove E")
    head = solution.removeNthFromEnd(head, 1)
    solution.print_list(head)

    print("Remove C")
    head = solution.removeNthFromEnd(head, 1)
    solution.print_list(head)

    print("Remove nothing")
    head = solution.removeNthFromEnd(head, 1)
    solution.print_list(head)

    # assert head == None
