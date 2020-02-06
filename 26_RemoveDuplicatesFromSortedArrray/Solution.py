from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0   # the index of the element we're currently looking at
        b = 0   # the index of the element we're going to overwrite
        while i < len(nums):
            if i == 0:
                # if we're at the beginning the move b forward
                b += 1
            elif nums[i - 1] != nums[i]:
                # if not the same as previous then we're good to replace
                nums[b] = nums[i]
                b += 1
            # always increase i
            i += 1
        return b


if __name__ == "__main__":
    sol = Solution()

    input = [1, 1, 2]
    result = sol.removeDuplicates(input)
    assert result == 2

    input = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result = sol.removeDuplicates(input)
    assert result == 5

    input = [0, 0, 0, 0, 0, 0, 0]
    result = sol.removeDuplicates(input)
    assert result == 1
