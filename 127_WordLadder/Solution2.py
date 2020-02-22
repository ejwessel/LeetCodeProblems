from typing import List
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_combo = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]
                word_combo[key].append(word)

        queue = deque()
        queue.append((beginWord, 1))

        while queue:
            current_word, depth = queue.popleft()

            if current_word == endWord:
                return depth

            for i in range(len(current_word)):
                key = current_word[:i] + '*' + current_word[i + 1:]
                for prospective_words in word_combo[key]:
                    queue.append((prospective_words, depth + 1))
                # after adding everything zero out the list so that we can ignore it
                word_combo[key] = []

        return 0


if __name__ == "__main__":
    # sol = Solution()
    # result = sol.isDistanceOne('hot', 'dog')
    # assert not result
    # result = sol.isDistanceOne('hot', 'hog')
    # assert result

    sol = Solution()
    begin = 'hit'
    end = 'cog'
    wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
    result = sol.ladderLength(begin, end, wordList)
    assert result == 5

    sol = Solution()
    begin = 'hit'
    end = 'cog'
    wordList = ['hot', 'dot', 'dog', 'lot', 'log']
    result = sol.ladderLength(begin, end, wordList)
    assert result == 0

