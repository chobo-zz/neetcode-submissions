class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # top down memoization
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            res = float("infinity")

            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
                    memo[amount] = res
            return res
            
        
        minCoins = dfs(amount)
        return minCoins if minCoins < float("infinity") else -1
            