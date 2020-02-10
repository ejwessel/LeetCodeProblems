from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        seen = set()
        seen.add(None)  # add none so it can be ignored
        output = []
        while len(stack) > 0:
            current_node = stack.pop()
            # if dead end continue
            if current_node is None:
                continue
            # visit the left if it hasn't been seen yet
            elif current_node.left not in seen:
                # we re-add the current node so we know what the next node is when we come back from left
                stack.append(current_node)
                stack.append(current_node.left)
            # if the left has been visited we can visit the right
            elif current_node.left in seen:
                seen.add(current_node)
                output.append(current_node.val)
                stack.append(current_node.right)
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
