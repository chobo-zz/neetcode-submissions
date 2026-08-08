class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dfs(i, j): # returns LCS between text1 and text2 starting at indexes i and j
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = 0
            if text1[i] == text2[j]:
                res = 1 + dfs(i + 1, j + 1)
            else:
                res = max(dfs(i, j + 1), dfs(i + 1, j))
            memo[(i, j)] = res

            return res
        
        return dfs(0, 0)