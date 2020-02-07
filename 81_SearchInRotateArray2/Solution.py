from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        if len(nums) == 0:
            return False

        b = 0
        e = len(nums)

        # continue iterating as long as the range is more than 1 element
        while (e - b) > 1:
            mid = int((b + e) / 2)

            is_left_sorted = nums[b] <= nums[mid - 1]
            is_right_sorted = nums[mid] <= nums[e - 1]

            # edge case is that both appear to be sorted, but which is not sorted
            if is_left_sorted and is_right_sorted:
                # look at left side
                for i in range(b, mid - 1):
                    # if at any point we identify it's not sorted then mark left as not sorted
                    if nums[i] > nums[i + 1]:
                        is_left_sorted = False

            # compare the target with a sorted side
            if is_left_sorted:
                if nums[b] <= target <= nums[mid - 1]:
                    # go left
                    e = mid
                    continue
                else:
                    # go right
                    b = mid
                    continue
            if is_right_sorted:
                if nums[mid] <= target <= nums[e - 1]:
                    # go right
                    b = mid
                    continue
                else:
                    # go left
                    e = mid
                    continue

        return nums[b] == target




if __name__ == "__main__":
    sol = Solution()

    input = [1, 2, 1, 1, 1, 1]
    result = sol.search(input, 2)
    assert result

    input = [1, 1, 1, 2, 1, 1]
    result = sol.search(input, 2)
    assert result

    input = [1, 1, 2, 1, 1, 1]
    result = sol.search(input, 2)
    assert result

    input = [1, 1, 1, 2, 2, 5, 5, 6, 7, 7, 9, 0, 0]

    result = sol.search(input, 1)
    assert result

    result = sol.search(input, 0)
    assert result

    result = sol.search(input, 9)
    assert result

    result = sol.search(input, 7)
    assert result

    result = sol.search(input, 8)
    assert not result

    result = sol.search(input, 4)
    assert not result

    input = [1, 0]
    result = sol.search(input, 1)
    assert result

    result = sol.search(input, 0)
    assert result

    result = sol.search(input, 9)
    assert not result

    input = [1]
    result = sol.search(input, 1)
    assert result

    result = sol.search(input, 0)
    assert not result

    input = []
    result = sol.search(input, 0)
    assert not result
