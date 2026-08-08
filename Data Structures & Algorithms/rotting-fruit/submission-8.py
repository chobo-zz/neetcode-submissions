class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows, cols = len(grid), len(grid[0])

        minutes = 0
        q = deque()
        fresh = 0

        def processNextCell(r, c):
            nonlocal fresh
            if r >= rows or c >= cols or r < 0 or c < 0 or grid[r][c] != 1:
                return
            fresh -= 1
            grid[r][c] = 2
            q.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
            
                processNextCell(r + 1, c)
                processNextCell(r - 1, c)
                processNextCell(r, c + 1)
                processNextCell(r, c - 1)
            minutes += 1
        return minutes if fresh == 0 else -1

        