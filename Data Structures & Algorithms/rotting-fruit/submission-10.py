class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return None

        rows, cols = len(grid), len(grid[0])
        q = deque()
        minutes = 0
        fresh = 0

        def processNextCell(r, c):
            nonlocal fresh
            if r == rows or c == cols or r < 0 or c < 0 or grid[r][c] != 1:
                return
            q.append((r, c))
            fresh -= 1
            grid[r][c] = 2

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                processNextCell(r + 1, c)
                processNextCell(r - 1, c)
                processNextCell(r, c + 1)
                processNextCell(r, c - 1)
            minutes += 1
        
        return minutes if fresh == 0 else -1


