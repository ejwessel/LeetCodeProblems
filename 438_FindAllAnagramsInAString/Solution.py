from typing import List
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) == 0:
            return []
        if len(p) > len(s):
            return []

        p_freq = self.getFreq(p)
        freq_map = defaultdict(int)
        b = 0
        e = 0
        while e < len(p):
            freq_map[s[e]] += 1
            e += 1

        e = len(p) - 1

        answer = []
        while e < len(s):
            # check if the frequencies are the same
            if freq_map == p_freq:
                answer.append(b)

            # remove b char
            freq_map[s[b]] -= 1
            if freq_map[s[b]] == 0:
                del freq_map[s[b]]
            b += 1

            # add e char
            e += 1
            if e >= len(s):
                break
            freq_map[s[e]] += 1

        return answer

    def getFreq(self, s):
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        return freq


if __name__ == "__main__":
    sol = Solution()
    result = sol.findAnagrams("cbaebabacd", "abc")
    assert result == [0, 6]

    result = sol.findAnagrams("abab", "ab")
    assert result == [0, 1, 2]

    result = sol.findAnagrams("abab", "a")
    assert result == [0, 2]

    result = sol.findAnagrams("", "a")
    assert result == []

    result = sol.findAnagrams("b", "a")
    assert result == []

    result = sol.findAnagrams("a", "a")
    assert result == [0]

    result = sol.findAnagrams("abababababababab", "ab")
    assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    result = sol.findAnagrams("aaaaaaaaaa", "aaaaaaaaaaaaa")
    assert result == []
