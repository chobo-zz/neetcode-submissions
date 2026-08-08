class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charToLastIndex = {}

        for i, v in enumerate(s):
            charToLastIndex[v] = i
        
        res = []
        curLength = 0
        endIndex = 0

        for i, v in enumerate(s):
            curLength += 1
            endIndex = max(endIndex, charToLastIndex[v])

            if i == endIndex:
                res.append(curLength)
                curLength = 0
        
        return res



