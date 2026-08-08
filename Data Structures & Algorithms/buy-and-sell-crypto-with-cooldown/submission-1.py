class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {} # (ith day, buying/selling) -> max profit

        def dfs(i, buying): # returns max profit at ith day
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            if buying:
                profitIfBuy = dfs(i + 1, False) - prices[i]
                profitIfCooldown = dfs(i + 1, True)
                maxProfit = max(profitIfBuy, profitIfCooldown)
                memo[(i, buying)] = maxProfit
            else:
                profitIfSell = dfs(i + 2, True) + prices[i]
                profitIfCooldown = dfs(i + 1, False)
                maxProfit = max(profitIfSell, profitIfCooldown)
                memo[(i, buying)] = maxProfit
            return memo[(i, buying)]
        
        return dfs(0, True)