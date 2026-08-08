class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {} # (i, j) -> true

        def dfs(i, j):
            if j == len(p):
                return i == len(s)

            if (i, j) in memo:
                return memo[(i, j)]

            isMatch = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if (j + 1) < len(p) and p[j + 1] == "*":
                res = (
                    isMatch and dfs(i + 1, j) or
                    dfs(i, j + 2)
                )
            else:
                res = isMatch and dfs(i + 1, j + 1)
            
            memo[(i, j)] = res
            return res

        return dfs(0, 0)