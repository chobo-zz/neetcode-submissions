class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = [i for i in range(n)]
        used = [] # (end, room number)
        count = [0] * n

        for roomNumber, meeting in enumerate(meetings):
            nextStartTime, nextEndTime = meeting

            while used and used[0][0] <= nextStartTime:
                _, lastRoomNumber = heapq.heappop(used)
                heapq.heappush(available, lastRoomNumber)
            
            if not available:
                lastEndTime, lastRoomNumber = heapq.heappop(used)
                heapq.heappush(available, lastRoomNumber)
                nextEndTime = lastEndTime + (nextEndTime - nextStartTime)

            nextRoomNumber = heapq.heappop(available)
            heapq.heappush(used, (nextEndTime, nextRoomNumber))
            count[nextRoomNumber] += 1

        return count.index(max(count))