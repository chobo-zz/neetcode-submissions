class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {} # (i, j) -> True

        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(i, j): # returns whether we can interleave s1 and s2 to become s3 starting at indexes i (s1) and j (s2)
            if i == len(s1) and j == len(s2):
                return True
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i < len(s1) and s1[i] == s3[i + j]:
                if dfs(i + 1, j):
                    memo[(i, j)] = True
                    return True
            if j < len(s2) and s2[j] == s3[i + j]:
                if (dfs(i, j + 1)):
                    memo[(i, j)] = True
                    return True
            
            memo[(i, j)] = False
            return memo[(i, j)]

        return dfs(0, 0)