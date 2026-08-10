class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, max_profit = 0,0
        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            max_profit = max(max_profit, prices[right] - prices[left])
        return max_profit