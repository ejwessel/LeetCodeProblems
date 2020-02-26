from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal_tuple(self, root: TreeNode) -> List[int]:
        output = []
        stack = [(root, 'left')]

        while stack:
            current, dir = stack.pop()
            if not current:
                continue
            if dir == 'left':
                output.append(current.val)
                stack.append((current, 'right'))
                stack.append((current.left, 'left'))
            else:
                stack.append((current.right, 'left'))
        return output

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        output = []
        while stack:
            current = stack.pop()
            if not current:
                continue
            output.append(current.val)
            stack.append(current.right)
            stack.append(current.left)
        return output

if __name__ == "__main__":
    sol = Solution()

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_1.right = node_2
    node_2.left = node_3
    output = sol.preorderTraversal(node_1)
    assert output == [1, 2, 3]

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_1.right = node_2
    node_2.left = node_3
    node_2.right = node_4
    node_4.right = node_5
    output = sol.preorderTraversal(node_1)
    assert output == [1, 2, 3, 4, 5]

    output = sol.preorderTraversal(None)
    assert output == []
