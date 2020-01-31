MAX_INT = (1 << 31) - 1
MIN_INT = -(1 << 31)


class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = False
        if x < 0:
            sign = True

        x_str = str(abs(x))
        new_str = ''

        # reverse the string
        for i in range(len(x_str) - 1, -1, -1):
            new_str += x_str[i]

        # convert string back into int
        new_int = int(new_str)
        if sign:
            new_int *= -1

        # check boundary cases
        if new_int > MAX_INT or new_int < MIN_INT:
            return 0

        return new_int


if __name__ == "__main__":
    sol = Solution().reverse(23)
    assert sol == 32

    sol = Solution().reverse(230)
    assert sol == 32

    sol = Solution().reverse(-32)
    assert sol == -23

    sol = Solution().reverse(123)
    assert sol == 321

    sol = Solution().reverse(-123)
    assert sol == -321

    sol = Solution().reverse(120)
    assert sol == 21

    sol = Solution().reverse(1 << 32)
    assert sol == 0

    sol = Solution().reverse(-(1 << 32))
    assert sol == 0