class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        1. I: (str, str) O: int longest common sub sequence
        2. subsequence can be none without changing relative order
            min 1 len, only lowercase
        3.  some match - spread charas
            no match
            all match
            first match not the max: "oxcpqrsvwf" "shmtulqrypy"
        4. DP: T:O(nm) S:(nm)
        """
        R, C = len(text1), len(text2)
        dp = {(r, C): 0 for r in range(R)}
        dp.update({(R, c): 0 for c in range(C)})
        
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[(i,j)] = 1 + dp.get((i+1,j+1), 0)
                else:
                    dp[(i,j)] = max(dp.get((i+1,j), 0), dp.get((i,j+1), 0))
        return dp[(0,0)]