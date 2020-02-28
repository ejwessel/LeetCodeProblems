from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        You may assume no duplicate exists in the array.
        '''
        return self.findMinHelper(nums, (0, len(nums)))

    def findMinHelper(self, nums, range):
        begin, end = range
        # if the range we're at is not sorted then ignore it and continue looking for the non sorted range
        # -1 because range is the upper
        if nums[begin] <= nums[end - 1]:
            return nums[begin]

        # well never reach this section of code if we have a sorted region
        # look for the non sorted region
        split = (begin + end) // 2
        if nums[begin] > nums[split - 1]:
            return self.findMinHelper(nums, (begin, split))
        else:
            return self.findMinHelper(nums, (split, end))


if __name__ == "__main__":
    sol = Solution()

    result = sol.findMin([4, 5, 6, 7, 0, 1, 2])
    assert result == 0

    result = sol.findMin([3, 4, 5, 1, 2])
    assert result == 1

    result = sol.findMin([3, 4, 5, 6, 1, 2])
    assert result == 1

    result = sol.findMin([3, 4, 5, 0, 1, 2])
    assert result == 0

    result = sol.findMin([3, 5, 7, 9, 12, 53, 0, 1])
    assert result == 0

    result = sol.findMin([3])
    assert result == 3

