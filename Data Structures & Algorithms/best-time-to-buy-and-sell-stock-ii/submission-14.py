class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {} # (i, bought) -> max profit

        def dfs(i, buying):
            if i == len(prices):
                return 0
            
            if (i, buying) in memo:
                return memo[(i, buying)]
            if buying:
                profitIfSkip = dfs(i + 1, True)
                profitIfBuy = -prices[i] + dfs(i + 1, False)
                res = max(profitIfSkip, profitIfBuy)
            else:
                profitIfSell = prices[i] + dfs(i + 1, True)
                profitIfSkip = dfs(i + 1, False)
                res = max(profitIfSell, profitIfSkip)
            
            memo[(i, buying)] = res
            return res
        
        return dfs(0, True)

