from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def connect(self, root: Node) -> Node:
        if root is None:
            return None

        stack = [root]

        while len(stack):
            current = stack.pop()

            if current is None:
                continue

            # if we're at a leaf continue
            if not current.left and not current.right:
                continue

            # link children
            current.left.next = current.right

            # bridge gap
            if current.next:
                current.right.next = current.next.left

            stack.append(current.right)
            stack.append(current.left)

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

    level_below_output = printLevelOrder(node.left)
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
    sol.connect(node_1)
    output = printLevelOrder(node_1)
    assert output == [1, '#']

    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_1.left = node_2
    node_1.right = node_3
    sol.connect(node_1)
    output = printLevelOrder(node_1)
    assert output == [1, '#', 2, 3, '#']

    node_1 = Node(1)
    node_1.left = None
    node_1.right = None
    sol.connect(node_1)
    output = printLevelOrder(node_1)
    assert output == [1, '#']
