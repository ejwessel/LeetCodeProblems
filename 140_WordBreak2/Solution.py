from typing import List
from collections import defaultdict

class Solution:
    def __init__(self):
        self.memo = defaultdict(list)

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self._wordBreakHelper(s, wordDict)
        return self.memo[s]

    def _wordBreakHelper(self, s: str, wordDict: List[str]):
        if s is '':
            self.memo[s].append(s)
            return

        for i in range(1, len(s) + 1):
            left_sub = s[:i]
            right_sub = s[i:]

            # don't continue if the left sub it not a word
            if left_sub not in wordDict:
                continue

            # perform analysis on the right substring if it doesn't exist
            if right_sub not in self.memo:
                self._wordBreakHelper(right_sub, wordDict)

            # combine the solutions with left
            for string in self.memo[right_sub]:
                if string is '':
                    self.memo[s].append(left_sub)
                else:
                    self.memo[s].append(left_sub + ' ' + string)



if __name__ == "__main__":

    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    sol = Solution()
    result = sol.wordBreak(s, wordDict)
    assert result == ['cat sand dog', 'cats and dog']

    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    sol = Solution()
    result = sol.wordBreak(s, wordDict)
    assert result == ['pine apple pen apple', 'pine applepen apple', 'pineapple pen apple']

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    sol = Solution()
    result = sol.wordBreak(s, wordDict)
    assert result == []

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    sol = Solution()
    result = sol.wordBreak(s, wordDict)
    assert result == []
