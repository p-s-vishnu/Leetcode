class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Time & space = O(n)
        Bottom up - tabulation
        """
        dp = {len(s): 1}    # for empty string
        
        for i in range(len(s)-1, -1, -1):
            # single digit
            dp[i] = dp[i+1] if s[i] != '0' else 0
            
            # double digit check
            if i+1 < len(s) and (s[i] == '1' or (s[i]=='2' and s[i+1] in '0123456')): 
                dp[i] += dp[i+2]
        
        return dp[0]