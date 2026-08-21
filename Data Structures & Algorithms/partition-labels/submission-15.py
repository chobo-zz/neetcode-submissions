class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        charToLastIndex = defaultdict(int)

        for i, c in enumerate(s):
            charToLastIndex[c] = i

        partitionSize = 0
        partitionEnd = 0
        for i, c in enumerate(s):
            partitionSize += 1
            partitionEnd = max(partitionEnd, charToLastIndex[c])
            
            if i >= partitionEnd:
                res.append(partitionSize)
                partitionSize = 0
            
        
        return res