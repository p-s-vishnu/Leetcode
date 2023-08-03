class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        1. I: List[int] O:bool
        2. sorted - increasing order, first int gt last of prev row
            n:rows, m:cols
        3. [[1,3,4,6], [7,8,9,10], [11,12,13,14]] target:10, O:True
        4. bsearch - T:O(log(nm)) S:O(1)
        """
        def condition(mid):
            return target > matrix[mid // c][mid % c] 
        
        r, c =  len(matrix),  len(matrix[0])
        l, r = 0, r*c -1
        while l < r:
            mid = l + (r-l)//2
            if condition(mid):
                l = mid + 1
            else:
                r = mid
                
        return matrix[l // c][l % c] == target