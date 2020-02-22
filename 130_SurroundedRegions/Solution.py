from typing import List

class Solution:
    def __init__(self):
        self.visited_cells = set()
        self.dfs_visited = set()
        self.row_length = 0
        self.col_length = 0
        self.board = []

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == []:
            return []

        self.board = board
        self.row_length = len(board)
        self.col_length = len(board[0])

        for r in range(self.row_length):
            for c in range(self.col_length):
                if (r, c) in self.visited_cells:
                    continue

                can_color = self.dfsTraversal((r, c))
                if can_color:
                    for cell in self.dfs_visited:
                        board[cell[0]][cell[1]] = 'X'

                # copy visited cells in dfs
                self.visited_cells.union(self.dfs_visited)
                # reset visited cells in dfs
                self.dfs_visited.clear()

    def dfsTraversal(self, current_cell):
        r, c = current_cell

        if r < 0 or r >= self.row_length or c < 0 or c >= self.col_length:
            return False

        if current_cell in self.dfs_visited:
            return True

        # mark current cell as visited
        self.dfs_visited.add(current_cell)

        if self.board[r][c] == 'X':
            return True

        return (
            # top, right, bottom, left
            self.dfsTraversal((r - 1, c)) and
            self.dfsTraversal((r, c + 1)) and
            self.dfsTraversal((r + 1, c)) and
            self.dfsTraversal((r, c - 1))
        )

def printBoard(board):
    for row in board:
        print(row)
    print()

if __name__ == "__main__":
    sol = Solution()
    board = [
    ]
    sol.solve(board)
    printBoard(board)
    assert board == [
    ]

    sol = Solution()
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    sol.solve(board)
    printBoard(board)
    assert board == [
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'X']
    ]

    board = [
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'O', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
    ]
    sol.solve(board)
    printBoard(board)
    assert board == [
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X']
    ]

    board = [
        ['O', 'O', 'O', 'O', 'O'],
        ['O', 'X', 'X', 'X', 'O'],
        ['O', 'X', 'O', 'X', 'O'],
        ['O', 'X', 'X', 'X', 'O'],
        ['O', 'O', 'O', 'O', 'O'],
    ]
    sol.solve(board)
    printBoard(board)
    assert board == [
        ['O', 'O', 'O', 'O', 'O'],
        ['O', 'X', 'X', 'X', 'O'],
        ['O', 'X', 'X', 'X', 'O'],
        ['O', 'X', 'X', 'X', 'O'],
        ['O', 'O', 'O', 'O', 'O']
    ]

    board = [
        ['O', 'O', 'O', 'O', 'O'],
        ['O', 'X', 'X', 'X', 'O'],
        ['O', 'X', 'O', 'X', 'O'],
        ['O', 'X', 'X', 'X', 'O'],
    ]
    sol.solve(board)
    printBoard(board)
    assert board == [
        ['O', 'O', 'O', 'O', 'O'],
        ['O', 'X', 'X', 'X', 'O'],
        ['O', 'X', 'X', 'X', 'O'],
        ['O', 'X', 'X', 'X', 'O'],
    ]

    board = [
        ['O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O'],
    ]
    sol.solve(board)
    printBoard(board)
    assert board == [
        ['O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O'],
    ]

    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
    ]
    sol.solve(board)
    printBoard(board)
    assert board == [
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
    ]

    board = [
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X', 'X'],
        ['X', 'O', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X', 'X'],
    ]
    sol.solve(board)
    printBoard(board)
    assert board == [
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X', 'X'],
        ['X', 'O', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X', 'X'],
    ]

    board = [
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'O', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X', 'X'],
    ]
    sol.solve(board)
    printBoard(board)
    assert board == [
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X', 'X'],
    ]
