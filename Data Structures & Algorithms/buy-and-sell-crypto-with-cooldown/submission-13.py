class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            
            if (i, canBuy) in memo:
                return memo[(i, canBuy)]
            
            maxProfit = 0
            if canBuy:
                profitIfBuy = -prices[i] + dfs(i + 1, False)
                profitIfSkip = dfs(i + 1, True)
                maxProfit = max(profitIfBuy, profitIfSkip)
            else:
                profitIfSell = prices[i] + dfs(i + 2, True)
                profitIfSkip = dfs(i + 1, False)
                maxProfit = max(profitIfSell, profitIfSkip)
            
            memo[(i, canBuy)] = maxProfit
            return maxProfit
        
        return dfs(0, True)