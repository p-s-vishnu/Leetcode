class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        T:O(n*n + n*m*w ) 
        S:O(n)
        """
        dp = [True] + [False]*len(s)
        
        # n: len of s, O(n)
        for i in range(len(s)):
            if not dp[i]: 
                continue
                
            # O(n)
            substring = s[i:]
            # O(m), m: len of wordDict
            for word in wordDict:
                # O(w), w: average word length
                if substring.startswith(word):
                    dp[i+len(word)] = True

        return dp[-1]