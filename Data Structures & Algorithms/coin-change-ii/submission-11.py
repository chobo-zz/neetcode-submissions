class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {} # (i, remaining) -> distinct combinations possible

        def dfs(i, remaining):
            if remaining == 0:
                return 1
            if remaining < 0 or i >= len(coins):
                return 0
            if (i, remaining) in memo:
                return memo[(i, remaining)]
                            
            memo[(i, remaining)] = dfs(i, remaining - coins[i]) + dfs(i + 1, remaining)
        
            return memo[(i, remaining)]

        return dfs(0, amount)