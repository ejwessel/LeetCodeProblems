from typing import List
from itertools import permutations

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def insertIntoArrayTree(self, number, list):
        current_index = 0
        while list[current_index] is not None:
            # add to left
            if number < list[current_index]:
                current_index = 2 * current_index + 1
            # add to right
            elif number > list[current_index]:
                current_index = 2 * current_index + 2
        list[current_index] = number

    def generateTupleArray(self, n, permutation):
        list = [None] * (2**n)
        for number in permutation:
            self.insertIntoArrayTree(number, list)
        return tuple(list)

    def createGraph(self, array_representation):
        root = None
        nodes = {}
        # walk through the array representation and reconstruct the graph
        for i in range(len(array_representation)):
            if array_representation[i] is None:
                continue

            node = TreeNode(array_representation[i])
            nodes[i] = node
            if i == 0:
                root = node
            else:
                # it's a left node
                if i % 2 == 1:
                    parent_idx = (i - 1) // 2
                    nodes[parent_idx].left = node
                # it's a right node
                elif i % 2 == 0:
                    parent_idx = (i - 2) // 2
                    nodes[parent_idx].right = node
        return root

    def generateTrees(self, n: int) -> List[TreeNode]:

        if n == 0:
            return []

        numbers = [i for i in range(1, n + 1)]
        perm_list = permutations(numbers)

        # get all the array representations of graphs
        solutions = set()
        for perm in perm_list:
            tuple_array = self.generateTupleArray(n, perm)
            if tuple_array in solutions:
                continue
            solutions.add(tuple_array)

        # create graphs
        results = []
        for sol in solutions:
            new_root = self.createGraph(sol)
            results.append(new_root)
        return results


if __name__ == "__main__":
    sol = Solution()
    results = sol.generateTrees(0)

    sol = Solution()
    results = sol.generateTrees(3)

    sol = Solution()
    results = sol.generateTrees(1)
