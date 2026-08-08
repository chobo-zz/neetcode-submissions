class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            curInterval = intervals[i]

            if curInterval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], curInterval[1])
            else:
                res.append(curInterval)
        
        return res

