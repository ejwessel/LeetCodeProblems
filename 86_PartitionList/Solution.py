# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_list(head: ListNode):
    output = []
    current = head
    while current is not None:
        output.append(current.val)
        current = current.next
    return output

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        if head is None:
            return None
        elif head.next is None:
            return head

        tail = None
        current = head
        stop = None  # where the current will stop
        last_node = None  # only used for appending

        # identify last node to append to
        while current is not None:
            last_node = current
            current = current.next

        current = head
        stop = last_node

        while current is not stop:
            if tail is None and current.val >= x:
                # if we need to move the head
                head = current.next
                last_node.next = current
                current.next = None
                last_node = current
                current = head
            elif current.val >= x:
                # we need to move elements inside
                tail.next = current.next
                last_node.next = current
                current.next = None
                last_node = current
                current = tail.next
            else:
                tail = current
                current = current.next

        #handle stop_node
        if tail is None and current.val >= x:
            # if we need to move the head
            head = current.next
            last_node.next = current
            current.next = None
        elif current.next is not None and current.val >= x:
            # we need to move elements inside
            tail.next = current.next
            last_node.next = current
            current.next = None

        return head


if __name__ == "__main__":
    sol = Solution()

    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_1.next = node_2
    output = print_list(node_1)
    print(output)
    head = sol.partition(node_1, 2)
    output = print_list(head)
    print(output)
    print()
    assert output == [1, 2]

    node_1 = ListNode(3)
    output = print_list(node_1)
    print(output)
    head = sol.partition(node_1, 3)
    output = print_list(head)
    print(output)
    print()
    assert output == [3]

    node_1 = ListNode(3)
    output = print_list(node_1)
    print(output)
    head = sol.partition(node_1, 2)
    output = print_list(head)
    print(output)
    print()
    assert output == [3]

    node_1 = ListNode(1)
    node_2 = ListNode(4)
    node_3 = ListNode(3)
    node_4 = ListNode(2)
    node_5 = ListNode(5)
    node_6 = ListNode(2)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    output = print_list(node_1)
    print(output)
    head = sol.partition(node_1, 3)
    output = print_list(head)
    print(output)
    print()
    assert output == [1, 2, 2, 4, 3, 5]

    node_1 = ListNode(3)
    node_2 = ListNode(2)
    node_3 = ListNode(5)
    node_4 = ListNode(2)
    node_5 = ListNode(1)
    node_6 = ListNode(4)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    output = print_list(node_1)
    print(output)
    head = sol.partition(node_1, 3)
    output = print_list(head)
    print(output)
    print()
    assert output == [2, 2, 1, 3, 5, 4]

    node_1 = ListNode(3)
    node_2 = ListNode(2)
    node_1.next = node_2
    output = print_list(node_1)
    print(output)
    head = sol.partition(node_1, 3)
    output = print_list(head)
    print(output)
    print()
    assert output == [2, 3]

