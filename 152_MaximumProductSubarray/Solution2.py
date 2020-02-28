from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        running_max_product = nums[0]
        running_min_product = nums[0]

        for i in range(1, len(nums)):
            candidates = (nums[i], running_max_product * nums[i], running_min_product * nums[i])
            running_max_product = max(candidates)
            running_min_product = min(candidates)
            max_product = max(max_product, running_max_product)

        return max_product

if __name__ == "__main__":
    sol = Solution()

    result = sol.maxProduct([2, 3, -2, 4])
    assert result == 6

    result = sol.maxProduct([-2, 0, -1])
    assert result == 0

    result = sol.maxProduct([2, 3, -2, 4, -1])
    assert result == 48
