class CharNode:
    def __init__(self, char):
        self.char = char
        self.neighbors = dict()

class WordDictionary:
    """
    Recursive Approach
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.begin_node = CharNode(None)

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.addWordHelper(word, self.begin_node)

    def addWordHelper(self, word: str, current_node: CharNode):
        # no more word then the current character needs to have a terminator
        if word is '':
            current_node.neighbors['*'] = CharNode('*')
        else:
            # if the char is not in the neighbors add it
            if word[0] not in current_node.neighbors:
                current_node.neighbors[word[0]] = CharNode(word[0])
            # then move to it
            self.addWordHelper(word[1:], current_node.neighbors[word[0]])

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.searchHelper(word, self.begin_node)

    def searchHelper(self, word: str, current_node: CharNode):
        """
        :param word: the remaining word
        :param current_node: the current character we're at in the trie
        :return: true if the word exists, false otherwise
        """
        # if there is no more word and we can terminate at this word then great
        if len(word) == 0 and '*' in current_node.neighbors:
            return True
        # if there is no more word then we can't terminate
        elif len(word) == 0:
            return False

        # if the next character is a neighbor, jump to it
        if word[0] in current_node.neighbors:
            return self.searchHelper(word[1:], current_node.neighbors[word[0]])
        # next char is undetermined, jump to all neighbors
        elif word[0] is '.':
            for neighbor in current_node.neighbors.values():
                if self.searchHelper(word[1:], neighbor):
                    return True
        # no match, therefore word cannot be found, fail
        return False

if __name__ == "__main__":
    sol = WordDictionary()
    sol.addWord("bad")
    sol.addWord("dad")
    sol.addWord("mad")

    result = sol.search('pad')
    assert not result

    result = sol.search('bad')
    assert result

    result = sol.search('.ad')
    assert result

    result = sol.search('b..')
    assert result

    result = sol.search('b.m')
    assert not result

    result = sol.search('b...d')
    assert not result

    result = sol.search('b...')
    assert not result

    result = sol.search('b......')
    assert not result

    result = sol.search('...')
    assert result

    result = sol.search('..')
    assert not result

    sol.addWord('maddie')

    result = sol.search('madd')
    assert not result

    result = sol.search('madd.')
    assert not result


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)