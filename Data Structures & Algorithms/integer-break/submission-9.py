class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {} # (num -> max product of numbers (k >= 2) that can sum up to num)

        def dfs(num): # returns max product of numbers (k >= 2) that can sum up to num
            if num <= 1:
                return 0
                
            if num in memo:
                return memo[num]
            
            maxProduct = 0
            for i in range(1, num):
                withoutBreak = i * (num - i)
                withBreak = i * dfs(num - i)
                maxProduct = max(maxProduct, withoutBreak, withBreak)
            
            memo[num] = maxProduct
            return maxProduct
        
        return dfs(n)