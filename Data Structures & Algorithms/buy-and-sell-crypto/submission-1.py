class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(0, len(prices)):
            min_future_amount = 0
            window = prices[i+1:]
            for sell_price in window:
                if prices[i] < sell_price:
                    min_future_amount = max(min_future_amount, sell_price - prices[i])
            max_profit = max(max_profit, min_future_amount)
        return max_profit