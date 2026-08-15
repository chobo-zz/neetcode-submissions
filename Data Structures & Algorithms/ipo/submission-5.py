class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pairs = [(c, p) for p, c in zip(profits, capital)]
        heapq.heapify(pairs)
        heap = []

        while k:
            while pairs and pairs[0][0] <= w:
                heapq.heappush(heap, -heapq.heappop(pairs)[1])
            
            if not heap:
                break
            
            w += -heapq.heappop(heap)

            k -= 1
                

        return w
        