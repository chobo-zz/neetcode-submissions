class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, canBuy): # returns max profit starting from index i and whether we can currently buy stock
            if i >= len(prices):
                return 0
            
            if (i, canBuy) in memo:
                return memo[(i, canBuy)]
            
            memo[(i, canBuy)] = 0
            if canBuy:
                profitIfBuy = dfs(i + 1, False) - prices[i] 
                profitIfCooldown = dfs(i + 1, True)
                memo[(i, canBuy)] = max(profitIfBuy, profitIfCooldown)
            else:
                profitIfSell = dfs(i + 2, True) + prices[i]
                profitIfCooldown = dfs(i + 1, False)
                memo[(i, canBuy)] = max(profitIfSell, profitIfCooldown)
            
            return memo[(i, canBuy)]
        
        return dfs(0, True)
