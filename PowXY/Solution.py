class Solution:
    def myPow(self, x, n):
        if x == 0:
            return 0
        elif n == 0:
            return 1
        else:
            abs_n = abs(n)
            # when n is less then our x is really the denominator
            if n < 0:
                x = 1/x
            # loop over the n range
            product = 1.00000
            for i in range(abs_n):
                product *= x

            return round(product, 5)



if __name__ == "__main__":
    sol = Solution()

    result = sol.myPow(2.00000, 10)
    assert result == 1024.00000

    result = sol.myPow(2.10000, 3)
    assert result == 9.26100

    result = sol.myPow(2.00000, -2)
    assert result == 0.25
