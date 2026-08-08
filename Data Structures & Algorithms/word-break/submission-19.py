class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(i): # returns if we can segment s with given words starting from index i
            if i >= len(s):
                return True
            
            if i in memo:
                return memo[i]
            
            memo[i] = False
            for word in wordDict:
                wordLen = len(word)
                if s[i:i + wordLen] == word:
                    if dfs(i + wordLen):
                        memo[i] = True
                        break
            return memo[i]
        
        return dfs(0)
            