class Solution:
    def groupAnagrams(self, strs):
        freq_to_words = {}
        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word not in freq_to_words:
                freq_to_words[sorted_word] = []
            freq_to_words[sorted_word].append(word)

        result = []
        for key in freq_to_words.keys():
            result.append(freq_to_words[key])
        return result


if __name__ == "__main__":

    sol = Solution()

    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = sol.groupAnagrams(input)
    assert result == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
