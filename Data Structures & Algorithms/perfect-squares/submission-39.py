class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}

        def dfs(target):
            if target == 0:
                return 0
            
            if target in memo:
                return memo[target]

            res = float("inf")
            for i in range(int(math.sqrt(target)), 0, -1):
                square = i * i
                res = min(res, 1 + dfs(target - square))
            memo[target] = res
            return res
        
        return dfs(n)
