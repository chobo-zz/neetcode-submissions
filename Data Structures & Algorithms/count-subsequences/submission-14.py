class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {} # (i, j) -> num of subsequences
        if len(t) > len(s):
            return 0

        def dfs(i, j):
            if j >= len(t):
                return 1
            
            if i >= len(s) and j < len(t):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = 0
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                res += dfs(i + 1, j)
                
            memo[(i, j)] = res
            return res
        
        return dfs(0, 0)