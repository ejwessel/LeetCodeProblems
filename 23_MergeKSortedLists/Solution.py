from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # head and tail of linked list
        answer_list_head = None
        answer_list_tail = None

        # while there are lists to search through
        while lists:
            min_head = (None, None)
            # loop through heads of lists looking for the min
            for i in range(len(lists)):
                if min_head[1] is None:
                    min_head = (i, lists[i])
                elif min_head[1] is not None and lists[i].val < min_head[1].val:
                    min_head = (i, lists[i])

            # capture node_to_add if there is one
            if min_head[1] is not None:
                node_to_add = min_head[1]
                lists[min_head[0]] = node_to_add.next
                node_to_add.next = None

            # remove empty list from lists
            if lists[min_head[0]] is None:
                lists.pop(min_head[0])

            # nothing to add continue
            if min_head[1] is None:
                continue

            # append to answer list
            if answer_list_head is None:
                answer_list_head = node_to_add
                answer_list_tail = node_to_add
            else:
                answer_list_tail.next = node_to_add
                answer_list_tail = answer_list_tail.next

        return answer_list_head


def print_linked_list(head: ListNode):
    output = []
    current = head
    while current:
        output.append(current.val)
        current = current.next
    return output

if __name__ == "__main__":
    sol = Solution()
    node1_2 = ListNode(2)
    node1_3 = ListNode(5)
    linked_lists = [node1_2, None, node1_3]
    result = sol.mergeKLists(linked_lists)
    output = print_linked_list(result)
    assert output == [2, 5]

    node1_3 = ListNode(5)
    linked_lists = [None, node1_3]
    result = sol.mergeKLists(linked_lists)
    output = print_linked_list(result)
    assert output == [5]

    linked_lists = [None, None]
    result = sol.mergeKLists(linked_lists)
    output = print_linked_list(result)
    assert output == []

    linked_lists = [None]
    result = sol.mergeKLists(linked_lists)
    output = print_linked_list(result)
    assert output == []

    node1_1 = ListNode(1)
    node1_2 = ListNode(4)
    node1_3 = ListNode(5)
    node1_1.next = node1_2
    node1_2.next = node1_3
    output = print_linked_list(node1_1)
    assert output == [1, 4, 5]

    node2_1 = ListNode(1)
    node2_2 = ListNode(3)
    node2_3 = ListNode(4)
    node2_1.next = node2_2
    node2_2.next = node2_3
    output = print_linked_list(node2_1)
    assert output == [1, 3, 4]

    node3_1 = ListNode(2)
    node3_2 = ListNode(6)
    node3_1.next = node3_2
    output = print_linked_list(node3_1)
    assert output == [2, 6]

    linked_lists = [node1_1, node2_1, node3_1]
    result = sol.mergeKLists(linked_lists)
    output = print_linked_list(result)
    assert output == [1, 1, 2, 3, 4, 4, 5, 6]

    node3_1 = ListNode(2)
    node3_2 = ListNode(6)
    linked_lists = [node3_1, node3_2]
    result = sol.mergeKLists(linked_lists)
    output = print_linked_list(result)
    assert output == [2, 6]
