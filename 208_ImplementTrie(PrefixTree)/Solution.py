class CharNode:
    def __init__(self, char):
        self.char = char
        self.next_nodes = dict()
        self.is_word = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.start = CharNode(None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.insertHelper(word, self.start)

    def insertHelper(self, word: str, current_node: CharNode):
        if word is '':
            current_node.is_word = True
        else:
            if word[0] not in current_node.next_nodes:
                current_node.next_nodes[word[0]] = CharNode(word[0])
            self.insertHelper(word[1:], current_node.next_nodes[word[0]])

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.searchHelper(word, self.start)

    def searchHelper(self, word: str, current_node: CharNode):
        # if we have found a word
        if len(word) == 0 and current_node.is_word:
            return True
        # if we've run out of characters, but the character we stopped at is non terminating
        elif len(word) == 0:
            return False
        # if the word is not in the next nodes
        elif word[0] not in current_node.next_nodes:
            return False
        return self.searchHelper(word[1:], current_node.next_nodes[word[0]])


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.startsWithHelper(prefix, self.start)

    def startsWithHelper(self, word, current_node):
        if len(word) == 0:
            return True
        if word[0] not in current_node.next_nodes:
            return False
        return self.startsWithHelper(word[1:], current_node.next_nodes[word[0]])

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    result = trie.search("apple")
    assert result
    result = trie.search('app')
    assert not result
    result = trie.startsWith('app')
    assert result
    trie.insert("app")
    result = trie.search('app')
    assert result
    result = trie.startsWith('app')
    assert result

    trie.insert("bananas")
    result = trie.startsWith("banana")
    assert result
    result = trie.startsWith("bananaz")
    assert not result
    result = trie.startsWith("bananazzzz")
    assert not result


