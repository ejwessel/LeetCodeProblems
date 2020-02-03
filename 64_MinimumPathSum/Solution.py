from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # we start at 1 because 0,0 doesn't need anything added to it
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                # ignore the starting spot
                if row == 0 and col == 0:
                    continue
                elif row == 0:
                    grid[row][col] = grid[row][col] + grid[row][col - 1]
                elif col == 0:
                    grid[row][col] = grid[row][col] + grid[row - 1][col]
                else:
                    grid[row][col] = grid[row][col] + min(grid[row][col - 1], grid[row - 1][col])

        return grid[len(grid) - 1][len(grid[0]) - 1]

if __name__ == "__main__":
    sol = Solution()

    input = [
        [1],
    ]
    result = sol.minPathSum(input)
    assert result == 1

    input = [
        [1, 3, 1],
    ]
    result = sol.minPathSum(input)
    assert result == 5

    input = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    result = sol.minPathSum(input)
    assert result == 7

    input = [
        [1, 3, 1, 2, 2, 1],
        [4, 1, 6, 2, 1, 1],
        [1, 5, 2, 3, 5, 1],
        [1, 1, 3, 4, 1, 1],
        [1, 9, 7, 1, 2, 9]
    ]
    result = sol.minPathSum(input)
    assert result == 22

