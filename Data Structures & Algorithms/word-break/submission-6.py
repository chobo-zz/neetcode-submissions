class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {} # can we segment s starting from index i (i -> true/false)

        def dfs(i): # returns if we can segment s starting from index i
            if i >= len(s):
                return True
            
            if i in memo:
                return memo[i]

            
            for word in wordDict:
                wordLength = len(word)
                if (i + wordLength) <= len(s) and s[i:i + wordLength] == word:
                    if dfs(i + wordLength):
                        memo[i] = True
                        return True
            memo[i] = False
            return memo[i]
        
        return dfs(0)
            
                