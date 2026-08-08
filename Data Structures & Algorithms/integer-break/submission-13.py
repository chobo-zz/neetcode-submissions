class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}

        # returns max product of numbers that also sum up to num
        def dfs(num):
            if num <= 1: # any number less than 2 cannot be broken up any further
                return 0
            
            if num in memo:
                return memo[num]
            
            maxProduct = 0
            
            # we choose all numbers i from range 1 to num - 1 that will be subtracted from num 
            # and check product of those numbers (num - i) * i
            # for each number chosen, we have two choices: do not break and break.
            for i in range(1, num):
                withoutBreak = i * (num - i)
                withBreak = i * dfs(num - i)
                maxProduct = max(maxProduct, withoutBreak, withBreak)
            
            memo[num] = maxProduct
            return maxProduct
        
        return dfs(n)
            