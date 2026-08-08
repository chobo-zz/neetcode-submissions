class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charToLastIndex = {}

        for i in range(len(s)):
            charToLastIndex[s[i]] = i
        
        partitionLength = 0
        partitionEnd = 0
        res = []
        for i in range(len(s)):
            partitionLength += 1
            if charToLastIndex[s[i]] > partitionEnd:
                partitionEnd = charToLastIndex[s[i]]
            
            if i == partitionEnd:
                res.append(partitionLength)
                partitionLength = 0
        
        return res