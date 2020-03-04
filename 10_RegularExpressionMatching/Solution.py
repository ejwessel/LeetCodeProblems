class Solution:
    def isMatch(self, text, pattern):
        if len(text) == 0 and len(pattern) == 0:
            # if no more text and no more pattern we're good
            return True
        elif len(text) > 0 and len(pattern) == 0:
            # if we have text but no pattern then fail
            return False

        # boolean to help us determine if we have lengths to compare
        # also helps prevent out of bounds errors
        has_size = len(text) > 0 and len(pattern) > 0

        # handle star pattern
        if len(pattern) > 1 and pattern[1] == '*':
            # handle star match or .* match
            if has_size and (text[0] == pattern[0] or pattern[0] == '.'):
                # consume text or consume text and pattern
                return self.isMatch(text[1:], pattern) or \
                       self.isMatch(text, pattern[2:])
            else:
                # finished matching text, consume the pattern
                return self.isMatch(text, pattern[2:])
        elif has_size and (text[0] == pattern[0] or pattern[0] == '.'):
            # consume text and pattern
            return self.isMatch(text[1:], pattern[1:])
        elif not has_size:
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
