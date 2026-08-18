class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights:
            return 0
        rows, cols = len(heights), len(heights[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        heap = [(0, 0, 0)] # (effort, x, y)
        visited = set()

        while True:
            effort, x, y = heapq.heappop(heap)
            if x == rows - 1 and y == cols - 1:
                return effort

            if (x, y) in visited:
                continue
            visited.add((x, y))
            
            for dr, dc in directions:
                nr, nc = x + dr, y + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in visited:
                    continue
                newEffort = max(effort, abs(heights[nr][nc] - heights[x][y]))
                heapq.heappush(heap, (newEffort, nr, nc))
                
            
