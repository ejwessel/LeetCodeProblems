class Solution:
    def searchRange(self, nums, target):
        return self._selectRange(0, len(nums) - 1, nums, target)

    def _selectRange(self, i, j, nums, target):
        if i > j:
            return [-1, -1]
        elif not (nums[i] <= target <= nums[j]):
            return [-1, -1]
        elif (i == j) and nums[i] == target:
            return [i, i]
        else:
            split = int((i + j) / 2)

            left_list = self._selectRange(i, split, nums, target)
            right_list = self._selectRange(split + 1, j, nums, target)
            return self.combined_list(left_list, right_list)

    def combined_list(self, left_list, right_list):
        return_list = [None, None]

        # configure left side of list
        if left_list[0] == -1 and right_list[0] > -1:
            return_list[0] = right_list[0]
        elif left_list[0] > -1 and right_list[0] == -1:
            return_list[0] = left_list[0]
        else:
            return_list[0] = min(left_list[0], right_list[0])

        # configure right side of list
        if left_list[1] == -1 and right_list[1] > -1:
            return_list[1] = right_list[1]
        elif left_list[1] > -1 and right_list[1] == -1:
            return_list[1] = left_list[1]
        else:
            return_list[1] = max(left_list[1], right_list[1])

        return return_list


if __name__ == "__main__":
    sol = Solution()

    result = sol.combined_list([-1, -1], [-1, -1])
    assert result == [-1, -1]

    result = sol.combined_list([2, 3], [5, 7])
    assert result == [2, 7]

    result = sol.combined_list([-1, 3], [5, -1])
    assert result == [5, 3]

    result = sol.searchRange([5, 7, 7, 8, 8, 10], 8)
    assert result == [3, 4]

    result = sol.searchRange([5, 7, 7, 8, 8, 10], 6)
    assert result == [-1, -1]

    result = sol.searchRange([], 6)
    assert result == [-1, -1]

    result = sol.searchRange([-10, -8, -5, -3, 0, 1, 3, 6, 9, 11], 6)
    assert result == [7, 7]
