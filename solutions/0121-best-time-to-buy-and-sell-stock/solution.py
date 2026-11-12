class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            profit = max(profit, prices[i] - min_price)  
        return profit
