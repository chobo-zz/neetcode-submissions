class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        heap = [] # (length, endTime)
        i = 0
        res = defaultdict(int)

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i][0], intervals[i][1]
                heapq.heappush(heap, (end - start + 1, end))
                i += 1
            
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            res[q] = heap[0][0] if heap else -1
        
        return [res[q] for q in queries]

            

