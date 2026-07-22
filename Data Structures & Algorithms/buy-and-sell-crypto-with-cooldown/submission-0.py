class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, holding):
            # base case: ran out of days
            if i >= len(prices):
                return 0
            
            if (i, holding) in memo:
                return memo[(i, holding)]

            # option 1: do nothing today (always available)
            skip = dfs(i + 1, holding)
            
            if holding:
                # option 2: sell today
                sell = dfs(i + 2, False) + prices[i]
                result = max(skip, sell)
            else:
                # option 3: buy today
                buy = dfs(i + 1, True) - prices[i]
                result = max(skip, buy)
            
            memo[(i, holding)] = result
            return result
        
        return dfs(0, False)

