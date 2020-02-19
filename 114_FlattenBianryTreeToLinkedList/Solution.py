# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        self._flatten(root)

    def _flatten(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        left_end = self._flatten(root.left)
        right_end = self._flatten(root.right)

        # if there is a left, link it to the right
        if left_end is not None:
            left_end.right = root.right

        # link left to right and clear out  left
        if root.left is not None:
            root.right = root.left
            root.left = None

        # if there is a right end, return it
        if right_end is not None:
            return right_end
        # in the event there is no right end, we need left end
        elif left_end is not None:
            return left_end
        # in the event there is no left or right, return just the node
        return root

class Solution2:
    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return None

        stack = [root]

        while len(stack):
            current = stack.pop()
            # will not append 'None' nodes
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

            current.left = None

            # this is the trick:
            # this works because we add right then left
            # right is the next element we want as the right
            # because the stack will visit the right element after the left tree, we can access it and link it
            if len(stack) > 0:
                current.right = stack[-1]
            else:
                current.right = None

def printInOrder(node: TreeNode):
    if node is None:
        return []

    output = []
    left_output = printInOrder(node.left)
    output += left_output

    output.append(node.val)

    right_output = printInOrder(node.right)
    output += right_output
    return output


if __name__ == "__main__":
    sol = Solution()

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_1.left = node_2
    node_2.left = node_3
    node_3.left = node_4
    output = printInOrder(node_1)
    sol.flatten(node_1)
    output = printInOrder(node_1)
    assert output == [1, 2, 3, 4]


    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_1.left = node_2
    node_1.right = node_5
    node_2.left = node_3
    node_2.right = node_4
    node_5.right = node_6
    sol.flatten(node_1)
    output = printInOrder(node_1)
    assert output == [1, 2, 3, 4, 5, 6]

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_7 = TreeNode(7)
    node_8 = TreeNode(8)
    node_9 = TreeNode(9)
    node_10 = TreeNode(10)
    node_11 = TreeNode(11)
    node_12 = TreeNode(12)
    node_1.left = node_2
    node_1.right = node_7
    node_2.left = node_3
    node_2.right = node_6
    node_3.left = node_4
    node_3.right = node_5
    node_7.left = node_8
    node_7.right = node_11
    node_8.left = node_9
    node_8.right = node_10
    node_11.right = node_12
    sol.flatten(node_1)
    output = printInOrder(node_1)
    assert output == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    sol.flatten(node_1)
    output = printInOrder(node_1)
    assert output == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    node_1 = TreeNode(1)
    sol.flatten(node_1)
    output = printInOrder(node_1)
    assert output == [1]

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_7 = TreeNode(7)
    node_8 = TreeNode(8)
    node_9 = TreeNode(9)
    node_10 = TreeNode(10)
    node_11 = TreeNode(11)
    node_12 = TreeNode(12)
    node_1.left = node_2
    node_2.left = node_3
    node_3.left = node_4
    node_4.left = node_5
    node_5.left = node_6
    node_6.left = node_7
    node_7.left = node_8
    node_8.left = node_9
    node_9.left = node_10
    node_10.left = node_11
    node_11.left = node_12
    output = printInOrder(node_1)
    sol.flatten(node_1)
    output = printInOrder(node_1)
    assert output == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    sol = Solution2()

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_1.left = node_2
    node_2.left = node_3
    node_3.left = node_4
    output = printInOrder(node_1)
    sol.flatten(node_1)
    output = printInOrder(node_1)
    assert output == [1, 2, 3, 4]


    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_1.left = node_2
    node_1.right = node_5
    node_2.left = node_3
    node_2.right = node_4
    node_5.right = node_6
    sol.flatten(node_1)
    output = printInOrder(node_1)
    assert output == [1, 2, 3, 4, 5, 6]

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_7 = TreeNode(7)
    node_8 = TreeNode(8)
    node_9 = TreeNode(9)
    node_10 = TreeNode(10)
    node_11 = TreeNode(11)
    node_12 = TreeNode(12)
    node_1.left = node_2
    node_1.right = node_7
    node_2.left = node_3
    node_2.right = node_6
    node_3.left = node_4
    node_3.right = node_5
    node_7.left = node_8
    node_7.right = node_11
    node_8.left = node_9
    node_8.right = node_10
    node_11.right = node_12
    sol.flatten(node_1)
    output = printInOrder(node_1)
    assert output == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    sol.flatten(node_1)
    output = printInOrder(node_1)
    assert output == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    node_1 = TreeNode(1)
    sol.flatten(node_1)
    output = printInOrder(node_1)
    assert output == [1]

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_7 = TreeNode(7)
    node_8 = TreeNode(8)
    node_9 = TreeNode(9)
    node_10 = TreeNode(10)
    node_11 = TreeNode(11)
    node_12 = TreeNode(12)
    node_1.left = node_2
    node_2.left = node_3
    node_3.left = node_4
    node_4.left = node_5
    node_5.left = node_6
    node_6.left = node_7
    node_7.left = node_8
    node_8.left = node_9
    node_9.left = node_10
    node_10.left = node_11
    node_11.left = node_12
    output = printInOrder(node_1)
    sol.flatten(node_1)
    output = printInOrder(node_1)
    assert output == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    output = printInOrder(None)
    assert output == []

