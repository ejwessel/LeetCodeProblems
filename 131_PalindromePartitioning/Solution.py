class Solution:
    def __init__(self):
        self.solutions = []
        self.temp_sol = []
        self.known_palindromes = {}

    def partition(self, s: str):
        if not s:
            return []
        self._partition(s)
        return self.solutions

    def _partition(self, s: str):
        if s is '':
            self.solutions.append(self.temp_sol.copy())
        else:
            for i in range(len(s) + 1):
                sub_left = s[:i]
                sub_right = s[i:]
                if sub_left is not '' and self.isPalindrome(sub_left):
                    self.temp_sol.append(sub_left)
                    self._partition(sub_right)
                    self.temp_sol.pop()


    def isPalindrome(self, s):
        if s in self.known_palindromes:
            return self.known_palindromes[s]

        for i in range(int(len(s) / 2)):
            if s[i] != s[len(s) - 1 - i]:
                self.known_palindromes[s] = False
                return False
        self.known_palindromes[s] = True
        return True

if __name__ == "__main__":

    sol = Solution()
    result = sol.isPalindrome("abba")
    assert result
    result = sol.isPalindrome("abb")
    assert not result

    sol = Solution()
    result = sol.partition("aab")
    assert result == [['a', 'a', 'b'], ['aa', 'b']]

    sol = Solution()
    result = sol.partition("abbac")
    assert result == [['a', 'b', 'b', 'a', 'c'], ['a', 'bb', 'a', 'c'], ['abba', 'c']]

    sol = Solution()
    result = sol.partition("a")
    assert result == [['a']]

    sol = Solution()
    result = sol.partition("")
    assert result == []
