from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = [(beginWord, 1)]
        while queue:
            current = queue.pop(0)
            # check if we found the word
            if current[0] == endWord:
                return current[1]

            #  traverse list to determine next elements to add
            i = 0
            while i < len(wordList):
                if self.isDistanceOne(wordList[i], current[0]):
                    queue.append((wordList[i], current[1] + 1))
                    # don't increment 1 here because the list is reduced by 1
                    wordList.pop(i)
                else:
                    i += 1
        return 0

    def isDistanceOne(self, w1, w2):
        found_change = False
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                if found_change:
                    return False
                found_change = True
        return found_change

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

