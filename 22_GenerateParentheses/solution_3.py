class Solution:

    def __init__(self):
        self.solution = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.solution = []
        self._generateParenthesis(n, n, "")
        return self.solution

    def _generateParenthesis(self, left_used, right_used, paren_str):
        # we ensure that we can never add a right paren before a left param
        if left_used > right_used:
            return
        if left_used == 0 and right_used == 0:
            self.solution.append(paren_str)
            return
        if left_used > 0:
            self._generateParenthesis(left_used - 1, right_used, paren_str + "(")
        if right_used > 0:
            self._generateParenthesis(left_used, right_used - 1, paren_str + ")")

if __name__ == "__main__":
    sol = Solution()
    result = sol.generateParenthesis(0)
    print(result)
    print(len(result))
    print()

    result = sol.generateParenthesis(1)
    print(result)
    print(len(result))
    print()

    result = sol.generateParenthesis(2)
    print(result)
    print(len(result))
    print()

    result = sol.generateParenthesis(3)
    print(result)
    print(len(result))
    print()

    result = sol.generateParenthesis(4)
    print(result)
    print(len(result))
    print()

    print("missing")
    list1 = set(["()()()()","(()()())","(()())()","()(()())","((()()))","(())()()","()(())()","((())())","()()(())","(()(()))","((()))()","()((()))","(((())))"])
    list2 = set(["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])
    diff = list1.difference(list2)
    print(diff)
    diff = list2.difference(list1)
    print(diff)


