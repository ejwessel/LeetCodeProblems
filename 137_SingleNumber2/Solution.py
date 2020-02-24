from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_freq = {}
        for num in nums:
            if num not in num_freq:
                num_freq[num] = 0
            num_freq[num] += 1

        for num, freq in num_freq.items():
            if freq == 1:
                return num


if __name__ == "__main__":
    sol = Solution()

    result = sol.singleNumber([2, 2, 3, 2])
    assert result == 3

    result = sol.singleNumber([0, 1, 0, 1, 0, 1, 99])
    assert result == 99
