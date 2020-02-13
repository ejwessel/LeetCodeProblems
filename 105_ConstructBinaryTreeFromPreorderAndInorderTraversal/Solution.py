from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.preorder = None
        self.inorder = None
        self.pre_idx = None

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.preorder = preorder
        self.inorder = inorder
        self.pre_idx = 0

        return self._buildOrder((0, len(inorder)))

    def _buildOrder(self, node_range):
        if node_range[0] >= node_range[1]:
            return None

        root = TreeNode(self.preorder[self.pre_idx])

        # identify root pivot
        pivot = self.inorder.index(root.val)

        # move pre_idx forward
        self.pre_idx += 1

        left_range = (node_range[0], pivot)
        right_range = (pivot + 1, node_range[1])

        left_root = self._buildOrder(left_range)
        right_root = self._buildOrder(right_range)

        root.left = left_root
        root.right = right_root

        return root


def printInOrderTraversal(root: TreeNode) -> List[int]:
    if root is None:
        return []

    output = []
    left_output = printInOrderTraversal(root.left)
    output += left_output
    output += [root.val]
    right_output = printInOrderTraversal(root.right)
    output += right_output
    return output


def printPreOrderTraversal(root: TreeNode) -> List[int]:
    if root is None:
        return []

    output = [root.val]
    left_output = printPreOrderTraversal(root.left)
    output += left_output
    right_output = printPreOrderTraversal(root.right)
    output += right_output
    return output


if __name__ == "__main__":
    sol = Solution()

    inorder = []
    preorder = []
    root = sol.buildTree(preorder, inorder)
    output = printInOrderTraversal(root)
    assert output == inorder
    output = printPreOrderTraversal(root)
    assert output == preorder

    inorder = [9]
    preorder = [9]
    root = sol.buildTree(preorder, inorder)
    output = printInOrderTraversal(root)
    assert output == inorder
    output = printPreOrderTraversal(root)
    assert output == preorder

    inorder = [2, 9, 5, 6, 4, 3, 15, 11, 20, 7]
    preorder = [3, 9, 2, 6, 5, 4, 20, 15, 11, 7]
    root = sol.buildTree(preorder, inorder)
    output = printInOrderTraversal(root)
    assert output == inorder
    output = printPreOrderTraversal(root)
    assert output == preorder

    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = sol.buildTree(preorder, inorder)
    output = printInOrderTraversal(root)
    assert output == inorder
    output = printPreOrderTraversal(root)
    assert output == preorder

    preorder = [3, 20, 7]
    inorder = [3, 20, 7]
    root = sol.buildTree(preorder, inorder)
    output = printInOrderTraversal(root)
    assert output == inorder
    output = printPreOrderTraversal(root)
    assert output == preorder
