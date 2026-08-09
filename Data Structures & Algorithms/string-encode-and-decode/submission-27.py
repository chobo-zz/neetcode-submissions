class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        delimiter = "#"

        for word in strs:
            wordLen = len(word)
            res.append(str(wordLen))
            res.append(delimiter)
            res.append(word)
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        res = []

        i, j = 0, 0

        while i < len(s):
            while s[j] != "#":
                j += 1
            wordLen = int(s[i:j])
            j += 1
            i = wordLen + j
            word = s[j:i]
            res.append(word)
            j = i
        return res
