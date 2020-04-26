class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # add empty char at beginning
        s = ' ' + s
        t = ' ' + t
        num_cols = len(s)
        num_rows = len(t)
        distance_matrix = self.createDistanceMatrix(num_cols, num_rows)

        for row_i in range(1, num_rows):
            for col_i in range(1, num_cols):
                if s[col_i] == t[row_i]:
                    diagonal_val = distance_matrix[row_i - 1][col_i - 1]
                    distance_matrix[row_i][col_i] = diagonal_val
                else:
                    left_val = distance_matrix[row_i - 1][col_i]
                    diagonal_val = distance_matrix[row_i - 1][col_i - 1]
                    top_val = distance_matrix[row_i][col_i - 1]
                    distance_matrix[row_i][col_i] = min(left_val, diagonal_val, top_val) + 1

        return distance_matrix[-1][-1] == 1

    def createDistanceMatrix(self, num_cols, num_rows):
        # +1 to row and col to help represent empty string
        distance_matrix = [[0 for i in range(0, num_cols)] for r in range(0, num_rows)]
        top_row = [i for i in range(0, num_cols)]
        distance_matrix[0] = top_row
        for i in range(1, num_rows):
            distance_matrix[i][0] = i
        return distance_matrix

    def printDistanceMatrix(self, matrix):
        for row in matrix:
            print(row)
        print()


if __name__ == '__main__':
    sol = Solution()
    result = sol.isOneEditDistance('hello', 'hella')
    assert result

    result = sol.isOneEditDistance('ab', 'acb')
    assert result

    result = sol.isOneEditDistance('cab', 'ad')
    assert not result

    result = sol.isOneEditDistance('a', 'b')
    assert result

    result = sol.isOneEditDistance('benyam', 'ephrem')
    assert not result

    result = sol.isOneEditDistance('1203', '1213')
    assert result
