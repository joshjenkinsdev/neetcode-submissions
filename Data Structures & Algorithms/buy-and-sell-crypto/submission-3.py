class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell_ptr = 1
        buy_ptr = 0
        max_gain = 0
        if len(prices) == 1:
            return 0
        while sell_ptr < len(prices):
            if prices[buy_ptr] < prices[sell_ptr]:
                max_gain = max(max_gain, prices[sell_ptr] - prices[buy_ptr])
            else:
                buy_ptr = sell_ptr
            sell_ptr += 1
        return max_gain