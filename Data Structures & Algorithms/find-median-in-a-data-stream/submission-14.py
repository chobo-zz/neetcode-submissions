class MedianFinder:

    # small is max heap that stores the smaller half of values
    # large is min heap that stores the larger half of values
    # small (maxheap) [1, 2, 3] 
    # large (minHeap) [4, 5, 6]
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.large, num)

        if self.small and -self.small[0] > self.large[0]:
            heapq.heappush(self.small, -heapq.heappop(self.large))
        
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))
        

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.large) < len(self.small):
            return -self.small[0]
        else:
            return (self.large[0] + -self.small[0]) / 2
        
        