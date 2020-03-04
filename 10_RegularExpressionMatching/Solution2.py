class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.regExpRecursive(0, 0, s, p)

    def regExpRecursive(self, sPtr, rPtr, s, vRegex):
        if len(s) == sPtr and len(vRegex) == rPtr:
            return True
        elif len(s) == sPtr:
            if rPtr <= len(vRegex) - 2 and vRegex[rPtr + 1] == '*':
                return self.regExpRecursive(sPtr, rPtr + 2, s, vRegex)
            else:
                return False
        elif len(vRegex) <= rPtr:
            return False
        else:
            if rPtr <= len(vRegex) - 2 and vRegex[rPtr + 1] == '*':
                cprChar = vRegex[rPtr]
                if sPtr < len(s) and (s[sPtr] == cprChar or cprChar == '.'):
                    return self.regExpRecursive(sPtr, rPtr + 2, s, vRegex) or self.regExpRecursive(sPtr + 1,
                                                                                                   rPtr, s,
                                                                                                   vRegex)
                return self.regExpRecursive(sPtr, rPtr + 2, s, vRegex)
            elif vRegex[rPtr] == '.' or vRegex[rPtr] == s[sPtr]:
                return self.regExpRecursive(sPtr + 1, rPtr + 1, s, vRegex)
            else:
                return False

if __name__ == "__main__":
    sol = Solution()
    result = sol.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
    assert not result
    result = sol.isMatch("baaaaaaaaaaaaa", "a*a*a*a*a*a*a*a*a*a*")
    assert not result
    result = sol.isMatch("a", "..")
    assert not result
    result = sol.isMatch("a", ".*..a*")
    assert not result
    result = sol.isMatch("bcbbba", "b.*.*a*a")
    assert result
    result = sol.isMatch("bbbba", ".*a*a")
    assert result
    result = sol.isMatch("aaa", "a*a")
    assert result
    result = sol.isMatch("", "b*")
    assert result
    result = sol.isMatch("aa", "a")
    assert not result
    result = sol.isMatch("aa", "aa")
    assert result
    result = sol.isMatch("abc", "a.c")
    assert result
    result = sol.isMatch("a", "")
    assert not result
    result = sol.isMatch("", "")
    assert result
    result = sol.isMatch("abbb", "ab*")
    assert result
    result = sol.isMatch("abd", "ab*c")
    assert not result
    result = sol.isMatch("ab", "abcefg")
    assert not result
    result = sol.isMatch("", "ce")
    assert not result
    result = sol.isMatch("baa", ".*a*")
    assert result
