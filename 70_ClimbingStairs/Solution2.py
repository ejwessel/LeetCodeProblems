from collections import deque

class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        It's a fibonacci sequence
        :param n:
        :return:
        '''
        last_two_nums = deque(maxlen=2)
        last_two_nums.append(1)
        for i in range(n):
            # if the queue has two elements we can use them
            if len(last_two_nums) >= 2:
                last_two_nums.append(last_two_nums[-1] + last_two_nums[-2])
            # if there is 1 element we can add to it
            else:
                last_two_nums.append(last_two_nums[-1])
        return last_two_nums[-1]


if __name__ == "__main__":
    sol = Solution()
    result = sol.climbStairs(1)
    assert result == 1

    sol = Solution()
    result = sol.climbStairs(2)
    assert result == 2

    sol = Solution()
    result = sol.climbStairs(3)
    assert result == 3

    sol = Solution()
    result = sol.climbStairs(4)
    assert result == 5

    sol = Solution()
    result = sol.climbStairs(5)
    assert result == 8

    sol = Solution()
    result = sol.climbStairs(6)
    assert result == 13

    sol = Solution()
    result = sol.climbStairs(7)
    assert result == 21
