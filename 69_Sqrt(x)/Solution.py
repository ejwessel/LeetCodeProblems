import math
class Solution:
    def mySqrt(self, x: int) -> int:
        val = 1
        count = 3
        while x > 0:
            x -= count
            count += 2
            val += 1
        # -1 because we over counted
        return val - 1

if __name__ == "__main__":
    sol = Solution()
    result = sol.mySqrt(9)
    assert result == 3

    result = sol.mySqrt(23)
    assert result == 4

    result = sol.mySqrt(25)
    assert result == 5

    result = sol.mySqrt(100)
    assert result == 10
