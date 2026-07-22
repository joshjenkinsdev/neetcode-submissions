class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        slow, fast = 0, 1
        max_profit = 0
        while fast < len(prices):
            if prices[slow] < prices[fast]:
                max_profit = max(max_profit, prices[fast]-prices[slow])
            else:
                slow = fast
            fast += 1

        return max_profit