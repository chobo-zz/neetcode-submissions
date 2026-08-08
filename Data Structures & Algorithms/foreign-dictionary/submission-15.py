class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c: [] for word in words for c in word }

        for i in range(0, len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            shorterLen = min(len(w1), len(w2))
            if w1[:shorterLen] == w2[:shorterLen] and len(w1) > len(w2):
                return ""
            
            for j in range(shorterLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
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
            
            for neiChar in adj[char]:
                if neiChar not in visited:
                    if not dfs(neiChar):
                        return False
            
            visiting.remove(char)
            visited.add(char)
            res.append(char)

            return True
        
        for char in adj:
            if not dfs(char):
                return ""
        
        return "".join(reversed(res))