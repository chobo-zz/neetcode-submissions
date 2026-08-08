class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {} # minimum operations to match starting at i and j indexes

        def dfs(i, j): # index at word1, index at word2
            # if i reaches end, we would need to insert remaining characters to match
            if i == len(word1):
                return len(word2) - j
            # if j reaches end, we would need to delete remaining characters to match
            if j == len(word2):
                return len(word1) - i

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                # characters match, so increment both pointers, no operation needed
                res = dfs(i + 1, j + 1)
            else:
                # characters do not match, we need to perform operation (3 choices)
                res = 1 + min(
                    dfs(i + 1, j), # delete from s1
                    dfs(i, j + 1), # add to s1
                    dfs(i + 1, j + 1) # replace in s1
                )
            
            memo[(i, j)] = res
            return res
        
        return dfs(0, 0)

        

