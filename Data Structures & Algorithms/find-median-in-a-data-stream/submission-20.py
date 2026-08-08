class MedianFinder:

    def __init__(self):
        # two heaps, small and large
        # small is maxHeap that stores smaller half of numbers 
        # large is minHeap that stores larger half of numbers

        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        if self.large and self.large[0] < -self.small[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
        