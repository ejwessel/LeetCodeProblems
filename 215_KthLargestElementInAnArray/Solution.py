from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


if __name__ == "__main__":
    sol = Solution()
    result = sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    assert result == 4

    result = sol.findKthLargest([3, 2, 1, 5, 6, 4], 2)
    assert result == 5

