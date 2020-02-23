class Solution:
    def __init__(self):
        self.solutions = []
        self.temp_sol = []

    def partition(self, s: str):
        if not s:
            return []
        self._partition(s)
        return self.solutions

    def _partition(self, s: str):
        if s is '':
            self.solutions.append(self.temp_sol.copy())
        else:
            for i in range(1, len(s) + 1):
                sub_left = s[:i]
                sub_right = s[i:]
                is_palindrome = sub_left == sub_left[::-1]
                if is_palindrome:
                    self.temp_sol.append(sub_left)
                    self._partition(sub_right)
                    self.temp_sol.pop()

if __name__ == "__main__":

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
