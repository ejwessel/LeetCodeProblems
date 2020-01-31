numeral_to_int = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 0:
            return 0
        elif len(s) == 1:
            return numeral_to_int[s]
        else:
            double_char = s[:2]
            if double_char in numeral_to_int:
                return numeral_to_int[double_char] + self.romanToInt(s[2:])
            return numeral_to_int[s[:1]] + self.romanToInt(s[1:])


if __name__ == "__main__":
    sol = Solution()

    result = sol.romanToInt("III")
    assert result == 3

    result = sol.romanToInt("IV")
    assert result == 4

    result = sol.romanToInt("IX")
    assert result == 9

    result = sol.romanToInt("LVIII")
    assert result == 58

    result = sol.romanToInt("MCMXCIV")
    assert result == 1994

    result = sol.romanToInt("MMMCDLXIII")
    assert result == 3463