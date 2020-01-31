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

        # have a mapping of Symbol to Value
        # input [1, 3999]

        total = 0
        i = 0
        while i < len(s):
            if (i + 1) >= len(s):
                total += numeral_to_int[s[i]]
                i += 1
                continue

            combined_c = s[i] + s[i + 1]

            if combined_c in numeral_to_int:
                total += numeral_to_int[combined_c]
                i += 1  # we are using 2 chars here...
            else:
                total += numeral_to_int[s[i]]
            i += 1

        return total


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