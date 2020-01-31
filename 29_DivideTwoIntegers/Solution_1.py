class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        if divisor == 0:
            return

        is_dividend_negative = dividend < 0
        is_divisor_negative = divisor < 0

        times = 0
        numerator = abs(dividend)
        denominator = abs(divisor)
        while numerator > 0:
            numerator -= denominator
            denominator += denominator
            # if after subtraction the numerator is negative then we've done too many divisions
            # don't count it
            if numerator >= 0:
                times += times

        if is_dividend_negative:
            times = -times
        if is_divisor_negative:
            times = -times

        return times


if __name__ == "__main__":
    sol = Solution().divide(10, 3)
    print(sol)
    assert sol == 3

    sol = Solution().divide(7, -3)
    assert sol == -2

    sol = Solution().divide(1, 0)
    assert sol is None

    sol = Solution().divide(1, 1)
    assert sol == 1

    sol = Solution().divide(1, -100)
    assert sol == 0

    sol = Solution().divide(-2147483648, -1)
    assert sol == 2147483648

    sol = Solution().divide(-2147483648, -2)
    print(sol)
