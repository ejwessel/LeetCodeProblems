class Solution:
    def isValidSudoku(self, board):
        result = self.check_row(board)
        if not result:
            return result
        result = self.check_column(board)
        if not result:
            return result

        return self.check_3x3(board)

    def check_row(self, board):
        col_len = len(board[0])
        row_len = len(board)
        for row in range(row_len):
            seen_nums = set()
            for column in range(col_len):
                if board[row][column] == '.':
                    continue
                elif board[row][column] in seen_nums:
                    return False
                seen_nums.add(board[row][column])
        return True

    def check_column(self, board):
        col_len = len(board[0])
        row_len = len(board)
        for column in range(col_len):
            seen_nums = set()
            for row in range(row_len):
                if board[row][column] == '.':
                    continue
                elif board[row][column] in seen_nums:
                    return False
                seen_nums.add(board[row][column])
        return True

    def check_3x3(self, board):
        col_len = len(board[0])
        row_len = len(board)
        grid_truth = True
        for col in range(0, col_len, 3):
            for row in range(0, row_len, 3):
                grid_truth = grid_truth and self.check_grid((col, row), board)
                if not grid_truth:
                    return grid_truth
        return True

    def check_grid(self, coord_start, board):
        col_len = 3
        row_len = 3
        seen_nums = set()
        for column in range(coord_start[1], coord_start[1] + col_len):
            for row in range(coord_start[0], coord_start[0] + row_len):
                if board[row][column] == '.':
                    continue
                elif board[row][column] in seen_nums:
                    return False
                seen_nums.add(board[row][column])
        return True


if __name__ == "__main__":
    sol = Solution()

    board = [
        ['1', '9', '9']
    ]
    isValid = sol.check_row(board)
    assert isValid == False

    board = [
        ['1', '9', '.']
    ]
    isValid = sol.check_row(board)
    assert isValid == True

    board = [
        ['1', '2', '3']
    ]
    isValid = sol.check_row(board)
    assert isValid == True

    board = [
        ['9', '2', '3'],
        ['9', '3', '1'],
        ['9', '2', '1']
    ]
    isValid = sol.check_column(board)
    assert isValid == False

    board = [
        ['1', '2', '3'],
        ['2', '3', '1'],
        ['3', '1', '2']
    ]
    isValid = sol.check_column(board)
    assert isValid == True

    board = [
        ['1', '.', '3'],
        ['.', '3', '1'],
        ['3', '1', '.']
    ]
    isValid = sol.check_column(board)
    assert isValid == True

    board = [
        ['1', '.', '3'],
        ['.', '3', '1'],
        ['3', '1', '.']
    ]
    isValid = sol.check_grid((0, 0), board)
    assert isValid == False

    board = [
        ['1', '.', '2'],
        ['.', '3', '4'],
        ['6', '5', '.']
    ]
    isValid = sol.isValidSudoku(board)
    assert isValid == True

    board = [
        ["5", "3", ".",  ".", "7", ".",  ".", ".", "."],
        ["6", ".", ".",  "1", "9", "5",  ".", ".", "."],
        [".", "9", "8",  ".", ".", ".",  ".", "6", "."],

        ["8", ".", ".",  ".", "6", ".",  ".", ".", "3"],
        ["4", ".", ".",  "8", ".", "3",  ".", ".", "1"],
        ["7", ".", ".",  ".", "2", ".",  ".", ".", "6"],

        [".", "6", ".",  ".", ".", ".",  "2", "8", "."],
        [".", ".", ".",  "4", "1", "9",  ".", ".", "5"],
        [".", ".", ".",  ".", "8", ".",  ".", "7", "9"]
    ]
    isValid = sol.isValidSudoku(board)
    assert isValid == True

    board = [
      ["8", "3", ".",  ".", "7", ".",  ".", ".", "."],
      ["6", ".", ".",  "1", "9", "5",  ".", ".", "."],
      [".", "9", "8",  ".", ".", ".",  ".", "6", "."],

      ["8", ".", ".",  ".", "6", ".",  ".", ".", "3"],
      ["4", ".", ".",  "8", ".", "3",  ".", ".", "1"],
      ["7", ".", ".",  ".", "2", ".",  ".", ".", "6"],

      [".", "6", ".",  ".", ".", ".",  "2", "8", "."],
      [".", ".", ".",  "4", "1", "9",  ".", ".", "5"],
      [".", ".", ".",  ".", "8", ".",  ".", "7", "9"]
    ]
    isValid = sol.isValidSudoku(board)
    assert isValid == False

    board = [
      ["5", "3", ".",  ".", "7", ".",  ".", ".", "."],
      ["6", ".", ".",  "1", "9", "5",  ".", ".", "."],
      [".", "9", "8",  ".", ".", ".",  ".", "6", "."],

      ["8", ".", ".",  ".", "6", ".",  ".", ".", "3"],
      ["4", ".", ".",  "8", ".", "3",  ".", ".", "1"],
      ["7", ".", ".",  "3", "2", ".",  ".", ".", "6"],

      [".", "6", ".",  ".", ".", ".",  "2", "8", "."],
      [".", ".", ".",  "4", "1", "9",  ".", ".", "5"],
      [".", ".", ".",  ".", "8", ".",  ".", "7", "9"]
    ]
    isValid = sol.isValidSudoku(board)
    assert isValid == False