class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        rows, cols = len(matrix), len(matrix[0])

        def dfs(x, y, prev):
            if x < 0 or x >= rows or y < 0 or y >= cols or matrix[x][y] <= prev:
                return 0
            
            if (x, y) in memo:
                return memo[(x, y)]
            
            res = 1 + max(
                dfs(x + 1, y, matrix[x][y]),
                dfs(x - 1, y, matrix[x][y]),
                dfs(x, y + 1, matrix[x][y]),
                dfs(x, y - 1, matrix[x][y])
            )
            memo[(x, y)] = res
            return res
        
        LIP = 0
        for x in range(rows):
            for y in range(cols):
                LIP = max(LIP, dfs(x, y, -1))
        
        return LIP