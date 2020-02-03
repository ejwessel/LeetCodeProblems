class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        counts how many unique path are on a m x n board starting top left to bottom right
        :param m: the number of columns
        :param n: the number of rows
        :return: the number of unique paths
        '''

        if m <= 0 or n <= 0:
            return 0
        elif m == 1 or n == 1:
            return 1

        matrix = []
        for row in range(n):
            matrix.append([0] * m)

        # set up columns
        for col in range(1, len(matrix[0])):
            matrix[0][col] = 1

        # set up rows
        for row in range(1, len(matrix)):
            matrix[row][0] = 1

        # compute over matrix
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                matrix[row][col] = matrix[row - 1][col] + matrix[row][col - 1]

        # answer is in the last bottom right cell
        return matrix[n - 1][m - 1]

if __name__ == "__main__":
    sol = Solution()

    result = sol.uniquePaths(7, 3)
    assert result == 28

    result = sol.uniquePaths(3, 3)
    assert result == 6

    result = sol.uniquePaths(3, 2)
    assert result == 3

    result = sol.uniquePaths(3, 1)
    assert result == 1

    result = sol.uniquePaths(1, 3)
    assert result == 1

    # 1 element should mean there are no paths or 1 path?
    result = sol.uniquePaths(1, 1)
    assert result == 1

    result = sol.uniquePaths(0, 0)
    assert result == 0

    result = sol.uniquePaths(5, 6)
    assert result == 126


