class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = x ** 2 + y ** 2
            heap.append((dist, x, y))
        
        res = []
        heapq.heapify(heap)
        while k > 0:
            k -= 1
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])
        
        return res
        
        
        