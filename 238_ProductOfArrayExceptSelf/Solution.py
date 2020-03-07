from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                product *= nums[j]
            output.append(product)
        return output

if __name__ == "__main__":
    sol = Solution()
    output = sol.productExceptSelf([1, 2, 3, 4])
    assert output == [24, 12, 8, 6]

    output = sol.productExceptSelf([5, 3, 1, 4])
    assert output == [12, 20, 60, 15]
