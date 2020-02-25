# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node_list = []
        current = head
        # add all nodes to list
        while current is not None:
            node_list.append(current)
            current = current.next

        for i in range(len(node_list) // 2):
            # if node_list[i] is not node_list[len(node_list) - 1 - i]:
            node_list[i].next = node_list[len(node_list) - 1 - i]

            # if node_list[len(node_list) - 1 - i] is not node_list[i + 1]:
            node_list[len(node_list) - 1 - i].next = node_list[i + 1]

def printLLOrder(head: ListNode):
    output = []
    current = head
    while current is not None:
        output.append(current.val)
        current = current.next
    return output

if __name__ == "__main__":
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    node_6 = ListNode(6)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    output = printLLOrder(node_1)
    print(output)
    sol = Solution()
    sol.reorderList(node_1)
    # output = printLLOrder(node_1)
    # print(output)

    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    node_6 = ListNode(6)
    node_7 = ListNode(7)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7
    output = printLLOrder(node_1)
    print(output)
