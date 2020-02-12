
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        # [1, n + 1] because we go from 1 to n inclusive
        return self.numTreesHelper(1, n + 1)

    def numTreesHelper(self, start, end):
        if start >= end:
            return 1

        tree_count = 0
        for i in range(start, end):
            left_subtree_count = self.numTreesHelper(start, i)
            right_subtree_count = self.numTreesHelper(i + 1, end)

            if left_subtree_count > 0 and right_subtree_count > 0:
                tree_count += left_subtree_count * right_subtree_count
            elif right_subtree_count == 0:
                tree_count += left_subtree_count
            elif left_subtree_count == 0:
                tree_count += right_subtree_count
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
