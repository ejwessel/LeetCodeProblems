from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.solutions = []

    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        self._pathSum(root, target, [])
        return self.solutions

    def _pathSum(self, root, target, num_list):
        if root is None:
            return
        if root.left is None and root.right is None:
            if sum(num_list) + root.val == target:
                self.solutions.append(num_list + [root.val])
        else:
            self._pathSum(root.left, target, num_list + [root.val])
            self._pathSum(root.right, target, num_list + [root.val])


class Solution2:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        output = []
        paths = self._pathSum(root)
        for path in paths:
            if sum(path) == target:
                output.append(path)
        return output

    def _pathSum(self, root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]

        output = []

        left_path = self._pathSum(root.left)
        if left_path is not None:
            for path in left_path:
                output.append([root.val] + path)

        right_path = self._pathSum(root.right)
        if right_path is not None:
            for path in right_path:
                output.append([root.val] + path)

        return output


if __name__ == "__main__":

    node_1 = TreeNode(5)
    node_2 = TreeNode(4)
    node_3 = TreeNode(8)
    node_4 = TreeNode(11)
    node_5 = TreeNode(13)
    node_6 = TreeNode(4)
    node_7 = TreeNode(7)
    node_8 = TreeNode(2)
    node_9 = TreeNode(5)
    node_10 = TreeNode(1)
    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_3.left = node_5
    node_3.right = node_6
    node_4.left = node_7
    node_4.right = node_8
    node_6.left = node_9
    node_6.right = node_10

    sol = Solution()
    result = sol.pathSum(node_1, 22)
    assert result == [[5, 4, 11, 2], [5, 8, 4, 5]]

    sol = Solution()
    result = sol.pathSum(node_1, 26)
    assert result == [[5, 8, 13]]

    sol = Solution()
    result = sol.pathSum(node_1, 100)
    assert result == []

    node_1 = TreeNode(5)
    sol = Solution()
    result = sol.pathSum(node_1, 5)
    assert result == [[5]]

    # =========================

    node_1 = TreeNode(5)
    node_2 = TreeNode(4)
    node_3 = TreeNode(8)
    node_4 = TreeNode(11)
    node_5 = TreeNode(13)
    node_6 = TreeNode(4)
    node_7 = TreeNode(7)
    node_8 = TreeNode(2)
    node_9 = TreeNode(5)
    node_10 = TreeNode(1)
    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_3.left = node_5
    node_3.right = node_6
    node_4.left = node_7
    node_4.right = node_8
    node_6.left = node_9
    node_6.right = node_10

    sol = Solution2()
    result = sol.pathSum(node_1, 22)
    assert result == [[5, 4, 11, 2], [5, 8, 4, 5]]

    sol = Solution2()
    result = sol.pathSum(node_1, 26)
    assert result == [[5, 8, 13]]

    sol = Solution2()
    result = sol.pathSum(node_1, 100)
    assert result == []

    node_1 = TreeNode(5)
    sol = Solution2()
    result = sol.pathSum(node_1, 5)
    assert result == [[5]]

    sol = Solution2()
    result = sol.pathSum(None, 5)
    assert result == []
