class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charToLastIndex = {}

        for i, v in enumerate(s):
            charToLastIndex[v] = i
        
        res = []
        partitionLength = 0
        partitionEnd = 0
        for i, v in enumerate(s):
            partitionLength += 1

            if charToLastIndex[v] > partitionEnd:
                partitionEnd = charToLastIndex[v]
            
            if i >= partitionEnd:
                res.append(partitionLength)
                partitionLength = 0
        
        return res