class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.ans = []
        self.find_sum(sorted(candidates), target, [])
        return self.ans

    def find_sum(self, candidates, target, used_nums):
        if target == 0:
            self.ans.append(used_nums)
            return
        for i, num in enumerate(candidates):
            if num > target:
                break
            self.find_sum(candidates[i:], target - num, used_nums + [num])
        return

if __name__ == "__main__":

    sol = Solution()
    result = sol.combinationSum([2, 3, 6, 7], 7)
    assert result == [[2, 2, 3], [7]]

    sol = Solution()
    result = sol.combinationSum([2, 3, 5], 8)
    assert result == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    sol = Solution()
    result = sol.combinationSum([2, 3, 5], 1)
    assert result == []

    sol = Solution()
    result = sol.combinationSum([], 19)
    assert result == []