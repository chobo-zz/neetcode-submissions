class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)] # x-coor, y-coor, path sum so far
        pathSums = { (0, 0): grid[0][0] } # stores best possible path sums for each (x, y) coordinate
        directions = [[0, 1], [1, 0]]

        while heap:
            path, x, y = heapq.heappop(heap)

            if (x, y) in pathSums and path > pathSums[(x, y)]:
                continue

            if x == m - 1 and y == n - 1:
                return path
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx >= m or ny >= n:
                    continue
                
                newPathSum = path + grid[nx][ny]
                if (nx, ny) not in pathSums or newPathSum < pathSums[(nx, ny)]:
                    pathSums[(nx, ny)] = newPathSum
                    heapq.heappush(heap, (newPathSum, nx, ny))
        
