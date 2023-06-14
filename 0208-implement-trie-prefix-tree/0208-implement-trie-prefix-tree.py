class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    """
    T:O(m)
    S:O(m)
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        p = self.root
        for w in word:
            if w not in p.children:
                p.children[w] = TrieNode()
            p = p.children[w]
        p.is_word = True

    def search(self, word: str) -> bool:
        p = self.root
        for w in word:
            if w not in p.children:
                return False
            p = p.children[w]
        return p.is_word

    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for w in prefix:
            if w not in p.children:
                return False
            p = p.children[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)