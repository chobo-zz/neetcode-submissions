class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c: [] for word in words for c in word }
        visiting = set()
        visited = set()
        res = []

        for i in range(len(words) - 1):
            firstWord = words[i]
            secondWord = words[i + 1]

            minLength = min(len(firstWord), len(secondWord))

            if len(firstWord) > len(secondWord) and firstWord[:minLength] == secondWord[:minLength]:
                return ""
            
            for j in range(minLength):
                if firstWord[j] != secondWord[j]:
                    adj[firstWord[j]].append(secondWord[j])
                    break
        
        def dfs(char):
            if char in visiting:
                return False
            
            if char in visited:
                return True
            
            visiting.add(char)
            for nei in adj[char]:
                if not dfs(nei):
                    return False
            visiting.remove(char)
            visited.add(char)
            res.append(char)
            return True
        
        for c in adj:
            if not dfs(c):
                return ""
        res.reverse()
        return "".join(res)