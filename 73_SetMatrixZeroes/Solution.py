from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        row_len = len(matrix)
        col_len = len(matrix[0])
        # flag all rows and columns
        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        # set columns
        if col_len > 1:
            # start at 1 to not overwrite the flags - yet
            for row in range(1, row_len):
                # if the column isn't flagged ignore it
                if matrix[row][0] != 0:
                    continue
                for col in range(col_len):
                    matrix[row][col] = 0

        # set rows
        if row_len > 1:
            # start at 1 to not overwrite the flags - yet
            for col in range(1, col_len):
                # if the row isn't flagged ignore it
                if matrix[0][col] != 0:
                    continue
                for row in range(row_len):
                    matrix[row][col] = 0

        # handle the flags columns and rows
        if matrix[0][0] == 0:
            for col in range(col_len):
                matrix[0][col] = 0
            for row in range(row_len):
                matrix[row][0] = 0


if __name__ == "__main__":
    sol = Solution()

    # marked the [0][0] too soon
    input = [
        [1, 1, 1],
        [0, 1, 2]
    ]
    sol.setZeroes(input)
    assert input == [
        [0, 1, 1],
        [0, 0, 0]
    ]

    input = [
        [1, 2, 3, 0, 5]
    ]
    sol.setZeroes(input)
    assert input == [
        [0, 0, 0, 0, 0]
    ]

    input = [
        [1],
        [2],
        [3],
        [0],
        [5]
    ]
    sol.setZeroes(input)
    assert input == [
        [0],
        [0],
        [0],
        [0],
        [0]
    ]

    input = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 0, 5],
        [1, 0, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
    ]
    sol.setZeroes(input)
    assert input == [
        [1, 0, 3, 0, 5],
        [1, 0, 3, 0, 5],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 3, 0, 5],
        [1, 0, 3, 0, 5]
    ]

    input = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    sol.setZeroes(input)
    assert input == [
        [0, 0, 0, 0],
        [0, 4, 5, 0],
        [0, 3, 1, 0]
    ]
