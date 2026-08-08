class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        distance = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr, nc) in visited or grid[nr][nc] != 2147483647:
                        continue
                    visited.add((nr, nc))
                    q.append((nr, nc))
            distance += 1
        