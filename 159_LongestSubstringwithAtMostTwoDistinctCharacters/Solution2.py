from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        longest_substring_length = 0
        start = 0
        end = 0
        freq_map = defaultdict(int)

        while end < len(s):
            # only add to the map and increase window size if the window has 2 distinct characters
            if len(freq_map.keys()) <= 2:
                freq_map[s[end]] += 1
                end += 1

            # only remove from the map and decrease window size if the window has more than 2 distinct characters
            if len(freq_map.keys()) > 2:
                freq_map[s[start]] -= 1
                # move to prevent key from being counted
                if freq_map[s[start]] == 0:
                    del freq_map[s[start]]
                start += 1

            # check if the window length is longer than current longest string
            candidate_substring_length = end - start
            longest_substring_length = max(longest_substring_length, candidate_substring_length)

        # print(longest_substring)
        return longest_substring_length

if __name__ == "__main__":

    sol = Solution()
    result = sol.lengthOfLongestSubstringTwoDistinct('eceba')
    assert result == 3

    result = sol.lengthOfLongestSubstringTwoDistinct('ccaabbb')
    assert result == 5

    result = sol.lengthOfLongestSubstringTwoDistinct('cacacabbbbccc')
    assert result == 7

    result = sol.lengthOfLongestSubstringTwoDistinct('abcdeegfg')
    assert result == 3





