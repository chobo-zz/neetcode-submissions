class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charToLastIndex = defaultdict(int)

        for i, c in enumerate(s):
            charToLastIndex[c] = i
        
        res = []
        partitionEnd = 0
        partitionSize = 1

        for i, c in enumerate(s):
            
            partitionEnd = max(partitionEnd, charToLastIndex[c])

            if i >= partitionEnd:
                res.append(partitionSize)
                partitionSize = 0
            partitionSize += 1
        return res