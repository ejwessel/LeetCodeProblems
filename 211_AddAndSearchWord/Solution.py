class CharNode:
    def __init__(self, char):
        self.char = char
        self.neighbors = dict()

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.max_size = 0
        self.word_dict = set()
        self.starting_chars = dict()
        self.chars = dict()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.max_size = max(self.max_size, len(word))
        self.word_dict.add(word)

        # create starting node if needed for starting char
        char_start = word[0]
        if char_start not in self.chars:
            self.chars[char_start] = CharNode(char_start)
        # add the first character to starting characters
        self.starting_chars[char_start] = self.chars[char_start]

        # link up chars
        current_node = self.chars[char_start]
        for i in range(1, len(word)):
            current_char = word[i]
            if current_char not in self.chars:
                self.chars[current_char] = CharNode(current_char)
            # link the chars together if needed
            current_node.neighbors[current_char] = self.chars[current_char]
            # update current node
            current_node = self.chars[current_char]



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if len(word) > self.max_size:
            return False
        elif word in self.word_dict:
            return True
        elif word is '':
            return False

        if word[0] is '.':
            for start in self.starting_chars:
                if self.searchHelper(word[1:], start):
                    return True
        elif word[0] in self.starting_chars:
            return self.searchHelper(word[1:], word[0])

    def searchHelper(self, word: str, prev: str):
        if word is '':
            return True

        # if we have any char then go through prev char neighbors looking for answer
        if word[0] is '.':
            for neighbor in self.chars[prev].neighbors:
                if self.searchHelper(word[1:], neighbor):
                    return True
        elif word[0] in self.chars:
            return self.searchHelper(word[1:], word[0])
        else:
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

    # this method won't work because I've associated nodes improperly

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)