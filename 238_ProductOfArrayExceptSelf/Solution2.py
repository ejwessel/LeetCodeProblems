from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left_right_product will be used to keep track of left products
        # left most product is initially 1
        left_right_product = [1]
        # start 1 from the left since left most product is 1
        for i in range(1, len(nums)):
            # since we're excluding the current num, capture previous num and previous product
            left_right_product.append(nums[i - 1] * left_right_product[i - 1])

        # r starts at 1 since we'll be making our way from right to left
        r = 1
        for i in reversed(range(len(nums))):
            # product from right to left will be prior product by current product
            left_right_product[i] = r * left_right_product[i]
            r *= nums[i]

        return left_right_product


if __name__ == "__main__":
    sol = Solution()
    output = sol.productExceptSelf([5, 3, 1, 4])
    assert output == [12, 20, 60, 15]

    output = sol.productExceptSelf([1, 2, 3, 4])
    assert output == [24, 12, 8, 6]

