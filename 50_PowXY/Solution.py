import math


class Solution:
    def myPow_inefficient(self, x, n):
        if x == 0:
            return 0
        elif n == 0:
            return 1
        else:
            abs_n = abs(n)
            # when n is less then our x is really the denominator
            if n < 0:
                x = 1 / x
            # loop over the n range
            product = 1.00000
            for i in range(abs_n):
                product *= x

            return round(product, 5)

    def myPow(self, x, n):
        # handle edge cases
        if x == 0:
            return 0
        elif x == 1:
            return x
        elif n == 0:
            return 1

        # when n is less then our x is really the denominator
        if n < 0:
            x = 1 / x
        n = abs(n)

        product = 1
        # as long as we can double i then continue
        while n >= 2:
            prod = x
            i = 1
            # only if we can exponentially increase should we continue
            while (i + i) < n:
                prod *= prod
                i += i
            n -= i
            product *= prod

        # handle straggler n
        if n == 1:
            product *= x

        return round(product, 5)

if __name__ == "__main__":
    sol = Solution()

    # result = sol.myPow_inefficient(2.00000, 10)
    # assert result == 1024.00000
    #
    # result = sol.myPow_inefficient(2.10000, 3)
    # assert result == 9.26100
    #
    # result = sol.myPow_inefficient(2.00000, -2)
    # assert result == 0.25
    #
    # result = sol.myPow_inefficient(-2.00000, 3)
    # assert result == -8.00000

    result = sol.myPow(2.00000, 0)
    assert result == 1.00000

    result = sol.myPow(2.00000, 1)
    assert result == 2.00000

    result = sol.myPow(0.00000, 1)
    assert result == 0.00000

    result = sol.myPow(2.00000, 10)
    assert result == 1024.00000

    result = sol.myPow(2.10000, 3)
    assert result == 9.26100

    result = sol.myPow(2.00000, -2)
    assert result == 0.25

    result = sol.myPow(-2.00000, 3)
    assert result == -8.00000

    result = sol.myPow(2.00000, 11)
    assert result == 2048

    result = sol.myPow(2.00000, 1000)
    print(result)

    result = sol.myPow(2.00000, int(math.pow(2, 31) - 1))
    print(result)
