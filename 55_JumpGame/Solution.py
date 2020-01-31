from typing import List


class Solution:
    def canJump_inoptimal(self, nums: List[int]) -> bool:
        can_access_end = list(bytearray(len(nums)))

        for i in reversed(range(len(nums))):
            # for when we start at the end
            if i == len(nums) - 1:
                can_access_end[i] = 1
            else:
                sub_list = can_access_end[i: min(i + nums[i] + 1, len(nums))]
                output = int(''.join(map(str, sub_list)), 2)
                # alternative way
                #output = sum(c << i for i, c in enumerate(sub_list))
                if output > 0:
                    can_access_end[i] = 1

        # answer will be at the front
        return can_access_end[0]

    def canJump(self, nums: List[int]) -> bool:
        # keep track of last best index to avoid scanning
        last_best_idx = len(nums) - 1
        # work our way backwards
        for i in reversed(range(len(nums))):
            # >= to last best index then we're good
            if i + nums[i] >= last_best_idx:
                last_best_idx = i

        return last_best_idx == 0


if __name__ == "__main__":
    sol = Solution()

    nums = [1]
    result = sol.canJump_inoptimal(nums)
    assert result

    nums = [2, 3, 1, 1, 4]
    result = sol.canJump_inoptimal(nums)
    assert result

    nums = [3, 2, 1, 0, 4]
    result = sol.canJump_inoptimal(nums)
    assert not result

    nums = [9, 9, 9, 9, 1]
    result = sol.canJump_inoptimal(nums)
    assert result

    nums = [9, 0, 0, 0, 1]
    result = sol.canJump_inoptimal(nums)
    assert result

    nums = [0, 9, 9, 9, 1]
    result = sol.canJump_inoptimal(nums)
    assert not result

    nums = [1, 2, 0, 1]
    result = sol.canJump_inoptimal(nums)
    assert result

    nums = [1, 1, 0, 1]
    result = sol.canJump_inoptimal(nums)
    assert not result

    nums = [1]
    result = sol.canJump(nums)
    assert result

    nums = [2, 3, 1, 1, 4]
    result = sol.canJump(nums)
    assert result

    nums = [3, 2, 1, 0, 4]
    result = sol.canJump(nums)
    assert not result

    nums = [9, 9, 9, 9, 1]
    result = sol.canJump(nums)
    assert result

    nums = [9, 0, 0, 0, 1]
    result = sol.canJump(nums)
    assert result

    nums = [0, 9, 9, 9, 1]
    result = sol.canJump(nums)
    assert not result

    nums = [1, 2, 0, 1]
    result = sol.canJump(nums)
    assert result

    nums = [1, 1, 0, 1]
    result = sol.canJump(nums)
    assert not result
