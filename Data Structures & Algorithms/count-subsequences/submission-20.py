class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def dfs(i, j): # returns distinct subsequences of s[i:] that make up t[j:]
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = 0
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
                res += dfs(i + 1, j)
            else:
                res += dfs(i + 1, j) 
            
            memo[(i, j)] = res
            return res
        
        return dfs(0, 0)
