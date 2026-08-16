class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}

        def dfs(i): # returns sentences formed starting from s[i:]
            if i == len(s):
                return [""]

            if i in memo:
                return memo[i]
            
            sentences = []
            for j in range(i, len(s)):
                word = s[i:j + 1]
                if word in wordDict:
                    nextSentences = dfs(j + 1)

                    for nextSentence in nextSentences:
                        sentence = word
                        if nextSentence:
                            sentence += " " + nextSentence
                        sentences.append(sentence)
            memo[i] = sentences
            return sentences
        return dfs(0)