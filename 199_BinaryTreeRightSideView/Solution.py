from typing import List
from collections import defaultdict
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.depth_map = defaultdict(list)

    def rightSideView(self, root: TreeNode) -> List[int]:
        self.rightSideViewHelper(root, 0)
        return self.identifyRightView()

    def rightSideViewHelper(self, root: TreeNode, depth: int):
        if root is None:
            return
        self.depth_map[depth].append(root.val)
        self.rightSideViewHelper(root.right, depth + 1)
        self.rightSideViewHelper(root.left, depth + 1)

    def identifyRightView(self):
        output = []
        for i in range(len(self.depth_map.keys())):
            output.append(self.depth_map[i][0])
        return output

if __name__ == "__main__":
    sol = Solution()
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_1.left = node_2
    node_1.right = node_3
    node_2.right = node_5
    node_3.right = node_4
    output = sol.rightSideView(node_1)
    assert output == [1, 3, 4]

    sol = Solution()
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
    node_13 = TreeNode(13)
    node_1.left = node_2
    node_1.right = node_3
    node_2.right = node_4
    node_3.left = node_5
    node_3.right = node_6
    node_4.right = node_7
    node_6.left = node_8
    node_7.left = node_9
    node_7.right = node_10
    node_9.left = node_11
    node_12.left = node_13
    output = sol.rightSideView(node_1)
    assert output == [1, 3, 6, 8, 10, 11]

    sol = Solution()
    output = sol.rightSideView(None)
    assert output == []
