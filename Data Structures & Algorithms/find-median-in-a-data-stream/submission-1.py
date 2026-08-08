class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        if len(self.nums) % 2:
            mid = len(self.nums) // 2
            return self.nums[mid]
        else:
            mid = len(self.nums) // 2 - 1
            return (self.nums[mid] + self.nums[mid + 1]) / 2
        