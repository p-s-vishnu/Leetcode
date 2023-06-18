class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        1. I:List[List[int]] O:List[int] in spiral order
        2. H&C
            [(0,1), (1,0),(0,-1),(-1,0)]
            -100 <= matrix[r][c] <= 100
            1 <= m, n <= 10
            matrix = m and n can be different
            no space or time constraints
            unique?
        3. TC
            normal - 3x3
            min - 1x1
            same evenxeven - 4x4
            evenxeven - 4x8
            oddxeven - 3x6
            evenxodd - 6x3
            
        4. Approaches
            4.1 Brute force [(0,1), (1,0),(0,-1),(-1,0)] and visited set
                T:O(mn) S:O(mn)
            4.2 Do not use visited set instead mark as something -> S:O(1) if output not considered in space needed
        """
        R,C = len(matrix), len(matrix[0])
        result = []
        visited = set()
        idx = 0 
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        r, c = 0,-1
        
        while len(visited) != R*C:
            i, j = directions[idx%4]
            while (r+i,c+j) not in visited and 0 <= r+i < R and 0 <= c+j < C:
                r, c = r+i, c+j
                visited.add((r,c))
                result.append(matrix[r][c])
            idx += 1
        return result