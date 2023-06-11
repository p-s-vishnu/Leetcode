class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        T: O(RC)
        S: O(logRC) 
        """
        R, C = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r,c):
            if (r,c) in visited or r < 0 or c < 0 or c >= C or r >= R or grid[r][c] != "1":
                return
            visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        islands = 0
        for i in range(R):
            for j in range(C):
                if (i,j) not in visited and grid[i][j]=="1":
                    islands += 1
                    dfs(i, j)
        
        return islands