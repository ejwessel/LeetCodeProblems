from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid[0])
        n = len(obstacleGrid)

        if m <= 0 or n <= 0:
            return 0
        elif m == 1 or n == 1:
            sum = 0
            for row in range(len(obstacleGrid)):
                for col in range(len(obstacleGrid[0])):
                    sum += obstacleGrid[row][col]

            if sum > 0:
                return 0
            else:
                return 1

        matrix = []
        for row in range(n):
            matrix.append([0] * m)

        # set up columns
        for col in range(1, len(matrix[0])):
            if obstacleGrid[0][col] == 1:
                matrix[0][col] = 0
                continue
            matrix[0][col] = 1

        # set up rows
        for row in range(1, len(matrix)):
            if obstacleGrid[row][0] == 1:
                matrix[row][0] = 0
                continue
            matrix[row][0] = 1

        # compute over matrix
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                # if there is an obstacle then the area is marked
                if obstacleGrid[row][col] == 1:
                    matrix[row][col] = 0
                    continue
                matrix[row][col] = matrix[row - 1][col] + matrix[row][col - 1]

        # answer is in the last bottom right cell
        return matrix[n - 1][m - 1]


if __name__ == "__main__":
    sol = Solution()

    obstacle_matrix = \
        [
            [0, 1, 0],
            [0, 1, 0],
        ]
    result = sol.uniquePathsWithObstacles(obstacle_matrix)
    assert result == 0


    obstacle_matrix = \
        [
            [0, 1, 0],
        ]
    result = sol.uniquePathsWithObstacles(obstacle_matrix)
    assert result == 0

    obstacle_matrix = \
        [
            [0],
            [1],
            [0],
        ]
    result = sol.uniquePathsWithObstacles(obstacle_matrix)
    assert result == 0

    obstacle_matrix = \
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
    result = sol.uniquePathsWithObstacles(obstacle_matrix)
    assert result == 2

    obstacle_matrix = \
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    result = sol.uniquePathsWithObstacles(obstacle_matrix)
    assert result == 17

    obstacle_matrix = \
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ]
    result = sol.uniquePathsWithObstacles(obstacle_matrix)
    assert result == 9

    obstacle_matrix = \
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 1, 0],
        ]
    result = sol.uniquePathsWithObstacles(obstacle_matrix)
    assert result == 5

    obstacle_matrix = \
        [
            [],
        ]
    result = sol.uniquePathsWithObstacles(obstacle_matrix)
    assert result == 0

    obstacle_matrix = \
        [
            [0],
        ]
    result = sol.uniquePathsWithObstacles(obstacle_matrix)
    assert result == 1

    obstacle_matrix = \
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 1, 1, 0],
        ]
    result = sol.uniquePathsWithObstacles(obstacle_matrix)
    assert result == 5
