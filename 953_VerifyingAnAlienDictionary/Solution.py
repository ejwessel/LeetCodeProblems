from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_to_idx = self.orderToIdx(order)
        longest_len = self.lenOfLongestWord(words)

        # go through all character indices
        for i in range(longest_len):
            # go through all words
            for w in range(1, len(words)):
                prev_word = words[w - 1]
                current_word = words[w]

                # compare the prefix first
                prev_prefix = prev_word[:i]
                current_prefix = current_word[:i]

                if prev_prefix is '' and current_prefix is '':
                    # no substring is empty, continue
                    continue
                elif prev_prefix != current_prefix:
                    # prev prefix and current prefix are not comparable continue
                    continue
                # if index can't be reached then order is maintained
                if i >= len(prev_word):
                    continue

                # if prev word is greater than current word order is not maintained
                # don't compare words if the length is not at least 2
                if i > 1 and len(prev_word) > len(current_word):
                    return False

                # detect if ordering is incorrect
                prev_char = prev_word[i]
                current_char = current_word[i]
                if char_to_idx[prev_char] > char_to_idx[current_char]:
                    return False

        return True

    def orderToIdx(self, order):
        char_to_idx = {}
        for i in range(len(order)):
            char_to_idx[order[i]] = i
        return char_to_idx

    def lenOfLongestWord(self, words):
        longest_len = 0
        for word in words:
            longest_len = max(longest_len, len(word))
        return longest_len


if __name__ == "__main__":
    sol = Solution()

    output = sol.orderToIdx("hlabcdefgijkmnopqrstuvwxyz")
    assert output == {'h': 0, 'l': 1, 'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6, 'f': 7, 'g': 8, 'i': 9, 'j': 10, 'k': 11,
                      'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22,
                      'x': 23, 'y': 24, 'z': 25}

    result = sol.isAlienSorted(["hall", "hallow", "heb", "hef"], "hlabcdefgijkmnopqrstuvwxyz")
    assert result

    output = sol.lenOfLongestWord(["hello", "leetcode"])
    assert output == 8

    result = sol.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
    assert result

    result = sol.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz")
    assert not result

    result = sol.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz")
    assert not result

    result = sol.isAlienSorted(["hall", "hallow", "halloween", "lab", "labrador", "apple", "barn"], "hlabcdefgijkmnopqrstuvwxyz")
    assert result

