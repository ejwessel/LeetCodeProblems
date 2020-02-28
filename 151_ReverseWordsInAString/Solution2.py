class Solution:
    def reverseWords(self, s: str) -> str:
        components = s.split(' ')
        new_order = []
        for i in reversed(range(len(components))):
            if components[i] is '':
                continue
            else:
                new_order.append(components[i])
        return ' '.join(new_order)

if __name__ == "__main__":
    sol = Solution()
    output = sol.reverseWords("the sky is blue")
    assert output == "blue is sky the"

    output = sol.reverseWords("  hello world!  ")
    assert output == "world! hello"

    output = sol.reverseWords("a good   example")
    assert output == "example good a"

