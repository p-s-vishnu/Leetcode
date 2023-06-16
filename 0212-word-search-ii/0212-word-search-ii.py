class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
    def add_word(self, word):
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.is_word = True
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        1. I: List[List[str]] O: List[str] matches
        2. Highlights/Constraints
            Acceptable Vertical and horizontal match both forward and backward
            Letters of Words are unique
            Lowercase letters only
        3. TC
            Duplicate letters children of same letter
        4. Approaches
            1. Brute force DFS - w*m*n*4^(w) - 4^(w) or 4^(m*n) based on implementation
                4 direction movement, w is the length of the word being added
            2. Trie implementation: T: O(m*n*4^(w)) S:O(total words len + m*n)
        5. Code and test
        """
        # build trie
        trie = TrieNode()
        for w in words:
            trie.add_word(w)
        
        result = set()
        visited = set()
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(i, j, node, w = ''):
            if (i, j) in visited or board[i][j] not in node.children:
                return
            visited.add((i,j))
            w = w+board[i][j]
            node = node.children[board[i][j]]
            if node.is_word:
                result.add(w)
                
            if i>0:         dfs(i-1, j, node, w)
            if i<ROWS-1:    dfs(i+1, j, node, w)
            if j>0:         dfs(i, j-1, node, w)
            if j<COLS-1:    dfs(i, j+1, node, w)
            visited.remove((i,j))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie) 
        return list(result)