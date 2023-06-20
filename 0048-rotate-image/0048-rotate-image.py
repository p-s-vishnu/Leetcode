class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix) - 1
        if r == 0:
            return
        
        while l < r:
            for i in range(r-l):
                top, bottom = l, r
                topleft = matrix[top][l+i]
                
                matrix[top][l+i] = matrix[bottom-i][l]              # move tl = bl 
                matrix[bottom-i][l]  = matrix[bottom][r-i]          # bl = br
                matrix[bottom][r-i] = matrix[top+i][r]              # br = tr
                matrix[top+i][r] = topleft                          # tr = tl
            l += 1
            r -= 1
                