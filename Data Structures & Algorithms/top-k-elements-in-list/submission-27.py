class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = [] # (count, num)
        count = Counter(nums)

        for num, count in count.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for count, num in heap]