class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            nStart, nEnd = newInterval

            if nEnd < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif nStart > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(nStart, intervals[i][0]), max(nEnd, intervals[i][1])]
        res.append(newInterval)

        return res