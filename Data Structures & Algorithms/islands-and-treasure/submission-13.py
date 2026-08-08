class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None

        rows, cols = len(grid), len(grid[0])

        q = deque()
        visited = set()
        distance = 0

        def processNextCell(r, c):
            if (r >= rows or c >= cols or r < 0 or c < 0 or grid[r][c] == -1 or (r, c) in visited):
                return
            visited.add((r, c))
            q.append((r, c))
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c))
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                processNextCell(r + 1, c)
                processNextCell(r - 1, c)
                processNextCell(r, c + 1)
                processNextCell(r, c - 1)
            distance += 1
