class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, canBuy): # returns max profit starting on ith day and whether we can buy or not
            if i >= len(prices):
                return 0
            
            if (i, canBuy) in memo:
                return memo[(i, canBuy)]
            
            if canBuy:
                profitIfBuy = dfs(i + 1, False) - prices[i]
                profitIfCooldown = dfs(i + 1, True)
                maxProfit = max(profitIfBuy, profitIfCooldown)
            else:
                profitIfSell = dfs(i + 2, True) + prices[i]
                profitIfCooldown = dfs(i + 1, False)
                maxProfit = max(profitIfSell, profitIfCooldown)
            
            memo[(i, canBuy)] = maxProfit
            return maxProfit
        
        return dfs(0, True)