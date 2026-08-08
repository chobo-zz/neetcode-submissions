class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        prevEnd = intervals[0][1]

        count = 0
        for i in range(1, len(intervals)):
            curInterval = intervals[i]
            if prevEnd > curInterval[0]:
                count += 1
                prevEnd = min(prevEnd, curInterval[1])
            else:
                prevEnd = curInterval[1]
        
        return count