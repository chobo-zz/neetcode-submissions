class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (-dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        
        while k:
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])
            k -= 1
        
        return res