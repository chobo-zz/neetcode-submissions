class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = {}
        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j  # insert remaining chars
            if j == len(word2):
                return len(word1) - i  # delete remaining chars
            if (i, j) in dp:
                return dp[(i, j)]
            if word1[i] == word2[j]:
                res = dfs(i + 1, j + 1)
            else:
                res = 1 + min(
                    dfs(i + 1, j),     # delete
                    dfs(i, j + 1),     # insert
                    dfs(i + 1, j + 1)  # replace
                )
            dp[(i, j)] = res
            return res

        return dfs(0, 0)