class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap = [(c, p) for c, p in zip(capital, profits)]
        maxHeap = []
        heapq.heapify(minHeap)

        for _ in range(k):
            while minHeap and minHeap[0][0] <= w:
                capital, profit = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -profit)
            
            if maxHeap:
                w += -heapq.heappop(maxHeap)
            
        
        return w