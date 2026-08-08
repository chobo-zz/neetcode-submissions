class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # find last position of char in string, mark it

        charToLastIndex = {}

        for i, v in enumerate(s):
            charToLastIndex[v] = i
        
        # each partition extends to the last known position

        curLength = 0
        partitionEnd = 0
        res = []
        for i, v in enumerate(s):
            curLength += 1
            partitionEnd = max(partitionEnd, charToLastIndex[v])

            if i == partitionEnd:
                res.append(curLength)
                curLength = 0
        
        return res
