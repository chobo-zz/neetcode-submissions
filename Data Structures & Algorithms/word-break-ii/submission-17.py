class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        wordDict = set(wordDict)

        def dfs(i): # returns sentences able to be formed starting from s[i:]
            if i == len(s):
                return [""]
            
            if i in memo:
                return memo[i]
            
            res = []
            for j in range(i, len(s)):
                word = s[i : j + 1]
                if word in wordDict:
                    nextSentences = dfs(j + 1)

                    for nextSentence in nextSentences:
                        newSentence = word
                        if nextSentence != "":
                            newSentence += " " + nextSentence
                        res.append(newSentence)

            
            memo[i] = res
            return res
        
        return dfs(0)