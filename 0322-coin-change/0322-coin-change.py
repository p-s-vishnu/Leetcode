class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        T:O(n_coins * amount) 
        S:O(amount)
        """
        dp = {0:0}
        default = amount +1 
        for c in coins:
            for i in range(c, amount+1):
                dp[i] = min(1+dp.get(i-c, default), dp.get(i, default))
        return -1 if dp.get(amount, default) == default else dp[amount]