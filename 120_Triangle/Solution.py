from typing import List

class Solution:
    def __init__(self):
        self.minimum = float('inf')

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.minTriangle(triangle, 0, 0, 0)
        return self.minimum

    def minTriangle(self, tri, depth, start, current_sum):
        if depth == len(tri):
            self.minimum = min(self.minimum, current_sum)
        else:
            # handle root
            if depth == 0:
                value = tri[depth][0]
                self.minTriangle(tri, depth + 1, 0, current_sum + value)
            else:
                for i in range(start, start + 2):
                    value = tri[depth][i]
                    self.minTriangle(tri, depth + 1, i, current_sum + value)

if __name__ == "__main__":
    input = [
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
    ]
    sol = Solution()
    result = sol.minimumTotal(input)
    assert result == 11

    input = [
        [2],
        [3,4]
    ]
    sol = Solution()
    result = sol.minimumTotal(input)
    assert result == 5

    input = [
        [2],
    ]
    sol = Solution()
    result = sol.minimumTotal(input)
    assert result == 2

    input = [
    ]
    sol = Solution()
    result = sol.minimumTotal(input)
    assert result == 2
