# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self._isValidBST(root, (float('-inf'), float('inf')))

    def _isValidBST(self, root: TreeNode, val_range: tuple) -> bool:
        # when we hit a the end
        if root is None:
            return True

        # if we have a value check it as we go down
        if not val_range[0] < root.val < val_range[1]:
            return False

        # lazy evaluate the left and right tree
        return self._isValidBST(root.left, (val_range[0], root.val)) and \
               self._isValidBST(root.right, (root.val, val_range[1]))


if __name__ == "__main__":
    sol = Solution()

    result = sol.isValidBST(None)
    assert result

    node_1 = TreeNode(1)
    result = sol.isValidBST(node_1)
    assert result

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_1.right = node_2
    result = sol.isValidBST(node_1)
    assert result

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_1.left = node_2
    result = sol.isValidBST(node_1)
    assert not result

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_2.left = node_1
    node_2.right = node_3
    result = sol.isValidBST(node_2)
    assert result

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_5.left = node_1
    node_5.right = node_4
    node_4.left = node_3
    node_4.right = node_6
    result = sol.isValidBST(node_5)
    assert not result
