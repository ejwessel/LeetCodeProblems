from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # work our way backwards from last element of list to the element before the first
        for depth in reversed(range(1, len(triangle))):
            # stop 1 before the end since we seek +1 for every i
            for i in range(0, len(triangle[depth]) - 1):
                min_val = min(triangle[depth][i], triangle[depth][i + 1])
                triangle[depth - 1][i] += min_val
        return triangle[0][0]


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
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3],
        [-3, 2, 7, 2, 10],
        [9, 4, 7, 12, -8, -2]
    ]
    sol = Solution()
    result = sol.minimumTotal(input)
    assert result == 10
