from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if len(matrix) == 0:
            return []

        col_start = 0
        row_start = 0

        col_len = len(matrix[0])
        row_len = len(matrix)

        layer = 0
        output = []

        while col_start < col_len / 2 and row_start < row_len / 2:

            # case when we hit the center
            if col_start == col_len - 1 - layer and row_start == row_len - 1 - layer:
                output.append(matrix[row_start][col_start])

            # prevents double backing
            last_seen_row = None
            last_seen_col = None

            # top row
            for i in range(col_start, col_len - 1 - layer):
                output.append(matrix[row_start][i])
                last_seen_row = (row_start, i)
            # right row
            for i in range(row_start, row_len - 1 - layer):
                output.append(matrix[i][col_len - 1 - layer])
                last_seen_col = (i, col_len - 1 - layer)
            # bottom row
            for i in reversed(range(col_start + 1, col_len - layer)):
                # if we begin to double back stop
                if (row_len - 1 - layer, i) == last_seen_row:
                    break
                output.append(matrix[row_len - 1 - layer][i])
            # left column
            for i in reversed(range(row_start + 1, row_len - layer)):
                # if we begin to double back stop
                if (i, col_start) == last_seen_col:
                    break
                output.append(matrix[i][col_start])

            col_start += 1
            row_start += 1
            layer += 1

        return output


if __name__ == "__main__":
    sol = Solution()

    input = []
    result = sol.spiralOrder(input)
    assert result == []

    input = [
        [1, 2, 3]
    ]
    result = sol.spiralOrder(input)
    assert result == [1, 2, 3]

    input = [
        [1],
        [2],
        [3]
    ]
    result = sol.spiralOrder(input)
    assert result == [1, 2, 3]

    input = [
        [1]
    ]
    result = sol.spiralOrder(input)
    assert result == [1]

    input = [
        [1],
        [2]
    ]
    result = sol.spiralOrder(input)
    assert result == [1, 2]

    input = [
        [1, 2],
    ]
    result = sol.spiralOrder(input)
    assert result == [1, 2]

    input = [
        [1, 2],
        [3, 4],
    ]
    result = sol.spiralOrder(input)
    assert result == [1, 2, 4, 3]

    input = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result = sol.spiralOrder(input)
    assert result == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    input = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    result = sol.spiralOrder(input)
    assert result == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    input = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 2, 3],
        [4, 5, 6]
    ]
    result = sol.spiralOrder(input)
    assert result == [1, 2, 3, 6, 9, 3, 6, 5, 4, 1, 7, 4, 5, 8, 2]

    input = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 1],
        [2, 3, 4, 5, 6],
    ]
    result = sol.spiralOrder(input)
    assert result == [1, 2, 3, 4, 5, 1, 6, 5, 4, 3, 2, 6, 7, 8, 9]

    input = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 1],
        [2, 3, 4, 5, 6],
        [7, 8, 9, 1, 2],
        [3, 4, 5, 6, 7]
    ]
    result = sol.spiralOrder(input)
    assert result == [1, 2, 3, 4, 5, 1, 6, 2, 7, 6, 5, 4, 3, 7, 2, 6, 7, 8, 9, 5, 1, 9, 8, 3, 4]

    input = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 1],
        [2, 3, 4, 5, 6],
        [7, 8, 9, 1, 2],
    ]
    result = sol.spiralOrder(input)
    assert result == [1, 2, 3, 4, 5, 1, 6, 2, 1, 9, 8, 7, 2, 6, 7, 8, 9, 5, 4, 3]

    input = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
    ]
    result = sol.spiralOrder(input)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 6, 5, 4, 3, 2]

    input = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
    ]
    result = sol.spiralOrder(input)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 7, 6, 5, 4, 3, 2, 2, 3, 4, 5, 6, 7]

