class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        rows, cols = len(matrix), len(matrix[0])
        res = 1

        def dfs(r, c, prev): # returns LIP starting from r, c
            if r < 0 or c < 0 or r >= rows or c >= cols or matrix[r][c] <= prev:
                return 0
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            memo[(r, c)] = 1 + max(
                dfs(r + 1, c, matrix[r][c]),
                dfs(r - 1, c, matrix[r][c]),
                dfs(r, c + 1, matrix[r][c]),
                dfs(r, c - 1, matrix[r][c])
            )

            return memo[(r, c)]
        
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c, -1))
        
        return res
