class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}

        def dfs(num):
            if num <= 1:
                return 0
            
            if num in memo:
                return memo[num]
            
            maxProduct = 0
            for i in range(1, num):
                withBreak = i * dfs(num - i)
                withoutBreak = i * (num - i)
                maxProduct = max(maxProduct, withBreak, withoutBreak)
            
            memo[num] = maxProduct
            return maxProduct
        
        return dfs(n)