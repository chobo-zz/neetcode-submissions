class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        availableHeap = [i for i in range(n)]
        usedHeap = [] # (end, room)
        count = [0] * n

        for start, end in meetings:
            while usedHeap and usedHeap[0][0] <= start:
                _, room = heapq.heappop(usedHeap)
                heapq.heappush(availableHeap, room)
            
            if not availableHeap:
                lastEnd, room = heapq.heappop(usedHeap)
                end = (end - start) + lastEnd
                heapq.heappush(availableHeap, room)
            
            room = heapq.heappop(availableHeap)
            heapq.heappush(usedHeap, (end, room))
            count[room] += 1
        
        return count.index(max(count))