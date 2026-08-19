class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}

        def dfs(target): # returns max product that of target that can be split up to sum target
            if target == 1:
                return 0
            
            if target in memo:
                return memo[target]

            res = 0
            for i in range(1, target):
                withoutBreak = i * (target - i)
                withBreak = i * dfs(target - i)
                res = max(res, withoutBreak, withBreak)
            
            memo[target] = res
            return res
        
        return dfs(n)
