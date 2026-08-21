class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        availableRooms = [i for i in range(n)]
        usedRooms = [] # (meetingEnd, roomNumber)
        usedCount = [0] * n

        for i in range(len(meetings)):
            while usedRooms and usedRooms[0][0] <= meetings[i][0]:
                _, roomNumber = heapq.heappop(usedRooms)
                heapq.heappush(availableRooms, roomNumber)
            
            if not availableRooms:
                meetingEnd, roomNumber = heapq.heappop(usedRooms)
                heapq.heappush(availableRooms, roomNumber)
                originalDuration = meetings[i][1] - meetings[i][0]
                meetings[i][0] = meetingEnd
                meetings[i][1] = meetingEnd + originalDuration
            
            roomToUse = heapq.heappop(availableRooms)
            heapq.heappush(usedRooms, (meetings[i][1], roomToUse))
            usedCount[roomToUse] += 1
        
        return usedCount.index(max(usedCount))

