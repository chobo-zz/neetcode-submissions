class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        memo = {} # (i, j) -> num distinct subsequences


        def dfs(i, j): # index of s, index of t
            if i >= len(s) and j < len(t):
                return 0

            if j >= len(t):
                return 1
            
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
