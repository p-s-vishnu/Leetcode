class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        1. I:List[List[int] O: List[int]
        2. T:(MN) S:O(1) Result excluded
        3. M!=N, 1x1, Mx1, 1xN
        4. 
        """
        if not matrix:
            return []
    
        res = []
        n, m = len(matrix), len(matrix[0])
        r = c = 0
        going_up = True
        
        while r < n and c < m:
            if going_up:
                while r >=0 and c < m:
                    res.append(matrix[r][c])
                    r -= 1
                    c += 1
                if c == m:
                    c -= 1
                    r += 2
                else:
                    r += 1
            else:
                while r < n and c >=0:
                    res.append(matrix[r][c])
                    r += 1
                    c -= 1
                if r == n:
                    r -= 1
                    c += 2
                else:
                    c += 1
            going_up = not going_up
            
        return res