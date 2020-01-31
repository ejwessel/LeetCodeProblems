import re

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        Assume we are dealing with an environment
        which could only store integers within
        the 32-bit signed integer range: [−2^(31),  2^(31) − 1]
        """

        INT_MIN = -2147483648
        INT_MAX = 2147483647

        # sanity check input to see if it fits expected input
        input_match = re.match("(\ )*(\+|\-)?[0-9]+", str)

        # return 0 if there is no match
        if input_match is None:
            return 0

        # strip whitespace
        matched_string = input_match.group(0)
        matched_string = matched_string.strip(" ")

        # print(matched_string)

        int_value = int(matched_string)

        # handle if value is out of range
        if int_value > INT_MAX:
            return INT_MAX
        elif int_value < INT_MIN:
            return INT_MIN

        return int_value


if __name__ == "__main__":
    output = Solution().myAtoi("42")
    assert(output == 42)
    output = Solution().myAtoi("   -42")
    assert(output == -42)
    output = Solution().myAtoi("4193 with words")
    assert(output == 4193)
    output = Solution().myAtoi("words and 987")
    assert(output == 0)
    output = Solution().myAtoi("-91283472332")
    assert(output == -2147483648)
    output = Solution().myAtoi("+-2")
    assert(output == 0)