from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        You may assume no duplicate exists in the array.
        '''
        begin = 0
        end = len(nums)
        while nums[begin] > nums[end - 1]:
            split = (begin + end) // 2
            if nums[begin] > nums[split - 1]:
                end = split
            else:
                begin = split
        return nums[begin]


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

