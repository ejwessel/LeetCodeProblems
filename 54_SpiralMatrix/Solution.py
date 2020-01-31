from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        col_start = 0
        row_start = 0

        col_len = len(matrix[0])
        row_len = len(matrix)

        layer = 0

        while col_start < col_len / 2 and row_start < row_len / 2:
            # top row
            for i in range(col_start, col_len - layer):
                print(matrix[row_start][i])
            # right row
            for i in range(row_start, row_len - layer):
                print(matrix[i][col_len - 1 - layer])
            # bottom row
            for i in reversed(range(col_start, col_len - layer)):
                print(matrix[row_len - 1 - layer][i])
            # left column
            for i in reversed(range(row_start, row_len - layer)):
                print(matrix[i][col_start])

            col_start += 1
            row_start += 1




if __name__ == "__main__":
    sol = Solution()

    input = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected_output = [1,2,3,6,9,8,7,4,5]
    sol.spiralOrder(input)

    input = [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ]
    expected_output = [1,2,3,4,8,12,11,10,9,5,6,7]
    sol.spiralOrder(input)
