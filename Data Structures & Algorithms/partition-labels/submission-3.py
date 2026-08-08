class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charToLastIndex = {}

        for i, v in enumerate(s):
            charToLastIndex[v] = i
        
        curLength = 0
        partitionEnd = 0
        res = []
        for i in range(len(s)):
            curLength += 1
            partitionEnd = max(partitionEnd, charToLastIndex[s[i]])

            if i == partitionEnd:
                res.append(curLength)
                curLength = 0
        
        return res