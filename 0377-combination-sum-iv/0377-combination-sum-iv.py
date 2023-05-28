class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        T:O(n*m) 
        S:O(n)
        """
        dp = [1] + [0]*target

        for i in range(1, target+1):
            for n in nums:
                if i >= n:
                    dp[i] += dp[i-n]

        return dp[target]
    