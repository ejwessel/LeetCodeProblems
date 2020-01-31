def rotate_image(m):
    row = 0
    col = 0
    layer = 0
    while row < len(m) - 1 - layer:
        for i in range(len(m) - 1 - (2 * layer)):
            temp = m[row][col + i]
            m[row][col + i] = m[len(m) - 1 - layer - i][col] # top pulling from left
            m[len(m) - 1 - layer - i][col] = m[len(m) - 1 - layer][len(m) - 1 - layer - i] # left pulling from bottom
            m[len(m) - 1 - layer][len(m) - 1 - layer - i] = m[row + i][len(m) - 1 - layer] # bottom pulling from right
            m[row + i][len(m) - 1 - layer] = temp

        row += 1
        col += 1
        layer += 1


def print_matrix(matrix):
    for line in matrix:
        print(line)

if __name__ == "__main__":
    matrix = [
        [],
    ]
    print_matrix(matrix)
    print("=>")
    rotate_image(matrix)
    assert matrix == [[]]
    print_matrix(matrix)
    print()

    matrix = [
        [1],
    ]
    print_matrix(matrix)
    print("=>")
    rotate_image(matrix)
    assert matrix == [[1]]
    print_matrix(matrix)
    print()

    matrix = [
        [1, 2],
        [3, 4],
    ]
    print_matrix(matrix)
    print("=>")
    rotate_image(matrix)
    assert matrix == [[3, 1], [4, 2]]
    print_matrix(matrix)
    print()

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_matrix(matrix)
    print("=>")
    rotate_image(matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    print_matrix(matrix)
    print()

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 1, 2, 3],
        [4, 5, 6, 7]
    ]
    print_matrix(matrix)
    print("=>")
    rotate_image(matrix)
    assert matrix == [[4, 9, 5, 1], [5, 1, 6, 2], [6, 2, 7, 3], [7, 3, 8, 4]]
    print_matrix(matrix)
    print()

    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 1],
        [2, 3, 4, 5, 6],
        [7, 8, 9, 1, 2],
        [3, 4, 5, 6, 7]
    ]
    print_matrix(matrix)
    print("=>")
    rotate_image(matrix)
    assert matrix == [[3, 7, 2, 6, 1], [4, 8, 3, 7, 2], [5, 9, 4, 8, 3], [6, 1, 5, 9, 4], [7, 2, 6, 1, 5]]
    print_matrix(matrix)
    print()

    matrix = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 1, 2, 3],
        [4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 1, 2, 3],
        [4, 5, 6, 7, 8, 9],
    ]
    print_matrix(matrix)
    print("=>")
    rotate_image(matrix)
    assert matrix == [[4, 7, 1, 4, 7, 1], [5, 8, 2, 5, 8, 2], [6, 9, 3, 6, 9, 3], [7, 1, 4, 7, 1, 4], [8, 2, 5, 8, 2, 5], [9, 3, 6, 9, 3, 6]]
    print_matrix(matrix)
    print()


