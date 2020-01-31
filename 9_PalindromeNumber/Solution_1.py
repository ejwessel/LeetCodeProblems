class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        num_list = []
        while x != 0:
            num_list.append(x % 10)
            x = int(x / 10)

        for i in range(int(len(num_list) / 2)):
            if num_list[i] != num_list[len(num_list) - 1 - i]:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()

    output = sol.isPalindrome(121)
    assert output == True

    output = sol.isPalindrome(-121)
    assert output == False

    output = sol.isPalindrome(10)
    assert output == False