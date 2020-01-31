class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""

        first_word = strs[0]
        word_list = strs[1:]
        lcp = ''

        for i in range(len(first_word)):
            temp = first_word[i]
            for word in word_list:
                if i >= len(word):
                    return lcp
                elif temp != word[i]:
                    return lcp
            lcp += temp
        return lcp


if __name__ == "__main__":

    sol = Solution()

    list = ['flower', 'flow', 'flight']
    result = sol.longestCommonPrefix(list)
    assert result == 'fl'

    list = ["dog","racecar","car"]
    result = sol.longestCommonPrefix(list)
    assert result == ''

    list = ["taco"]
    result = sol.longestCommonPrefix(list)
    assert result == 'taco'

    list = []
    result = sol.longestCommonPrefix(list)
    assert result == ''