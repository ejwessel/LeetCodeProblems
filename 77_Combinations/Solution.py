from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        pass

if __name__ == "__main__":
    sol = Solution()

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

