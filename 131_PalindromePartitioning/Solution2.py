from collections import defaultdict

class Solution:
    def __init__(self):
        self.known_palindromes = {}
        self.memo = defaultdict(list)

    def partition(self, s: str):
        return self._parition(s, 0, len(s))

    def _parition(self, string, begin, end):
        if begin >= end:
            return []
        else:
            for i in range(begin, end):
                left_range = (begin, i)
                right_range = (i, end)
                sub_left = string[begin: i]
                right_sub = string[i: end]

                if sub_left is '':
                    continue

                if right_range in self.memo:
                    right_partitions = self.memo[right_range]
                    for right in right_partitions:
                        self.memo[left_range].append([sub_left + right])
                else:
                    if self.isPalindrome(sub_left):
                        right_partitions = self._parition(string, i, end)
                        for right in right_partitions:
                            self.memo[left_range].append([sub_left + right])

            return self.memo[left_range]


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
    print(result)
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
