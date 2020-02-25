A_bound = 65
Z_bound = 90
zero_bound = 48
nine_bound = 57

class Solution:
    def isPalindromeAscii(self, s: str) -> bool:
        begin = 0
        end = len(s) - 1
        while begin < end:
            # if not alpha numeric
            begin_ascii = ord(s[begin].upper())
            if not(zero_bound <= begin_ascii <= nine_bound) and not(A_bound <= begin_ascii <= Z_bound):
                begin += 1
                continue

            # if not alpha numeric
            end_ascii = ord(s[end].upper())
            if not (zero_bound <= end_ascii <= nine_bound) and not (A_bound <= end_ascii <= Z_bound):
                end -= 1
                continue

            # check if characters match
            if s[begin].upper() != s[end].upper():
                return False

            # move closer to center if they are
            begin += 1
            end -= 1
        return True

    def isPalindrome(self, s: str) -> bool:
        begin = 0
        end = len(s) - 1
        while begin < end:
            # if not alpha numeric
            if not s[begin].isalnum():
                begin += 1
                continue

            # if not alpha numeric
            if not s[end].isalnum():
                end -= 1
                continue

            # check if characters match
            if s[begin].upper() != s[end].upper():
                return False

            # move closer to center if they are
            begin += 1
            end -= 1
        return True


if __name__ == "__main__":
    sol = Solution()

    result = sol.isPalindrome('abba')
    assert result

    result = sol.isPalindrome('abbca')
    assert not result

    result = sol.isPalindrome('')
    assert result

    result = sol.isPalindrome('A man, a plan, a canal: Panama')
    assert result

    result = sol.isPalindrome('race a car')
    assert not result

