class Solution:
    def reverseWords(self, s: str) -> str:
        # remove spaces
        s = ' '.join(s.split())
        components = s.split(' ')
        components.reverse()
        return ' '.join(components)

if __name__ == "__main__":
    sol = Solution()
    output = sol.reverseWords("the sky is blue")
    assert output == "blue is sky the"

    output = sol.reverseWords("  hello world!  ")
    assert output == "world! hello"

    output = sol.reverseWords("a good   example")
    assert output == "example good a"
