from typing import List

class Solution:
    def __init__(self):
        self.memo = set()

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # empty string is true because it's only possible to reach
        # here if all words prior were in the dict
        if s == '':
            return True

        for i in range(1, len(s) + 1):
            sub_left = s[:i]
            sub_right = s[i:]
            # if the left substring is not in the dict then no point in continuing
            if sub_left not in wordDict:
                continue

            # skip over if we know this particular type of path nets nothing
            if sub_right in self.memo:
                continue

            # all systems are clear, we can search this path
            if self.wordBreak(sub_right, wordDict):
                return True
        # if after searching all the paths and no results, then this path was false
        self.memo.add(s)
        return False


if __name__ == "__main__":

    s = 'leetcode'
    wordDict = ['leet', 'code']
    sol = Solution()
    result = sol.wordBreak(s, wordDict)
    assert result

    s = 'applepenapple'
    wordDict = ['apple', 'pen']
    sol = Solution()
    result = sol.wordBreak(s, wordDict)
    assert result

    s = 'catsandog'
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    sol = Solution()
    result = sol.wordBreak(s, wordDict)
    assert not result

    s = 'dig'
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    sol = Solution()
    result = sol.wordBreak(s, wordDict)
    assert not result
