class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charToLastIndex = defaultdict(int)

        for i, v in enumerate(s):
            charToLastIndex[v] = i
        
        res = []
        partitionEnd = 0
        curLen = 0
        for i in range(len(s)):
            curLen += 1
            char = s[i]
            partitionEnd = max(partitionEnd, charToLastIndex[char])
            
            if i == partitionEnd:
                res.append(curLen)
                curLen = 0
        
        return res
