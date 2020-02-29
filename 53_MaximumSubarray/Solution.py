from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = float('-inf')
        running_max = 0
        for num in nums:
            running_max += num
            running_max = max(running_max, num)
            max_val = max(max_val, running_max)
        return max_val

    def maxSubArray_inoptimal(self, nums: List[int]) -> int:
        max_val = float('-inf')
        for i in range(len(nums)):
            running_val = nums[i]
            max_val = max(max_val, running_val)
            for j in range(i + 1, len(nums)):
                running_val += nums[j]
                max_val = max(max_val, running_val)
        return max_val



if __name__ == "__main__":
    sol = Solution()
    result = sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    assert result == 6

    result = sol.maxSubArray_inoptimal([4, 2, -1, 9])
    assert result == 14

    result = sol.maxSubArray_inoptimal([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    assert result == 6

    result = sol.maxSubArray([4, 2, -1, 9])
    assert result == 14

