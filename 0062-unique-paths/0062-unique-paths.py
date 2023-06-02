class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        T:O(n)
        S:O(n), space can be more optimised by only using one row approach
        """
        dp = [[1]*n] * m
        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
        return dp[0][0]