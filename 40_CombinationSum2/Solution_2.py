class Solution:

    def __init__(self):
        self.result = []
        self.seen_set = set()

    def combinationSum2(self, candidates, target):
        self.combinationSum(sorted(candidates), target, tuple())
        return self.result

    def combinationSum(self, candidates, target, used_nums):
        if target == 0:
            if used_nums not in self.seen_set:
                self.result.append(list(used_nums))
                self.seen_set.add(used_nums)
        else:
            for i, num in enumerate(candidates):
                if num > target:
                    break
                # i + 1 since we're splitting the list with the remaining elements
                self.combinationSum(candidates[i + 1:], target - num, used_nums + (num,))


if __name__ == "__main__":
    sol = Solution()
    result = sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    assert result == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

    sol = Solution()
    result = sol.combinationSum2([2, 5, 2, 1, 2], 5)
    assert result == [[1, 2, 2], [5]]

    sol = Solution()
    result = sol.combinationSum2([1, 2], 4)
    assert result == []
