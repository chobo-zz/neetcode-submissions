class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)

        prefix = strs[0]

        for i in range(len(prefix)):

            for j in range(1, n):
                nextStr = strs[j]
                if i >= len(nextStr) or prefix[i] != nextStr[i]:
                    return prefix[:i]
        
        return prefix
            