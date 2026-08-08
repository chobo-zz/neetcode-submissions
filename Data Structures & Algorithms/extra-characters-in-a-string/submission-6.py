class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        memo = {}
        dictionary = set(dictionary)

        def dfs(i): # returns min number extra chars to break up s into dict words
            if i == len(s):
                return 0
            
            if i in memo:
                return memo[i]
            
            res = 1 + dfs(i + 1)
            for j in range(i, len(s)):
                word = s[i : j + 1]
                if word in dictionary:
                    res = min(res, dfs(j + 1))
            memo[i] = res
            return res
        
        return dfs(0)