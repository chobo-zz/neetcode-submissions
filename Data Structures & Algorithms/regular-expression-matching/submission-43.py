class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True
            
            if j >= len(p):
                return False
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] = False
            isMatch = i < len(s) and (p[j] == "." or s[i] == p[j])
            if (j + 1) < len(p) and p[j + 1] == "*":
                memo[(i, j)] = (isMatch and dfs(i + 1, j)) or dfs(i, j + 2)
            else:
                memo[(i, j)] = isMatch and dfs(i + 1, j + 1)
            return memo[(i, j)]
        
        return dfs(0, 0)