class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        memo = {}

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            res = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < rows and nc < cols and nr >= 0 and nc >= 0 and matrix[nr][nc] > matrix[r][c]:
                    res = max(res, 1 + dfs(nr, nc))
            memo[(r, c)] = res
            return res

        for r in range(rows):
            for c in range(cols):
                dfs(r, c)
        
        return max(memo.values())