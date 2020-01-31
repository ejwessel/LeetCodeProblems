class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""

        min_length = self.min_len(strs)
        lcp = ""
        for i in range(min_length):
            i_char = None
            for word in strs:
                if i_char is None:
                    i_char = word[i]
                elif i_char != word[i]:
                    return lcp
            lcp += i_char
        return lcp

    def min_len(self, strs):
        min_length = None
        for word in strs:
            if min_length is None:
                min_length = len(word)
            else:
                min_length = min(min_length, len(word))

        return min_length


if __name__ == "__main__":

    sol = Solution()

    list = ['flower', 'flow', 'flight']
    result = sol.min_len(list)
    assert result == 4
    result = sol.longestCommonPrefix(list)
    assert result == 'fl'

    list = ["dog","racecar","car"]
    result = sol.min_len(list)
    assert result == 3
    result = sol.longestCommonPrefix(list)
    assert result == ''

    list = ["taco"]
    result = sol.min_len(list)
    assert result == 4
    result = sol.longestCommonPrefix(list)
    assert result == 'taco'

    list = []
    result = sol.min_len(list)
    assert result == None
    result = sol.longestCommonPrefix(list)
    assert result == ''