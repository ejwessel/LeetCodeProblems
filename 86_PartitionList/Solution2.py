# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, new_node: ListNode):
        if self.head is None:
            self.head = new_node
            self.last_node = new_node
        else:
            self.last_node.next = new_node
            self.last_node = self.last_node.next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        right_partition = LinkedList()
        current = head
        tail = None

        while current is not None:
            # need to move head
            if tail is None and current.val >= x:
                head = current.next
                current.next = None
                right_partition.append(current)
                current = head
            # need to move elements inside
            elif current.val >= x:
                next_node = current.next
                tail.next = next_node
                current.next = None
                right_partition.append(current)
                current = tail.next
            # skip over elements
            else:
                tail = current
                current = current.next

        # we moved through a list, tail is at the very last element
        if tail is not None:
            tail.next = right_partition.head
        # 1 element is left in the list and it's head
        elif tail is None and head is not None:
            head.next = right_partition.head
        # there are no elements left in the left partition
        elif tail is None and head is None:
            head = right_partition.head

        return head


def print_list(head: ListNode):
    output = []
    current = head
    while current is not None:
        output.append(current.val)
        current = current.next
    return output

if __name__ == "__main__":
    sol = Solution()

    node_1 = ListNode(3)
    output = print_list(node_1)
    print(output)
    head = sol.partition(node_1, 3)
    output = print_list(head)
    print(output)
    print()
    assert output == [3]

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

    node_1 = ListNode(3)
    node_2 = ListNode(3)
    node_1.next = node_2
    output = print_list(node_1)
    print(output)
    head = sol.partition(node_1, 3)
    output = print_list(head)
    print(output)
    print()
    assert output == [3, 3]

    node_1 = ListNode(3)
    node_2 = ListNode(1)
    node_1.next = node_2
    output = print_list(node_1)
    print(output)
    head = sol.partition(node_1, 3)
    output = print_list(head)
    print(output)
    print()
    assert output == [1, 3]
