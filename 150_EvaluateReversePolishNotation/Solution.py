from typing import List


class Solution:
    def is_numeric(self, character):
        if character == '+' or character == '-' or character == '*' or character == '/':
            return False
        return True

    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return None
        s = []
        # as long as there are tokens to add or we have yet to fully evaluate the stack continue
        while tokens or len(s) > 2:
            if len(s) > 2 and self.is_numeric(s[len(s) - 1]) and self.is_numeric(s[len(s) - 2]):
                # problem checking that the last two digits are integers
                param1 = int(s.pop())
                param2 = int(s.pop())
                operator = s.pop()
                if operator == "+":
                    s.append(str(param1 + param2))
                elif operator == "*":
                    s.append(str(param1 * param2))
                elif operator == "/":
                    s.append(str(int(param1 / param2)))
                elif operator == "-":
                    s.append(str(param1 - param2))
            else:
                s.append(tokens.pop())

        return int(s[0])


if __name__ == "__main__":
    sol = Solution()
    result = sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    assert result == 22

    sol = Solution()
    result = sol.evalRPN(["2", "1", "+", "3", "*"])
    assert result == 9

    sol = Solution()
    result = sol.evalRPN(["4", "13", "5", "/", "+"])
    assert result == 6

    sol = Solution()
    result = sol.evalRPN(["4"])
    assert result == 4

    sol = Solution()
    result = sol.evalRPN([])
    assert not result

    sol = Solution()
    result = sol.evalRPN(
        ["-78", "-33", "196", "+", "-19", "-", "115", "+", "-", "-99", "/", "-18", "8", "*", "-86", "-", "-", "16", "/",
         "26", "-14", "-", "-", "47", "-", "101", "-", "163", "*", "143", "-", "0", "-", "171", "+", "120", "*", "-60",
         "+", "156", "/", "173", "/", "-24", "11", "+", "21", "/", "*", "44", "*", "180", "70", "-40", "-", "*", "86",
         "132", "-84", "+", "*", "-", "38", "/", "/", "21", "28", "/", "+", "83", "/", "-31", "156", "-", "+", "28",
         "/", "95", "-", "120", "+", "8", "*", "90", "-", "-94", "*", "-73", "/", "-62", "/", "93", "*", "196", "-",
         "-59", "+", "187", "-", "143", "/", "-79", "-89", "+", "-"])
    assert result == 165
