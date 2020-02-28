class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        prev = '1'
        count = 1
        while count < n:
            # formulate the new prev
            char_count = 1
            new_prev = ''
            prev_char = prev[0]
            for i in range(1, len(prev)):
                if prev[i] == prev_char:
                    char_count += 1
                else:
                    new_prev += str(char_count) + prev_char
                    char_count = 1
                    prev_char = prev[i]
            # handle left overs
            new_prev += str(char_count) + prev_char

            prev = new_prev
            count += 1
        return prev


if __name__ == "__main__":
    sol = Solution()
    result = sol.countAndSay(1)
    assert result == '1'

    result = sol.countAndSay(2)
    assert result == '11'

    result = sol.countAndSay(3)
    assert result == '21'

    result = sol.countAndSay(4)
    assert result == '1211'

    result = sol.countAndSay(5)
    assert result == '111221'

    result = sol.countAndSay(6)
    assert result == '312211'

    result = sol.countAndSay(7)
    assert result == '13112221'
