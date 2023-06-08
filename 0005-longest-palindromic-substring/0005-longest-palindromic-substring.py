from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        DP
        T:O(n2)
        S:O(n2)
        
        Expand from center logic
        T:O(n2)
        S:O(1)
        """
        dp = [ [False]*len(s) for _ in range(len(s)) ]
        ans = [0,0]
        
        # Initialisation - len of 1
        for i in range(len(s)):
            dp[i][i] = True
            
        # Initialisation - len of 2
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i, i+1]
    
        # Compute other lengths
        for diff in range(2, len(s)):
            for i in range(len(s) - diff):
                if s[i] == s[i+diff] and dp[i+1][i+diff-1]:
                    dp[i][i+diff] = True
                    ans = [i, i+diff]
        
        return s[ans[0]:ans[1]+1]
        
        # Brute force: O(n3) S:O(n2)
#         def isPalindrome(string):
#             return string == string[::-1]
        
#         d = defaultdict(list)		# key len: value list of strings
#         for i in range(len(s)):
#             for j in range(i+1, len(s)):
#                 s_slice = s[i:j]
#                 if len(s_slice)>0 and isPalindrome(s_slice):
#                     d[len(s_slice)].append(s_slice)
#         max_len = max(d.keys())
#         return d[max_len][0]
