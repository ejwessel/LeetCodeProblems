# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def treeToDoublyList(self, root: Node) -> Node:
        left, right = self.treeToDoublyListHelper(root)
        # handle if given a null value and the left right are still null
        if left is not None:
            # make circular
            left.left = right
            right.right = left
            # left is the head
        return left

    def treeToDoublyListHelper(self, root: Node) -> (Node, Node):
        if root is None:
            return None, None

        l_left, l_right = self.treeToDoublyListHelper(root.left)
        r_left, r_right = self.treeToDoublyListHelper(root.right)

        # link root to left and right
        if l_right is not None:
            l_right.right = root
            root.left = l_right
        elif l_left is not None:
            l_left.right = root
            root.left = l_left

        if r_left is not None:
            r_left.left = root
            root.right = r_left
        elif r_right is not None:
            r_right.left = root
            root.right = r_right

        # handle return val
        left_answer = l_left
        if left_answer is None:
            left_answer = root

        right_answer = r_right
        if right_answer is None:
            right_answer = root

        return left_answer, right_answer


def linkedListOutput(head: Node):
    output = []
    current = head
    seen = set()
    while current is not None and current not in seen:
        seen.add(current)
        output.append(current.val)
        current = current.right
    return output


if __name__ == "__main__":
    node_a = Node('A')
    node_b = Node('B')
    node_c = Node('C')
    node_d = Node('D')
    node_a.right = node_b
    node_b.right = node_c
    node_c.right = node_d
    output = linkedListOutput(node_a)
    assert output == ['A', 'B', 'C', 'D']

    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(6)
    node_7 = Node(7)
    node_8 = Node(8)
    node_9 = Node(9)
    node_5.left = node_3
    node_5.right = node_7
    node_3.left = node_2
    node_3.right = node_4
    node_2.left = node_1
    node_7.left = node_6
    node_7.right = node_8
    node_8.right = node_9
    sol = Solution()
    head = sol.treeToDoublyList(node_5)
    output = linkedListOutput(head)
    assert output == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    node_4 = Node(4)
    node_2 = Node(2)
    node_5 = Node(5)
    node_1 = Node(1)
    node_3 = Node(3)

    node_4.left = node_2
    node_4.right = node_5
    node_2.left = node_1
    node_2.right = node_3

    sol = Solution()
    head = sol.treeToDoublyList(node_4)
    output = linkedListOutput(head)
    assert output == [1, 2, 3, 4, 5]

    sol = Solution()
    head = sol.treeToDoublyList(None)
    output = linkedListOutput(head)
    assert output == []

    sol = Solution()
    node_1 = Node(1)
    head = sol.treeToDoublyList(node_1)
    output = linkedListOutput(head)
    assert output == [1]

