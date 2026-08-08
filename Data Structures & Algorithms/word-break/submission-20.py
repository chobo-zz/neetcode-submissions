class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(i): # returns whether we can segment s starting at index i
            if i >= len(s):
                return True
            
            if i in memo:
                return memo[i]
            
            memo[i] = False
            for word in wordDict:
                wordLen = len(word)
                if s[i:i + wordLen] == word and dfs(i + wordLen):
                    memo[i] = True
            
            return memo[i]
        
        return dfs(0)
            

                    