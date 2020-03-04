# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        new_root, left_node = self.upsideDownBinaryTreeHelper(root)
        return new_root

    def upsideDownBinaryTreeHelper(self, root: TreeNode):
        if not root.left and not root.right:
            return (root, root)

        new_root, left_node = self.upsideDownBinaryTreeHelper(root.left)
        left_node.right = root
        left_node.left = root.right
        root.left = None
        root.right = None
        return (new_root, root)

def preOrderTraversal(root: TreeNode):
    if root is None:
        return []
    left_output = preOrderTraversal(root.left)
    right_output = preOrderTraversal(root.right)
    return [root.val] + left_output + right_output

if __name__ == "__main__":
    sol = Solution()

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_2.right = node_5
    output = preOrderTraversal(node_1)
    assert output == [1, 2, 4, 5, 3]
    result = sol.upsideDownBinaryTree(node_1)
    output = preOrderTraversal(result)
    assert output == [4, 5, 2, 3, 1]

    result = sol.upsideDownBinaryTree(None)
    output = preOrderTraversal(result)
    assert output == []

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_7 = TreeNode(7)
    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_2.right = node_5
    node_4.left = node_6
    node_4.right = node_7
    output = preOrderTraversal(node_1)
    assert output == [1, 2, 4, 6, 7, 5, 3]
    result = sol.upsideDownBinaryTree(node_1)
    output = preOrderTraversal(result)
    assert output == [6, 7, 4, 5, 2, 3, 1]
