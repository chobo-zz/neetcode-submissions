class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(i):
            if i >= len(s):
                return True
            if i in memo:
                return memo[i]

            res = False
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
                    if dfs(i + len(word)):
                        res = True
                        return res
            
            memo[i] = res
            return res
        
        return dfs(0)