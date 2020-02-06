from typing import List


class Solution:
    def removeDuplicates_1(self, nums: List[int]) -> int:
        i = 0
        e = len(nums) - 1
        c = 1
        prev_c = None
        while i < e:
            if nums[i] == nums[i + 1]:
                c += 1
                if c == 3:
                    nums[i + 1], nums[e] = nums[e], nums[i + 1]
                    e -= 1
                    c -= 1
                    if nums[i + 1] > nums[i + 2] and i + 1 is not e:
                        nums[i + 1], nums[i + 2] = nums[i + 2], nums[i + 1]
                else:
                    i += 1
            elif nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                i -= 1
                c = prev_c
            elif nums[i] < nums[i + 1]:
                prev_c = c
                c = 1
                i += 1
        return e + 1


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

