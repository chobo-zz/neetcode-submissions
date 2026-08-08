class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            curInterval = intervals[i]

            if newInterval[0] > curInterval[1]:
                res.append(curInterval)
            elif newInterval[1] < curInterval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval[0] = min(newInterval[0], curInterval[0])
                newInterval[1] = max(newInterval[1], curInterval[1])
        
        res.append(newInterval)
        return res