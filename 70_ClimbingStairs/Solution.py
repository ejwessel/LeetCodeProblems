class Solution:
    def __init__(self):
        self.solutions = 0

    def climbStairs(self, n: int) -> int:
        self.climbStairsHelper(n)
        return self.solutions

    def climbStairsHelper(self, n):
        if n == 0:
            self.solutions += 1
            return
        elif n < 0:
            return

        for i in range(1, 3):
            self.climbStairsHelper(n - i)




if __name__ == "__main__":
    sol = Solution()
    result = sol.climbStairs(1)
    print(result)

    sol = Solution()
    result = sol.climbStairs(2)
    print(result)

    sol = Solution()
    result = sol.climbStairs(3)
    print(result)

    sol = Solution()
    result = sol.climbStairs(4)
    print(result)

    sol = Solution()
    result = sol.climbStairs(5)
    print(result)

    sol = Solution()
    result = sol.climbStairs(6)
    print(result)

    sol = Solution()
    result = sol.climbStairs(7)
    print(result)
