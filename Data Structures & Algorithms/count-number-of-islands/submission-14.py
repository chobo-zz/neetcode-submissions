class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        possibleDirections = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        res = 0
        if not grid:
            return res

        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = "0"

            while q:
                r, c = q.popleft()

                for x, y in possibleDirections:
                    nr, nc = r + x, c + y

                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] != "0":
                        q.append((nr, nc))
                        grid[nr][nc] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += 1
                    bfs(r, c)

        return res