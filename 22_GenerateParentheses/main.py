class Solution:

    def generate_left(self, str):
        return "()" + str

    def generate_right(self, str):
        return str + "()"

    def generate_inside(self, str):
        return "(" + str + ")"

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        size_to_list = {
            0: [],
            1: ["()"]
        }

        if n == 0:
            return size_to_list[0]
        elif n == 1:
            return size_to_list[1]

        for i in range(2, n + 1):
            size_to_list[i] = []

            for item in size_to_list[i - 1]:
                left = self.generate_left(item)
                if left not in size_to_list[i]:
                    size_to_list[i].append(left)

                right = self.generate_right(item)
                if right not in size_to_list[i]:
                    size_to_list[i].append(right)

                inside = self.generate_inside(item)
                if inside not in size_to_list[i]:
                    size_to_list[i].append(inside)

        return size_to_list[n]

if __name__ == "__main__":
    sol = Solution()
    result = sol.generateParenthesis(0)
    print(result)
    print(len(result))

    result = sol.generateParenthesis(1)
    print(result)
    print(len(result))

    result = sol.generateParenthesis(2)
    print(result)
    print(len(result))

    result = sol.generateParenthesis(3)
    print(result)
    print(len(result))

    result = sol.generateParenthesis(4)
    print(result)
    print(len(result))

    print("missing")
    list1 = set(["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])
    list2 = set(["()()()()",
     "(()()())", "()(()())", "(()())()", "((()()))", "()()(())", "()(())()", "(()(()))", "(())()()", "((())())",
     "()((()))", "((()))()", "(((())))"])

    diff = list1.difference(list2)
    print(diff)


