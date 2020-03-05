## Implement Trie (Prefix Tree)

Runtime:
- insert(word): O(n)
    - takes the length of the word to insert
- search(word): O(n)
    - takes the length of the word to search
- startsWith(prefix): O(n)
    - takes the length of the prefix to search
    
Space:
- insert(word): O(n)
    - takes the length of the word to insert
- search(word): O(n)
    - takes the length of the word to search in the recursive stack
- startsWith(prefix): O(n)
    - takes the length of the prefix to search in the recursive stack
