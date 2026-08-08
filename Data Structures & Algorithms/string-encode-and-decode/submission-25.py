class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            wordLen = str(len(word))
            res += wordLen + "#" + word
        return res
    def decode(self, s: str) -> List[str]:
        res = []

        i, j = 0, 0

        while i < len(s):
            while s[j] != "#":
                j += 1
            wordLen = int(s[i:j])
            j += 1
            i = j + wordLen
            word = s[j:i]
            res.append(word)
            j = i
        return res
