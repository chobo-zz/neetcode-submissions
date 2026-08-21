class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort()

        res.append(intervals[0])

        for i in range(1, len(intervals)):
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
        
        return res
    