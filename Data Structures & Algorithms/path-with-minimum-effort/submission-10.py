class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights:
            return 0
        visited = set()
        minHeap = [(0, 0, 0)] # (max absolute difference seen so far, row, col)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        rows, cols = len(heights), len(heights[0])
        res = float("inf")
        while minHeap:
            effort, r, c = heapq.heappop(minHeap)
            if r == rows - 1 and c == cols - 1:
                return effort
            if (r, c) in visited:
                continue
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr, nc) in visited:
                    continue
                heapq.heappush(minHeap, (max(effort, abs(heights[r][c] - heights[nr][nc])), nr, nc))

