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

        s = e = rooms = 0
        ans = 0

        while s < len(intervals):
            if startTimes[s] < endTimes[e]:
                rooms += 1
                ans = max(ans, rooms)
                s += 1
            else:
                e += 1
                rooms -= 1
        
        return ans