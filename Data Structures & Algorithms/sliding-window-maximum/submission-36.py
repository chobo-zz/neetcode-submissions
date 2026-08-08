class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        res = []

        
        for i in range(len(nums)):
            heapq.heappush(maxHeap, (-nums[i], i))

            if i >= k - 1:
                while maxHeap and maxHeap[0][1] <= i - k:
                    heapq.heappop(maxHeap)
                res.append(-maxHeap[0][0])
        
        return res
