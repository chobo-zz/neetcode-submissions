class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {} # (i, buying) -> max profit starting from i

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            if buying:
                profitIfBuy = dfs(i + 1, False) - prices[i]
                profitIfCoolDown = dfs(i + 1, True)
                maxProfit = max(profitIfBuy, profitIfCoolDown)
                memo[(i, buying)] = maxProfit
            else:
                profitIfSell = dfs(i + 2, True) + prices[i]
                profitIfCoolDown = dfs(i + 1, False)
                maxProfit = max(profitIfSell, profitIfCoolDown)
                memo[(i, buying)] = maxProfit
            return memo[(i, buying)]
        
        return dfs(0, True)