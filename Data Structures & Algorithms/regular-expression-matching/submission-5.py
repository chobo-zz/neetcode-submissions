class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {} # (i, j) -> boolean

        def dfs(i, j): # returns whether s[i:] matches p[j:]
            if j >= len(p):
                return i >= len(s) # if j reached end, either we matched strings or didn't 

            if (i, j) in memo:
                return memo[(i, j)]
            
            isMatch = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if (j + 1) < len(p) and p[j + 1] == "*":
                res = (
                    (isMatch and dfs(i + 1, j)) or # choose *
                    dfs(i, j + 2)                  # do not choose *
                )
                memo[(i, j)] = res
                return res
            
            if isMatch:
                res = dfs(i + 1, j + 1) # characters match but is not wildcard matching
                memo[(i, j)] = res
                return res
            
            # previous two if-blocks failed to match, so we return False by default
            memo[(i, j)] = False
            return False

        return dfs(0, 0)