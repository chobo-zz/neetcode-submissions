"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        startTimes = sorted([i.start for i in intervals])
        endTimes = sorted([i.end for i in intervals])

        startIndex, endIndex = 0, 0
        maxRoomsNeeded = 0
        roomsBeingUsed = 0

        while startIndex < len(startTimes):
            if startTimes[startIndex] < endTimes[endIndex]:
                roomsBeingUsed += 1
                maxRoomsNeeded = max(maxRoomsNeeded, roomsBeingUsed)
                startIndex += 1
            else:
                roomsBeingUsed -= 1
                endIndex += 1
        
        return maxRoomsNeeded


