from typing import List


class Solution:
    def binarySearch(self, elements, target):
        s = 0
        e = len(elements)

        while (s < e):
            mid = int((s + e) / 2)
            if elements[mid] == target:
                return True
            elif target < elements[mid]:
                e = mid
            elif target > elements[mid]:
                s = mid + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s = 0
        e = len(matrix)

        # ensure there are elements
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False

        while (s < e):
            mid = int((s + e) / 2)
            if matrix[mid][0] <= target <= matrix[mid][len(matrix[0]) - 1]:
                return self.binarySearch(matrix[mid], target)
            elif target < matrix[mid][0]:
                e = mid
            elif target > matrix[mid][len(matrix[0]) - 1]:
                s = mid + 1

        return False

if __name__ == "__main__":
    sol = Solution()

    matrix = [
    ]
    result = sol.searchMatrix(matrix, 13)
    assert not result

    matrix = [
        [],
    ]
    result = sol.searchMatrix(matrix, 13)
    assert not result

    elements = [1, 2, 3, 4, 6, 7, 8, 9, 10]
    result = sol.binarySearch(elements, 8)
    assert result
    result = sol.binarySearch(elements, 5)
    assert not result
    result = sol.binarySearch(elements, 11)
    assert not result
    result = sol.binarySearch(elements, -10)
    assert not result
    result = sol.binarySearch(elements, 6)
    assert result

    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    result = sol.searchMatrix(matrix, 13)
    assert not result
    result = sol.searchMatrix(matrix, 3)
    assert result
    result = sol.searchMatrix(matrix, 999)
    assert not result
    result = sol.searchMatrix(matrix, -10)
    assert not result

    matrix = [
        [1,   3,  5,  7],
    ]
    result = sol.searchMatrix(matrix, 13)
    assert not result
    result = sol.searchMatrix(matrix, -22)
    assert not result
    result = sol.searchMatrix(matrix, 3)
    assert result

    matrix = [
        [1],
        [3],
        [5],
        [7],
    ]
    result = sol.searchMatrix(matrix, 13)
    assert not result
    result = sol.searchMatrix(matrix, 3)
    assert result
    result = sol.searchMatrix(matrix, 100)
    assert not result

    matrix = [
        [1],
    ]
    result = sol.searchMatrix(matrix, 13)
    assert not result
    result = sol.searchMatrix(matrix, 3)
    assert not result
    result = sol.searchMatrix(matrix, 100)
    assert not result
    result = sol.searchMatrix(matrix, 1)
    assert result

