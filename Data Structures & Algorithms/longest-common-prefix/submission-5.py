class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        
        
        prefixStr = strs[0]

        if n <= 1:
            return prefixStr

        res = ""
        for i in range(len(prefixStr)):
            prefixChar = prefixStr[i]
            for j in range(1, n):
                if i >= len(strs[j]) or not prefixChar == strs[j][i]:
                    return res
            res += prefixChar
        return res
            

