class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        res = []
        pac = set()
        atl = set()

        def dfs(r, c, visited, prevHeight):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or prevHeight > heights[r][c]:
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        

        for r in range(rows):
            dfs(r, 0, pac, 0)
            dfs(r, cols - 1, atl, 0)
        
        for c in range(cols):
            dfs(0, c, pac, 0)
            dfs(rows - 1, c, atl, 0)

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res