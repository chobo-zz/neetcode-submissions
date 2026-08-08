class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remaining): # min ways to make up remaining with given coins
            if remaining == 0:
                return 0
        
            
            if remaining in memo:
                return memo[remaining]
            
            res = float("inf")
            for coin in coins:
                if coin <= remaining:
                    res = min(res, 1 + dfs(remaining - coin))
            
            memo[remaining] = res
            return res
        
        minCoins = dfs(amount)
        return minCoins if minCoins != float("inf") else -1