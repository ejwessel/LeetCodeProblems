class Solution:
    def validPalindromeInoptimal(self, s: str) -> bool:
        for i in range(len(s)):
            left = s[:i]
            right = s[i + 1:]
            new_string = left + right
            if new_string == new_string[::-1]:
                return True
        return False

    def validPalindrome(self, s: str) -> bool:
        # if the incoming string is already a palindrome
        if s == s[::-1]:
            return True

        # it must be possible to remove one char
        # use two pointers
        b = 0
        e = len(s) - 1
        while b < e:
            # if characters match move pointers closer
            if s[b] == s[e]:
                b += 1
                e -= 1
            else:
                # if we're here it means there is a possibility of a character being removed
                left_str = s[b:e]  # [b, e)
                right_str = s[b + 1:e + 1]  # (b, e]

                # if either side is 1 character we have a palindrome
                if len(left_str) == 1 or len(right_str) == 1:
                    return True

                # it's possible that either the left or right variation of this is a palindrome.
                # check both sides since it could be that either side is a palindrome
                left_truth = left_str == left_str[::-1]
                right_truth = right_str == right_str[::-1]
                return left_truth or right_truth


if __name__ == "__main__":
    sol = Solution()
    result = sol.validPalindrome('abca')
    assert result

    result = sol.validPalindrome('ebcbbececabbacecbbcbe')
    assert result

    result = sol.validPalindrome('aba')
    assert result

    result = sol.validPalindrome('abckba')
    assert result

    result = sol.validPalindrome('abcbkka')
    assert not result

    result = sol.validPalindrome('abcbka')
    assert result

    result = sol.validPalindrome('abc')
    assert not result

