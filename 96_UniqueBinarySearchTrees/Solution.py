class Solution:

    def __init__(self):
        self.range_cache = {}

    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        # [1, n + 1] because we go from 1 to n inclusive
        return self.numTreesHelper(1, n + 1)

    def numTreesHelper(self, start, end):
        if start >= end:
            return 1

        diff = end - start
        if diff in self.range_cache:
            return self.range_cache[diff]

        tree_count = 0
        for i in range(start, end):
            left_subtree_count = self.numTreesHelper(start, i)
            right_subtree_count = self.numTreesHelper(i + 1, end)
            tree_count += left_subtree_count * right_subtree_count
        self.range_cache[diff] = tree_count
        return tree_count


if __name__ == "__main__":
    sol = Solution()
    result = sol.numTrees(0)
    assert result == 0

    sol = Solution()
    result = sol.numTrees(3)
    assert result == 5

    sol = Solution()
    result = sol.numTrees(4)
    assert result == 14

    sol = Solution()
    result = sol.numTrees(5)
    assert result == 42
