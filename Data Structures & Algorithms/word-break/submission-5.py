class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # top down memoization

        memo = { len(s): True }

        def dfs(i):
            if i == len(s):
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
            return False

        return dfs(0)