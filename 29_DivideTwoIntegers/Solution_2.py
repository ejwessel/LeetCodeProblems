MIN_VAL = -1 << 31  # -2^31,
MAX_VAL = (1 << 31) - 1  # 2^31-1

class Solution:

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # don't divide by 0
        if divisor == 0:
            return

        is_dividend_negative = dividend < 0
        is_divisor_negative = divisor < 0

        numerator = abs(dividend)
        denominator = abs(divisor)
        answer = 0

        while numerator >= denominator:
            shift_amt = self.get_shift_amt(denominator, numerator)
            numerator -= (denominator << shift_amt)
            answer += (1 << shift_amt)

        # if either is negative then we need to update answer
        if is_divisor_negative != is_dividend_negative:
            answer = -answer

        answer = self.handle_boundry(answer)
        return answer

    def get_shift_amt(self, denominator, numerator):
        shift_amt = 1
        while (denominator << shift_amt) < numerator:
            shift_amt += 1
        # stopped at shifting too high, go back 1 shift
        shift_amt -= 1
        return shift_amt

    def handle_boundry(self, number):
        if number < 0:
            number = max(MIN_VAL, number)
        elif number > 0:
            number = min(MAX_VAL, number)
        return number


if __name__ == "__main__":

    sol = Solution().divide(1, 0)
    assert sol is None

    sol = Solution().divide(1, 1)
    assert sol == 1

    sol = Solution().divide(10, 3)
    assert sol == 3

    sol = Solution().divide(7, -3)
    assert sol == -2

    sol = Solution().divide(1, -100)
    assert sol == 0

    sol = Solution().divide(5, 100)
    assert sol == 0

    sol = Solution().divide(35, 8)
    assert sol == 4

    sol = Solution().divide(-2147483648, -1)
    assert sol == 2147483647

