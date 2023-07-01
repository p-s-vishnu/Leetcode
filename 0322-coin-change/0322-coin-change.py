class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        T:O(n_coins * amount) 
        S:O(amount)
        """
        default = amount +1 
        dp = [0] + [default] * amount
        for c in coins:
            for i in range(c, amount+1):
                dp[i] = min(1+dp[i-c], dp[i])
        return -1 if dp[amount] == default else dp[amount]