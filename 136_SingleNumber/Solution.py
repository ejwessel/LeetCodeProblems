from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        char_freq = {}
        for num in nums:
            if num not in char_freq:
                char_freq[num] = 0
            char_freq[num] += 1

        for num, freq in char_freq.items():
            if freq == 1:
                return num

if __name__ == "__main__":
    sol = Solution()
    result = sol.singleNumber([2, 2, 1])
    assert result == 1

    result = sol.singleNumber([4, 1, 2, 1, 2])
    assert result == 4

    result = sol.singleNumber([])
    assert result == 4
