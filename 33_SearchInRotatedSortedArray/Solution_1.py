class Solution:
    def search(self, nums, target):
        pass

        # sorted array
        # rotated around a point
        # no duplicates in the array
        # runtime must be O(log n) - no linear search
        # return index of target, otherwise return -1

        # The base idea is that you still do a binary search,
        # but you need to be selective of picked side

        return self._search(0, len(nums) - 1, nums, target)

    def _search(self, i, j, nums, target):

        # boundaries overlap
        if i > j:
            return -1
        # we're looking at 1 element
        if i == j:
            #check if element is target
            if target != nums[i]:
                return -1
            else:
                return i
        else:
            split = int((i + j) / 2)
            result_left = self._search(i, split, nums, target)
            result_right = self._search(split + 1, j, nums, target)

            if result_left > result_right:
                return result_left

            # implicit else
            return result_right

if __name__ == "__main__":
    sol = Solution()

    result = sol.search([4, 5, 6, 7, 0, 1, 2], 0)
    assert result == 4

    result = sol.search([4, 5, 6, 7, 0, 1, 2], 3)
    assert result == -1

    result = sol.search([4], 3)
    assert result == -1

    result = sol.search([3], 3)
    assert result == 0

    result = sol.search([0, 1, 2, 3, 4, 5, 6, 7, 8], 3)
    assert result == 3

    result = sol.search([-10, -8, -6, -3, -2, 0, 1, 2, 3, 4, 5, 6, 7, 8], 3)
    assert result == 8

    result = sol.search([-10, -8, -6, -3, -2, 0, 1, 2, 3, 4, 5, 6, 7, 8], -6)
    assert result == 2

    result = sol.search([-10, -8, -6, -3, -2, 0, 1, 2, 3, 4, 5, 6, 7, 8], -5)
    assert result == -1

    result = sol.search([], -5)
    assert result == -1