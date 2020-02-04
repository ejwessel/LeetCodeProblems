from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                temp = nums[i]
                nums[i] = nums[left]
                nums[left] = temp
                i += 1
                left += 1
            elif nums[i] == 2:
                temp = nums[i]
                nums[i] = nums[right]
                nums[right] = temp
                right -= 1
            else:
                i += 1


if __name__ == "__main__":
    sol = Solution()

    nums = [2, 0, 2, 1, 1, 0]
    sol.sortColors(nums)
    print(nums)

    nums = [2, 1, 2, 0, 1, 0]
    sol.sortColors(nums)
    print(nums)

    nums = [2, 2, 2, 1, 1, 0]
    sol.sortColors(nums)
    print(nums)
