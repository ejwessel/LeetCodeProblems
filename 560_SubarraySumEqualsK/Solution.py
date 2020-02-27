from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total_sum = 0
        num_freq = {0: 1}
        sum_count = 0

        for num in nums:
            total_sum += num
            needed_num = total_sum - k
            # check if the needed num has been seen before and increase count
            if needed_num in num_freq:
                sum_count += num_freq[needed_num]

            # increase frequency of seeing the running sum
            if total_sum not in num_freq:
                num_freq[total_sum] = 0
            num_freq[total_sum] += 1

        return sum_count


if __name__ == "__main__":
    sol = Solution()

    result = sol.subarraySum([0], 0)
    assert result == 1

    result = sol.subarraySum([1], 1)
    assert result == 1

    result = sol.subarraySum([2, 3, -2, -2, 4, 1, 2], 5)
    assert result == 4

    result = sol.subarraySum([1, 1, 1], 2)
    assert result == 2

    result = sol.subarraySum([1, 2, 1, 2, 1], 3)
    assert result == 4

