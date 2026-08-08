class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()
        distance = 0

        def processNextCell(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or grid[r][c] == -1:
                return
            
            q.append((r, c))
            visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                processNextCell(r + 1, c)
                processNextCell(r - 1, c)
                processNextCell(r, c + 1)
                processNextCell(r, c - 1)
            distance += 1
    

