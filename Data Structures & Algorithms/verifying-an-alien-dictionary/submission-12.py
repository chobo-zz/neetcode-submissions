class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        charToIndex = { v: i for i, v in enumerate(order) }
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            minLen = min(len(word1), len(word2))
            if word1[:minLen] == word2[:minLen] and len(word1) >= len(word2):
                return False
            
            for j in range(minLen):
                if word1[j] != word2[j]:
                    if charToIndex[word1[j]] > charToIndex[word2[j]]:
                        return False
                    break
        return True
