class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        minutes = 0
        fresh = 0

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        def dfs(r, c):
            nonlocal minutes
            nonlocal fresh

            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return
            fresh -= 1
            grid[r][c] = 2
            q.append((r, c))

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
            minutes += 1
        return minutes if not fresh else -1
        
