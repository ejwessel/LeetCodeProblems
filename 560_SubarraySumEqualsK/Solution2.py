from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_count = 0
        for i in range(len(nums)):
            # considered current element is a value
            if nums[i] == k:
                sum_count += 1
            running_sum = nums[i]
            # start 1 after
            for j in range(i + 1, len(nums)):
                running_sum += nums[j]
                # check if we have a sum
                if running_sum == k:
                    sum_count += 1
        return sum_count


if __name__ == "__main__":
    sol = Solution()

    result = sol.subarraySum([0], 0)
    assert result == 1

    result = sol.subarraySum([1], 1)
    assert result == 1

    result = sol.subarraySum([2, 3, -2, -2, 4, 1, 2], 5)
    assert result == 4

    result = sol.subarraySum([1, 1, 1], 2)
    assert result == 2

    result = sol.subarraySum([1, 2, 1, 2, 1], 3)
    assert result == 4

