class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, remaining): # returns distinct combos starting at index i, with remaining amount
            if remaining == 0:
                return 1
            
            if i >= len(coins) or remaining < 0:
                return 0
            
            if (i, remaining) in memo:
                return memo[(i, remaining)]
            
            res = 0
            res += dfs(i + 1, remaining)
            res += dfs(i, remaining - coins[i])
            
            memo[(i, remaining)] = res
            return res

        return dfs(0, amount)