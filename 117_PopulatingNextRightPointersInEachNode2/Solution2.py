from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        # traverse only down to the left
        current = root
        while current is not None:
            if not root.left and not root.right:
                current = current.next
                continue

            # traverse through the linked list to the right
            list_cursor = current
            prev = None
            while list_cursor is not None:

                # link children
                if list_cursor.left:
                    list_cursor.left.next = list_cursor.right

                # set prev is not set, set it to whatever we can find
                if prev is None:
                    if list_cursor.right:
                        prev = list_cursor.right
                    elif list_cursor.left:
                        prev = list_cursor.left
                else:
                    if list_cursor.left:
                        prev.next = list_cursor.left
                        prev = prev.next
                    elif list_cursor.right:
                        prev.next = list_cursor.right
                        prev = prev.next

                list_cursor = list_cursor.next

            current = current.left
        return root


def printLevelOrder(node: Node) -> List:
    # only traverse left side
    if node is None:
        return []

    output = []
    current = node
    while current is not None:
        output.append(current.val)
        current = current.next

    if node.left:
        level_below_output = printLevelOrder(node.left)
    else:
        level_below_output = printLevelOrder(node.right)
    output += ['#']
    output += level_below_output
    return output


if __name__ == "__main__":
    sol = Solution()

    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(6)
    node_7 = Node(7)
    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_2.right = node_5
    node_3.left = node_6
    node_3.right = node_7

    sol.connect(node_1)
    output = printLevelOrder(node_1)
    assert output == [1, '#', 2, 3, '#', 4, 5, 6, 7, '#']

    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_1.left = node_2
    node_1.right = node_3
    sol.connect(node_1)
    output = printLevelOrder(node_1)
    assert output == [1, '#', 2, 3, '#']

    node_1 = Node(1)
    sol.connect(node_1)
    output = printLevelOrder(node_1)
    assert output == [1, '#']

    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(6)
    node_7 = Node(7)
    node_8 = Node(8)
    node_9 = Node(9)
    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_2.right = node_5
    node_3.left = node_6
    node_3.right = node_7
    node_4.left = node_8
    node_7.right = node_9

    sol.connect(node_1)
    output = printLevelOrder(node_1)
    assert output == [1, '#', 2, 3, '#', 4, 5, 6, 7, '#', 8, 9, '#']

    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(6)
    node_7 = Node(7)
    node_8 = Node(8)
    node_9 = Node(9)
    node_10 = Node(10)
    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_2.right = node_5
    node_3.left = node_6
    node_3.right = node_7
    node_4.left = node_8
    node_4.right = node_9
    node_7.right = node_10

    sol.connect(node_1)
    output = printLevelOrder(node_1)
    assert output == [1, '#', 2, 3, '#', 4, 5, 6, 7, '#', 8, 9, 10, '#']

    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_1.right = node_2
    node_2.right = node_3
    node_3.right = node_4
    node_4.right = node_5

    sol.connect(node_1)
    output = printLevelOrder(node_1)
    assert output == [1, '#', 2, '#', 3, '#', 4, '#', 5, '#']
