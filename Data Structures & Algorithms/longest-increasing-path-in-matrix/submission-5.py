class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        memo = {} # (r, c) -> max path int
        rows, cols = len(matrix), len(matrix[0])
        LIP = 1

        def dfs(r, c, prev): # prev to make sure we only visit increasing cells
            if r < 0 or c < 0 or r >= rows or c >= cols or matrix[r][c] <= prev:
                return 0

            if (r, c) in memo:
                return memo[(r, c)]
            
            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))

            memo[(r, c)] = res
            return res
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, -1)
        
        return max(memo.values())
