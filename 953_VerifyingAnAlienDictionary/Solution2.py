from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_to_idx = self.orderToIdx(order)
        for i in range(1, len(words)):
            result = self.isOrdered(words[i - 1], words[i], char_to_idx)
            if not result:
                return False
        return True

    def isOrdered(self, prev, current, order_idx):
        max_len = max(len(prev), len(current))
        for i in range(max_len):
            if i >= len(prev):
                break
            elif i >= len(current):
                return False

            prev_char = prev[i]
            current_char = current[i]

            if order_idx[prev_char] < order_idx[current_char]:
                break
            elif order_idx[prev_char] == order_idx[current_char]:
                continue
            elif order_idx[prev_char] > order_idx[current_char]:
                return False
        return True


    def orderToIdx(self, order):
        char_to_idx = {}
        for i in range(len(order)):
            char_to_idx[order[i]] = i
        return char_to_idx

if __name__ == "__main__":
    sol = Solution()

    output = sol.orderToIdx("hlabcdefgijkmnopqrstuvwxyz")
    assert output == {'h': 0, 'l': 1, 'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6, 'f': 7, 'g': 8, 'i': 9, 'j': 10, 'k': 11,
                      'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22,
                      'x': 23, 'y': 24, 'z': 25}

    result = sol.isAlienSorted(["hall", "hallow", "heb", "hef"], "hlabcdefgijkmnopqrstuvwxyz")
    assert result

    result = sol.isAlienSorted(["app", "apple", "ball"], "abcdefghijklmnopqrstuvwxyz")
    assert result

    result = sol.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz")
    assert not result

    result = sol.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
    assert result

    result = sol.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz")
    assert not result

    result = sol.isAlienSorted(["hall", "hallow", "halloween", "lab", "labrador", "apple", "barn"],
                               "hlabcdefgijkmnopqrstuvwxyz")
    assert result

    result = sol.isAlienSorted(["my", "f"], "gelyriwxzdupkjctbfnqmsavho")
    assert not result
