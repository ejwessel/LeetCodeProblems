from typing import List


class Solution:
    def __init__(self):
        self.solutions = []

    def combine(self, n: int, k: int):
        self._combine(n, k, 1, [])
        return self.solutions

    def _combine(self, n: int, k: int, start: int, sol: List) -> List[List[int]]:
        if len(sol) == k:
            self.solutions.append(sol)
        else:
            bound = n - (k - (start))
            for i in range(start, bound):
                self._combine(n, k, i + 1, sol + [i])


if __name__ == "__main__":
    sol = Solution()

    result = sol.combine(4, 4)
    print(result)

    n = 4
    k = 2
    for a in range(1, n):
        for b in range(a + 1, n + 1):
            print(a, b)
    print()

    n = 4
    k = 3
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                print(a, b, c)
    print()

    n = 4
    k = 4
    for a in range(1, n - 2):
        for b in range(a + 1, n - 1):
            for c in range(b + 1, n):
                for d in range(c + 1, n + 1):
                    print(a, b, c, d)
