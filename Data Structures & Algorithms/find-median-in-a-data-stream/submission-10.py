class MedianFinder:

    def __init__(self):
        self.small = [] # max heap that stores lower half of nums
        self.large = [] # min heap that stores greater half of nums

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        if self.small and self.large and -self.small[0] > self.large[0]:
            num = -heapq.heappop(self.small)
            heapq.heappush(self.large, num)
        
        if len(self.small) > len(self.large) + 1:
            num = -heapq.heappop(self.small)
            heapq.heappush(self.large, num)
        
        if len(self.small) < len(self.large) - 1:
            num = heapq.heappop(self.large)
            heapq.heappush(self.small, -num)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]

        return (-self.small[0] + self.large[0]) / 2        