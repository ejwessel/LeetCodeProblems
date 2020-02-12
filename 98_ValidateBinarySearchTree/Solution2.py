from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 0 node, 1 left bound, 2 right bound
        stack = deque()
        stack.append((root, float('-inf'), float('inf')))

        while len(stack) > 0:
            current_root = stack.pop()
            if current_root[0] is None:
                continue

            # handle bounds
            if not current_root[1] < current_root[0].val < current_root[2]:
                return False

            right_node = current_root[0].right
            left_node = current_root[0].left
            stack.append((right_node, current_root[0].val, current_root[2]))
            stack.append((left_node, current_root[1], current_root[0].val))

        return True


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
