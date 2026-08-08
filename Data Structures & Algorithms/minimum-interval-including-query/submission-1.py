class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort both intervals and queries (copy) in ascending order
        # use a min heap to keep track of (length, endPoint)
        # if current interval's start is <= current query -> possible contender, so add to heap
        # among possible contenders, the intervals whose end is < current query is not valid, so pop them
        # peek the minimum heap and return its value. if no values in heap, return -1
        # ensure we return answers in order of original query array (thats why we use a copy of the sorted queries)

        intervals.sort(key=lambda pair: pair[0])
        minHeap = []
        res = {}
        i = 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        
        return [res[q] for q in queries]
