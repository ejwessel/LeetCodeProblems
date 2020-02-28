class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        len_needle = len(needle)
        len_haystack = len(haystack)

        if len_needle == 0:
            return 0

        for i in range(len(haystack)):
            if i + len_needle > len_haystack:
                return -1

            h_i = i
            for n_i in range(len_needle):
                if haystack[h_i] != needle[n_i]:
                    break
                # continue to move forward if characters match
                h_i += 1

            # check if we made it to the end of the comparison
            if h_i == i + len_needle:
                return i

        # no result
        return -1


if __name__ == "__main__":
    sol = Solution()

    result = sol.strStr("hello", "ll")
    assert result == 2

    result = sol.strStr("aaaaa", "bba")
    assert result == -1

    result = sol.strStr("hammerammenrammerammer", "ammerammer")
    assert result == 12

    result = sol.strStr("hammer", "")
    assert result == 0
