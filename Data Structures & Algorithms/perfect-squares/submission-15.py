class Solution:
    def numSquares(self, n: int) -> int:
        memo = { 0: 0 } # (number -> min number of perfect squares that sum to number)

        def dfs(num): # returns min number of perfect squares that sum to num
            if num in memo:
                return memo[num]
            
            numSquares = num
            for i in range(int(math.sqrt(num)) + 1, 0, -1):
                square = i * i
                if square <= num:
                    numSquares = min(numSquares, 1 + dfs(num - square))
            
            memo[num] = numSquares
            return numSquares
        
        return dfs(n)