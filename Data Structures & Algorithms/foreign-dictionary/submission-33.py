class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if not words:
            return ""

        adjList = { c: [] for word in words for c in word }

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            minLen = min(len(w1), len(w2))

            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjList[w1[j]].append(w2[j])
                    break
        
        visiting = set()
        visited = set()
        res = []
        def dfs(char):
            if char in visiting:
                return False
            
            if char in visited:
                return True
            
            visiting.add(char)
            for nei in adjList[char]:
                if not dfs(nei):
                    return False
            visiting.remove(char)
            visited.add(char)
            res.append(char)
            return True
        
        for c in adjList:
            if not dfs(c):
                return ""
        return "".join(reversed(res))