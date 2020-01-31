from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_access_end = [False] * len(nums)

        for i in reversed(range(len(nums))):
            # for when we start at the end
            if i == len(nums) - 1:
                can_access_end[i] = True
            else:
                can_access = False

                # limit how many elements we need to look over
                limit = min(i + nums[i] + 1, len(nums))

                # start 1 after current index
                for k in range(i + 1, limit):
                    if can_access_end[k]:
                        can_access_end[i] = True
                        break

        # answer will be at the front
        return can_access_end[0]


if __name__ == "__main__":
    sol = Solution()

    nums = []
    result =

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
