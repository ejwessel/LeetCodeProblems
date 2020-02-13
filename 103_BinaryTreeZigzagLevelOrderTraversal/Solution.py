from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.nodes_at_level = []

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self._zigzagLevelOrder(root, 0)
        return self.nodes_at_level

    def _zigzagLevelOrder(self, root: TreeNode, depth: int):
        if root is None:
            return

        # create list for depth if it doesn't exist
        if depth >= len(self.nodes_at_level):
            self.nodes_at_level.insert(depth, [])

        # depending on depth we need to append or prepend
        if depth % 2 == 0:
            self.nodes_at_level[depth].append(root.val)
        else:
            self.nodes_at_level[depth].insert(0, root.val)

        self._zigzagLevelOrder(root.left, depth + 1)
        self._zigzagLevelOrder(root.right, depth + 1)

if __name__ == "__main__":
    sol = Solution()

    node_3 = TreeNode(3)
    node_9 = TreeNode(9)
    node_20 = TreeNode(20)
    node_15 = TreeNode(15)
    node_7 = TreeNode(7)
    node_3.left = node_9
    node_3.right = node_20
    node_20.left = node_15
    node_20.right = node_7
    result = sol.zigzagLevelOrder(node_3)
    assert result == [[3], [20, 9], [15, 7]]

    result = sol.zigzagLevelOrder(None)
    print(result)
