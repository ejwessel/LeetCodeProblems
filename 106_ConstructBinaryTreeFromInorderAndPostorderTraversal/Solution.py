from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.inorder = None
        self.postorder = None
        self.post_idx = None

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.inorder = inorder
        self.postorder = postorder
        self.post_idx = len(postorder) - 1

        return self._buildTree((0, len(inorder)))

    def _buildTree(self, range_val):
        if range_val[1] <= range_val[0]:
            return None

        root = TreeNode(self.postorder[self.post_idx])

        pivot = self.inorder.index(root.val)

        right_range = (pivot + 1, range_val[1])
        left_range = (range_val[0], pivot)

        self.post_idx -= 1
        right_root = self._buildTree(right_range)
        left_root = self._buildTree(left_range)

        root.right = right_root
        root.left = left_root

        return root

def printInorderTraversal(root: TreeNode) -> List[int]:
    if root is None:
        return []

    output = []
    left_output = printInorderTraversal(root.left)
    output += left_output
    output += [root.val]
    right_output = printInorderTraversal(root.right)
    output += right_output
    return output

def printPostorderTraversal(root: TreeNode) -> List[int]:
    if root is None:
        return []

    output = []
    left_output = printPostorderTraversal(root.left)
    output += left_output
    right_output = printPostorderTraversal(root.right)
    output += right_output
    output += [root.val]
    return output


if __name__ == "__main__":
    sol = Solution()

    inorder = []
    postorder = []
    result = sol.buildTree(inorder, postorder)
    output = printInorderTraversal(result)
    assert output == inorder
    output = printPostorderTraversal(result)
    assert output == postorder

    inorder = [9]
    postorder = [9]
    result = sol.buildTree(inorder, postorder)
    output = printInorderTraversal(result)
    assert output == inorder
    output = printPostorderTraversal(result)
    assert output == postorder

    inorder = [2, 9, 5, 6, 4, 3, 15, 11, 20, 7]
    postorder = [2, 5, 4, 6, 9, 11, 15, 7, 20, 3]
    result = sol.buildTree(inorder, postorder)
    output = printInorderTraversal(result)
    assert output == inorder
    output = printPostorderTraversal(result)
    assert output == postorder

    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    result = sol.buildTree(inorder, postorder)
    output = printInorderTraversal(result)
    assert output == inorder
    output = printPostorderTraversal(result)
    assert output == postorder
