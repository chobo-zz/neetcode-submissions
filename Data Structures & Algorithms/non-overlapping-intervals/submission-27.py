class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        count = 0
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                count += 1
                prevEnd = min(prevEnd, intervals[i][1])
            else:
                prevEnd = intervals[i][1]
        
        return count