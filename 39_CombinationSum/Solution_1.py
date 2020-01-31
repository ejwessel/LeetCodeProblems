class Solution:

    def __init__(self):
        self.result = []
        self.seen_set = set()

    def combinationSum(self, candidates, target):
        for num in candidates:
            # skip over numbers that are too large
            if num > target:
                continue
            self.find_combination([num], candidates, target)
        return self.result

    def find_combination(self, used_nums, candidates, target):
        sum = 0
        for used_num in used_nums:
            sum += used_num

        if sum > target:
            return
        elif sum == target:
            used_nums.sort()
            used_num_tuple = tuple(used_nums)
            if used_num_tuple not in self.seen_set:
                self.result.append(used_nums)
                self.seen_set.add(used_num_tuple)

        for num in candidates:
            self.find_combination(used_nums + [num], candidates, target)


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

    sol = Solution()
    result = sol.combinationSum([7, 3, 9, 6], 6)
    assert result == [[3,3],[6]]

