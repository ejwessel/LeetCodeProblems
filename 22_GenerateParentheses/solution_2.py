class Solution:

    def __init__(self):
        self.solution = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.solution = {}
        self._generateParenthesis(0, n, "")
        return self.solution[n]

    def _generateParenthesis(self, current_depth, max_depth, s):
        if current_depth > max_depth:
            return
        if current_depth == max_depth:
            if max_depth not in self.solution.keys():
                self.solution[max_depth] = []

            if s not in self.solution[max_depth] and s != "":

                self.solution[max_depth].append(s)
            return

        self._generateParenthesis(current_depth + 1, max_depth, s + '()')
        self._generateParenthesis(current_depth + 1, max_depth, '()' + s)
        self._generateParenthesis(current_depth + 1, max_depth, '(' + s + ')')

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


