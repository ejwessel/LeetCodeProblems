from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        # [1, n + 1] because we go from 1 to n inclusive
        return self.generateTreesHelper(1, n + 1)

    def generateTreesHelper(self, start, end):
        if start >= end:
            return [None]

        subtrees = []
        for i in range(start, end):
            left_subtrees = self.generateTreesHelper(start, i)
            right_subtrees = self.generateTreesHelper(i + 1, end)

            # construct this level tree before passing up
            for left in left_subtrees:
                for right in right_subtrees:
                    new_node = TreeNode(i)
                    new_node.left = left
                    new_node.right = right
                    subtrees.append(new_node)
        return subtrees

def printPreOrderTraversal(node: TreeNode):
    if node is None:
        return [None]
    output = [node.val]
    output += printPreOrderTraversal(node.left)
    output += printPreOrderTraversal(node.right)
    return output

def printResults(trees):
    for tree in trees:
        print(printPreOrderTraversal(tree))

if __name__ == "__main__":
    sol = Solution()
    results = sol.generateTrees(0)

    sol = Solution()
    results = sol.generateTrees(3)
    printResults(results)

    print()

    sol = Solution()
    results = sol.generateTrees(4)
    printResults(results)
