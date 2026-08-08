class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x:x[0])
        res = {}
        heap = [] # (length, endPoint)

        i = 0 # index for current interval we are choosing
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q: # interval is possible contender
                length = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(heap, (length, intervals[i][1]))
                i += 1
            
            while heap and heap[0][1] < q: # pop intervals which end before reaching q
                heapq.heappop(heap)
            res[q] = heap[0][0] if heap else -1
        
        return [res[q] for q in queries]