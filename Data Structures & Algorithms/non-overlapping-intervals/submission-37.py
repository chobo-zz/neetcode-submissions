class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        prevEnd = intervals[0][1]
        removed = 0

        for i in range(1, len(intervals)):
            if prevEnd <= intervals[i][0]:
                prevEnd = intervals[i][1]
            else:
                prevEnd = min(prevEnd, intervals[i][1])
                removed += 1
        
        return removed