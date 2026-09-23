class TrieNode:

    def __init__ (self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        

    def search(self, word: str) -> bool:
        
        return self.search_rec(word, 0, self.root)
                
            
    def search_rec(self, word, i, node):
        cur = node

        for j in range(i, len(word)):
            c = word[j]

            if c == '.':
                for k in cur.children.values():
                    if self.search_rec(word, j + 1, k):
                        return True
                return False

            if c not in cur.children:
                return False

            cur = cur.children[c]
        return cur.endOfWord