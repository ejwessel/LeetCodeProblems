from typing import List


class Solution:
    def __init__(self):
        self.solutions = []
        self.nums = None

    def combine(self, n: int, k: int):
        # +1 to n because we start counting at 1 and so the upper range needs to be 1 higher
        # 1 to start because we start counting at 1
        self._combine(n + 1, k, 1, [])

    def _combine(self, n: int, k: int, start: int, sol: List) -> List[List[int]]:
        if len(sol) == k:
            self.solutions.append(sol)
        else:
            # the bound is computed to optimize the upper bound
            bound = min(n, n - (k - start))
            # in of bound and n so that we don't go over n
            for i in range(start, bound):
                self._combine(n, k, i + 1, sol + [self.nums[i - 1]])

    def subsets(self, nums):
        self.nums = nums
        for k in range(len(nums) + 1):
            self.combine(len(nums), k)
        return self.solutions


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3]
    result = sol.subsets(nums)
    assert result == [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

    sol = Solution()
    nums = [1, 2, 3, 4]
    result = sol.subsets(nums)
    assert result == [[], [1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]

    sol = Solution()
    nums = [0]
    result = sol.subsets(nums)
    assert result == [[], [0]]

    sol = Solution()
    nums = [2, 3, 5]
    result = sol.subsets(nums)

