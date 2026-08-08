class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for x, y in points:
            distToOrigin = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(heap, (distToOrigin, x, y))
        
        while k:
            k -= 1
            d, x, y = heapq.heappop(heap)
            res.append([x, y])
        
        return res
