class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        distance = 1

        def processNextCell(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 2147483647:
                return
            grid[r][c] = distance 
            q.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                processNextCell(r + 1, c)
                processNextCell(r - 1, c)
                processNextCell(r, c + 1)
                processNextCell(r, c - 1)
            distance += 1
    

