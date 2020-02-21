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

        current = root
        # traverses downward by level
        while current:
            cursor = current
            prev = None
            first_child = None

            # traverses across linked list to the right
            while cursor:
                # if the level is a linked list we should always visit left before right
                if cursor.left:
                    if not prev:
                        prev = cursor.left
                        first_child = prev
                    elif prev:
                        prev.next = cursor.left
                        prev = prev.next

                if cursor.right:
                    if not prev:
                        prev = cursor.right
                        first_child = prev
                    elif prev:
                        prev.next = cursor.right
                        prev = prev.next

                # move linked list over to right
                cursor = cursor.next

            # set the next node to the next available child
            current = first_child
        return root

class Printer:
    def __init__(self):
        self.level_map = {}

    def printLevelOrder(self, node: Node) -> List:
        self.populate_level_map(node, 0)
        output = []
        # go over the levels
        for level in self.level_map.values():
            level_output = []
            current = level
            # ever node is a linked list at a level, populate the values into a an output
            while current is not None:
                level_output.append(current.val)
                current = current.next
            output += level_output
            output += ['#']
        return output

    def populate_level_map(self, node: Node, depth):
        if node is None:
            return

        # only save the first occurrence at the depth,
        # since if it were to be connected entirely, we can traverse the LL
        if depth not in self.level_map:
            self.level_map[depth] = node

        # continue DFS to populate the rest of the map
        self.populate_level_map(node.left, depth + 1)
        self.populate_level_map(node.right, depth + 1)


if __name__ == "__main__":
    sol = Solution()

    node_0 = Node(1)
    node_1 = Node(2)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(3)
    node_5 = Node(3)
    node_6 = Node(3)
    node_7 = Node(4)
    node_8 = Node(4)
    node_9 = Node(4)
    node_10 = Node(4)
    node_11 = Node(4)
    node_12 = Node(4)
    node_15 = Node(5)
    node_16 = Node(5)
    node_0.left = node_1
    node_0.right = node_2
    node_1.left = node_3
    node_1.right = node_4
    node_2.left = node_5
    node_2.right = node_6
    node_3.left = node_7
    node_3.right = node_8
    node_4.left = node_9
    node_4.right = node_10
    node_5.left = node_11
    node_5.right = node_12
    node_7.left = node_15
    node_7.right = node_16
    sol.connect(node_0)
    printer = Printer()
    output = printer.printLevelOrder(node_0)
    assert output == [1, '#', 2, 2, '#', 3, 3, 3, 3, '#', 4, 4, 4, 4, 4, 4, '#', 5, 5, '#']

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
    printer = Printer()
    output = printer.printLevelOrder(node_1)
    assert output == [1, '#', 2, 3, '#', 4, 5, 6, 7, '#', 8, 9, '#']

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
    printer = Printer()
    output = printer.printLevelOrder(node_1)
    assert output == [1, '#', 2, 3, '#', 4, 5, 6, 7, '#']

    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_1.left = node_2
    node_1.right = node_3
    sol.connect(node_1)
    printer = Printer()
    output = printer.printLevelOrder(node_1)
    assert output == [1, '#', 2, 3, '#']

    node_1 = Node(1)
    sol.connect(node_1)
    printer = Printer()
    output = printer.printLevelOrder(node_1)
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
    printer = Printer()
    output = printer.printLevelOrder(node_1)
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
    printer = Printer()
    output = printer.printLevelOrder(node_1)
    assert output == [1, '#', 2, '#', 3, '#', 4, '#', 5, '#']
