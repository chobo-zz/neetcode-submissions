class MedianFinder:

    def __init__(self):
        self.small = [] # maxHeap that stores the bigger values
        self.large = [] # minHeap that stores the smaller values

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, num * -1)

        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        if len(self.small) < len(self.large):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2

        
        