class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c: [] for word in words for c in word }
        res = []
        visiting = set()
        visited = set()

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            minLength = min(len(w1), len(w2))

            if w1[:minLength] == w2[:minLength] and len(w1) > len(w2):
                return ""

            for j in range(minLength):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break
        
        def dfs(c):
            if c in visiting:
                return False
            
            if c in visited:
                return True

            visiting.add(c)
            
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            
            visiting.remove(c)
            visited.add(c)
            res.append(c)
            return True
        
        for c in adj:
            if not dfs(c):
                return ""
        
        return "".join((reversed(res)))
