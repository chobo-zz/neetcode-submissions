class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        rows, cols = len(matrix), len(matrix[0])

        def dfs(r, c, prev):
            if r < 0 or c < 0 or r >= rows or c >= cols or matrix[r][c] <= prev:
                return 0
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            res = 1 + max(
                dfs(r + 1, c, matrix[r][c]),
                dfs(r - 1, c, matrix[r][c]),
                dfs(r, c + 1, matrix[r][c]),
                dfs(r, c - 1, matrix[r][c])
            )

            memo[(r, c)] = res
            return res
        
        LIS = 1
        for r in range(rows):
            for c in range(cols):
                LIS = max(LIS, dfs(r, c, -1))
        
        return LIS
            
            