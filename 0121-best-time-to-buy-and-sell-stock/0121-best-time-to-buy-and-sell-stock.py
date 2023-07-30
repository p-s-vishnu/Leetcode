class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        
        l = max_profit = 0
        for r in range(l+1, len(prices)):
            if prices[r] < prices[l]: l = r
            max_profit = max(max_profit, prices[r] - prices[l])
        return max_profit