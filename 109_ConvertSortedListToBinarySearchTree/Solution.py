from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.list_representation = None

    def _linkedlist_to_list(self, head: ListNode) -> List[ListNode]:
        list_representation = []
        current = head
        while current is not None:
            list_representation.append(current)
            current = current.next
        return list_representation

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        self.list_representation = self._linkedlist_to_list(head)
        return self._list_to_graph((0, len(self.list_representation)))

    def _list_to_graph(self, range_val):
        if range_val[0] >= range_val[1]:
            return None

        mid = (range_val[0] + range_val[1]) // 2
        root = TreeNode(self.list_representation[mid].val)

        left_range = (range_val[0], mid)
        right_range = (mid + 1, range_val[1])

        left_node = self._list_to_graph(left_range)
        right_node = self._list_to_graph(right_range)

        root.left = left_node
        root.right = right_node
        return root

def print_inorder_traversal(root: TreeNode):
    if root is None:
        return []
    output = []
    left_output = print_inorder_traversal(root.left)
    output += left_output
    output += [root.val]
    right_output = print_inorder_traversal(root.right)
    output += right_output
    return output


if __name__ == "__main__":
    sol = Solution()

    node_1 = ListNode(-10)
    node_2 = ListNode(-8)
    node_3 = ListNode(-5)
    node_4 = ListNode(-3)
    node_5 = ListNode(-1)
    node_6 = ListNode(0)
    node_7 = ListNode(2)
    node_8 = ListNode(4)
    node_9 = ListNode(8)
    node_10 = ListNode(12)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7
    node_7.next = node_8
    node_8.next = node_9
    node_9.next = node_10
    result = sol.sortedListToBST(node_1)
    output = print_inorder_traversal(result)
    assert output == [-10, -8, -5, -3, -1, 0, 2, 4, 8, 12]

    node_1 = ListNode(-10)
    node_2 = ListNode(-8)
    node_3 = ListNode(-5)
    node_4 = ListNode(-3)
    node_5 = ListNode(-1)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    result = sol.sortedListToBST(node_1)
    output = print_inorder_traversal(result)
    assert output == [-10, -8, -5, -3, -1]

    node_1 = ListNode(-10)
    result = sol.sortedListToBST(node_1)
    output = print_inorder_traversal(result)
    assert output == [-10]

    output = print_inorder_traversal(None)
    assert output == []
