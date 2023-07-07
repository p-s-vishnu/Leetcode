from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        T: O(r*c)
        S: O(r + c)
        """
        rows, cols, box = defaultdict(set),defaultdict(set),defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if r in rows and board[r][c] in rows[r]: 
                    return False
                if c in cols and board[r][c] in cols[c]: 
                    return False
                b_idx = (r//3)*3+c//3
                if b_idx in box and board[r][c] in box[b_idx]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                box[b_idx].add(board[r][c])
                
        return True