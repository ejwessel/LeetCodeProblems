
class Solution:
    def __init__(self):
        self.solutions = []
        self.nums = None

    def combine(self, n: int, k: int):
        self._combine(n, k, 0, [])

    def _combine(self, n, k, start, sol):
        if len(sol) == k:
            self.solutions.append(sol)
            return

        bound = min(n, n - (k - start - 1))
        for i in range(start, bound):
            # this conditional forces skipping of duplicate elements
            if i != start and self.nums[i] == self.nums[i - 1]:
               continue

            # start 1 after current i
            self._combine(n, k, i + 1, sol + [self.nums[i]])


    def subsetsWithDup(self, nums):
        # by sorting the numbers we can skip over duplicates
        self.nums = sorted(nums)

        # +1 so we can get nCk where k == n
        for k in range(len(nums) + 1):
            self.combine(len(nums), k)
        return self.solutions


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3]
    result = sol.subsetsWithDup(nums)
    assert result == [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

    sol = Solution()
    nums = [1, 2, 2]
    result = sol.subsetsWithDup(nums)
    assert result == [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]

    sol = Solution()
    nums = [1, 2, 2, 2]
    result = sol.subsetsWithDup(nums)
    assert result == [[], [1], [2], [1, 2], [2, 2], [1, 2, 2], [2, 2, 2], [1, 2, 2, 2]]

    sol = Solution()
    nums = [1, 2, 2, 3]
    result = sol.subsetsWithDup(nums)
    print(result)
    assert result == [[], [1], [2], [3], [1, 2], [1, 3], [2, 2], [2, 3], [1, 2, 2], [1, 2, 3], [2, 2, 3], [1, 2, 2, 3]]

    # sol = Solution()
    # nums = [1, 2, 3]
    # result = sol.subsetsWithDup(nums)
    # print(result)
    # assert result == [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    #
    # sol = Solution()
    # nums = [1, 2, 3, 4]
    # result = sol.subsetsWithDup(nums)
    # assert result == [[], [1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]
    #
    # sol = Solution()
    # nums = [0]
    # result = sol.subsetsWithDup(nums)
    # assert result == [[], [0]]
    #
    # sol = Solution()
    # nums = [2, 3, 5]
    # result = sol.subsetsWithDup(nums)
    # assert result == [[], [2], [3], [5], [2, 3], [2, 5], [3, 5], [2, 3, 5]]
    #
    # sol = Solution()
    # nums = [1, 2, 2]
    # result = sol.subsetsWithDup(nums)
    #
    # print(result)
