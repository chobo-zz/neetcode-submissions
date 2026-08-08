class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            start, end = newInterval

            if end < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif start > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(start, intervals[i][0]), max(end, intervals[i][1])]
            
        res.append(newInterval)
        
        return res