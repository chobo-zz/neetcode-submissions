"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTimes = sorted([interval.start for interval in intervals])
        endTimes = sorted([i.end for i in intervals])

        startIndex, endIndex = 0, 0
        roomCount = 0
        maxRoomCount = 0

        while startIndex < len(intervals):
            if startTimes[startIndex] < endTimes[endIndex]:
                roomCount += 1
                maxRoomCount = max(maxRoomCount, roomCount)
                startIndex += 1
            else:
                roomCount -= 1
                endIndex += 1
        return maxRoomCount
        