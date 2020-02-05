from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                # start from every coordinate and do a DFS
                if self._search(board, word, (r, c), set()):
                    return True
        # only reach here if the entire board was searched and nothing was found
        return False

    def _search(self, board: List[List[str]], remaining_word: str, current_coordinate: tuple, seen_coordinates: set):
        '''

        :param board: board to search over
        :param remaining_word: the word that we're looking for
        :param current_coordinate: the current coordinate to search from; represented as a tuple (x, y)
        :param seen_coordinates: the coordinates visited
        :return: True if the word has been found, False otherwise
        '''
        if len(remaining_word) == 0:
            # if we're out of characters then we've found the word
            return True
        elif current_coordinate in seen_coordinates:
            # if we've already been to this coordinate ignore it
            return False
        elif current_coordinate[0] < 0 or current_coordinate[1] < 0 or\
                current_coordinate[0] >= len(board) or current_coordinate[1] >= len(board[0]):
            # coordinate is out of bounds
            return False
        elif board[current_coordinate[0]][current_coordinate[1]] != remaining_word[0]:
            # if the board character is not the first character coordinate then we can't continue this path
            return False
        else:
            # if we've made it this far then the board character at the coordinate matches
            updated_seen_coordinates = set.copy(seen_coordinates)
            updated_seen_coordinates.add(current_coordinate)

            # Top
            found = self._search(
                board,
                remaining_word[1:],
                (current_coordinate[0] - 1, current_coordinate[1]),
                updated_seen_coordinates
            )
            if found:
                return True

            # Right
            found = self._search(
                board,
                remaining_word[1:],
                (current_coordinate[0], current_coordinate[1] + 1),
                updated_seen_coordinates
            )
            if found:
                return True

            # Bottom
            found = self._search(
                board,
                remaining_word[1:],
                (current_coordinate[0] + 1, current_coordinate[1]),
                updated_seen_coordinates
            )
            if found:
                return True

            # Left
            found = self._search(
                board,
                remaining_word[1:],
                (current_coordinate[0], current_coordinate[1] - 1),
                updated_seen_coordinates
            )
            if found:
                return True

            return False


if __name__ == "__main__":
    sol = Solution()

    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    result = sol.exist(board, "ABCCED")
    assert result

    result = sol.exist(board, "SEE")
    assert result

    result = sol.exist(board, "ABCB")
    assert not result

    result = sol.exist(board, "ABCESCFSADEE")
    assert result

    result = sol.exist(board, "ABCESCFSADEEA")
    assert not result

    result = sol.exist(board, "F")
    assert result

    board = [
        ['A'],
    ]
    result = sol.exist(board, "F")
    assert not result

    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E'],
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E'],
        ['A', 'D', 'E', 'E']
    ]
    result = sol.exist(board, "ABCCFSABCCFDECBASFCSEEDDEE")
    assert result

    result = sol.exist(board, "ABCCFBCCFDECCFBASADDEEEE")
    assert result

    board = [
        []
    ]
    result = sol.exist(board, "ABC")
    assert not result

    board = [
    ]
    result = sol.exist(board, "ABC")
    assert not result

    '''
    longer than the board size √
    words smaller than board size √
    words that exist √
    words that !exist √
    small board √
    large board √
    board with no items [] √
    board with no items [[]] √
    '''
