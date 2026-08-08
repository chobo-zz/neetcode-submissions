class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
        count = Counter(nums) # val -> count

        for val, count in count.items():
            heapq.heappush(heap, (count, val))
            if len(heap) > k:
                heapq.heappop(heap)
        return [val for count, val in heap]


            

        