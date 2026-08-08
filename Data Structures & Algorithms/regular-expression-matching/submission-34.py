class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i, j): # returns whether s[i:] can match on p[j:]
            if i >= len(s) and j >= len(p):
                return True

            if j >= len(p):
                return False
            
            if (i, j) in memo:
                return memo[(i, j)]
            res = False
            isMatch = i < len(s) and (p[j] == "." or p[j] == s[i])

            if (j + 1) < len(p) and p[j + 1] == "*":
                res = (isMatch and dfs(i + 1, j)) or dfs(i, j + 2)
            else:
                res = isMatch and dfs(i + 1, j + 1)
            
            memo[(i, j)] = res
            return res
        
        return dfs(0, 0)
