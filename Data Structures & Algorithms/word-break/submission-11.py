class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {} # whether we can segment s starting from i (i -> true/false)

        def dfs(i): # returns if we can segment s starting from index i
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            
            for word in wordDict:
                wordLen = len(word)
                if (i + wordLen) <= len(s) and s[i:i + wordLen] == word:
                    if dfs(i + wordLen):
                        memo[i] = True
                        return True
            
            memo[i] = False
            return False

        
        return dfs(0)