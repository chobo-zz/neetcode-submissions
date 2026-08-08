class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {} 

        def dfs(i): # how many ways to decode to end starting at index i
            if i >= len(s):
                return 1
            
            if i in memo:
                return memo[i]

            if s[i] == "0":
                return 0
            
            res = 0
            res += dfs(i + 1)

            if (i + 1) < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                res += dfs(i + 2)
            
            memo[i] = res

            return memo[i]
        
        return dfs(0)
