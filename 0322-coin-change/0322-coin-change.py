class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        T:O(n_coins * amount) 
        S:O(amount)
        """
        dp = [0] + [amount+1]*amount
        
        for c in coins:
            for i in range(c, amount+1):
                dp[i] = min(dp[i], 1+dp[i-c])
                
        return -1 if dp[amount] == amount+1 else dp[amount]