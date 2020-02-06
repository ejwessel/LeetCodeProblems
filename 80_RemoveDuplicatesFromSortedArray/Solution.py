from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0  # current index of element we're looking at
        b = 0  # current index of element we're going to overwrite
        count = 1  # count to keep track of how many of an element we've seen

        while i < len(nums):
            if i == 0:
                # we're at the beginning
                nums[b] == nums[i]
                b += 1
            elif nums[i - 1] != nums[i]:
                # new element is identified
                nums[b] = nums[i]
                b += 1
                count = 1
            elif nums[i - 1] == nums[i]:
                # duplicate element identified
                count += 1
                if count <= 2:
                    # condition to write when there are duplicates
                    nums[b] = nums[i]
                    b += 1
            # every iteration increases i
            i += 1
        return b


if __name__ == "__main__":
    sol = Solution()

    nums = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3]
    result = sol.removeDuplicates(nums)
    print(nums)
    print(result)
    assert result == 8

    nums = [0, 0, 1, 1, 1, 1, 2, 2, 2, 3]
    result = sol.removeDuplicates(nums)
    print(nums)
    print(result)
    assert result == 7

    nums = [1, 1, 1, 2, 2, 3]
    result = sol.removeDuplicates(nums)
    print(nums)
    print(result)
    assert result == 5

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    result = sol.removeDuplicates(nums)
    print(nums)
    print(result)
    assert result == 7

    nums = [0, 0, 0, 0, 0, 0]
    result = sol.removeDuplicates(nums)
    print(nums)
    print(result)
    assert result == 2

