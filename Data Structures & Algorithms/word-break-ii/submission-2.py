class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        wordDict = set(wordDict)

        def dfs(i):
            if i >= len(s):
                return [""]
            
            if i in memo:
                return memo[i]

            res = []

            for j in range(i, len(s)):
                curWord = s[i: j + 1]
                if curWord not in wordDict:
                    continue
                
                nextWords = dfs(j + 1)

                for nextWord in nextWords:
                    sentence = curWord

                    if nextWord:
                        sentence += " " + nextWord
                    res.append(sentence)
            memo[i] = res
            return res
        
        return dfs(0)
