class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        availableHeap = [i for i in range(n)] # (meeting room number)
        usedHeap = [] # (meeting's end time, meeting room number)

        meetings.sort()
        roomCounter = [0] * n

        for startTime, endTime in meetings:
            while usedHeap and usedHeap[0][0] <= startTime:
                _, roomNumber = heapq.heappop(usedHeap)
                heapq.heappush(availableHeap, roomNumber)

            if not availableHeap:
                lastEndTime, lastRoomNumber = heapq.heappop(usedHeap)
                originalDuration = endTime - startTime
                endTime = lastEndTime + originalDuration
                heapq.heappush(availableHeap, lastRoomNumber)

            roomNumber = heapq.heappop(availableHeap)
            heapq.heappush(usedHeap, (endTime, roomNumber))
            roomCounter[roomNumber] += 1
        
        return roomCounter.index(max(roomCounter))

        
    