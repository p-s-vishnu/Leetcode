class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
    def insert(self, word):
        p = self
        for w in word:
            if w not in p.children:
                p.children[w] = TrieNode()
            p = p.children[w]
        p.is_word = True

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        1. I: (List[List[str]], str) O: bool
        2. all lower case? min 1 word len and matrix min 1
        3. normal, duplicate 
            lower matrix and upper word
        4. DFS Trie, T:O(m*n*4^(w)) S:O(m*n)
        """
        R, C = len(board), len(board[0])
        visited = set()
        root = TrieNode()
        root.insert(word)
        
        
        
        def dfs(i, j, w, node):
            if (i,j) in visited or w not in node.children:
                return False
            visited.add((i, j))
            node = node.children[w]
            if node.is_word:
                return True
            if i > 0:       
                if dfs(i-1, j, board[i-1][j], node):
                    return True
            if i < R-1:     
                if dfs(i+1, j, board[i+1][j], node):
                    return True
            if j > 0:       
                if dfs(i, j-1, board[i][j-1], node):
                    return True
            if j < C-1:     
                if dfs(i, j+1, board[i][j+1], node):
                    return True
            visited.remove((i,j))
            return False
        
        for r in range(R):
            for c in range(C):
                if dfs(r, c, board[r][c], root):
                    return True
        return False
                