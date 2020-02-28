from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        values = []
        max_product = None
        for i in range(len(nums)):
            running_product = nums[i]
            values.append(running_product)
            if max_product is None:
                max_product = nums[i]
            else:
                max_product = max(max_product, running_product)
            for j in range(i + 1, len(nums)):
                running_product *= nums[j]
                values.append(running_product)
                max_product = max(max_product, running_product)
        values.sort()
        print(values)
        return max_product


if __name__ == "__main__":
    sol = Solution()

    result = sol.maxProduct([2, 3, -2, 4])
    assert result == 6

    result = sol.maxProduct([-2, 0, -1])
    assert result == 0

    result = sol.maxProduct([2, 3, -2, 4, -1])
    assert result == 48
