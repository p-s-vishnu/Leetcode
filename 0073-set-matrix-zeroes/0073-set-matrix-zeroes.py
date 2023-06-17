class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        I: matrix, O:None
        2. if element 0 entire R,C 0 but no ripple effect
        3. TC
            center 0
            overlapping 0s
            No 0s
        4. 2 pass save rows and cols to be 0. T:O(mn) S:O(m+n)
            2 pass inplace make all rows and cols None, then 2nd pass None to 0. T:O(m*n*(m+n)), S:O(1)
        """
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] is None or matrix[r][c] != 0:
                    continue
                for r0 in range(len(matrix)):
                    if matrix[r0][c] != 0:
                        matrix[r0][c] = None
                
                for c0 in range(len(matrix[0])):
                    if matrix[r][c0] != 0:
                        matrix[r][c0] = None
        
        # pass 2 to make None to 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] is None:
                    matrix[r][c] = 0
                    