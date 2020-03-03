from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.findPeakElementHelper(nums, 0, len(nums))

    def findPeakElementHelper(self, nums, begin, end):
        # bounds crossed, no solution
        if begin >= end:
            return None

        pivot = (begin + end) // 2
        # if we've found a peak
        if self.checkIsPeak(nums, pivot):
            return pivot

        # visit 1 to pivot
        left_peak = self.findPeakElementHelper(nums, begin, pivot)
        if left_peak is not None:
            return left_peak

        # visit 1 after the pivot
        right_peak = self.findPeakElementHelper(nums, pivot + 1, end)
        if right_peak is not None:
            return right_peak

        return None

    def checkIsPeak(self, nums, index):
        if len(nums) == 1:
            return True
        elif index == 0:
            return nums[index] > nums[index + 1]
        elif index == len(nums) - 1:
            return nums[-1] > nums[-2]
        else:
            return nums[index - 1] < nums[index] > nums[index + 1]


if __name__ == "__main__":
    sol = Solution()

    nums = [1, 2, 1, 3, 5, 6, 4]
    result = sol.checkIsPeak(nums, 1)
    assert result
    result = sol.checkIsPeak(nums, 0)
    assert not result
    result = sol.checkIsPeak(nums, len(nums) - 1)
    assert not result

    nums = [9, 1]
    peak = sol.findPeakElement(nums)
    assert peak == 0

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    peak = sol.findPeakElement(nums)
    assert peak == 8

    nums = [1, 2, 1, 3, 5, 6, 4]
    peak = sol.findPeakElement(nums)
    assert peak == 1

    nums = [5]
    peak = sol.findPeakElement(nums)
    assert peak == 0

    nums = [1, 9]
    peak = sol.findPeakElement(nums)
    assert peak == 1

    nums = [1, 2, 3, 4, 5, 6, 7, 9, 8]
    peak = sol.findPeakElement(nums)
    assert peak == 7

