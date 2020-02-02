from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        m = []
        for row in range(n):
            m.append([0] * n)

        count = 1
        start = 0  # represents col and row
        layer = 0

        while start <= n / 2:
            # can only go into the center if n is odd
            if n % 2 != 0 and start == int(n / 2):
                m[start][start] = count

            #  top
            for i in range(start, n - 1 - layer):
                m[start][i] = count
                count += 1

            # right
            for i in range(start, n - 1 - layer):
                m[i][n - 1 - layer] = count
                count += 1

            # bottom
            for i in reversed(range(start + 1, n - layer)):
                m[n - 1 - layer][i] = count
                count += 1

            # left
            for i in reversed(range(start + 1, n - layer)):
                m[i][start] = count
                count += 1

            start += 1
            layer += 1

        return m

if __name__ == "__main__":
    sol = Solution()

    result = sol.generateMatrix(2)
    assert result == [[1, 2], [4, 3]]

    result = sol.generateMatrix(3)
    assert result == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

    result = sol.generateMatrix(4)
    assert result == [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]

    result = sol.generateMatrix(5)
    assert result == [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]
