from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        # left, root, right
        output = []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        # LEFT
        if left is not []:
            output += left
        # ROOT
        output.append(root.val)
        # RIGHT
        if right is not []:
            output += right
        return output


if __name__ == "__main__":
    sol = Solution()

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_1.right = node_2
    node_2.left = node_3
    output = sol.inorderTraversal(node_1)
    assert output == [1, 3, 2]

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_1.right = node_2
    output = sol.inorderTraversal(node_1)
    assert output == [1, 2]

    node_1 = TreeNode(1)
    output = sol.inorderTraversal(node_1)
    assert output == [1]

    output = sol.inorderTraversal(None)
    assert output == []

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_1.left = node_2
    node_1.right = node_3
    node_3.left = node_4
    node_3.right = node_5
    output = sol.inorderTraversal(node_1)
    assert output == [2, 1, 4, 3, 5]
