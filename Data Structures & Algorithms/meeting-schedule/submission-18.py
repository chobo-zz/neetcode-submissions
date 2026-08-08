"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda i: i.start)

        prevEnd = intervals[0].end
        for i in range(1, len(intervals)):
            curInterval = intervals[i]

            if curInterval.start < prevEnd:
                return False
            prevEnd = curInterval.end
        
        return True
