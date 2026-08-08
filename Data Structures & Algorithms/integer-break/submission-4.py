class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}

        def dfs(num): # returns max product for sum of k integers that make up num

            if num in memo:
                return memo[num]
            
            maxProduct = 0
            for i in range(1, num):
                maxProduct = max(
                    maxProduct, 
                    i * max(num - i, dfs(num - i))
                )
        
            memo[num] = maxProduct
            return maxProduct
        
        return dfs(n)
            
