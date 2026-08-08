class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict) # O(1) lookups
        memo = {} # valid sentences formed from s[i:]

        def dfs(i): # returns valid sentences starting from s[i:]
            if i >= len(s): # base case: if we reached end of s, return empty string sentence
                return [""]

            if i in memo:
                return memo[i] # memoized lookups to avoid recomputations of same paths
            
            res = []
            for j in range(i, len(s)):
                curWord = s[i: j + 1]

                if curWord not in wordDict:
                    continue

                # we were able to form a valid word in this current call, 
                # so make a recursive call past the word's last index to see if we can form valid sentence
                # with the rest of the string
                nextSentences = dfs(j + 1)

                for nextSentence in nextSentences:
                    curSentence = curWord

                    if nextSentence:
                        curSentence += " " + nextSentence
                    res.append(curSentence)
                            
            memo[i] = res
            return res
        return dfs(0)