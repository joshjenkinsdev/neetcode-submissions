class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        next1_hold0, next1_hold1 = 0, 0
        next2_hold0, next2_hold1 = 0, 0
        
        for i in range(len(prices) - 1, -1, -1):
            cur_hold0 = max(next1_hold0, next1_hold1 - prices[i])
            cur_hold1 = max(next1_hold1, next2_hold0 + prices[i])
            
            next2_hold0, next2_hold1 = next1_hold0, next1_hold1
            next1_hold0, next1_hold1 = cur_hold0, cur_hold1
        
        return next1_hold0