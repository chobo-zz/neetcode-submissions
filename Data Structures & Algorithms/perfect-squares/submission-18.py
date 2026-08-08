class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}

        def dfs(remaining): # returns min num perfect squares that can sum up to remaining
            if remaining == 0:
                return 0
            
            if remaining in memo:
                return memo[remaining]
            
            minWays = float("inf")

            for num in range(int(math.sqrt(remaining)), 0, -1):
                square = num * num

                if square <= remaining:
                    minWays = min(minWays, 1 + dfs(remaining - square))
            
            memo[remaining] = minWays
            return minWays
        
        return dfs(n)