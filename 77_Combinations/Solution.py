from typing import List


class Solution:
    def __init__(self):
        self.solutions = []

    def combine(self, n: int, k: int):
        # +1 to n because we start counting at 1 and so the upper range needs to be 1 higher
        # 1 to start because we start counting at 1
        self._combine(n + 1, k, 1, [])
        return self.solutions

    def _combine(self, n: int, k: int, start: int, sol: List) -> List[List[int]]:
        if len(sol) == k:
            self.solutions.append(sol)
        else:
            # the bound is computed to optimize the upper bound
            bound = min(n, n - (k - start))
            # in of bound and n so that we don't go over n
            for i in range(start, bound):
                self._combine(n, k, i + 1, sol + [i])


if __name__ == "__main__":
    # sol = Solution()
    # result = sol.combine(4, 0)
    # assert result == [[]]  # may need to be []
    #
    # sol = Solution()
    # result = sol.combine(4, 1)
    # assert result == [[1], [2], [3], [4]]

    sol = Solution()
    result = sol.combine(4, 2)
    assert result == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

    sol = Solution()
    result = sol.combine(4, 3)
    assert result == [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]

    sol = Solution()
    result = sol.combine(4, 4)
    assert result == [[1, 2, 3, 4]]

    sol = Solution()
    result = sol.combine(4, 5)
    assert result == []

    sol = Solution()
    result = sol.combine(0, 1)
    assert result == []

    sol = Solution()
    result = sol.combine(1, 1)
    assert result == [[1]]

    sol = Solution()
    result = sol.combine(2, 1)
    assert result == [[1], [2]]
