# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.sum_number = ''

    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if not root.left and not root.right:
            self.sum_number += str(root.val)
            value = int(self.sum_number)
            self.sum_number = self.sum_number[:-1]
            return value
        else:
            intermittent_val = 0
            self.sum_number += str(root.val)
            intermittent_val += self.sumNumbers(root.left)
            intermittent_val += self.sumNumbers(root.right)
            self.sum_number = self.sum_number[:-1]
            return intermittent_val


if __name__ == "__main__":
    sol = Solution()
    node_1 = TreeNode(1)
    result = sol.sumNumbers(node_1)
    assert result == 1

    sol = Solution()
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_1.left = node_2
    node_1.right = node_3
    result = sol.sumNumbers(node_1)
    assert result == 25

    sol = Solution()
    node_4 = TreeNode(4)
    node_9 = TreeNode(9)
    node_0 = TreeNode(0)
    node_5 = TreeNode(5)
    node_1 = TreeNode(1)
    node_4.left = node_9
    node_4.right = node_0
    node_9.left = node_5
    node_9.right = node_1
    result = sol.sumNumbers(node_4)
    assert result == 1026

    sol = Solution()
    result = sol.sumNumbers(None)
    assert result == 0
