class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == "__main__":
    sol = Solution().twoSum([2, 7, 11, 15], 9)
    assert sol == [0, 1]

    sol = Solution().twoSum([3, 2, 4], 6)
    assert sol == [1, 2]
